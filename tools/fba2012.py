#!/usr/bin/env python
# FB Alpha 2012 en la PS4: DAT de cada core generado desde su código fuente, verificación de romsets con la lógica de carga
# del core (open_archive de libretro.cpp) y listas de RetroArch con el core que corresponde a cada carpeta.
#   python tools/fba2012.py dat [--fuentes DIR]        clona los cores en los commits de 2020 y escribe los DAT en emu/RETROARCH/database/dat/
#   python tools/fba2012.py verificar CARPETA [--tsv F] dice, zip a zip, con qué core arranca, qué ROMs le faltan y a qué carpeta va
#   python tools/fba2012.py listas                      verifica las carpetas de arcade de emu/ROMS y genera sus .lpl

import argparse
import collections
import glob
import json
import os
import re
import subprocess
import sys
import tempfile
import zipfile
from xml.sax.saxutils import escape, quoteattr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import retroarch_lists as ral  # noqa: E402

DAT_DIR = os.path.join(ral.RA, "database", "dat")
PARSED = os.path.join(DAT_DIR, "fba2012.json")

# core -> (commit de libretro/<core> anterior a julio de 2020, subcarpeta con src/, versión de romset, carpeta en emu/ROMS)
# Los cores de la consola son del port R4 (30-06-2020). Las tablas de ROMs de estos commits coinciden con las de 2026,
# salvo cuatro BIOS Universe opcionales añadidas a neogeo.zip, así que la fecha exacta del binario no cambia el resultado.
CORES = {
    "fbalpha2012": ("fa97cd2784a337f8ac774c2ce8a136aee69b5f43", "svn-current/trunk", "0.2.97.29", "ARCADE/FBNEO"),
    "fbalpha2012_cps1": ("a65d5cfe973c1cd254105e2c8f9350e0b5e4ea96", "", "0.2.97.28", "ARCADE/FBNEO/CPS1"),
    "fbalpha2012_cps2": ("9dd4e46febfe58d7db43e573f43fadc66f9b09f9", "", "0.2.97.28", "ARCADE/FBNEO/CPS2"),
    "fbalpha2012_cps3": ("eb2716633ca633e0480254c27fe233ef1c4d8399", "svn-current/trunk", "0.2.97.29", "ARCADE/FBNEO/CPS3"),
    "fbalpha2012_neogeo": ("e43fa0989f98bc6596582736a59ea0fbf9e76923", "", "0.2.97.29", "NEOGEO"),
}
DEDICATED = ["fbalpha2012_cps1", "fbalpha2012_cps2", "fbalpha2012_cps3", "fbalpha2012_neogeo"]
PLAYABLE = ("ok", "arranca con CRC distinta")
# Drivers que arrancan pero no son juegos
NOT_GAMES = {"neocdz": "sistema Neo Geo CDZ sin CD, no es un juego"}
# libretro.cpp deja pasar sin asia-s3.rom si neogeo.zip trae otra BIOS
NEOGEO_ASIA_S3 = 0x91B64BE3

_special = re.compile(r"[\"'/]")


# ---------------------------------------------------------------- lectura del código fuente

def strip_comments(s):
    out, i, n = [], 0, len(s)
    while i < n:
        c = s[i]
        if c in "\"'":
            j = i + 1
            while j < n and s[j] != c and s[j] != "\n":
                j += 2 if s[j] == "\\" else 1
            out.append(s[i:j + 1])
            i = j + 1
        elif s.startswith("//", i):
            j = s.find("\n", i)
            if j < 0:
                break
            i = j
        elif s.startswith("/*", i):
            j = s.find("*/", i + 2)
            if j < 0:
                break
            out.append("\n" * s.count("\n", i, j))
            i = j + 2
        else:
            m = _special.search(s, i)
            if not m:
                out.append(s[i:])
                break
            if m.start() == i:
                out.append(c)
                i += 1
            else:
                out.append(s[i:m.start()])
                i = m.start()
    return "".join(out)


def eval_cond(expr):
    # Ninguna macro definida: ROM_VERIFY, FBA_DEBUG y compañía están apagadas en los builds de libretro
    e = re.sub(r"defined\s*\(?\s*\w+\s*\)?", " 0 ", expr)
    e = e.replace("&&", " and ").replace("||", " or ")
    e = re.sub(r"!(?!=)", " not ", e)
    e = re.sub(r"\b[A-Za-z_]\w*\b", lambda m: m.group(0) if m.group(0) in ("and", "or", "not") else "0", e)
    try:
        return bool(eval(e, {"__builtins__": {}}))
    except Exception:
        return False


def preprocess(text):
    out, stack, active = [], [], True
    for line in text.split("\n"):
        m = re.match(r"\s*#\s*(if|ifdef|ifndef|elif|else|endif)\b(.*)", line)
        if not m:
            out.append(line if active else "")
            continue
        kw, rest = m.group(1), m.group(2).strip()
        if kw in ("if", "ifdef", "ifndef"):
            c = eval_cond(rest) if kw == "if" else kw == "ifndef"
            stack.append([active, c])
            active = active and c
        elif kw == "elif" and stack:
            parent, taken = stack[-1]
            c = not taken and eval_cond(rest)
            stack[-1][1] = taken or c
            active = parent and c
        elif kw == "else" and stack:
            parent, taken = stack[-1]
            active = parent and not taken
            stack[-1][1] = True
        elif kw == "endif" and stack:
            active = stack.pop()[0]
        out.append("")
    return "\n".join(out)


def split_fields(body):
    fields, cur, depth, i, n = [], [], 0, 0, len(body)
    while i < n:
        c = body[i]
        if c == '"':
            j = i + 1
            while j < n and body[j] != '"':
                j += 2 if body[j] == "\\" else 1
            cur.append(body[i:j + 1])
            i = j + 1
            continue
        depth += c in "({["
        depth -= c in ")}]"
        if c == "," and depth == 0:
            fields.append("".join(cur).strip())
            cur = []
        else:
            cur.append(c)
        i += 1
    if "".join(cur).strip():
        fields.append("".join(cur).strip())
    return fields


def c_string(field):
    parts = re.findall(r'L?"((?:[^"\\]|\\.)*)"', field)
    if not parts:
        return None
    s = re.sub(r"\\x([0-9a-fA-F]{1,2})", lambda m: chr(int(m.group(1), 16)), "".join(parts))
    return s.replace('\\"', '"').replace("\\\\", "\\").replace("\\0", "\0").split("\0", 1)[0]


def c_int(expr):
    return int(eval(re.sub(r"(?<=[0-9a-fA-F])[uUlL]+\b", "", expr.strip()), {"__builtins__": {}}))


def parse_file(path, source, problems):
    # RomDesc, PickRom y RomInfo son static: se resuelven dentro de su archivo (muchos drivers los llaman "Drv")
    with open(path, encoding="latin-1") as f:
        text = preprocess(strip_comments(f.read()))
    descs, picks, fns, drivers = {}, {}, {}, {}
    for m in re.finditer(r"(?:static\s+)?struct\s+BurnRomInfo\s+(\w+)RomDesc\s*\[\s*\]\s*=\s*\{(.*?)\}\s*;", text, re.S):
        roms = []
        for e in re.finditer(r'\{\s*"((?:[^"\\]|\\.)*)"\s*,\s*([^,{}]+?)\s*,\s*([^,{}]+?)\s*,\s*([^{}]*?)\s*\}', m.group(2)):
            try:
                size, crc = c_int(e.group(2)), c_int(e.group(3)) & 0xFFFFFFFF
            except Exception:
                problems.append(f"{source}: ROM sin evaluar {e.group(0)[:80]}")
                continue
            flags = e.group(4)
            roms.append({"name": e.group(1), "size": size, "crc": crc, "opt": "BRF_OPT" in flags,
                         "nodump": "BRF_NODUMP" in flags, "empty": flags.strip() in ("0", "")})
        descs[m.group(1)] = roms
    for m in re.finditer(r"\bSTD_ROM_PICK\s*\(\s*(\w+)\s*\)", text):
        picks[m.group(1)] = [m.group(1)]
    for m in re.finditer(r"\bSTDROMPICKEXT\s*\(\s*(\w+)\s*,\s*(\w+)\s*,\s*(\w+)\s*\)", text):
        picks[m.group(1)] = [m.group(2), m.group(3)]
    for m in re.finditer(r"\bSTD_ROM_FN\s*\(\s*(\w+)\s*\)", text):
        fns[m.group(1) + "RomInfo"] = m.group(1)
    for m in re.finditer(r"\bstruct\s+BurnDriver[DX]?\s+(\w+)\s*=\s*\{(.*?)\}\s*;", text, re.S):
        f = split_fields(m.group(2))
        if len(f) < 20:
            problems.append(f"{source}: driver {m.group(1)} con {len(f)} campos")
            continue
        # Orden de struct BurnDriver (burnint.h): nombre, padre, placa, samples, año, nombre completo, comentario, fabricante…
        drivers[m.group(1)] = {
            "source": source, "name": c_string(f[0]), "parent": c_string(f[1]), "board": c_string(f[2]),
            "year": c_string(f[4]) or "", "description": c_string(f[5]) or "", "comment": c_string(f[6]) or "",
            "manufacturer": c_string(f[7]) or "", "working": "BDF_GAME_WORKING" in f[13],
            "boardrom": "BDF_BOARDROM" in f[13], "rominfo": f[19].strip(),
        }
    return descs, picks, fns, drivers


def parse_core(root):
    src = os.path.join(root, "src")
    drv_dir = os.path.join(src, "burn", "drv")
    files, problems, all_descs = {}, [], collections.defaultdict(list)
    for dirpath, _, names in os.walk(drv_dir):
        for name in names:
            if name.endswith((".cpp", ".c")):
                source = os.path.relpath(os.path.join(dirpath, name), drv_dir).replace(os.sep, "/")
                files[source] = parse_file(os.path.join(dirpath, name), source, problems)
                for k, v in files[source][0].items():
                    all_descs[k].append(v)
    # Solo cuentan los drivers de pDriver[] en src/dep/generated/driverlist*.h (sin FBA_DEBUG)
    listed = set()
    for p in glob.glob(os.path.join(src, "dep", "generated", "driverlist*.h")):
        with open(p, encoding="latin-1") as f:
            t = preprocess(strip_comments(f.read()))
        if "pDriver[]" in t:
            listed |= set(re.findall(r"&\s*(BurnDrv\w+)", t[t.find("pDriver[]"):]))
    games = {}
    for source, (descs, picks, fns, drivers) in files.items():
        for var, d in drivers.items():
            if var not in listed:
                continue
            pick = picks.get(fns.get(d["rominfo"]))
            if pick is None:
                problems.append(f"{source}: {d['name']} usa {d['rominfo']}, que no sale de STD_ROM_FN en su archivo")
                continue
            parts = [descs[p] if p in descs else (all_descs[p][0] if len(all_descs.get(p, [])) == 1 else None) for p in pick]
            if None in parts:
                problems.append(f"{source}: {d['name']} sin tabla RomDesc {pick}")
                continue
            if d["name"] in games:
                continue  # BurnDrvNeoGeoMVS repite "neogeo"; vale el primero, la BIOS
            games[d["name"]] = {k: v for k, v in d.items() if k != "rominfo"} | {
                "roms": parts[0], "board_roms": parts[1] if len(parts) > 1 else []}
    return games, problems


# ---------------------------------------------------------------- DAT

def write_dat(games, core, version, commit, path):
    lines = ['<?xml version="1.0"?>',
             '<!DOCTYPE datafile PUBLIC "-//Logiqx//DTD ROM Management Datafile//EN" "http://www.logiqx.com/Dats/datafile.dtd">',
             "<datafile>", "\t<header>", f"\t\t<name>FB Alpha 2012 ({core})</name>",
             f"\t\t<description>FB Alpha v{version} - core {core} de libretro, commit {commit[:7]}, generado desde el código fuente</description>",
             "\t\t<category>Standard DatFile</category>", f"\t\t<version>{version}</version>",
             "\t\t<author>tools/fba2012.py</author>", '\t\t<clrmamepro forcenodump="ignore"/>', "\t</header>"]
    for name in sorted(games):
        g = games[name]
        attrs = f"name={quoteattr(name)}" + (' isbios="yes"' if g["boardrom"] else "")
        if g["parent"]:
            attrs += f" cloneof={quoteattr(g['parent'])} romof={quoteattr(g['parent'])}"
        elif g["board"]:
            attrs += f" romof={quoteattr(g['board'])}"
        desc = g["description"] + (f" [{g['comment']}]" if g["comment"] else "") + ("" if g["working"] or g["boardrom"] else " [no funciona]")
        lines += [f"\t<game {attrs}>", f"\t\t<description>{escape(desc)}</description>",
                  f"\t\t<year>{escape(g['year'])}</year>", f"\t\t<manufacturer>{escape(g['manufacturer'])}</manufacturer>"]
        parent = {r["crc"]: r["name"] for r in games[g["parent"]]["roms"] if r["crc"]} if g["parent"] in games else {}
        for r in g["roms"]:
            if r["empty"] or not r["name"] or not r["size"]:
                continue
            a = f"name={quoteattr(r['name'])}" + (f" merge={quoteattr(parent[r['crc']])}" if r["crc"] in parent else "")
            a += f' size="{r["size"]}"' + (' status="nodump"' if r["nodump"] or not r["crc"] else f' crc="{r["crc"]:08x}"')
            lines.append(f"\t\t<rom {a}/>")
        lines.append("\t</game>")
    lines.append("</datafile>")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")


def cmd_dat(args):
    os.makedirs(DAT_DIR, exist_ok=True)
    parsed = {}
    for core, (commit, sub, version, _) in CORES.items():
        repo = os.path.join(args.fuentes, core)
        if not os.path.isdir(os.path.join(repo, ".git")):
            subprocess.run(["git", "clone", "-q", "--filter=blob:none", "--no-checkout",
                            f"https://github.com/libretro/{core}.git", repo], check=True)
        subprocess.run(["git", "-C", repo, "-c", "advice.detachedHead=false", "checkout", "-q", commit], check=True)
        games, problems = parse_core(os.path.join(repo, sub))
        write_dat(games, core, version, commit, os.path.join(DAT_DIR, f"FB Alpha 2012 - {core} (v{version}).dat"))
        parsed[core] = {"commit": commit, "version": version, "games": games}
        print(f"{core:20} {len(games):5} drivers | commit {commit[:7]}" + (f" | avisos: {len(problems)}" if problems else ""))
        for p in problems:
            print("   ", p)
    with open(PARSED, "w", encoding="utf-8", newline="\n") as f:
        json.dump(parsed, f, ensure_ascii=False, separators=(",", ":"))


# ---------------------------------------------------------------- verificación

def load_parsed():
    if not os.path.exists(PARSED):
        sys.exit(f"Falta {PARSED}: ejecuta antes  python tools/fba2012.py dat")
    with open(PARSED, encoding="utf-8") as f:
        return json.load(f)


def read_zips(folder):
    zips = {}
    for name in sorted(os.listdir(folder)):
        if name.lower().endswith(".zip") and os.path.isfile(os.path.join(folder, name)):
            with zipfile.ZipFile(os.path.join(folder, name)) as z:
                zips[name[:-4]] = [(i.filename, i.CRC, i.file_size) for i in z.infolist() if not i.is_dir()]
    return zips


def archive_order(games, name):
    # BurnGetZipName: el propio juego, la placa y la cadena de padres
    g = games[name]
    order = [name] + ([g["board"]] if g["board"] else [])
    p = g["parent"]
    while p and p not in order:
        order.append(p)
        p = games[p]["parent"] if p in games else None
    return order


def verify(games, zips, name):
    # open_archive(): por cada zip, cada ROM se busca por CRC y, si no, por nombre; con tamaño distinto sigue buscando
    g = games[name]
    used = [a for a in archive_order(games, name) if a in zips]
    roms = [(r, False) for r in g["roms"]] + [(r, True) for r in g["board_roms"]]
    state, bios_found = {}, False
    for a in used:
        for i, (r, board) in enumerate(roms):
            if i in state and state[i][0]:
                continue
            if r["empty"] or not r["size"] or not r["crc"]:
                state[i] = (True, False)
                continue
            hit = next((e for e in zips[a] if e[1] == r["crc"]), None)
            by_name = hit is None
            if by_name:
                hit = next((e for e in zips[a] if e[0] == r["name"]), None)
            if hit is not None:
                bios_found |= board
                state[i] = (hit[2] == r["size"], by_name)
    missing, other_crc = [], []
    for i, (r, board) in enumerate(roms):
        if i in state and state[i][0]:
            if state[i][1]:
                other_crc.append(r["name"])
        elif not r["opt"] and not (g["board"] == "neogeo" and r["crc"] == NEOGEO_ASIA_S3 and bios_found):
            missing.append(r["name"] + (" (tamaño distinto)" if i in state else ""))
    status = "falla" if missing else ("arranca con CRC distinta" if other_crc else "ok")
    return {"status": status, "missing": missing, "other_crc": other_crc, "used": used}


def plan(parsed, zips):
    # Cada juego va a la carpeta de su core; los cores dedicados mandan salvo que el general lo arranque y el dedicado no
    choice = {}
    for n in zips:
        full = verify(parsed["fbalpha2012"]["games"], zips, n) if n in parsed["fbalpha2012"]["games"] else None
        ded = next((c for c in DEDICATED if n in parsed[c]["games"]), None)
        if ded:
            v = verify(parsed[ded]["games"], zips, n)
            choice[n] = (ded, v) if v["status"] in PLAYABLE or not (full and full["status"] in PLAYABLE) else ("fbalpha2012", full)
        elif full:
            choice[n] = ("fbalpha2012", full)
    folders, needed = collections.defaultdict(list), collections.defaultdict(set)
    for n, (core, v) in choice.items():
        g = parsed[core]["games"][n]
        if g["boardrom"] or n in NOT_GAMES or v["status"] not in PLAYABLE:
            continue
        for z in v["used"]:
            needed[z].add(n)
            if CORES[core][3] not in folders[z]:
                folders[z].append(CORES[core][3])
    rows = []
    for n in zips:
        core, v = choice.get(n, ("", None))
        g = parsed[core]["games"][n] if core else None
        if n in NOT_GAMES:
            dest, why = ["EXTRAS/ARCADE-otros"], NOT_GAMES[n]
        elif folders[n]:
            dest = folders[n]
            if g is None:
                why = f"padre sin driver propio; lo necesitan {len(needed[n])} clones"
            elif g["boardrom"]:
                why = f"BIOS de placa de {len(needed[n])} juegos"
            elif v["status"] not in PLAYABLE:
                why = f"no arranca, pero es padre de {len(needed[n] - {n})} juegos que sí: le faltan " + ", ".join(v["missing"])
            elif v["status"] == "ok":
                why = "arranca" + ("" if g["working"] else "; el core marca el driver como que no funciona")
            else:
                why = "arranca con alguna ROM de CRC distinta (puede fallar): " + ", ".join(v["other_crc"])
        elif g is None:
            dest, why = ["EXTRAS/ARCADE-sin-driver"], "no existe en FB Alpha 2012"
        elif g["boardrom"]:
            dest, why = ["EXTRAS/ARCADE-otros"], "BIOS de placa sin ningún juego que arranque"
        else:
            dest, why = ["EXTRAS/ARCADE-incompletos"], f"faltan ROMs de la v{parsed[core]['version']}: " + ", ".join(v["missing"])
        desc = g["description"] if g else ""
        rows.append({"zip": n + ".zip", "core": core, "estado": v["status"] if v else "sin driver",
                     "carpetas": " + ".join(dest), "juego": desc, "motivo": why})
    return rows


def cmd_verificar(args):
    parsed = load_parsed()
    rows = plan(parsed, read_zips(args.carpeta))
    print("zips por carpeta:")
    for k, v in sorted(collections.Counter(r["carpetas"] for r in rows).items()):
        print(f"  {k:45} {v:5}")
    if args.tsv:
        with open(args.tsv, "w", encoding="utf-8", newline="\n") as f:
            f.write("zip\tcore\testado\tcarpetas\tjuego\tmotivo\n")
            for r in rows:
                f.write("\t".join(r[k] for k in ("zip", "core", "estado", "carpetas", "juego", "motivo")) + "\n")
        print(f"detalle en {args.tsv}")


# ---------------------------------------------------------------- listas de RetroArch

def cmd_listas(args):
    parsed = load_parsed()
    for core, (_, _, version, folder) in CORES.items():
        path = os.path.join(ral.EMU, "ROMS", *folder.split("/"))
        if not os.path.isdir(path):
            continue
        zips = read_zips(path)
        games = parsed[core]["games"]
        info = ral.read_info(core)
        items, count, notes = [], collections.Counter(), []
        for n in zips:
            if n not in games:
                count["sin driver (padre de relleno)"] += 1
                continue
            g = games[n]
            if g["boardrom"] or n in NOT_GAMES:
                count["BIOS"] += 1
                continue
            v = verify(games, zips, n)
            count[v["status"]] += 1
            if v["status"] not in PLAYABLE:
                notes.append(f"{n}: no arranca, faltan " + ", ".join(v["missing"]))
                continue
            label = g["description"] + ("" if g["working"] else " [no funciona bien]")
            if v["status"] != "ok":
                notes.append(f"{n}: arranca con CRC distinta en " + ", ".join(v["other_crc"]))
            items.append({"path": f"{ral.PS4_ROMS}/{folder}/{n}.zip", "label": label,
                          "core_path": f"{ral.PS4_CORES}/{core}_libretro_ps4.self", "core_name": info["display_name"],
                          "crc32": "DETECT", "db_name": f"{info['corename']}.lpl"})
        if not items:
            continue
        items.sort(key=lambda i: i["label"].lower())
        playlist = {"version": "1.4", "default_core_path": f"{ral.PS4_CORES}/{core}_libretro_ps4.self",
                    "default_core_name": info["display_name"], "label_display_mode": 0, "right_thumbnail_mode": 0,
                    "left_thumbnail_mode": 0, "sort_mode": 0, "items": items}
        os.makedirs(ral.PLAYLISTS, exist_ok=True)
        with open(os.path.join(ral.PLAYLISTS, f"{info['corename']}.lpl"), "w", encoding="utf-8", newline="\n") as f:
            json.dump(playlist, f, indent=2, ensure_ascii=False)
            f.write("\n")
        print(f"{folder:20} {info['corename']:22} {len(items):5} juegos en la lista | " + ", ".join(f"{k}: {v}" for k, v in count.items()))
        for note in notes:
            print("   ", note)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("dat")
    p.add_argument("--fuentes", default=os.path.join(tempfile.gettempdir(), "fba2012-fuentes"))
    p = sub.add_parser("verificar")
    p.add_argument("carpeta")
    p.add_argument("--tsv")
    sub.add_parser("listas")
    args = parser.parse_args()
    {"dat": cmd_dat, "verificar": cmd_verificar, "listas": cmd_listas}[args.cmd](args)


if __name__ == "__main__":
    main()

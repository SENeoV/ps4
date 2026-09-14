#!/usr/bin/env python
# Juegos de DOS en la PS4: descomprime cada .zip/.dosz en su carpeta de emu/ROMS/DOS (o emu/ROMS/SCUMMVM si ScummVM lo
# ejecuta), le escribe el lanzador (.conf para dosbox_svn o .scummvm) y guarda el original en emu/ORIGINALES/DOS/.
#   python tools/dos.py CARPETA            simula: qué haría con cada .zip/.dosz de la carpeta
#   python tools/dos.py CARPETA --hacer    lo hace y lo apunta en cleanup-<fecha>.tsv
#   python tools/dos.py --informe          regenera emu/ROMS/DOS/LANZADORES.md a partir de los .conf

import collections
import datetime
import os
import re
import shutil
import subprocess
import sys
import unicodedata
import zipfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EMU = os.path.join(REPO, "emu")
ROMS_DOS = os.path.join(EMU, "ROMS", "DOS")
ROMS_SCUMMVM = os.path.join(EMU, "ROMS", "SCUMMVM")
ORIGINALES = os.path.join(EMU, "ORIGINALES", "DOS")
PS4_DOS = "/data/ROMS/DOS"
EXE = (".exe", ".com", ".bat")
# zipfile solo lee stored, deflate, bzip2 y lzma; los zip de los 90 usan a veces implode o shrink y van con 7-Zip
SUPPORTED = {0, 8, 12, 14}
SEVENZIP = r"C:\Program Files\7-Zip\7z.exe"

# Juegos que ScummVM ejecuta, por título normalizado -> id de ScummVM (comprobados en las tablas de detección de la rama 2.2)
SCUMMVM_IDS = {
    "castleofdrbrain": "castlebrain", "codenameiceman": "iceman", "conquestsofthelongbowthelegendofrobinhood": "longbow",
    "ecoquestthesearchforcetus": "ecoquest", "freddypharkasfrontierpharmacist": "freddypharkas", "jonesinthefastlane": "jones",
    "kingsquest4theperilsofrosella": "kq4sci", "kingsquest5absencemakestheheartgoyonder": "kq5",
    "kingsquest6heirtodaygonetomorrow": "kq6", "laurabowthecolonelsbequest": "laurabow", "leisuresuitlarry2": "lsl2",
    "leisuresuitlarry3passionatepattiinpursuitofthepulsatingpectorals": "lsl3", "mixedupfairytales": "fairytales",
    "peppersadventuresintime": "pepper", "policequest2thevengeance": "pq2", "policequest3thekindred": "pq3",
    "questforgloryiitrialbyfire": "qfg2", "questforgloryiiiwagesofwar": "qfg3", "spacequest3thepiratesofpestulon": "sq3",
    "spacequest4rogerwilcoandthetimerippers": "sq4", "spacequest5thenextmutation": "sq5", "donaldducksplayground": "ddp",
    "goldrush": "goldrush", "kingsquest2romancingthethrone": "kq2", "kingsquest3toheirishuman": "kq3",
    "leisuresuitlarryinthelandoftheloungelizards": "lsl1", "manhunternewyork": "mh1", "mixedupmothergoose": "mixedup",
    "spacequest2vohaulsrevenge": "sq2", "theblackcauldron": "bc", "loom": "loom", "zakmckrackenandthealienmindbenders": "zak",
    "gobliiins": "gob1", "gobliins2theprincebuffoon": "gob2", "weentheprophecy": "ween", "dreamweb": "dreamweb",
    "eyeofthebeholder": "eob", "flightoftheamazonqueen": "queen", "futurewars": "fw", "lureofthetemptress": "lure",
}
# Archivos que delatan un motor de ScummVM; el .scummvm va en la carpeta donde aparece el primero
SCUMMVM_MARKERS = ["resource.map", "resmap.000", "words.tok", "logdir", "00.lfl", "000.lfl", "disk01.lec", "intro.stk",
                   "dreamweb.r00", "queen.1", "queen.1c", "lure.exe", "eob.exe", "delphine.lnk", "part01", "sky.dsk", "dw.scn"]

TOOL_PREFIX = re.compile(r"^(install|instal|setup|config|setsound|sndsetup|soundset|sset|uninst|unins|readme|dos4gw|dos32a|pmode|"
                         r"cwsdpmi|pkunzip|pkunzjr|pkzip|unzip|lha|arj|catalog|mscdex|vesa|univbe|emm386|himem|keyb|register|deice|"
                         r"lzexe|pklite|loadpats|gravis|ipxdrv|ultrasnd|sblaster|makeboot|bootdisk|loadfix|rtm|dpmi|go32|disktest|"
                         r"emstest|memtest|detectcd|autokill|cleardrv|testblas|mpscopy|makemode|pkconfig|bbconfig)", re.I)
TOOL_EXACT = {"sound", "snd", "read", "info", "help", "helpme", "demo", "intro", "test", "view", "mode", "select", "edit", "editor",
              "speed", "check", "patch", "update", "debug", "convert", "credits", "slide", "command", "autoexec", "mouse",
              "choice", "ansi", "diag", "hint", "cheat", "order", "manual", "drivers", "driver", "midi", "gus", "mt32", "cfg",
              "ibmsnd", "ibmsnds", "tandysnd", "fixit", "copysave", "hd35", "animplay", "language", "int10", "hgc", "freakfac",
              "myexist", "mymkdir", "basica", "gwbasic", "ibmbio", "ibmdos", "comio", "ms", "mset", "apply", "loadpat"}
LAUNCHER = re.compile(r"^(play|run|runme|go|start|game|begin|load|loader|launch)$", re.I)
VARIANT = [(re.compile(r"(cga|tdy|tandy|herc|hgc|mono)$", re.I), -2), (re.compile(r"ega$", re.I), -1)]


def norm(title):
    return re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode().lower())


def safe_name(n):
    t = unicodedata.normalize("NFKD", n).encode("ascii", "ignore").decode()
    return re.sub(r'[<>:"/\\|?*]', "", t).rstrip(". ")


def valid83(name):
    return re.fullmatch(r"[A-Za-z0-9_\-!#$%&'(){}^~@]{1,8}(\.[A-Za-z0-9_\-!#$%&'(){}^~@]{0,3})?", name) is not None


def dos_path(rel):
    # DOSBox solo ve nombres 8.3: los componentes largos se aproximan con el alias ~1 que genera
    parts = []
    for p in rel.split("/"):
        if valid83(p):
            parts.append(p.upper())
        else:
            stem, ext = os.path.splitext(p)
            parts.append(re.sub(r"[^A-Za-z0-9]", "", stem).upper()[:6] + "~1" + re.sub(r"[^A-Za-z0-9.]", "", ext).upper()[:4])
    return "\\".join(parts)


def tokens(title):
    return [t for t in re.findall(r"[a-z0-9]+", title.lower()) if t not in ("the", "of", "and", "a", "in", "to", "an")]


def score(rel, title, stems):
    base = os.path.basename(rel)
    stem, ext = os.path.splitext(base.lower())
    if TOOL_PREFIX.match(stem) or stem in TOOL_EXACT:
        return -10
    s = 0
    if LAUNCHER.match(stem):
        s += 4 if ext == ".bat" else 3
    tt = tokens(title)
    initials = "".join(t[0] if not t.isdigit() else t for t in tt)
    if tt and (stem == tt[0] or stem == initials or (len(initials) > 1 and stem.startswith(initials))):
        s += 4
    elif tt and (stem.startswith(tt[0][:4]) or any(len(t) >= 3 and stem.startswith(t[:5]) for t in tt)):
        s += 3
    if ext == ".bat" and any(o == stem for o, e in stems if e != ".bat"):
        s += 1
    if any(o != stem and o.startswith(stem) for o, _ in stems):
        s += 1
    for rx, pen in VARIANT:
        if rx.search(stem):
            s += pen
    return s + (ext != ".com") - rel.count("/")


def analyze(path):
    name = os.path.basename(path)
    title = re.sub(r"\.(zip|dosz)$", "", name, flags=re.I)
    info = {"archivo": name, "titulo": title, "carpeta": safe_name(title)}
    try:
        zf = zipfile.ZipFile(path)
    except (zipfile.BadZipFile, OSError) as e:
        return info | {"estado": "roto", "nota": f"no se abre como zip ({e})"}
    with zf:
        members = [i for i in zf.infolist() if not i.is_dir()]
        legacy = any(i.compress_type not in SUPPORTED for i in members)
        info["legacy"] = legacy
        if legacy:
            if not os.path.exists(SEVENZIP) or subprocess.run([SEVENZIP, "t", path], capture_output=True).returncode != 0:
                return info | {"estado": "roto", "nota": "compresión antigua de PKZIP que 7-Zip no da por buena"}
        elif zf.testzip() is not None:
            return info | {"estado": "roto", "nota": "CRC incorrecta dentro del zip"}
        autoboot = next((zf.read(i).decode("latin-1").strip() for i in members
                         if os.path.basename(i.filename).upper() == "AUTOBOOT.DBP" and i.compress_type in SUPPORTED), None)
        nested = {}
        for i in members:
            if i.filename.lower().endswith(".zip") and i.filename.count("/") <= 1 and i.compress_type in SUPPORTED:
                try:
                    with zipfile.ZipFile(zf.open(i)) as inner:
                        nested[i.filename] = [n for n in inner.namelist() if not n.endswith("/")]
                except (zipfile.BadZipFile, NotImplementedError):
                    pass
    files = [i.filename for i in members]
    sizes = {i.filename: i.file_size for i in members}
    tops = {f.split("/")[0] for f in files}
    unwrap = None
    if len(tops) == 1 and all("/" in f for f in files):
        top = next(iter(tops))
        if name.lower().endswith(".dosz") or not valid83(top):
            unwrap = top
    strip = (lambda f: f[len(unwrap) + 1:]) if unwrap else (lambda f: f)
    rel = [strip(f) for f in files]
    for z, inner in nested.items():
        sub = os.path.splitext(strip(z))[0]
        rel += [f"{sub}/{n}" for n in inner]
    info |= {"unwrap": unwrap, "anidados": list(nested), "rel": rel}
    lower = {os.path.basename(f).lower(): f for f in rel}

    sid = SCUMMVM_IDS.get(norm(title))
    marker = next((lower[m] for m in SCUMMVM_MARKERS if m in lower), None)
    if sid:
        return info | {"estado": "scummvm", "id": sid, "dir_id": os.path.dirname(marker) if marker else ""}
    if any(f.lower().endswith((".ex_", ".dl_")) for f in rel) and not any(f.lower().endswith(EXE) and not TOOL_PREFIX.match(os.path.basename(f)) for f in rel):
        return info | {"estado": "windows", "nota": "instalador de Windows 3.x: DOSBox no lo ejecuta sin Windows"}
    if autoboot:
        exe = re.sub(r"^[A-Za-z]:[\\/]*", "", autoboot.split("\n")[0].strip()).replace("\\", "/")
        match = next((f for f in rel if f.lower() == exe.lower()), None)
        if match:
            return info | {"estado": "seguro", "exe": match, "alternativas": [], "nota": "ejecutable indicado en AUTOBOOT.DBP"}
    stems = [os.path.splitext(os.path.basename(f).lower()) for f in rel if f.lower().endswith(EXE) and f.count("/") <= 2]
    cands = sorted(((score(f, title, stems), f) for f in rel if f.lower().endswith(EXE) and f.count("/") <= 2),
                   key=lambda c: (-c[0], c[1].count("/"), -sizes.get(c[1], 0), c[1].lower()))
    good = [c for c in cands if c[0] > -5]
    alts = [f for _, f in cands[1:6]]
    if marker and not sid:
        info["nota_scummvm"] = f"tiene {os.path.basename(marker)}: puede que ScummVM lo ejecute"
    if good:
        estado = "seguro" if len(good) == 1 or good[0][0] - good[1][0] >= 2 else "dudoso"
        return info | {"estado": estado, "exe": good[0][1], "alternativas": alts}
    floppy = [f for f in rel if f.lower().endswith((".img", ".ima")) and sizes.get(f, 0) <= 2_900_000]
    if floppy and not cands:
        return info | {"estado": "disquete", "imagen": floppy[0]}
    return info | {"estado": "instalar", "alternativas": [f for _, f in cands[:6]],
                   "nota": "solo trae el instalador: hay que instalarlo antes (en DOSBox del PC o en la consola)"}


def conf_text(info, folder):
    mount = f'mount c "{PS4_DOS}/{folder}"'
    lines = [f"# {info['titulo']}: lanzador generado por tools/dos.py", f"# Estado: {info['estado']}"]
    if info.get("alternativas"):
        lines.append("# Alternativas: " + ", ".join(dos_path(a) for a in info["alternativas"]))
    if info.get("nota"):
        lines.append(f"# Nota: {info['nota']}")
    if info.get("nota_scummvm"):
        lines.append(f"# Nota: {info['nota_scummvm']}")
    lines.append("[autoexec]")
    if info["estado"] == "disquete":
        lines += [f'imgmount a "{PS4_DOS}/{folder}/{info["imagen"]}" -t floppy', "boot a:"]
    else:
        lines += [mount, "c:"]
        target = info.get("exe")
        start = os.path.dirname(target or (info.get("alternativas") or [""])[0])
        if start:
            lines.append(f"cd {dos_path(start)}")
        lines.append(os.path.basename(target).upper() if target else "dir /w")
    return "\n".join(lines) + "\n"


def unzip(path, dest, strip=None):
    with zipfile.ZipFile(path) as zf:
        members = [i for i in zf.infolist() if not i.is_dir()]
        if all(i.compress_type in SUPPORTED for i in members):
            for i in members:
                rel = i.filename[len(strip) + 1:] if strip else i.filename
                out = os.path.join(dest, *rel.split("/"))
                os.makedirs(os.path.dirname(out), exist_ok=True)
                with zf.open(i) as src, open(out, "wb") as f:
                    shutil.copyfileobj(src, f)
            return
    # Compresión antigua: 7-Zip extrae a una carpeta temporal y de ahí se mueve, quitando la carpeta envoltorio si la hay
    tmp = dest.rstrip("\\/") + ".tmp7z"
    subprocess.run([SEVENZIP, "x", "-y", f"-o{tmp}", path], check=True, stdout=subprocess.DEVNULL)
    base = os.path.join(tmp, *strip.split("/")) if strip else tmp
    for dirpath, _, names in os.walk(base):
        for n in names:
            src = os.path.join(dirpath, n)
            out = os.path.join(dest, os.path.relpath(src, base))
            os.makedirs(os.path.dirname(out), exist_ok=True)
            os.replace(src, out)
    shutil.rmtree(tmp)


def extract(path, dest, info):
    unzip(path, dest, info["unwrap"])
    for z in info["anidados"]:
        inner = os.path.join(dest, *(z[len(info["unwrap"]) + 1:] if info["unwrap"] else z).split("/"))
        unzip(inner, os.path.splitext(inner)[0])


def unique_folder(base, taken):
    name, k = base, 2
    while name.lower() in taken:
        name = f"{base} ({k})"
        k += 1
    taken.add(name.lower())
    return name


def rel(p):
    return os.path.relpath(p, REPO).replace(os.sep, "/")


def informe():
    rows = []
    for name in sorted(os.listdir(ROMS_DOS)):
        if not name.lower().endswith(".conf"):
            continue
        with open(os.path.join(ROMS_DOS, name), encoding="utf-8") as f:
            text = f.read()
        estado = (re.search(r"^# Estado: (\S+)", text, re.M) or [None, "?"])[1]
        alts = (re.search(r"^# Alternativas: (.*)$", text, re.M) or [None, ""])[1]
        notas = "; ".join(re.findall(r"^# Nota: (.*)$", text, re.M))
        auto = text.split("[autoexec]", 1)[-1].strip().splitlines()
        rows.append((name[:-5], estado, auto[-1] if auto else "", alts, notas))
    count = collections.Counter(r[1] for r in rows)
    lines = ["# DOS: lanzadores", "",
             "Cada juego está descomprimido en su carpeta y se arranca con su `.conf`, que monta la carpeta como `C:` y ejecuta el programa. "
             "Los genera `tools/dos.py`, que elige el ejecutable por su nombre. **Sin probar en la consola.**", "",
             "- `seguro`: un único candidato claro. `dudoso`: hay otros posibles (columna *Alternativas*); si no arranca el bueno, "
             "se cambia la última línea del `.conf`.",
             "- `instalar`: el zip solo trae el instalador; el `.conf` deja la consola de DOS en la carpeta para ejecutarlo.",
             "- `disquete`: arranca desde una imagen de disquete.", "",
             "Resumen: " + ", ".join(f"{k} {v}" for k, v in sorted(count.items())), "",
             "| Juego | Estado | Arranca con | Alternativas | Notas |", "|---|---|---|---|---|"]
    for juego, estado, cmd, alts, notas in rows:
        if estado != "seguro" or notas:
            lines.append(f"| {juego} | {estado} | `{cmd}` | {alts} | {notas} |")
    lines += ["", f"Los {count.get('seguro', 0)} juegos `seguro` sin notas no se listan."]
    with open(os.path.join(ROMS_DOS, "LANZADORES.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")
    print(f"LANZADORES.md: {len(rows)} juegos | " + ", ".join(f"{k}: {v}" for k, v in sorted(count.items())))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    if "--informe" in sys.argv:
        informe()
        return
    source = sys.argv[1]
    do = "--hacer" in sys.argv
    archives = sorted(f for f in os.listdir(source) if f.lower().endswith((".zip", ".dosz")) and os.path.isfile(os.path.join(source, f)))
    taken = {n.lower() for d in (ROMS_DOS, ROMS_SCUMMVM) if os.path.isdir(d) for n in os.listdir(d)}
    results = []
    for a in archives:
        info = analyze(os.path.join(source, a))
        base = info["carpeta"]
        info["carpeta"] = unique_folder(base, taken) if info["estado"] not in ("roto", "windows") else base
        results.append(info)
    count = collections.Counter(r["estado"] for r in results)
    print("estados: " + ", ".join(f"{k}: {v}" for k, v in sorted(count.items())))
    print(f"con compresión antigua (se extraen con 7-Zip): {sum(1 for r in results if r.get('legacy'))}")
    for r in results:
        if r["estado"] in ("dudoso", "instalar", "disquete", "roto", "windows") or r.get("nota_scummvm"):
            detalle = r.get("exe") or r.get("imagen") or r.get("nota", "")
            print(f"  [{r['estado']}] {r['archivo']}: {detalle} | alternativas {r.get('alternativas', [])[:3]} {r.get('nota_scummvm', '')}")
    if not do:
        return
    log_path = os.path.join(REPO, f"cleanup-{datetime.date.today().isoformat()}.tsv")
    new = not os.path.exists(log_path)
    with open(log_path, "a", encoding="utf-8", newline="\n") as log:
        if new:
            log.write("accion\torigen\tdestino\tmotivo\n")
        for r in results:
            src = os.path.join(source, r["archivo"])
            if r["estado"] in ("roto", "windows"):
                dest = os.path.join(EMU, "EXTRAS", "DOS-malos" if r["estado"] == "roto" else "DOS-otros", r["archivo"])
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                os.replace(src, dest)
                log.write(f"MOVIDO\t{rel(src)}\t{rel(dest)}\t{r['nota']}\n")
                continue
            base_dir = ROMS_SCUMMVM if r["estado"] == "scummvm" else ROMS_DOS
            game_dir = os.path.join(base_dir, r["carpeta"])
            extract(src, game_dir, r)
            log.write(f"EXTRAIDO\t{rel(src)}\t{rel(game_dir)}/\tjuego de DOS descomprimido para la consola ({r['estado']})\n")
            if r["estado"] == "scummvm":
                launcher = os.path.join(game_dir, *[p for p in r["dir_id"].split("/") if p], r["carpeta"] + ".scummvm")
                with open(launcher, "w", encoding="utf-8", newline="\n") as f:
                    f.write(r["id"] + "\n")
                log.write(f"CREADO\t\t{rel(launcher)}\tlanzador de ScummVM (id {r['id']})\n")
            else:
                launcher = os.path.join(ROMS_DOS, r["carpeta"] + ".conf")
                with open(launcher, "w", encoding="utf-8", newline="\n") as f:
                    f.write(conf_text(r, r["carpeta"]))
                log.write(f"CREADO\t\t{rel(launcher)}\tlanzador de dosbox_svn ({r['estado']}: {r.get('exe') or r.get('imagen') or 'sin ejecutable'})\n")
            dest = os.path.join(ORIGINALES, r["archivo"])
            os.makedirs(ORIGINALES, exist_ok=True)
            os.replace(src, dest)
            log.write(f"MOVIDO\t{rel(src)}\t{rel(dest)}\toriginal del juego, catalogado; la copia descomprimida está en {rel(game_dir)}/\n")
            log.flush()
    informe()


if __name__ == "__main__":
    main()

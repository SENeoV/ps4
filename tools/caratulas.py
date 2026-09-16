#!/usr/bin/env python
# Segunda pasada de carátulas: las que retroarch_lists.py y fba2012.py no encuentran por nombre exacto.
# Baja el índice de cada carpeta del servidor de libretro y casa por título: quita etiquetas ([cr X], (Alt), (Disk 1),
# (Side A), [!]…), traduce regiones de GoodTools ((U) → USA), y en arcade pasa del nombre corto del zip al nombre de
# FBNeo con su base de datos; si un clon no tiene carátula, hereda la de su padre.
#   python tools/caratulas.py                 todas las listas
#   python tools/caratulas.py --only "DOS" "Commodore - 64"
#   python tools/caratulas.py --simular       dice qué encontraría sin descargar nada
# El índice de cada carpeta se guarda en emu/RETROARCH/database/thumbs-index/ (no se versiona).

import argparse
import concurrent.futures
import html
import json
import os
import re
import shutil
import sys
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import retroarch_lists as ral  # noqa: E402

INDEX_DIR = os.path.join(ral.RA, "database", "thumbs-index")
FBA_JSON = os.path.join(ral.RA, "database", "dat", "fba2012.json")
FBNEO_RDB = os.path.join(ral.RDB_DIR, "FBNeo - Arcade Games.rdb")
FBNEO_RDB_URL = "https://raw.githubusercontent.com/libretro/libretro-database/master/rdb/FBNeo%20-%20Arcade%20Games.rdb"
# lista -> carpeta del servidor, cuando no se llaman igual
SERVER_FOLDER = {
    "Commodore - 64 (PRG)": "Commodore - 64",
    "FB Alpha 2012": "FBNeo - Arcade Games",
    "FB Alpha 2012 CPS-1": "FBNeo - Arcade Games",
    "FB Alpha 2012 CPS-2": "FBNeo - Arcade Games",
    "FB Alpha 2012 CPS-3": "FBNeo - Arcade Games",
    "FB Alpha 2012 Neo Geo": "FBNeo - Arcade Games",
}
GOODTOOLS = {"U": "USA", "E": "Europe", "J": "Japan", "W": "World", "G": "Germany", "F": "France", "S": "Spain", "I": "Italy",
             "UE": "USA, Europe", "JU": "Japan, USA", "UK": "Europe", "A": "Australia", "K": "Korea", "B": "Brazil", "C": "China"}
REGION_ORDER = ["USA", "World", "Europe", "USA, Europe", "Japan, USA", "Japan", "Germany", "France", "Spain", "Italy"]


def norm_title(s):
    s = re.sub(r"\[.*?\]|\(.*?\)", " ", s.lower())
    s = re.sub(r"\b(the|a|an)\b", " ", s)
    return " ".join(re.sub(r"[^a-z0-9]+", " ", s).split())


def paren_tokens(s):
    return set(re.findall(r"[a-z0-9]+", " ".join(re.findall(r"\((.*?)\)", s.lower()))))


def regions_of(label):
    tags = re.findall(r"\((.*?)\)", label)
    out = []
    for t in tags:
        if t in GOODTOOLS:
            out.append(GOODTOOLS[t])
        elif any(r in t for r in ("USA", "Europe", "Japan", "World", "Germany", "France", "Spain", "Italy", "Netherlands", "Australia")):
            out.append(t)
    return out


def fetch_index(folder):
    os.makedirs(INDEX_DIR, exist_ok=True)
    cache = os.path.join(INDEX_DIR, folder + ".txt")
    if os.path.exists(cache):
        with open(cache, encoding="utf-8") as f:
            return [l.rstrip("\n") for l in f if l.strip()]
    url = f"{ral.THUMB_SERVER}/{urllib.parse.quote(folder)}/Named_Boxarts/"
    try:
        with urllib.request.urlopen(url, timeout=120) as r:
            page = r.read().decode("utf-8", "replace")
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        print(f"  no se pudo bajar el índice de {folder}: {e}")
        return []
    names = [html.unescape(urllib.parse.unquote(m))[:-4] for m in re.findall(r'href="([^"]+\.png)"', page)]
    with open(cache, "w", encoding="utf-8") as f:
        f.write("\n".join(names) + "\n")
    return names


class Indice:
    def __init__(self, names):
        self.exact = set(names)
        self.by_title = {}
        for n in names:
            self.by_title.setdefault(norm_title(n), []).append(n)

    def buscar(self, label):
        # 1) tal cual; 2) sin etiquetas de variante; 3) por título, eligiendo la región más parecida
        for cand in (label, re.sub(r"\s*\[[^\]]*\]", "", label).strip(),
                     re.sub(r"\s*\((Alt|Disk|Disc|Side|Tape|Rev|v\d|Beta|Proto|Unl|Program|Docs)[^)]*\)", "", label, flags=re.I).strip()):
            if cand in self.exact:
                return cand
        cands = self.by_title.get(norm_title(label))
        if not cands:
            return None
        if len(cands) == 1:
            return cands[0]
        regs = regions_of(label)
        tokens = paren_tokens(label)
        for r in regs:
            same = [c for c in cands if f"({r})" in c or f"({r}," in c]
            if same:
                return max(same, key=lambda c: len(tokens & paren_tokens(c)))
        for r in REGION_ORDER:
            same = [c for c in cands if f"({r})" in c]
            if same:
                return same[0]
        return max(cands, key=lambda c: len(tokens & paren_tokens(c)))


def load_fbneo():
    if not os.path.exists(FBNEO_RDB):
        with urllib.request.urlopen(FBNEO_RDB_URL, timeout=120) as r, open(FBNEO_RDB, "wb") as f:
            f.write(r.read())
    by_zip = {}
    for rec in ral.read_rdb(FBNEO_RDB):
        rom, name = rec.get("rom_name"), rec.get("name")
        if isinstance(rom, str) and name:
            by_zip[rom.lower().removesuffix(".zip")] = name
    return by_zip


def descargar(folder, name, target):
    url = f"{ral.THUMB_SERVER}/{urllib.parse.quote(folder)}/Named_Boxarts/{urllib.parse.quote(name)}.png"
    for _ in range(2):
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                ral.save_thumbnail(r.read(), target)
            return True
        except urllib.error.HTTPError:
            return False
        except (urllib.error.URLError, TimeoutError, OSError):
            continue
    return False


def procesar(lista, simular):
    with open(os.path.join(ral.PLAYLISTS, lista + ".lpl"), encoding="utf-8") as f:
        items = json.load(f)["items"]
    folder = SERVER_FOLDER.get(lista, lista)
    indice = Indice(fetch_index(folder))
    if not indice.exact:
        return
    arcade = folder == "FBNeo - Arcade Games"
    fbneo = load_fbneo() if arcade else {}
    fba = json.load(open(FBA_JSON, encoding="utf-8")) if arcade else {}
    parents = {n: g.get("parent") for core in fba.values() for n, g in core["games"].items()} if arcade else {}
    thumbs_dir = os.path.join(ral.THUMBS, lista, "Named_Boxarts")
    pendientes, heredan = [], []
    for it in items:
        label = it["label"]
        target = os.path.join(thumbs_dir, ral.thumb_name(label) + ".png")
        if os.path.exists(target):
            continue
        clean = re.sub(r"\s*\[no funciona bien\]$", "", label)
        found = None
        if arcade:
            short = os.path.splitext(os.path.basename(it["path"]))[0]
            chain, seen = [short], set()
            while chain[-1] in parents and parents[chain[-1]] and parents[chain[-1]] not in seen:
                seen.add(chain[-1])
                chain.append(parents[chain[-1]])
            for i, z in enumerate(chain):
                cand = fbneo.get(z)
                found = indice.buscar(cand) if cand else None
                if not found and i == 0:
                    found = indice.buscar(clean)
                if found:
                    if i > 0:
                        heredan.append(label)
                    break
        else:
            found = indice.buscar(clean)
        if found:
            pendientes.append((found, target))
    print(f"{lista:28} {len(items):6} juegos | sin carátula {sum(1 for it in items if not os.path.exists(os.path.join(thumbs_dir, ral.thumb_name(it['label']) + '.png'))):5} | encontradas ahora {len(pendientes):5}"
          + (f" (heredadas del padre {len(heredan)})" if heredan else ""), flush=True)
    if simular or not pendientes:
        return
    # Varios juegos pueden apuntar a la misma imagen del servidor: se baja una vez y se copia
    por_nombre = {}
    for name, target in pendientes:
        if target not in por_nombre.setdefault(name, []):
            por_nombre[name].append(target)
    def uno(name):
        targets = por_nombre[name]
        if not descargar(folder, name, targets[0]):
            return 0
        for t in targets[1:]:
            shutil.copyfile(targets[0], t)
        return len(targets)
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        ok = sum(pool.map(uno, list(por_nombre)))
    print(f"{'':28} descargadas {ok} de {len(pendientes)}", flush=True)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", nargs="+", metavar="LISTA")
    parser.add_argument("--simular", action="store_true")
    args = parser.parse_args()
    listas = sorted(os.path.splitext(f)[0] for f in os.listdir(ral.PLAYLISTS) if f.endswith(".lpl"))
    for lista in listas:
        if args.only and lista not in args.only:
            continue
        procesar(lista, args.simular)


if __name__ == "__main__":
    main()

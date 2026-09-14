#!/usr/bin/env python
# Cruza el catálogo con los DAT de No-Intro que publica libretro-database (libres) y dice, sistema a sistema,
# qué volcados son buenos, cuáles no están en el DAT y cuántos juegos del DAT faltan.
#   python tools/verificar_dumps.py                  todos los sistemas con lista
#   python tools/verificar_dumps.py --sistema NES GB
#   python tools/verificar_dumps.py --faltan         además, los juegos del DAT que no tienes (son muchos)
# Compara por SHA-1: el de la ROM dentro del zip (columna rom_sha1) o el del archivo suelto.

import argparse
import csv
import hashlib
import os
import re
import sys
import urllib.parse
import urllib.request
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import retroarch_lists as ral  # noqa: E402

DAT_DIR = os.path.join(ral.RA, "database", "dat", "no-intro")
FUENTE = "https://raw.githubusercontent.com/libretro/libretro-database/master/metadat/no-intro"
ROM = re.compile(r'rom\s*\(\s*name\s+"?([^"\n]+?)"?\s+size\s+(\d+)(?:\s+crc\s+(\w+))?(?:\s+md5\s+(\w+))?(?:\s+sha1\s+(\w+))?', re.I)


def bajar_dat(db):
    destino = os.path.join(DAT_DIR, db + ".dat")
    if os.path.exists(destino):
        return destino
    os.makedirs(DAT_DIR, exist_ok=True)
    url = f"{FUENTE}/{urllib.parse.quote(db)}.dat"
    try:
        with urllib.request.urlopen(url, timeout=60) as r:
            datos = r.read()
    except urllib.error.HTTPError:
        return None
    with open(destino, "wb") as f:
        f.write(datos)
    return destino


def leer_dat(path):
    # {sha1: nombre de la ROM}; las entradas sin sha1 (algunas de No-Intro) se ignoran
    with open(path, encoding="utf-8", errors="replace") as f:
        texto = f.read()
    return {m.group(5).lower(): m.group(1) for m in ROM.finditer(texto) if m.group(5)}


def sha1_variantes(path):
    # Varias huellas por ROM, como en las listas: tal cual, la del zip y sin cabecera (iNES 16, copiador 512, Lynx 64, 7800 128)
    try:
        if path.lower().endswith(".zip"):
            with zipfile.ZipFile(path) as z:
                datos = z.read(next(m for m in z.infolist() if not m.is_dir()))
        else:
            with open(path, "rb") as f:
                datos = f.read()
    except (OSError, zipfile.BadZipFile, StopIteration):
        return []
    trozos = [datos]
    if datos[:4] == b"NES\x1a":
        trozos.append(datos[16:])
    if datos[:4] == b"LYNX":
        trozos.append(datos[64:])
    if datos[1:10] == b"ATARI7800":
        trozos.append(datos[128:])
    if len(datos) % 1024 == 512:
        trozos.append(datos[512:])
    return [hashlib.sha1(t).hexdigest() for t in trozos]


def catalogo_por_sistema():
    filas = {}
    with open(os.path.join(ral.REPO, "inventory.csv"), encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            filas.setdefault(r["system"], []).append(r)
    return filas


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser()
    parser.add_argument("--sistema", nargs="+", metavar="CARPETA")
    parser.add_argument("--faltan", action="store_true", help="lista también los juegos del DAT que no están")
    args = parser.parse_args()

    catalogo = catalogo_por_sistema()
    print(f"{'Sistema':10} {'Archivos':>8} {'Buenos':>7} {'Sin DAT':>8} {'Faltan':>7}  DAT")
    for carpeta, (db, *_) in ral.SYSTEMS.items():
        if args.sistema and carpeta not in args.sistema:
            continue
        filas = catalogo.get(carpeta.split("/")[0], [])
        if not filas:
            continue
        path = bajar_dat(db)
        if not path:
            print(f"{carpeta:10} {len(filas):8} {'—':>7} {'—':>8} {'—':>7}  sin DAT de No-Intro")
            continue
        dat = leer_dat(path)
        buenos, sin_dat = [], []
        vistos = set()
        for r in filas:
            sha1 = (r["rom_sha1"] or r["sha1"]).lower()
            if sha1 in dat:
                buenos.append(r["file"])
                vistos.add(sha1)
                continue
            # No cuadra: puede ser que el DAT use el hash sin la cabecera, así que se recalcula desde el archivo
            otros = [s for s in sha1_variantes(os.path.join(ral.EMU, "ROMS", carpeta.split("/")[0], *r["file"].split("/"))) if s in dat]
            if otros:
                buenos.append(r["file"])
                vistos.add(otros[0])
            else:
                sin_dat.append(r["file"])
        faltan = set(dat) - vistos
        print(f"{carpeta:10} {len(filas):8} {len(buenos):7} {len(sin_dat):8} {len(faltan):7}  {os.path.basename(path)}")
        for n in sin_dat[:10]:
            print(f"   sin DAT: {n}")
        if len(sin_dat) > 10:
            print(f"   ... y {len(sin_dat) - 10} más sin DAT (hacks, traducciones, variantes o volcados alterados)")
        if args.faltan:
            for sha1 in sorted(faltan)[:20]:
                print(f"   falta:   {dat[sha1]}")
            if len(faltan) > 20:
                print(f"   ... y {len(faltan) - 20} más que faltan")


if __name__ == "__main__":
    main()

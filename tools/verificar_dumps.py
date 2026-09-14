#!/usr/bin/env python
# Cruza el catálogo con los DAT de No-Intro que publica libretro-database (libres) y dice, sistema a sistema,
# qué volcados son buenos, cuáles no están en el DAT y cuántos juegos del DAT faltan.
#   python tools/verificar_dumps.py                  todos los sistemas con lista
#   python tools/verificar_dumps.py --sistema NES GB
#   python tools/verificar_dumps.py --faltan         además, los juegos del DAT que no tienes (son muchos)
#   python tools/verificar_dumps.py --bios           las BIOS de emu/BIOS contra el System.dat de libretro
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
# Carpetas que no tienen DAT de No-Intro que valga: se dice por qué en vez de dar ceros
SIN_DAT = {
    "C64": "el DAT de No-Intro de C64 solo cubre cartuchos; estas son imágenes de disco y cinta",
    "C64/PRG": "programas TOSEC, sin DAT de No-Intro",
    "DOS": "juegos descomprimidos; no hay DAT",
    "SCUMMVM": "juegos descomprimidos; no hay DAT",
}
FUENTE = "https://raw.githubusercontent.com/libretro/libretro-database/master/metadat/no-intro"
ROM = re.compile(r'rom\s*\(\s*name\s+"?([^"\n]+?)"?\s+size\s+(\d+)(?:\s+crc\s+(\w+))?(?:\s+md5\s+(\w+))?(?:\s+sha1\s+(\w+))?', re.I)
SYSTEM_DAT = "https://raw.githubusercontent.com/libretro/libretro-database/master/dat/System.dat"
# Subcarpetas de emu/BIOS que no son BIOS (software libre) o que repiten las de la raíz con nombre No-Intro
BIOS_NO = ("PPSSPP/", "bluemsx/", "scummvm/", "Game Gear/", "Master System/", "Sega CD/", "Sega Genesis/")


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


def verificar_bios(catalogo):
    # System.dat agrupa las BIOS por sistema: game ( name "Sega - Mega-CD - Sega CD" ... rom ( name "bios_CD_U.bin" ... sha1 ... ) )
    destino = os.path.join(os.path.dirname(DAT_DIR), "System.dat")
    if not os.path.exists(destino):
        with urllib.request.urlopen(SYSTEM_DAT, timeout=60) as r, open(destino, "wb") as f:
            f.write(r.read())
    with open(destino, encoding="utf-8", errors="replace") as f:
        texto = f.read()
    conocidas = {}
    for bloque in re.split(r"\ngame\s*\(", texto)[1:]:
        sistema = re.search(r'name\s+"([^"]+)"', bloque)
        for m in ROM.finditer(bloque):
            if m.group(5):
                conocidas[m.group(5).lower()] = (sistema.group(1) if sistema else "?", m.group(1))
    print(f"{'BIOS':40} {'Resultado'}")
    for r in catalogo.get("BIOS", []):
        if r["file"].startswith(BIOS_NO):
            continue
        hit = conocidas.get(r["sha1"].lower())
        if hit:
            print(f"{r['file']:40} ok: {hit[1]} ({hit[0]})")
        else:
            print(f"{r['file']:40} NO está en System.dat (otra revisión, o no es una BIOS conocida)")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser()
    parser.add_argument("--sistema", nargs="+", metavar="CARPETA")
    parser.add_argument("--faltan", action="store_true", help="lista también los juegos del DAT que no están")
    parser.add_argument("--bios", action="store_true", help="comprueba las BIOS contra System.dat en vez de las ROMs")
    args = parser.parse_args()

    catalogo = catalogo_por_sistema()
    if args.bios:
        verificar_bios(catalogo)
        return
    print(f"{'Sistema':10} {'Archivos':>8} {'Buenos':>7} {'Sin DAT':>8} {'Faltan':>7}  DAT")
    for carpeta, (db, *_) in ral.SYSTEMS.items():
        if args.sistema and carpeta not in args.sistema:
            continue
        if carpeta in SIN_DAT:
            print(f"{carpeta:10} {'—':>8} {'—':>7} {'—':>8} {'—':>7}  {SIN_DAT[carpeta]}")
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

#!/usr/bin/env python
# Genera las listas de juegos (.lpl) de RetroArch PS4 cruzando las ROMs con las bases de datos de libretro, y prepara las carátulas.
#   python tools/retroarch_lists.py            listas + informe de cobertura
#   python tools/retroarch_lists.py --thumbs   además descarga/copia las carátulas que falten

import argparse
import concurrent.futures
import io
import json
import os
import re
import struct
import sys
import urllib.parse
import urllib.request
import zipfile
import zlib

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EMU = os.path.join(REPO, "emu")
RA = os.path.join(EMU, "RETROARCH")
RDB_DIR = os.path.join(RA, "database", "rdb")
PLAYLISTS = os.path.join(RA, "playlists")
THUMBS = os.path.join(RA, "thumbnails")
PS4_ROMS = "/data/ROMS"
PS4_CORES = "/data/self/retroarch/cores"
THUMB_SERVER = "https://thumbnails.libretro.com"
THUMB_MAX_PX = 512

# carpeta -> (base de datos / nombre de lista, core por defecto)
SYSTEMS = {
    "NES": ("Nintendo - Nintendo Entertainment System", "nestopia"),
    "SNES": ("Nintendo - Super Nintendo Entertainment System", "snes9x2010"),
    "GB": ("Nintendo - Game Boy", "gearboy"),
    "GBC": ("Nintendo - Game Boy Color", "gearboy"),
    "GBA": ("Nintendo - Game Boy Advance", "mgba"),
    "SMS": ("Sega - Master System - Mark III", "genesis_plus_gx"),
    "GG": ("Sega - Game Gear", "genesis_plus_gx"),
    "MD": ("Sega - Mega Drive - Genesis", "genesis_plus_gx"),
    "ATARI2600": ("Atari - 2600", "stella2014"),
    "ATARI7800": ("Atari - 7800", "prosystem"),
    "PCE": ("NEC - PC Engine - TurboGrafx 16", "mednafen_pce_fast"),
    "NGP": ("SNK - Neo Geo Pocket", "mednafen_ngp"),
    "NGPC": ("SNK - Neo Geo Pocket Color", "mednafen_ngp"),
    "WS": ("Bandai - WonderSwan", "mednafen_wswan"),
    "WSC": ("Bandai - WonderSwan Color", "mednafen_wswan"),
    "LYNX": ("Atari - Lynx", "handy"),
    "32X": ("Sega - 32X", "picodrive"),
    "VB": ("Nintendo - Virtual Boy", "mednafen_vb"),
}


def read_info(core):
    d = {}
    with open(os.path.join(RA, "info", f"{core}_libretro.info"), encoding="utf-8", errors="replace") as f:
        for line in f:
            m = re.match(r'^(\w+)\s*=\s*"(.*)"', line.strip())
            if m:
                d[m.group(1)] = m.group(2)
    return d


def mp_read(buf, pos):
    # Lector mínimo de MessagePack, suficiente para el formato libretrodb
    b = buf[pos]
    pos += 1
    if b <= 0x7F:
        return b, pos
    if b >= 0xE0:
        return b - 0x100, pos
    if 0x80 <= b <= 0x8F:
        return mp_map(buf, pos, b & 0x0F)
    if 0x90 <= b <= 0x9F:
        return mp_array(buf, pos, b & 0x0F)
    if 0xA0 <= b <= 0xBF:
        n = b & 0x1F
        return buf[pos:pos + n].decode("utf-8", "replace"), pos + n
    if b == 0xC0:
        return None, pos
    if b in (0xC2, 0xC3):
        return b == 0xC3, pos
    if b in (0xC4, 0xC5, 0xC6):
        width = {0xC4: 1, 0xC5: 2, 0xC6: 4}[b]
        n = int.from_bytes(buf[pos:pos + width], "big")
        pos += width
        return bytes(buf[pos:pos + n]), pos + n
    if b in (0xCC, 0xCD, 0xCE, 0xCF):
        width = {0xCC: 1, 0xCD: 2, 0xCE: 4, 0xCF: 8}[b]
        return int.from_bytes(buf[pos:pos + width], "big"), pos + width
    if b in (0xD0, 0xD1, 0xD2, 0xD3):
        width = {0xD0: 1, 0xD1: 2, 0xD2: 4, 0xD3: 8}[b]
        return int.from_bytes(buf[pos:pos + width], "big", signed=True), pos + width
    if b in (0xD9, 0xDA, 0xDB):
        width = {0xD9: 1, 0xDA: 2, 0xDB: 4}[b]
        n = int.from_bytes(buf[pos:pos + width], "big")
        pos += width
        return buf[pos:pos + n].decode("utf-8", "replace"), pos + n
    if b in (0xDC, 0xDD):
        width = {0xDC: 2, 0xDD: 4}[b]
        return mp_array(buf, pos + width, int.from_bytes(buf[pos:pos + width], "big"))
    if b in (0xDE, 0xDF):
        width = {0xDE: 2, 0xDF: 4}[b]
        return mp_map(buf, pos + width, int.from_bytes(buf[pos:pos + width], "big"))
    raise ValueError(f"tipo MessagePack no soportado 0x{b:02x} en {pos - 1}")


def mp_map(buf, pos, n):
    out = {}
    for _ in range(n):
        k, pos = mp_read(buf, pos)
        v, pos = mp_read(buf, pos)
        out[k] = v
    return out, pos


def mp_array(buf, pos, n):
    out = []
    for _ in range(n):
        v, pos = mp_read(buf, pos)
        out.append(v)
    return out, pos


def read_rdb(path):
    with open(path, "rb") as f:
        buf = f.read()
    if buf[:7] != b"RARCHDB":
        raise ValueError(f"{path}: no es una base de datos libretrodb")
    meta_offset = struct.unpack(">Q", buf[8:16])[0]
    pos, records = 16, []
    while pos < meta_offset:
        rec, pos = mp_read(buf, pos)
        if rec is None:
            break
        records.append(rec)
    return records


def rom_crcs(path):
    # Varias huellas por ROM: tal cual y sin cabecera (iNES 16 bytes, copiador 512, Lynx 64, Atari 7800 128)
    if path.lower().endswith(".zip"):
        with zipfile.ZipFile(path) as z:
            member = next(m for m in z.infolist() if not m.is_dir())
            data = z.read(member)
    else:
        with open(path, "rb") as f:
            data = f.read()
    crcs = [zlib.crc32(data)]
    if data[:4] == b"NES\x1a":
        crcs.append(zlib.crc32(data[16:]))
    if data[:4] == b"LYNX":
        crcs.append(zlib.crc32(data[64:]))
    if data[1:10] == b"ATARI7800":
        crcs.append(zlib.crc32(data[128:]))
    if len(data) % 1024 == 512:
        crcs.append(zlib.crc32(data[512:]))
    return crcs


def thumb_name(label):
    return re.sub(r'[&*/:`<>?\\|"]', "_", label)


def build(system_dir, db, core):
    folder = os.path.join(EMU, "ROMS", system_dir)
    rdb_path = os.path.join(RDB_DIR, db + ".rdb")
    if not os.path.isdir(folder) or not os.path.exists(rdb_path):
        return [], 0
    info = read_info(core)
    exts = {"." + e for e in info["supported_extensions"].split("|")} | {".zip"}
    by_crc = {}
    for rec in read_rdb(rdb_path):
        crc = rec.get("crc")
        if isinstance(crc, bytes) and len(crc) == 4 and rec.get("name"):
            by_crc.setdefault(int.from_bytes(crc, "big"), rec["name"])

    items, matched = [], 0
    for name in sorted(os.listdir(folder)):
        full = os.path.join(folder, name)
        # README.md se colaría: Genesis Plus GX acepta la extensión .md
        if not os.path.isfile(full) or name.lower() == "readme.md" or os.path.splitext(name)[1].lower() not in exts:
            continue
        crcs = rom_crcs(full)
        hit = next((c for c in crcs if c in by_crc), None)
        label = by_crc[hit] if hit is not None else os.path.splitext(name)[0]
        matched += hit is not None
        items.append({
            "path": f"{PS4_ROMS}/{system_dir}/{name}",
            "label": label,
            "core_path": f"{PS4_CORES}/{core}_libretro_ps4.self",
            "core_name": info["display_name"],
            "crc32": f"{(hit if hit is not None else crcs[0]):08X}|crc",
            "db_name": f"{db}.lpl",
            "_local": full,
            "_matched": hit is not None,
        })
    if not items:
        return [], 0
    items.sort(key=lambda i: i["label"].lower())

    os.makedirs(PLAYLISTS, exist_ok=True)
    playlist = {
        "version": "1.4",
        "default_core_path": f"{PS4_CORES}/{core}_libretro_ps4.self",
        "default_core_name": info["display_name"],
        "label_display_mode": 0,
        "right_thumbnail_mode": 0,
        "left_thumbnail_mode": 0,
        "sort_mode": 0,
        "items": [{k: v for k, v in i.items() if not k.startswith("_")} for i in items],
    }
    with open(os.path.join(PLAYLISTS, db + ".lpl"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(playlist, f, indent=2, ensure_ascii=False)
        f.write("\n")
    return items, matched


def save_thumbnail(data, target):
    from PIL import Image
    img = Image.open(io.BytesIO(data))
    img.thumbnail((THUMB_MAX_PX, THUMB_MAX_PX))
    if img.mode not in ("RGB", "RGBA"):
        img = img.convert("RGBA")
    os.makedirs(os.path.dirname(target), exist_ok=True)
    img.save(target, "PNG", optimize=True)


def fetch_thumbnail(db, item):
    target = os.path.join(THUMBS, db, "Named_Boxarts", thumb_name(item["label"]) + ".png")
    if os.path.exists(target):
        return "ya estaba"
    if item["_matched"]:
        url = f"{THUMB_SERVER}/{urllib.parse.quote(db)}/Named_Boxarts/{urllib.parse.quote(thumb_name(item['label']))}.png"
        for _ in range(2):
            try:
                with urllib.request.urlopen(url, timeout=30) as r:
                    save_thumbnail(r.read(), target)
                return "servidor"
            except urllib.error.HTTPError as e:
                if e.code == 404:
                    break
            except (urllib.error.URLError, TimeoutError, OSError):
                continue
    system_dir = os.path.basename(os.path.dirname(item["_local"]))
    media = os.path.join(EMU, "MEDIA", system_dir, os.path.splitext(os.path.basename(item["_local"]))[0] + ".png")
    if os.path.exists(media):
        with open(media, "rb") as f:
            save_thumbnail(f.read(), target)
        return "MEDIA"
    return "sin carátula"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser()
    parser.add_argument("--thumbs", action="store_true")
    parser.add_argument("--only", nargs="+", metavar="CARPETA", help="procesar solo estas carpetas de sistema, p. ej. --only ATARI7800")
    args = parser.parse_args()

    total = {"juegos": 0, "reconocidos": 0}
    for system_dir, (db, core) in SYSTEMS.items():
        if args.only and system_dir not in args.only:
            continue
        items, matched = build(system_dir, db, core)
        if not items:
            print(f"{system_dir:9} sin juegos o sin base de datos: no se genera lista", flush=True)
            continue
        total["juegos"] += len(items)
        total["reconocidos"] += matched
        line = f"{system_dir:9} {len(items):5} juegos | reconocidos en la base de datos {matched:5} ({matched / len(items):.0%})"
        if args.thumbs:
            with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
                results = list(pool.map(lambda i: fetch_thumbnail(db, i), items))
            counts = {k: results.count(k) for k in ("servidor", "MEDIA", "ya estaba", "sin carátula")}
            line += " | carátulas " + ", ".join(f"{k}: {v}" for k, v in counts.items() if v)
        print(line, flush=True)
    print(f"TOTAL {total['juegos']} juegos, {total['reconocidos']} reconocidos ({total['reconocidos'] / max(total['juegos'], 1):.0%})")


if __name__ == "__main__":
    main()

#!/usr/bin/env python
# Inventario de ROMs/BIOS/APPS/PKG por SHA-1 y catálogo de punteros (un .ref por archivo) para ver los juegos en cada commit.
#   python tools/inventory.py           incremental: reutiliza hashes si ruta y tamaño no cambian
#   python tools/inventory.py --force   recalcula todo

import csv
import hashlib
import os
import sys
import zipfile
from collections import Counter

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EMU = os.path.join(REPO, "emu")
CSV_PATH = os.path.join(REPO, "inventory.csv")
MD_PATH = os.path.join(REPO, "INVENTORY.md")
CATALOG = os.path.join(REPO, "catalogo")
# Raíces que se catalogan. En ROMS cada subcarpeta es un sistema; las demás son un sistema cada una
ROOTS = {
    "ROMS": os.path.join(EMU, "ROMS"),
    "BIOS": os.path.join(EMU, "BIOS"),
    "APPS": os.path.join(EMU, "APPS"),
    "PKG": os.path.join(REPO, "pkg"),
    "LINUX": os.path.join(REPO, "linux"),
}
# Subcarpetas (relativas a la raíz) que no se catalogan: linux/src/ son submódulos con código fuente, y los packs
# de texturas extraídos en linux/texturas/ son decenas de miles de .dds; de ellos se cataloga el .7z, no cada textura
SKIP_DIRS = {"LINUX": {"src", "texturas/GZL"}}
FIELDS = ["system", "file", "bytes", "sha1", "rom_sha1", "content_id"]


def hash_stream(f):
    h = hashlib.sha1()
    for chunk in iter(lambda: f.read(1 << 20), b""):
        h.update(chunk)
    return h.hexdigest()


def file_sha1(path):
    with open(path, "rb") as f:
        return hash_stream(f)


def zipped_rom_sha1(path):
    # Los DAT de No-Intro/Redump listan el hash de la ROM, no el del .zip que la envuelve
    if not path.lower().endswith(".zip"):
        return ""
    try:
        with zipfile.ZipFile(path) as z:
            members = [m for m in z.infolist() if not m.is_dir()]
            if len(members) != 1:
                return ""
            with z.open(members[0]) as f:
                return hash_stream(f)
    except zipfile.BadZipFile:
        return ""


def pkg_content_id(path):
    # El nombre del archivo no siempre coincide con el Content ID real: se lee de la cabecera (magic 7F 'CNT', 36 bytes en 0x40)
    if not path.lower().endswith(".pkg"):
        return ""
    with open(path, "rb") as f:
        head = f.read(0x64)
    if head[:4] != b"\x7fCNT":
        return ""
    return head[0x40:0x64].split(b"\0", 1)[0].decode("ascii", "replace")


def catalog_relpath(system, file):
    return f"{system}/{file}" if system in ROOTS else f"ROMS/{system}/{file}"


def disk_path(system, file):
    base = ROOTS[system] if system in ROOTS else os.path.join(ROOTS["ROMS"], system)
    return os.path.join(base, file)


def scan():
    for root, base in ROOTS.items():
        skip = SKIP_DIRS.get(root, set())
        for dirpath, dirs, names in os.walk(base):
            here = os.path.relpath(dirpath, base).replace(os.sep, "/")
            dirs[:] = [d for d in dirs if d != ".git" and (d if here == "." else f"{here}/{d}") not in skip]
            for name in names:
                if name.lower().endswith(".md"):
                    continue
                rel = os.path.relpath(os.path.join(dirpath, name), base).replace(os.sep, "/")
                if root == "ROMS":
                    system, _, file = rel.partition("/")
                    if not file:
                        continue
                else:
                    system, file = root, rel
                yield system, file


def load_cache(force):
    if force or not os.path.exists(CSV_PATH):
        return {}
    with open(CSV_PATH, encoding="utf-8", newline="") as f:
        return {(r["system"], r["file"], r["bytes"]): r for r in csv.DictReader(f)}


def write_csv(rows):
    with open(CSV_PATH, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def write_summary(rows):
    per = {}
    for r in rows:
        c = per.setdefault(r["system"], [0, 0])
        c[0] += 1
        c[1] += int(r["bytes"])
    lines = [
        "# Inventario",
        "",
        "Generado por `tools/inventory.py`, que se ejecuta solo en cada commit. Detalle en [`inventory.csv`](inventory.csv) "
        "y un puntero por archivo en [`catalogo/`](catalogo/).",
        "",
        "Hash: **SHA-1**. En los `.zip`, la columna `rom_sha1` es el de la ROM interior, que es el que se contrasta con los DAT de No-Intro/Redump. "
        "En los `.pkg`, `content_id` es el Content ID leído de la cabecera.",
        "",
    ]
    if not rows:
        lines.append("_Todavía no hay contenido._")
    else:
        total = sum(int(r["bytes"]) for r in rows)
        lines += [f"**Total: {len(rows)} archivos**", "", "| Sistema | Archivos | Tamaño |", "|---|--:|--:|"]
        lines += [f"| {s} | {n} | {b / 1048576:.1f} MB |" for s, (n, b) in sorted(per.items())]
        lines.append(f"| **TOTAL** | **{len(rows)}** | **{total / 1048576:.1f} MB** |")
    with open(MD_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")


def sync_catalog(rows):
    stats = Counter()
    wanted = set()
    for r in rows:
        ptr = os.path.normpath(os.path.join(CATALOG, catalog_relpath(r["system"], r["file"]) + ".ref"))
        wanted.add(os.path.normcase(ptr))
        body = f"sha1 {r['sha1']}\nsize {r['bytes']}\n"
        if r["rom_sha1"]:
            body += f"rom-sha1 {r['rom_sha1']}\n"
        if r["content_id"]:
            body += f"content-id {r['content_id']}\n"
        try:
            with open(ptr, encoding="utf-8") as f:
                current = f.read()
        except FileNotFoundError:
            current = None
        if current != body:
            os.makedirs(os.path.dirname(ptr), exist_ok=True)
            with open(ptr, "w", encoding="utf-8", newline="\n") as f:
                f.write(body)
            stats["punteros nuevos" if current is None else "punteros actualizados"] += 1
    for dirpath, _, names in os.walk(CATALOG, topdown=False):
        for name in names:
            p = os.path.join(dirpath, name)
            if name.endswith(".ref") and os.path.normcase(os.path.normpath(p)) not in wanted:
                os.remove(p)
                stats["punteros eliminados"] += 1
        if dirpath != CATALOG and not os.listdir(dirpath):
            os.rmdir(dirpath)
    return stats


def main():
    cache = load_cache("--force" in sys.argv)
    rows, stats = [], Counter()
    for system, file in sorted(scan()):
        path = disk_path(system, file)
        size = str(os.path.getsize(path))
        hit = cache.get((system, file, size))
        if hit and hit.get("sha1"):
            sha1 = hit["sha1"]
            rom = hit["rom_sha1"] if hit.get("rom_sha1") is not None else zipped_rom_sha1(path)
            stats["reutilizados"] += 1
        else:
            sha1, rom = file_sha1(path), zipped_rom_sha1(path)
            stats["hasheados"] += 1
            if stats["hasheados"] % 500 == 0:
                print(f"  {stats['hasheados']} hasheados...", file=sys.stderr)
        # El Content ID no se cachea: son 100 bytes y así el CSV viejo sin la columna sigue valiendo
        rows.append({"system": system, "file": file, "bytes": size, "sha1": sha1, "rom_sha1": rom, "content_id": pkg_content_id(path)})
    write_csv(rows)
    write_summary(rows)
    stats.update(sync_catalog(rows))
    print(f"OK -> {len(rows)} archivos | " + ", ".join(f"{k}: {v}" for k, v in stats.items()))


if __name__ == "__main__":
    main()

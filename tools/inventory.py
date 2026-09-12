#!/usr/bin/env python
# Inventario de ROMs/BIOS/APPS por SHA-1 y catálogo de punteros (un .ref por archivo) para ver los juegos en cada commit.
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
ROOTS = ("ROMS", "BIOS", "APPS")
FIELDS = ["system", "file", "bytes", "sha1", "rom_sha1"]


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


def emu_relpath(system, file):
    return f"{system}/{file}" if system in ("BIOS", "APPS") else f"ROMS/{system}/{file}"


def scan():
    for root in ROOTS:
        base = os.path.join(EMU, root)
        for dirpath, _, names in os.walk(base):
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
        "Hash: **SHA-1**. En los `.zip`, la columna `rom_sha1` es el de la ROM interior, que es el que se contrasta con los DAT de No-Intro/Redump.",
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
        ptr = os.path.normpath(os.path.join(CATALOG, emu_relpath(r["system"], r["file"]) + ".ref"))
        wanted.add(os.path.normcase(ptr))
        body = f"sha1 {r['sha1']}\nsize {r['bytes']}\n" + (f"rom-sha1 {r['rom_sha1']}\n" if r["rom_sha1"] else "")
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
        path = os.path.join(EMU, emu_relpath(system, file))
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
        rows.append({"system": system, "file": file, "bytes": size, "sha1": sha1, "rom_sha1": rom})
    write_csv(rows)
    write_summary(rows)
    stats.update(sync_catalog(rows))
    print(f"OK -> {len(rows)} archivos | " + ", ".join(f"{k}: {v}" for k, v in stats.items()))


if __name__ == "__main__":
    main()

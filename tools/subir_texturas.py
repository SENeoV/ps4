#!/usr/bin/env python
# Sube una carpeta de texturas de Dolphin a la PS4 en Linux por SFTP, archivo a archivo (sin tar: el pendrive
# escribe a ~1,7 MB/s y extraer allí miles de archivos pequeños con la caché llena baja a 150 KB/s).
#   MSYS_NO_PATHCONV=1 python tools/subir_texturas.py <ip> linux/texturas/GZL/Effects [--destino ~/.local/share/dolphin-emu/Load/Textures/GZL]
# Salta los archivos que ya están con el mismo tamaño, imprime el progreso cada 50 archivos y al final compara
# el hash conjunto (SHA-1 de la lista de SHA-1 por ruta) del PC con el de la consola.
import hashlib
import os
import posixpath
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ps4linux  # noqa: E402

DESTINO = "/home/ps4/.local/share/dolphin-emu/Load/Textures/GZL"


def hash_local(carpeta):
    h = hashlib.sha1()
    for ruta in sorted(os.path.relpath(os.path.join(d, f), carpeta).replace(os.sep, "/") for d, _, fs in os.walk(carpeta) for f in fs):
        with open(os.path.join(carpeta, ruta), "rb") as f:
            h.update(hashlib.sha1(f.read()).hexdigest().encode() + b"\n")
    return h.hexdigest()


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    ip, local = args[0], args[1].rstrip("/\\")
    destino = sys.argv[sys.argv.index("--destino") + 1] if "--destino" in sys.argv else DESTINO
    nombre = os.path.basename(local)
    remoto = posixpath.join(destino, nombre)
    c = ps4linux.connect(ip)
    s = c.open_sftp()

    archivos = [(d, f) for d, _, fs in os.walk(local) for f in fs]
    total = sum(os.path.getsize(os.path.join(d, f)) for d, f in archivos)
    print(f"{nombre}: {len(archivos)} archivos, {total / 2**20:.0f} MiB -> {remoto}", flush=True)

    hechos = set()
    for d, _, _ in os.walk(local):
        rel = os.path.relpath(d, local).replace(os.sep, "/")
        rdir = remoto if rel == "." else posixpath.join(remoto, rel)
        if rdir not in hechos:
            try:
                s.stat(rdir)
            except OSError:
                partes = rdir.split("/")
                for i in range(2, len(partes) + 1):
                    p = "/".join(partes[:i])
                    try:
                        s.stat(p)
                    except OSError:
                        s.mkdir(p)
            hechos.add(rdir)

    t0, hecho, saltados = time.time(), 0, 0
    for i, (d, f) in enumerate(sorted(archivos), 1):
        lp = os.path.join(d, f)
        rp = posixpath.join(remoto, os.path.relpath(lp, local).replace(os.sep, "/"))
        tam = os.path.getsize(lp)
        try:
            if s.stat(rp).st_size == tam:
                saltados += 1
                hecho += tam
                continue
        except OSError:
            pass
        s.put(lp, rp)
        hecho += tam
        if i % 50 == 0 or i == len(archivos):
            el = time.time() - t0
            print(f"  {i}/{len(archivos)}  {hecho / 2**20:6.0f} MiB  {el:5.0f} s  {hecho / 2**20 / el if el else 0:4.1f} MiB/s", flush=True)
    s.close()
    print(f"subida en {time.time() - t0:.0f} s ({saltados} ya estaban)", flush=True)

    hl = hash_local(local)
    _, o, _ = c.exec_command(
        f"cd '{remoto}' && find . -type f -print0 | LC_ALL=C sort -z | xargs -0 sha1sum | awk '{{print $1}}' | sha1sum; "
        f"find . -type f | wc -l; grep -E '^Dirty' /proc/meminfo", timeout=1800)
    salida = o.read().decode().split()
    hr = salida[0]
    print(f"hash PC {hl}\nhash PS4 {hr}\n{'IDENTICO' if hl == hr else 'DIFIERE'} | archivos en la PS4: {salida[2]} | {' '.join(salida[3:])}")
    c.close()
    sys.exit(0 if hl == hr else 1)


if __name__ == "__main__":
    main()

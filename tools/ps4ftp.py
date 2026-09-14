#!/usr/bin/env python
# FTP de GoldHEN (puerto 2121, anónimo, modo pasivo y UNA sola conexión: falla con transferencias en paralelo).
#   python tools/ps4ftp.py listar IP RUTA                   lista una carpeta de la consola
#   python tools/ps4ftp.py subir IP LOCAL REMOTO [--hacer]  sube una carpeta; salta lo que ya está con el mismo tamaño
#   python tools/ps4ftp.py verificar IP LOCAL REMOTO        compara nombre y tamaño, archivo a archivo
#   python tools/ps4ftp.py partidas IP [--hacer]            baja /data/retroarch/savefiles a emu/SAVES
# Subir, borrar o renombrar en la consola solo después de confirmarlo con el usuario; listar y descargar es libre.

import argparse
import ftplib
import os
import sys
import time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUERTO = 2121
SAVES = os.path.join(REPO, "emu", "SAVES")


def conectar(ip):
    ftp = ftplib.FTP()
    ftp.connect(ip, PUERTO, timeout=30)
    ftp.login()
    ftp.set_pasv(True)
    ftp.encoding = "utf-8"
    return ftp


def listar_remoto(ftp, ruta):
    # MLSD no está en este servidor: se usa LIST y se distingue carpeta por la primera letra de los permisos
    entradas = []
    try:
        ftp.retrlines(f"LIST {ruta}", entradas.append)
    except ftplib.error_perm as e:
        raise SystemExit(f"no se puede listar {ruta}: {e}")
    salida = []
    for linea in entradas:
        partes = linea.split(maxsplit=8)
        if len(partes) < 9:
            continue
        nombre = partes[8]
        if nombre in (".", ".."):
            continue
        salida.append((nombre, linea[0] == "d", int(partes[4]) if not linea[0] == "d" else 0))
    return salida


def recorrer_remoto(ftp, ruta):
    # Devuelve {ruta relativa: tamaño} de todos los archivos que cuelgan de ruta
    encontrados = {}
    pendientes = [""]
    while pendientes:
        rel = pendientes.pop()
        for nombre, es_dir, size in listar_remoto(ftp, f"{ruta}/{rel}".rstrip("/")):
            hijo = f"{rel}/{nombre}".lstrip("/")
            if es_dir:
                pendientes.append(hijo)
            else:
                encontrados[hijo] = size
    return encontrados


def recorrer_local(carpeta):
    encontrados = {}
    for dirpath, dirs, names in os.walk(carpeta):
        dirs.sort()
        for n in sorted(names):
            p = os.path.join(dirpath, n)
            encontrados[os.path.relpath(p, carpeta).replace(os.sep, "/")] = os.path.getsize(p)
    return encontrados


def mkdirs(ftp, ruta, creadas):
    # El servidor no crea carpetas intermedias; se van creando una a una y se recuerda cuáles ya existen
    partes = ruta.strip("/").split("/")
    for i in range(1, len(partes) + 1):
        sub = "/" + "/".join(partes[:i])
        if sub in creadas:
            continue
        try:
            ftp.mkd(sub)
        except ftplib.error_perm:
            pass
        creadas.add(sub)


def humano(n):
    for u in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.1f} {u}"
        n /= 1024
    return f"{n:.1f} TB"


def cmd_listar(args):
    ftp = conectar(args.ip)
    for nombre, es_dir, size in sorted(listar_remoto(ftp, args.ruta)):
        print(f"  {'dir ' if es_dir else humano(size).rjust(9)}  {nombre}")
    ftp.quit()


def cmd_subir(args):
    local = os.path.abspath(args.local)
    locales = recorrer_local(local)
    raros = [n for n in locales if any(ord(c) > 127 for c in n)]
    if raros:
        print(f"AVISO: {len(raros)} nombres con caracteres no ASCII; en la consola no coincidirán: {raros[:5]}")
    ftp = conectar(args.ip)
    remotos = recorrer_remoto(ftp, args.remoto) if args.remoto_existe else {}
    faltan = {n: s for n, s in locales.items() if remotos.get(n) != s}
    total = sum(faltan.values())
    print(f"local {len(locales)} archivos ({humano(sum(locales.values()))}); en la consola {len(remotos)}; "
          f"por subir {len(faltan)} ({humano(total)})")
    if not args.hacer:
        print("simulación: añade --hacer para subir")
        ftp.quit()
        return
    creadas, hechos, bytes_ok, t0 = set(), 0, 0, time.time()
    for rel in sorted(faltan):
        destino = f"{args.remoto.rstrip('/')}/{rel}"
        mkdirs(ftp, os.path.dirname(destino), creadas)
        with open(os.path.join(local, *rel.split("/")), "rb") as f:
            try:
                ftp.storbinary(f"STOR {destino}", f, blocksize=1 << 16)
            except (ftplib.all_errors, OSError) as e:
                print(f"  fallo en {rel}: {e}; reconecto y reintento")
                ftp = conectar(args.ip)
                f.seek(0)
                ftp.storbinary(f"STOR {destino}", f, blocksize=1 << 16)
        hechos += 1
        bytes_ok += faltan[rel]
        if hechos % 25 == 0 or bytes_ok == total:
            v = bytes_ok / max(time.time() - t0, 0.1)
            print(f"  {hechos}/{len(faltan)} ({humano(bytes_ok)} de {humano(total)}, {humano(v)}/s)", flush=True)
    ftp.quit()
    print(f"subidos {hechos} archivos en {time.time() - t0:.0f} s. Comprueba con:  python tools/ps4ftp.py verificar {args.ip} {args.local} {args.remoto}")


def cmd_verificar(args):
    local = os.path.abspath(args.local)
    locales = recorrer_local(local)
    ftp = conectar(args.ip)
    remotos = recorrer_remoto(ftp, args.remoto)
    ftp.quit()
    faltan = sorted(set(locales) - set(remotos))
    sobran = sorted(set(remotos) - set(locales))
    distintos = sorted(n for n in set(locales) & set(remotos) if locales[n] != remotos[n])
    print(f"local {len(locales)} | consola {len(remotos)} | faltan {len(faltan)} | sobran {len(sobran)} | tamaño distinto {len(distintos)}")
    for titulo, lista in (("faltan", faltan), ("sobran", sobran), ("tamaño distinto", distintos)):
        for n in lista[:20]:
            print(f"  {titulo}: {n}")
        if len(lista) > 20:
            print(f"  ... y {len(lista) - 20} más")
    return 1 if faltan or distintos else 0


def cmd_partidas(args):
    os.makedirs(SAVES, exist_ok=True)
    ftp = conectar(args.ip)
    remotos = recorrer_remoto(ftp, "/data/retroarch/savefiles")
    nuevas = []
    for rel, size in sorted(remotos.items()):
        destino = os.path.join(SAVES, *rel.split("/"))
        if os.path.exists(destino) and os.path.getsize(destino) == size:
            continue
        nuevas.append((rel, size, destino))
    print(f"partidas en la consola: {len(remotos)}; distintas o nuevas: {len(nuevas)}")
    for rel, size, _ in nuevas:
        print(f"  {rel} ({humano(size)})")
    if nuevas and args.hacer:
        for rel, size, destino in nuevas:
            os.makedirs(os.path.dirname(destino), exist_ok=True)
            with open(destino, "wb") as f:
                ftp.retrbinary(f"RETR /data/retroarch/savefiles/{rel}", f.write)
            ok = os.path.getsize(destino) == size
            print(f"  bajada {rel}: {'tamaño correcto' if ok else 'TAMAÑO DISTINTO'}")
    elif nuevas:
        print("simulación: añade --hacer para bajarlas (sobrescribe la copia del PC, no la de la consola)")
    ftp.quit()


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("listar")
    p.add_argument("ip")
    p.add_argument("ruta")
    p = sub.add_parser("subir")
    p.add_argument("ip")
    p.add_argument("local")
    p.add_argument("remoto")
    p.add_argument("--hacer", action="store_true")
    p.add_argument("--remoto-existe", action="store_true", help="mira antes qué hay ya en la consola (más lento)")
    p = sub.add_parser("verificar")
    p.add_argument("ip")
    p.add_argument("local")
    p.add_argument("remoto")
    p = sub.add_parser("partidas")
    p.add_argument("ip")
    p.add_argument("--hacer", action="store_true")
    args = parser.parse_args()
    sys.exit({"listar": cmd_listar, "subir": cmd_subir, "verificar": cmd_verificar, "partidas": cmd_partidas}[args.cmd](args) or 0)


if __name__ == "__main__":
    main()

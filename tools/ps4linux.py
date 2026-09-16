#!/usr/bin/env python
# SSH/SFTP a la PS4 cuando está arrancada en Linux (usuario ps4, clave ps4). Necesita paramiko (pip install paramiko).
#   python tools/ps4linux.py "comando" [...]        ejecuta comandos en la IP fija de Linux (192.168.1.33); para root, "sudo -S ..." (la clave entra sola)
#   python tools/ps4linux.py <ip> "comando" [...]   lo mismo contra otra IP (el hotspot del PC, por ejemplo)
#   python tools/ps4linux.py [<ip>] --put local remoto   copia un archivo por SFTP y comprueba el tamaño
#   python tools/ps4linux.py ip                     comprueba la IP fija y, si no responde, busca la consola por la MAC del Wi-Fi
# Rutas remotas que empiezan por "/": en Git Bash hay que ejecutar con MSYS_NO_PATHCONV=1, si no las convierte a rutas de Windows.

import os
import re
import socket
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

USER, PASSWORD = "ps4", "ps4"
LINUX_IP = "192.168.1.33"  # IP fija de Linux en la red de casa (perfil DIGIFIBRA-PLUS-938F de NetworkManager, desde el 16-09-2026)
WIFI_MAC = "e8-9e-b4-9e-bd-6f"  # MAC del Wi-Fi de la PS4 (Información del sistema), la que usa Linux
SUBNETS = ("192.168.1.", "192.168.137.")  # red de casa y punto de acceso móvil de Windows


def ssh_open(ip, timeout=3):
    with socket.create_connection((ip, 22), timeout=timeout) as s:
        return s.recv(64).decode(errors="replace").strip()


def find_ip():
    try:
        print(f"{LINUX_IP}  ssh abierto: {ssh_open(LINUX_IP)}  (IP fija)")
        return
    except OSError:
        print(f"{LINUX_IP} no responde (IP fija): buscando por la MAC del Wi-Fi...")

    def ping(ip):
        subprocess.run(["ping", "-n", "1", "-w", "300", ip], capture_output=True)
    with ThreadPoolExecutor(96) as ex:
        list(ex.map(ping, [f"{s}{i}" for s in SUBNETS for i in range(1, 255)]))
    arp = subprocess.run(["arp", "-a"], capture_output=True, text=True).stdout
    found = [l.split()[0] for l in arp.splitlines() if re.search(WIFI_MAC, l, re.I)]
    for ip in found:
        try:
            print(f"{ip}  ssh abierto: {ssh_open(ip)}")
        except OSError as e:
            print(f"{ip}  ssh cerrado ({type(e).__name__}); en la PS4: sudo systemctl start sshd")
    if not found:
        print("No aparece la MAC de la PS4: ¿está en Linux y con Wi-Fi conectado?")


def connect(ip):
    import paramiko
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(ip, username=USER, password=PASSWORD, timeout=20, look_for_keys=False, allow_agent=False)
    return c


def put(c, local, remote):
    size = os.path.getsize(local)
    t0, last = time.time(), [0]
    sftp = c.open_sftp()

    def progress(done, total):
        if done - last[0] >= 100 * 2**20 or done == total:
            last[0] = done
            print(f"  {done / 2**20:7.0f} / {total / 2**20:.0f} MiB  {int(time.time() - t0)} s", flush=True)

    sftp.put(local, remote, callback=progress)
    rsize = sftp.stat(remote).st_size
    sftp.close()
    print("remoto:", rsize, "bytes", "OK" if rsize == size else "DIFIERE")


def run(c, cmd):
    print(f"$ {cmd}", flush=True)
    stdin, stdout, stderr = c.exec_command(cmd, timeout=600)
    if "sudo -S" in cmd:
        stdin.write(PASSWORD + "\n")
        stdin.flush()
    stdin.channel.shutdown_write()
    out = stdout.read().decode(errors="replace") + stderr.read().decode(errors="replace")
    print(out.replace("[sudo] password for ps4: ", "").replace("[sudo] password for ps4:", "").strip(), flush=True)


def main():
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        sys.exit(__doc__ or open(__file__, encoding="utf-8").read().split("\n\n")[0])
    if args[0] == "ip":
        return find_ip()
    ip = args.pop(0) if re.fullmatch(r"\d+(\.\d+){3}", args[0]) else LINUX_IP  # sin IP delante, la fija
    c = connect(ip)
    try:
        if args and args[0] == "--put":
            put(c, args[1], args[2])
        else:
            for cmd in args:
                run(c, cmd)
    finally:
        c.close()


if __name__ == "__main__":
    main()

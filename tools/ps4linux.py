#!/usr/bin/env python
# SSH/SFTP a la PS4 cuando está arrancada en Linux (usuario ps4, clave ps4). Necesita paramiko (pip install paramiko).
#   python tools/ps4linux.py ip                     busca la IP por la MAC del Wi-Fi de la PS4 en la red local
#   python tools/ps4linux.py <ip> "comando" [...]   ejecuta comandos; para root, escribir "sudo -S ..." (la clave entra sola)
#   python tools/ps4linux.py <ip> --put local remoto   copia un archivo por SFTP y comprueba el tamaño
# Rutas remotas que empiezan por "/": en Git Bash hay que ejecutar con MSYS_NO_PATHCONV=1, si no las convierte a rutas de Windows.

import os
import re
import socket
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

USER, PASSWORD = "ps4", "ps4"
WIFI_MAC = "e8-9e-b4-9e-bd-6f"  # MAC del Wi-Fi de la PS4 (Información del sistema), la que usa Linux
SUBNETS = ("192.168.1.", "192.168.137.")  # red de casa y punto de acceso móvil de Windows


def find_ip():
    def ping(ip):
        subprocess.run(["ping", "-n", "1", "-w", "300", ip], capture_output=True)
    with ThreadPoolExecutor(96) as ex:
        list(ex.map(ping, [f"{s}{i}" for s in SUBNETS for i in range(1, 255)]))
    arp = subprocess.run(["arp", "-a"], capture_output=True, text=True).stdout
    found = [l.split()[0] for l in arp.splitlines() if re.search(WIFI_MAC, l, re.I)]
    for ip in found:
        try:
            with socket.create_connection((ip, 22), timeout=3) as s:
                print(f"{ip}  ssh abierto: {s.recv(64).decode(errors='replace').strip()}")
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
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        sys.exit(__doc__ or open(__file__, encoding="utf-8").read().split("\n\n")[0])
    if sys.argv[1] == "ip":
        return find_ip()
    ip = sys.argv[1]
    c = connect(ip)
    try:
        if len(sys.argv) > 2 and sys.argv[2] == "--put":
            put(c, sys.argv[3], sys.argv[4])
        else:
            for cmd in sys.argv[2:]:
                run(c, cmd)
    finally:
        c.close()


if __name__ == "__main__":
    main()

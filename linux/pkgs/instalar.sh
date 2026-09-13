#!/bin/sh
# Instala sin red los paquetes de esta carpeta: dolphin-emu, ppsspp (con sus dependencias), iw y wireless-regdb.
# Bajados del Arch Linux Archive con las versiones exactas de las bases de datos de la distro (2026-03-09),
# asi que casan con las librerias instaladas y no hace falta pacman -Syu.
#
# En la PS4, desde LXTerminal (clave de sudo: ps4):
#   sudo mkdir -p /mnt
#   sudo mount /dev/sda1 /mnt
#   sudo sh /mnt/pkgs/instalar.sh
#   sudo umount /mnt
set -e
cd "$(dirname "$0")"
pacman -U --noconfirm ./*.pkg.tar.zst
echo
echo "Instalado: Dolphin y PPSSPP estan en el menu (Juegos)."
echo "Wi-Fi con todos los canales:  sudo iw reg set ES; nmcli device wifi rescan; sleep 5; nmcli device wifi list"

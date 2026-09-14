#!/bin/sh
# Instala ps4-cpu en la PS4 con Linux. Ejecutar con sudo desde la carpeta que contiene estos archivos:
#   sudo sh instalar.sh
# Deja: /usr/local/bin/ps4-cpu (root, 755), los iconos en /usr/local/share/ps4-cpu/, sudo sin clave solo para
# ese script, y los dos accesos directos en el escritorio y en el menú (Juegos y Sistema) del usuario ps4.
set -e
cd "$(dirname "$0")"
USUARIO=${SUDO_USER:-ps4}
CASA=$(getent passwd "$USUARIO" | cut -d: -f6)

install -o root -g root -m 755 ps4-cpu /usr/local/bin/ps4-cpu
install -d -m 755 /usr/local/share/ps4-cpu
install -o root -g root -m 644 rendimiento.svg normal.svg /usr/local/share/ps4-cpu/

# sudo sin clave únicamente para este script (es de root y no lo puede editar el usuario)
printf '%s\n' "$USUARIO ALL=(root) NOPASSWD: /usr/local/bin/ps4-cpu" > /etc/sudoers.d/ps4-cpu
chmod 440 /etc/sudoers.d/ps4-cpu
visudo -cf /etc/sudoers.d/ps4-cpu >/dev/null

# menú de aplicaciones y escritorio
install -o root -g root -m 644 ps4-cpu-rendimiento.desktop ps4-cpu-normal.desktop /usr/share/applications/
install -d -o "$USUARIO" -g "$USUARIO" "$CASA/Desktop"
install -o "$USUARIO" -g "$USUARIO" -m 755 ps4-cpu-rendimiento.desktop ps4-cpu-normal.desktop "$CASA/Desktop/"

echo "ps4-cpu instalado. Prueba: ps4-cpu estado"

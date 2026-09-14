# VNC — ver el escritorio de la PS4 desde el móvil

Instalado el 14-09-2026: **x11vnc 0.9.17** (con `libvncserver 0.9.15`), del Arch Linux Archive del 09-03-2026, la misma fecha que las bases de datos de la distro, para no arrastrar una actualización parcial. Comparte la sesión X real (`:0`), así que se ve lo mismo que en la tele, Dolphin incluido.

## Conectar desde Android

| | |
|---|---|
| App | Cualquier visor VNC: *AVNC* (libre, F-Droid/Play), *bVNC*, *RealVNC Viewer* |
| Dirección | la IP de Linux, puerto **5900** (`192.168.1.180:5900` el 14-09; cambia con DHCP, ver `README.md`) |
| Contraseña | `ps4linux` (solo LAN; el puerto no sale de la red de casa) |
| Calidad | en la app, bajar calidad o color a 256 si va a tirones por Wi-Fi |

Arranca solo con el escritorio (`~/.config/autostart/x11vnc.desktop`) y sigue en marcha aunque se desconecte el visor (`-forever -shared`). Registro en `~/.vnc/x11vnc.log`.

**Coste:** x11vnc lee la pantalla a base de sondeos; con un juego 3D a 1080p en movimiento es trabajo de CPU en la PS4, que es justo lo que le falta a Dolphin. Con el visor conectado, los fps pueden bajar. Para mirar sin jugar da igual; para medir rendimiento, desconectar el visor.

## Cómo se instaló (para repetirlo)

Sin tocar `/etc/pacman.conf`: una copia temporal que apunta al archivo con la fecha de las bases de datos, y `pacman -S` normal contra ella.

```sh
sed 's|^Include = /etc/pacman.d/mirrorlist|Include = /tmp/mirrorlist-archive|' /etc/pacman.conf > /tmp/pacman-archive.conf
echo 'Server = https://archive.archlinux.org/repos/2026/03/09/$repo/os/$arch' > /tmp/mirrorlist-archive
sudo pacman --config /tmp/pacman-archive.conf -S x11vnc
x11vnc -storepasswd ps4linux ~/.vnc/passwd
```

Vale para cualquier otro paquete mientras la distro siga con las bases de datos del 09-03-2026: mismo método que `pkgs/instalar.sh` pero por red.

Línea de arranque (la del `autostart`):

```
x11vnc -display :0 -auth guess -rfbauth ~/.vnc/passwd -rfbport 5900 -forever -shared -noxdamage -nap -quiet -o ~/.vnc/x11vnc.log
```

`-noxdamage` porque con Vulkan/OpenGL a pantalla completa XDAMAGE no avisa bien de los cambios y se ven trozos sin refrescar; `-nap` baja el sondeo cuando no cambia nada. Parar: `pkill x11vnc`. Quitar del arranque: borrar `~/.config/autostart/x11vnc.desktop`.

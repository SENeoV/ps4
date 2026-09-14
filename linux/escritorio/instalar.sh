#!/bin/sh
# Accesos directos en el escritorio de la PS4 con Linux. Se ejecuta como el usuario ps4, sin root:
#   sh instalar.sh
# Pone en ~/Desktop (y en el menú del usuario):
#   - el lanzador de cada programa instalado que aparezca en la lista PROGRAMAS;
#   - uno por cada imagen de juego que haya en ~/Juegos, que la abre directamente en Dolphin;
#   - "Juegos", que abre esa carpeta, y "Apagar Linux", que apaga como es debido (la partición no tiene journal).
# Es idempotente: no pisa lo que ya esté en el escritorio, así que no toca los accesos de ps4-cpu.
set -e
cd "$(dirname "$0")"
DEST="$HOME/Desktop"
MENU="$HOME/.local/share/applications"
JUEGOS="$HOME/Juegos"
mkdir -p "$DEST" "$MENU"

# Nombres de .desktop que instala cada programa, según la distro
# Nombres de .desktop que instala cada programa, según la distro (de PPSSPP solo la variante SDL: la Qt es la misma app)
PROGRAMAS="dolphin-emu org.DolphinEmu.dolphin-emu PPSSPPSDL ppsspp org.ppsspp.PPSSPP rpcs3 net.rpcs3.RPCS3 \
retroarch firefox chromium pcmanfm lxterminal xterm htop"

for base in $PROGRAMAS; do
    for dir in /usr/share/applications /usr/local/share/applications "$MENU"; do
        origen="$dir/$base.desktop"
        if [ -f "$origen" ] && [ ! -e "$DEST/$base.desktop" ]; then
            cp "$origen" "$DEST/$base.desktop"
            chmod 755 "$DEST/$base.desktop"
            echo "escritorio: $base"
            break
        fi
    done
done

# Un acceso por juego: Dolphin arranca la imagen sin pasar por su lista
for juego in "$JUEGOS"/*.rvz "$JUEGOS"/*.iso "$JUEGOS"/*.gcm "$JUEGOS"/*.wbfs; do
    [ -e "$juego" ] || continue
    nombre=$(basename "$juego")
    nombre=${nombre%.*}
    archivo="$DEST/ps4-juego-$(echo "$nombre" | tr ' /' '--').desktop"
    [ -e "$archivo" ] && continue
    cat > "$archivo" <<FIN
[Desktop Entry]
Type=Application
Name=$nombre
Comment=Abre $nombre directamente en Dolphin
Exec=dolphin-emu -b -e "$juego"
Icon=applications-games
Terminal=false
Categories=Game;
StartupNotify=false
FIN
    chmod 755 "$archivo"
    echo "escritorio: $nombre (Dolphin)"
done

# Los dos propios; la carpeta de juegos se ajusta al usuario que ejecuta el script
for f in ps4-juegos.desktop ps4-apagar.desktop; do
    sed "s#/home/ps4/Juegos#$JUEGOS#" "$f" > "$MENU/$f"
    chmod 644 "$MENU/$f"
    [ -e "$DEST/$f" ] || { cp "$MENU/$f" "$DEST/$f"; chmod 755 "$DEST/$f"; echo "escritorio: $f"; }
done

echo "Listo. En LXDE los iconos salen solos; si no, botón derecho en el escritorio y Actualizar."

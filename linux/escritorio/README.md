# Escritorio de la PS4 con Linux

El escritorio de LXDE arranca vacío. `instalar.sh` deja en `~/Desktop` (y en el menú del usuario) accesos directos a lo que hay instalado, a los juegos y a las dos acciones que más se repiten.

| Acceso | Qué hace |
|---|---|
| El de cada programa instalado | Copia su `.desktop` de `/usr/share/applications`: Dolphin, PPSSPP, RPCS3, RetroArch, navegador, gestor de archivos y terminal, **solo los que existan** |
| Uno por juego de `~/Juegos` | `dolphin-emu -b -e <imagen>`: abre esa imagen (`.rvz`, `.iso`, `.gcm`, `.wbfs`) sin pasar por la lista de Dolphin |
| **Juegos** | Abre `~/Juegos` en el gestor de archivos |
| **Apagar Linux** | `systemctl poweroff`. La partición del pendrive **no tiene journal**: hay que apagar siempre desde aquí o desde el menú, nunca por las bravas |

No toca los accesos de [`../cpu/`](../cpu/README.md) (*CPU 2,1 GHz* y *CPU 1,6 GHz*) ni ningún otro que ya esté en el escritorio: si el archivo existe, lo deja como está. Se puede volver a ejecutar cuando se añadan juegos o programas nuevos.

## Instalación

Con la consola en Linux y desde el PC:

```bash
MSYS_NO_PATHCONV=1 python tools/ps4linux.py <ip> --put linux/escritorio /home/ps4/escritorio
MSYS_NO_PATHCONV=1 python tools/ps4linux.py <ip> "sh /home/ps4/escritorio/instalar.sh"
```

No hace falta root. Si se añaden juegos a `~/Juegos` después, basta con repetir la segunda orden.

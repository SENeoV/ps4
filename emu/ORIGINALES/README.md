# ORIGINALES — archivos comprimidos originales, no se suben

Algunos juegos tienen que ir descomprimidos en la consola: DOS y ScummVM. Aquí se guarda cada archivo tal como vino, y es lo que se cataloga, en `catalogo/ORIGINALES/`. Las copias descomprimidas de `emu/ROMS/DOS/` y `emu/ROMS/SCUMMVM/` son decenas de miles de archivos y no se catalogan (`SKIP_DIRS` de `tools/inventory.py`).

| Carpeta | Contenido |
|---|---|
| `DOS/` | Los 995 `.zip` y `.dosz` de la colección de DOS y el `.rar` de *Warcraft II* (14-09-2026). De ellos salen los 956 juegos de `ROMS/DOS/` y los 40 de `ROMS/SCUMMVM/` |

Los nombres son los de origen, con tildes incluidas, porque estos archivos no van a la consola.

Si una carpeta descomprimida se estropea, se rehace con `tools/dos.py`: se copia su original a una carpeta de trabajo y se ejecuta `python tools/dos.py CARPETA --hacer`.

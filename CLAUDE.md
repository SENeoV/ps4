# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Qué es este repo

Repo de cosas varias para una PS4 Pro con GoldHEN (firmware 12.52): emulación retro con RetroArch, PKGs de homebrew y juegos, y trucos. Los binarios (ROMs, BIOS, PKGs) viven solo en el PC y en la consola; git versiona documentación, scripts y **referencias** a esos binarios.

**Todo en español:** documentación, salida de los scripts y mensajes de commit.

Documentos de estado, que hay que mantener al día cuando algo cambia:

- `PLAN.md`: checklist maestra y hoja de ruta por tandas, con las casillas "ROMs" y "Probado en PS4" de cada sistema.
- `PENDIENTES.md`: lista priorizada (P0–P9) de lo que falta. Cada tarea indica quién la hace: 🧑 el usuario (BIOS, ROMs y juegos tienen copyright y solo los aporta el usuario; Claude no los consigue), 🤖 Claude (software libre y datos abiertos que se pueden descargar y verificar) y 🎮 en la consola.
- `INSTALL.md`: mapeo de carpetas PC → PS4 y procedimiento de instalación por FTP.
- `emu/ROMS/<SISTEMA>/README.md`: core, extensiones y BIOS de cada sistema. `emu/emuladores-ps4.md`: matriz global y sistemas descartados.

## Comandos

No hay build, tests ni linter: son scripts de Python 3 (3.10 en este PC, Windows) sin dependencias externas, salvo Pillow para las carátulas.

```bash
python tools/inventory.py                  # regenera inventory.csv, INVENTORY.md y catalogo/ (incremental por ruta + tamaño)
python tools/inventory.py --force          # recalcula todos los SHA-1
python tools/retroarch_lists.py            # regenera las listas .lpl e imprime la cobertura por sistema
python tools/retroarch_lists.py --thumbs   # además descarga o copia las carátulas que falten
python tools/guard.py pre-commit           # la comprobación anti-binarios del hook (pre-push lee el stdin del hook)
cp tools/hooks/pre-commit tools/hooks/pre-push .git/hooks/   # instalar los hooks en un clon nuevo
```

## Arquitectura

### emu/: la colección, que no se copia tal cual a la consola

Cada subcarpeta tiene su propio destino en la PS4 (tabla completa en `INSTALL.md`): `APPS/*.pkg` → `/data/pkg/`, `BIOS/` → `/data/retroarch/system/`, `ROMS/<SISTEMA>/` → `/data/ROMS/<SISTEMA>/`, `RETROARCH/{info,playlists,database/rdb,thumbnails}` → `/data/retroarch/...` y `SAVES/` → `/data/retroarch/savefiles/`. `MEDIA/` (carátulas originales) y `EXTRAS/` (duplicados, volcados malos, archivos que no son juegos) no se suben.

`.gitignore` ignora `emu/**` excepto los directorios, los `*.md`, `emu/RETROARCH/info/*.info` y `emu/RETROARCH/playlists/*.lpl`. Las `.rdb` y las carátulas se quedan solo en local.

### Catálogo por referencia (inventory.py, guard.py y hooks)

- `tools/inventory.py` recorre `emu/ROMS`, `emu/BIOS` y `emu/APPS` y escribe en `catalogo/` un `.ref` por archivo, con la misma ruta más `.ref`. Cada uno guarda `sha1`, `size` y, en los zip de un solo archivo, `rom-sha1` de la ROM interior, que es el hash que se cruza con los DAT de No-Intro/Redump. Borra los `.ref` huérfanos. Los `.ref`, `inventory.csv` e `INVENTORY.md` no se editan a mano.
- El hook `pre-commit` ejecuta inventory.py, hace `git add -A catalogo inventory.csv INVENTORY.md` y llama a guard.py. Por eso **cualquier commit arrastra los cambios del catálogo** que haya pendientes en `emu/`, y tarda si hay muchas ROMs nuevas que hashear.
- `tools/guard.py` bloquea, en pre-commit y en pre-push, cualquier archivo añadido o modificado que git detecte como binario o que pese más de 5 MB. Los hooks no se saltan.
- `pkg/` todavía no se cataloga. Está pendiente ampliar inventory.py para que la recorra.

### Listas de RetroArch (retroarch_lists.py)

- `SYSTEMS` asigna a cada carpeta de `emu/ROMS` su base de datos de libretro (que es también el nombre de la lista) y el core por defecto. Para añadir un sistema hacen falta tres cosas: la entrada en `SYSTEMS`, su `.rdb` de libretro-database en `emu/RETROARCH/database/rdb/` (no está versionada) y el `.info` del core en `emu/RETROARCH/info/`.
- Reconoce los juegos por CRC32 contra la `.rdb` con un lector MessagePack propio, y prueba también sin cabeceras de copiador. Los juegos que no reconoce entran igual, con el nombre del archivo.
- Las rutas de las `.lpl` son las de la consola, no las del PC: `/data/ROMS/...` y `/data/self/retroarch/cores/<core>_libretro_ps4.self`. Formato JSON 1.4, el mismo del historial de la consola.
- Las carátulas van a `thumbnails/<lista>/Named_Boxarts/` con el nombre oficial saneado. Si el servidor de libretro no la tiene, se usa `emu/MEDIA/<SISTEMA>/<rom>.png`.
- Salta `README.md` a propósito, porque Genesis Plus GX acepta la extensión `.md`.

### Reorganizaciones: cleanup-YYYY-MM-DD.tsv

Cada reorganización de la colección se registra movimiento a movimiento en `cleanup-<fecha>.tsv`, con las columnas `accion`, `origen`, `destino` y `motivo`. Hasta ahora no se ha borrado nada: los duplicados, los volcados malos y lo que no es un juego se apartan a `emu/EXTRAS/`, y las carátulas a `emu/MEDIA/`. Borrar lo apartado lo decide el usuario (ver P9 en `PENDIENTES.md`).

## La consola

- PS4 Pro con GoldHEN 12.52. **No actualizar el firmware**: GoldHEN depende de esa versión exacta.
- RetroArch es el port no oficial basado en 1.8.8 (`SSNE10000`), con los cores del Core Installer (`SSNE20000`). Core, extensiones y BIOS se verifican contra los `.info` de `emu/RETROARCH/info/`, que corresponden a los cores instalados. RetroArch empareja cada core con su `.info` por nombre de archivo; por eso `mupen64plus_libretro.info` está renombrado.
- No usar el *Online Updater* ni el *Core Updater* de RetroArch, porque apuntan a Bintray, que cerró. Todo se sube por FTP.
- Las rutas distinguen mayúsculas (`/data/ROMS` ≠ `/data/roms`). Los nombres de archivo van sin tildes ni ñ: FileZilla los sube con otra codificación y dejan de coincidir con el PC y con sus partidas.
- Los romsets de arcade tienen que ser exactamente de la versión del core (FB Alpha 2012, MAME 2003-Plus) y no se mezclan.

### Acceso por FTP

- FTP de GoldHEN: puerto 2121, anónimo, modo pasivo y **una sola conexión**, porque falla con transferencias en paralelo. GoldHEN se carga a mano tras cada reinicio y el FTP se activa desde su menú; si no conecta, pedírselo al usuario.
- La IP cambia. Se ve en la consola en *Ajustes → Red → Ver estado de la conexión* y suele acabar en `.1.201`. Confirmarla con el usuario antes de conectar.
- **Leer es libre**: listar, descargar para verificar hashes, revisar `retroarch.cfg`. **Subir, borrar o renombrar en la consola, solo después de confirmarlo con el usuario.**

## pkg/: PKGs de homebrew, juegos y herramientas

Está ignorada por git y de momento fuera del catálogo. Sirve para:

- homebrew que se instala en la consola: se sube a `/data/pkg/` y se instala desde *Debug Settings → Package Installer*, igual que `emu/APPS`;
- juegos y backups en fPKG;
- instalación remota desde el PC, con Remote PKG Installer (`FLTZ00003`) o PS4 Toolset (`SAAT29385`), que están en `pkg/utils/`;
- herramientas de Windows, en `pkg/win/`.

Las tiendas están en `pkg/stores/`. El nombre del archivo no siempre coincide con el Content ID del paquete (`PS4_CUSA01116_v2.32.pkg` contiene `CUSA01015`), así que el Content ID se lee de la cabecera: magic `\x7FCNT` y 36 bytes a partir del offset `0x40`.

## ps4_cheats/: trucos

Es un submódulo de `shadps4-emu/ps4_cheats`, pensado para el emulador shadPS4 de PC: trucos JSON en `CHEATS/` y parches XML en `PATCHES/`. Está en `.gitmodules`, pero también en `.gitignore`, y no está registrado en el índice (`git submodule status` lo marca con `-`). Su contenido no se edita.

Por ahora solo se consulta. La idea es llevar trucos a GoldHEN en la consola, pero ese flujo aún no está definido: antes de convertir o subir nada hay que verificar el formato y la ruta que espera GoldHEN. En `pkg/` está el PS4 Cheats Manager (`CHTM00777`).

## Git

Commits directos a `main`, con el mensaje en español.

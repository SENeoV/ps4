# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Qué es este repo

Repo de cosas varias para una PS4 Pro con GoldHEN (firmware 12.52): emulación retro con RetroArch, PKGs de homebrew y juegos, trucos y Linux. Los binarios (ROMs, BIOS, PKGs, kernels, distros) viven solo en el PC y en la consola; git versiona documentación, scripts y **referencias** a esos binarios.

**Todo en español:** documentación, salida de los scripts y mensajes de commit.

Documentos de estado, que hay que mantener al día cuando algo cambia:

- `PLAN.md`: checklist maestra y hoja de ruta por tandas, con las casillas "ROMs" y "Probado en PS4" de cada sistema.
- `PENDIENTES.md`: lista priorizada (P0–P9) de lo que falta. Cada tarea indica quién la hace: 🧑 el usuario (BIOS, ROMs y juegos tienen copyright y solo los aporta el usuario; Claude no los consigue), 🤖 Claude (software libre y datos abiertos que se pueden descargar y verificar) y 🎮 en la consola.
- `INSTALL.md`: mapeo de carpetas PC → PS4 y procedimiento de instalación por FTP.
- `emu/ROMS/<SISTEMA>/README.md`: core, extensiones y BIOS de cada sistema. `emu/emuladores-ps4.md`: matriz global y sistemas descartados.
- `docs/auditoria-2026-09-13.md`: qué afirmaciones de la documentación se verificaron, cuáles eran falsas y con qué fuente. Consultarlo antes de repetir una afirmación técnica sobre la consola o los cores.
- `docs/historico/`: borradores antiguos, como el `init.md` original de ChatGPT. No usar como referencia: contradicen lo verificado.

## Comandos

No hay build, tests ni linter: son scripts de Python 3 (3.10 en este PC, Windows) sin dependencias externas, salvo Pillow para las carátulas y paramiko para `tools/ps4linux.py`.

```bash
python tools/inventory.py                  # regenera inventory.csv, INVENTORY.md y catalogo/ (incremental por ruta + tamaño)
python tools/inventory.py --force          # recalcula todos los SHA-1
python tools/retroarch_lists.py            # regenera las listas .lpl e imprime la cobertura por sistema
python tools/retroarch_lists.py --thumbs   # además descarga o copia las carátulas que falten
python tools/caratulas.py [--simular]      # segunda pasada: casa por título contra el índice del servidor (etiquetas, GoodTools, FBNeo, padre del clon)
python tools/fba2012.py dat                # DAT de los 5 cores FB Alpha 2012 sacados de su código fuente (commits de 2020)
python tools/fba2012.py verificar CARPETA  # zip a zip: con qué core arranca, qué ROMs le faltan y a qué carpeta va
python tools/fba2012.py listas             # verifica las carpetas de arcade y regenera sus 5 listas
python tools/dos.py CARPETA [--hacer]      # juegos de DOS: descomprime, crea el .conf (o .scummvm) y guarda el zip en ORIGINALES
python tools/guard.py pre-commit           # la comprobación anti-binarios del hook (pre-push lee el stdin del hook)
python tools/ps4linux.py ip                # con la PS4 en Linux: comprueba la IP fija (192.168.1.33) y, si no responde, la busca por la MAC del Wi-Fi
MSYS_NO_PATHCONV=1 python tools/ps4linux.py [<ip>] "comando" | --put local remoto   # SSH/SFTP a la PS4 en Linux (ps4/ps4); sin <ip>, la fija
cp tools/hooks/pre-commit tools/hooks/pre-push .git/hooks/   # instalar los hooks en un clon nuevo
```

## Arquitectura

### emu/: la colección, que no se copia tal cual a la consola

Cada subcarpeta tiene su propio destino en la PS4 (tabla completa en `INSTALL.md`): `APPS/*.pkg` → `/data/pkg/`, `BIOS/` → `/data/retroarch/system/`, `ROMS/<SISTEMA>/` → `/data/ROMS/<SISTEMA>/`, `RETROARCH/{info,playlists,database/rdb,thumbnails}` → `/data/retroarch/...` y `SAVES/` → `/data/retroarch/savefiles/`. `MEDIA/` (carátulas originales), `EXTRAS/` (duplicados, volcados malos, archivos que no son juegos) y `ORIGINALES/` (el zip original de lo que va descomprimido, hoy DOS y ScummVM; se cataloga) no se suben.

- **Arcade (FB Alpha 2012):** una carpeta por core (`ARCADE/FBNEO/` general, `FBNEO/CPS1/`, `CPS2/`, `CPS3/` y `NEOGEO/`). El padre de un clon y la BIOS de placa tienen que estar en la misma carpeta que el juego, porque el core solo busca ahí. El set es v0.2.97.24, verificado zip a zip con `tools/fba2012.py` contra los DAT de los cores (v0.2.97.28/29), que quedan en `emu/RETROARCH/database/dat/` sin versionar.
- **DOS:** cada juego descomprimido en `DOS/<Juego>/` y arrancado con `DOS/<Juego>.conf`, que monta la ruta absoluta `/data/ROMS/DOS/<Juego>`. El programa lo elige un heurístico, y los no seguros están en `DOS/LANZADORES.md`. Las aventuras que ScummVM ejecuta van a `SCUMMVM/<Juego>/` con un `.scummvm` que contiene el id del juego.

`.gitignore` ignora `emu/**` excepto los directorios, los `*.md`, `emu/RETROARCH/info/*.info` y `emu/RETROARCH/playlists/*.lpl`. Las `.rdb` y las carátulas se quedan solo en local. `linux/**` sigue la misma regla (directorios y `*.md`).

### Catálogo por referencia (inventory.py, guard.py y hooks)

- `tools/inventory.py` recorre las raíces de `ROOTS` (`emu/ROMS`, con un sistema por subcarpeta; `emu/BIOS`, `emu/APPS`, `emu/ORIGINALES`, `pkg/` y `linux/`, que son un sistema cada una; `SKIP_DIRS`, con rutas relativas a la raíz y comodines de `fnmatch`, salta `linux/src/`, el pack de texturas extraído en `linux/texturas/GZL/`, las carpetas de juego descomprimidas `ROMS/DOS/*` y `ROMS/SCUMMVM/*`, y cualquier `.git`) y escribe en `catalogo/` un `.ref` por archivo, con la misma ruta más `.ref` (`pkg/` va bajo `catalogo/PKG/`, `linux/` bajo `catalogo/LINUX/`). Cada uno guarda `sha1`, `size` y, según el tipo, `rom-sha1` de la ROM interior en los zip de un solo archivo (el hash que se cruza con los DAT de No-Intro/Redump) o `content-id` leído de la cabecera en los `.pkg`. Borra los `.ref` huérfanos. Los `.ref`, `inventory.csv` e `INVENTORY.md` no se editan a mano.
- El hook `pre-commit` ejecuta inventory.py, hace `git add -A catalogo inventory.csv INVENTORY.md` y llama a guard.py. Por eso **cualquier commit arrastra los cambios del catálogo** que haya pendientes en `emu/`, `pkg/` o `linux/`, y tarda si hay muchas ROMs nuevas que hashear (o una distro de 2 GB).
- `tools/guard.py` bloquea, en pre-commit y en pre-push, cualquier archivo añadido o modificado que git detecte como binario o que pese más de 5 MB. Los hooks no se saltan.

### Listas de RetroArch (retroarch_lists.py)

- `SYSTEMS` asigna a cada carpeta de `emu/ROMS` su base de datos de libretro (que es también el nombre de la lista) y el core por defecto. Para añadir un sistema hacen falta tres cosas: la entrada en `SYSTEMS`, su `.rdb` de libretro-database en `emu/RETROARCH/database/rdb/` (no está versionada) y el `.info` del core en `emu/RETROARCH/info/`.
- Reconoce los juegos por CRC32 contra la `.rdb` con un lector MessagePack propio, y prueba también sin cabeceras de copiador. Los juegos que no reconoce entran igual, con el nombre del archivo.
- Las rutas de las `.lpl` son las de la consola, no las del PC: `/data/ROMS/...` y `/data/self/retroarch/cores/<core>_libretro_ps4.self`. Formato JSON 1.4, el mismo del historial de la consola.
- Las carátulas van a `thumbnails/<lista>/Named_Boxarts/` con el nombre oficial saneado. Si el servidor de libretro no la tiene, se usa `emu/MEDIA/<SISTEMA>/<rom>.png`.
- Salta `README.md` a propósito, porque Genesis Plus GX acepta la extensión `.md`.
- Opciones de `SYSTEMS`: `rdb`, si la base de datos no se llama como la lista (C64/PRG), y `recursive`, para leer subcarpetas (C64/PRG por letras, ScummVM). Un `.m3u` sustituye en la lista a sus discos, que no salen sueltos. La lista de DOS son los `.conf` de la raíz de `DOS/`.
- Las listas de arcade no salen de aquí sino de `tools/fba2012.py listas`: en arcade manda el romset y el nombre sale del DAT del core.

### Reorganizaciones: cleanup-YYYY-MM-DD.tsv

Cada reorganización de la colección se registra movimiento a movimiento en `cleanup-<fecha>.tsv`, con las columnas `accion`, `origen`, `destino` y `motivo`. Si el registro pasa de 5 MB hay que partirlo por áreas (`cleanup-<fecha>-<área>.tsv`, como el del 14-09), porque `guard.py` no deja pasar archivos mayores. Hasta ahora no se ha borrado nada: los duplicados, los volcados malos y lo que no es un juego se apartan a `emu/EXTRAS/`, y las carátulas a `emu/MEDIA/`. Borrar lo apartado lo decide el usuario (ver P9 en `PENDIENTES.md`).

## La consola

- PS4 Pro **CUH-7116B** con firmware 12.52, southbridge Baikal B1 y GoldHEN 2.4b18.10. **No actualizar el firmware**: GoldHEN cubre de 5.05 a 13.00, y por encima de 13.00 hoy no hay exploit.
- RetroArch es el port no oficial de OsirisX basado en 1.8.8 (`SSNE10000`, release R4 de 2020), con los cores del Core Installer (`SSNE20000`). Core, extensiones y BIOS se contrastan con los `.info` de `emu/RETROARCH/info/`, pero con una salvedad: hay un `.info` por core instalado, **pero son los del libretro actual, no los de los cores de 2020** (la consola muestra mGBA 0.8.1 y su `.info` dice 0.10-dev), así que extensiones y BIOS pueden no coincidir con el core real. RetroArch empareja cada core con su `.info` por nombre de archivo. `mupen64plus_libretro.info` es una copia del de Mupen64Plus-Next, pero el port trae `mupen64plus` y `mupen64plus_next` como cores distintos, así que probablemente describe el core equivocado; se deja como está.
- No usar el *Online Updater* ni el *Core Updater* de RetroArch, porque apuntan a Bintray, que cerró. Todo se sube por FTP.
- Las rutas distinguen mayúsculas (`/data/ROMS` ≠ `/data/roms`). Los nombres de archivo van sin tildes ni ñ: FileZilla los sube con otra codificación y dejan de coincidir con el PC y con sus partidas.
- Los romsets de arcade tienen que ser exactamente de la versión del core (FB Alpha 2012, MAME 2003-Plus) y no se mezclan.

### Acceso por FTP

- FTP de GoldHEN: puerto 2121, anónimo, modo pasivo y **una sola conexión**, porque falla con transferencias en paralelo. Para carpetas, `tools/ps4ftp.py subir` (reanudable) y `verificar`. **ESET** toma una subida de miles de archivos por un escaneo de puertos y bloquea la IP de la consola una hora (`WinError 10013` en todo, ni ping): la IP `.201` tiene excepción IDS desde el 16-09; falta añadir la `.33` de Linux (o toda la red), y si cambia alguna, rehacerla. GoldHEN se carga a mano tras cada reinicio (en 12.52, con el exploit Poops desde un Blu-ray; procedimiento en `INSTALL.md`) y el FTP se activa desde su menú; si no conecta, pedírselo al usuario.
- La IP cambia. Se ve en la consola en *Ajustes → Red → Ver estado de la conexión* y suele acabar en `.1.201`. Confirmarla con el usuario antes de conectar.
- **Leer es libre**: listar, descargar para verificar hashes, revisar `retroarch.cfg`. **Subir, borrar o renombrar en la consola, solo después de confirmarlo con el usuario.**

## pkg/: PKGs de homebrew, juegos y herramientas

Sus archivos no entran en git (`*.pkg` y `*.exe` están ignorados por extensión) y se catalogan como sistema `PKG` en `catalogo/PKG/`. Sirve para:

- homebrew que se instala en la consola: se sube a `/data/pkg/` y se instala desde *Debug Settings → Package Installer*, igual que `emu/APPS`;
- juegos y backups en fPKG;
- instalación remota desde el PC, con Remote PKG Installer (`FLTZ00003`) o PS4 Toolset (`SAAT29385`), que están en `pkg/utils/`;
- herramientas de Windows, en `pkg/win/`;
- payloads para Payload Guest, en `pkg/payloads/` (van a `/data/payloads/`): los de Linux y las herramientas del host webkitty, con tabla de compatibilidad en su README. `no-12.52/` y `no-subir/` no se suben a la consola.

Las tiendas están en `pkg/stores/`. El nombre del archivo no siempre coincide con el Content ID del paquete (`PS4_CUSA01116_v2.32.pkg` contiene `CUSA01015`), así que el Content ID fiable es el `content-id` del `.ref`, que inventory.py lee de la cabecera del PKG.

## linux/: Linux en la consola

Proyecto aparte de RetroArch, en marcha desde el 2026-09-13 y sin probar aún en la consola. Todo lo verificado sobre esta consola y el procedimiento están en `linux/README.md`; `linux/ps4-linux-tutorial.md` es una copia literal de la guía de DionKill (la referencia viva de la escena; los textos antiguos de psxitarch/ps4linux.com están superados).

- La consola es **Baikal B1** (leído en *Información del sistema* con GoldHEN): kernel **5.4.247** (el 7.x aún no soporta Baikal), distro con **Mesa ≤ 25.1** (con Mesa 26 no hay GPU) y **solo disco externo**. Repetir estas tres restricciones antes de proponer cualquier kernel o distro.
- `linux/{loader,kernel,initramfs,distros}/` llevan los binarios, ignorados por git y catalogados como sistema `LINUX`. `linux/src/` son submódulos con el código fuente de loader, initramfs y `archlinux-on-ps4`; no se catalogan.
- El initramfs que instala en USB es el de DionKill (`linux/initramfs/initramfs.cpio.gz`); su `install-psxitarch.sh` exige pendrive MBR ≥ 22 GB y la distro como `psxitarch.tar.gz` (gzip, no xz). El de feeRnt (`initramfs/feernt-1.0/`) solo instala en interno y no sirve aquí.
- Linux no se sube por FTP: va en el pendrive. Se arranca desde la consola con **Payload Guest** (`/data/payloads/`, `pkg/payloads/`); desde el PC, enviando el `.bin` al BinLoader de GoldHEN (puerto 9090) **sin sondear antes el puerto**: una conexión vacía apaga el BinLoader. Tocar la consola sigue siendo decisión del usuario. Los intentos y sus resultados se anotan en "Registro de pruebas" de `linux/README.md`; Dolphin, en `linux/dolphin.md`.

**Reglas aprendidas el 13-09-2026, para no repetir errores:**

- **Pantalla negra o "sin señal" tras el payload: la tele antes que nada.** Los kernels 5.4 de Baikal sacan 1080p60 fijo sin leer el EDID y el monitor Samsung no lo acepta; la tele LG sí. Forzar el EDID en `bootargs.txt` no sirve. Se perdieron seis intentos antes de probarlo.
- **El pendrive va en un puerto frontal** (el loader solo mira `/mnt/usb0` y `/mnt/usb1`), y bien encajado (si no, USB 2.0).
- **`bootargs.txt` tiene que llevar `root=LABEL=psxitarch`** o el initramfs se para en la rescue shell pidiendo `resume-boot`. El instalador lo borra al reparticionar.
- **Antes de Linux, `ps4-fan-threshold60.bin`** en Payload Guest: en Baikal nadie mueve el ventilador y la CPU llega a 71 °C jugando; los apagones de la madrugada fueron eso.
- **La CPU arranca a 1,6 GHz (P2) y el kernel no la sube**: no hay `cpufreq`. `linux/cpu/ps4-cpu rendimiento` (icono en el escritorio) la pone a 2,1 GHz por MSR y Dolphin pasa de 27 a 30 fps; se pierde al reiniciar. A 2,1 GHz jugando, 77-80 °C.
- Con la PS4 en Linux, `tools/ps4linux.py` (SSH, `ps4`/`ps4`; `sudo systemctl start sshd` ya está `enabled`). IP fija **192.168.1.33** desde el 16-09-2026 (en el perfil Wi-Fi de NetworkManager, no en el router); `ps4linux.py ip` la busca por la MAC solo si no responde. **En Git Bash, `MSYS_NO_PATHCONV=1`** o cualquier argumento que empiece por `/` llega convertido a ruta de Windows (una copia por SFTP falló dos veces por esto).
- **Dolphin reescribe sus `.ini` al cerrarse**: editarlos solo con Dolphin cerrado. Por SSH se maneja con `xdotool` (`DISPLAY=:0`): Shift+F1 guarda estado, Ctrl+Q en la ventana principal (hay dos) más Alt+Y en el diálogo *Confirm* lo cierra. Detalle en `linux/dolphin.md`.
- **Los ajustes por juego de Dolphin van en `~/.local/share/dolphin-emu/GameSettings/<ID>.ini`**, no en `~/.config/dolphin-emu/GameSettings/`: ahí Dolphin no mira, y los que se escribieron ahí el 13 y el 14-09 no se aplicaron nunca. Se leen al arrancar el juego (*Stop* y volver a lanzar basta). Los fps se leen con `ffmpeg -f x11grab` (la captura F9 de Dolphin no lleva el contador).
- **Payload Guest** solo lista `.bin` en la raíz de `/data/payloads/` y no lee subcarpetas; un `meta.json` sin `icon` lo rompe. Los nombres de paquete de Arch con `:` (epoch) no valen en FAT32 ni NTFS (Windows crea un flujo alternativo): renombrar.
- **No fiarse de nombres ni de lo que diga una release sin leerla**: el `initramfs.cpio.gz` que había descargado Javi era el de feeRnt, que no instala en externo; el `psxitarch.tar.xz`, el rootfs de 7coil de 2022. Identificar cada archivo por tamaño y SHA-1 contra su origen, y leer las notas de la release.
- **Hashear solo archivos estables**: un SHA-1 calculado mientras Chrome aún cerraba la descarga salió distinto del definitivo. Comprobar que tamaño y `mtime` no cambian antes de dar un hash por bueno.

## ps4_cheats/ y goldhen_cheats/: trucos

Dos submódulos con formatos parecidos pero destinos distintos:

- `goldhen_cheats/` es [GoldHEN/GoldHEN_Cheat_Repository](https://github.com/GoldHEN/GoldHEN_Cheat_Repository), el repositorio oficial que lee el menú de trucos de GoldHEN en la consola. Archivos `{TITLEID}_{versión}.json`, `.shn` o `.mc4` en `json/`, `shn/` y `mc4/`; en la PS4 van a `/user/data/GoldHEN/cheats/json/`, `/shn/` y `/mc4/` (un formato por juego y versión). Se suben por FTP; solo sirven para juegos de PS4, no para lo emulado en RetroArch.
- `ps4_cheats/` es `shadps4-emu/ps4_cheats`, trucos JSON y parches XML para el emulador shadPS4 de PC. Es un gitlink en el índice pero no está inicializado (`git submodule status` lo marca con `-`). Se conserva como histórico; no vale para GoldHEN.

Ninguno de los dos se edita. En `pkg/` está el PS4 Cheats Manager (`CHTM00777`). Detalle en `emu/emuladores-ps4.md`, sección "Trucos".

## Git

Commits directos a `main`, con el mensaje en español.

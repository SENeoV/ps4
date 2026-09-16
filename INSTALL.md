# Instalación en la PS4 (vía FTP / FileZilla)

Procedimiento para instalar RetroArch y validar la cadena completa con una ROM de NES o SNES.

## Mapeo de carpetas: importante

`emu/` **no se copia tal cual** a la consola. Cada subcarpeta tiene su destino:

| En el PC | En la PS4 | Notas |
|---|---|---|
| `emu/APPS/*.pkg` | `/data/pkg/` | Es la ruta donde el instalador los detecta. Temporal: tras instalar se pueden borrar |
| `emu/BIOS/*` | `/data/retroarch/system/` | **Ruta obligatoria.** Es la carpeta "system" de RetroArch |
| `emu/ROMS/<SISTEMA>/` | `/data/ROMS/<SISTEMA>/` | RetroArch puede navegar a cualquier ruta; `/data/ROMS` mantiene el mismo esquema que el PC |
| `emu/RETROARCH/info/*.info` | `/data/retroarch/info/` | Sin ellos RetroArch no reconoce extensiones ni elige el core solo |
| `emu/RETROARCH/playlists/*.lpl` | `/data/retroarch/playlists/` | Listas de juegos ya generadas, cada juego con su nombre y su core. Se regeneran con `python tools/retroarch_lists.py` |
| `emu/RETROARCH/database/rdb/*.rdb` | `/data/retroarch/database/rdb/` | Bases de datos de libretro: permiten a RetroArch reconocer juegos al escanear |
| `emu/RETROARCH/thumbnails/<lista>/` | `/data/retroarch/thumbnails/<lista>/` | Carátulas. La carpeta de cada sistema tiene que llamarse igual que su lista |
| `emu/RETROARCH/assets/` | `/data/retroarch/assets/` | Iconos y fuentes del menú. Sin ellos Ozone funciona pero sin iconos (101 MB) |
| `emu/SAVES/*.srm` | `/data/retroarch/savefiles/` | Partidas guardadas. Carpeta plana (`sort_savefiles_enable = "false"`). Subir sobrescribe la partida de la consola |
| `emu/ROMS/ARCADE/FBNEO/` y sus `CPS1/`, `CPS2/`, `CPS3/`; `emu/ROMS/NEOGEO/` | `/data/ROMS/...` con la misma ruta | Cada carpeta es de un core. El padre de cada clon y la BIOS de placa (`neogeo.zip`, `pgm.zip`) van en la misma carpeta que el juego |
| `emu/ROMS/DOS/` | `/data/ROMS/DOS/` | Las carpetas de juego y sus `.conf`. Cada `.conf` monta `/data/ROMS/DOS/<Juego>`, así que en otra ruta no arranca |
| `emu/ROMS/SCUMMVM/` | `/data/ROMS/SCUMMVM/` | Cada juego en su carpeta, con su `.scummvm` dentro |
| `emu/MEDIA/`, `emu/EXTRAS/`, `emu/ORIGINALES/` | — | **No se suben.** Carátulas, archivos que no son juegos y los zips originales de lo que va descomprimido |
| `emu/RETROARCH/database/dat/` | — | **No se sube.** DAT de FB Alpha 2012 para `tools/fba2012.py` |
| `linux/` | Pendrive USB (no FTP) | Linux: `bzImage`, `initramfs.cpio.gz` y la distro van en un pendrive FAT32, y el payload se envía al BinLoader de GoldHEN (puerto 9090). Procedimiento en [`linux/README.md`](linux/README.md) |

La carpeta `/data/retroarch/` no existirá hasta que RetroArch se haya ejecutado al menos una vez.

## Antes de empezar

1. Cargar **GoldHEN** en la consola (hay que hacerlo tras cada reinicio, no es CFW permanente). Cómo, en la sección siguiente.
2. Activar el **servidor FTP** desde el menú de GoldHEN.
3. Anotar la IP de la PS4 (Ajustes → Red → Ver estado de la conexión).

## Cargar GoldHEN en firmware 12.52

En 12.50/12.52 el único exploit público es **Poops**, que entra por un disco Blu-ray (BD-JB). Cada vez que la consola se apaga o reinicia hay que repetirlo; el modo reposo lo conserva.

Hace falta una sola vez:

- Un Blu-ray grabado con `Poops.iso` (o `henloader_lp`, que combina Lapse 9.00–12.02 y Poops 9.00–13.00 con GoldHEN 2.4b18.7 dentro).
- Un USB en **exFAT o FAT32** (partición MBR) con el GoldHEN más reciente. La consola lleva **2.4b18.10** (leído en *Información del sistema* el 2026-09-13); la 2.4b18.9 (12-02-2026) añadió 13.00 y arregló el arranque de Linux, y la 2.4b18.8 no arranca Linux. No está en los releases de GitHub (el último ahí es 2.4b18); se descarga desde la cuenta de SiSTRo.
- En la PS4: **HDCP activado** y, en Ajustes → Sistema, **no** desactivar los avisos durante la reproducción de vídeo.
- Conexión a internet **una vez**, para que el reproductor de Blu-ray se active.

Cada arranque:

1. Conectar el USB, después meter el disco.
2. Abrir el disco desde el menú; en 12.50/12.52 elegir Poops.
3. Esperar a que aparezca la notificación de GoldHEN. Que el disco se expulse solo es normal.

Si falla: **reiniciar la consola** antes de volver a intentarlo. Reabrir la aplicación del disco sin reiniciar hace que falle más.

**No actualizar el firmware.** Hoy hay exploit hasta 13.00; por encima no hay nada público. Bloquear las actualizaciones automáticas desde GoldHEN.

Fuentes: [henloader_lp](https://github.com/GoldHEN/henloader_lp), [BD-JB-1252](https://github.com/DefKorns/BD-JB-1252), [GoldHEN 2.4b18.9](https://www.biteyourconsole.net/2026/02/12/scena-ps4-goldhen-si-aggiorna-alla-versione-2-4b18-9-con-supporto-per-il-firmware-13-00/).

En FileZilla:

```
Servidor:  <IP de la PS4>
Puerto:    2121
Modo:      anónimo, sin usuario ni contraseña
```

Conviene poner FileZilla en **modo pasivo** y **1 sola conexión simultánea** — el FTP de GoldHEN es frágil con transferencias en paralelo y el Core Installer son 1,4 GB.

## Paso 1 — RetroArch (la app)

1. Subir por FTP a `/data/pkg/`:
   ```
   emu/APPS/PS4_SSNE10000_v4.00_Unofficial_RetroArch.pkg   (27 MB)
   ```
2. En la consola: **Ajustes → Debug Settings → Game → Package Installer**. Por defecto solo lee del USB: poner antes **Package Source** en `Hdd [hdd:/data/pkg/]` o `All`. Seleccionar el PKG e instalar.
3. Comprobar que aparece el icono de RetroArch en el menú principal.
4. **Abrir RetroArch una vez** y cerrarlo. Esto crea `/data/retroarch/`, que hace falta para los pasos siguientes.

## Paso 2 — Core Installer

RetroArch en PS4 **viene sin cores**: sin este paso se abre pero no ejecuta nada.

1. Subir a `/data/pkg/`:
   ```
   emu/APPS/PS4_SSNE20000_v4.00_RetroArch_Core_Installer.pkg   (1385 MB)
   ```
   Es una subida larga. Si FileZilla corta a mitad, reanudar en vez de reiniciar.
2. Instalar igual que el paso 1.
3. Ejecutar la app **Core Installer** desde el menú de la PS4 e instalar los cores.

No hay alternativa: el *Core Updater* de este port apunta a Bintray, que cerró en 2021, y desde la release R3 los cores solo se instalan con esta app. El Core Installer de este repo pesa 1385 MB, lo mismo que `Cores_Installer_r4.pkg`; existe un `r4.1` (1,27 GB, "Fixed Speed") para cuando algún core va acelerado.

## Paso 3 — ROM de prueba

Se empieza por NES o SNES a propósito: **no necesitan BIOS**, así que si algo falla, el fallo está en RetroArch o el core, no en una BIOS mal nombrada.

1. Subir la ROM a `/data/ROMS/NES/` (o `/data/ROMS/SNES/`).
2. En RetroArch: **Load Content** → navegar a esa ruta → seleccionar la ROM.
3. Elegir el core:
   - NES → *Nestopia* o *QuickNES*
   - SNES → *Snes9x*

## Paso 4 — Validación

La cadena está bien si:

- [ ] RetroArch arranca
- [ ] Aparecen cores en la lista (si está vacía, falló el paso 2)
- [ ] La ROM carga y se ve imagen
- [ ] Hay sonido
- [ ] El mando responde
- [ ] Guardar y cargar un save state funciona

Con eso validado, ya se puede meter contenido en volumen y pasar a los sistemas que sí necesitan BIOS.

## Uso diario de RetroArch

Rutas verificadas en *Ajustes → Carpeta* de la consola (13-09-2026):

| Qué | Dónde | Notas |
|---|---|---|
| Menú rápido durante un juego | **Start + Select** | Es el único atajo configurado (`retroarch.cfg`). Desde ahí: guardar/cargar estado, trucos, cerrar contenido |
| Partidas (`.srm`) | `/data/retroarch/savefiles/` | Carpeta plana. Se escriben al cerrar el juego, salvo que se active el autoguardado (ver `PENDIENTES.md`, P0) |
| Guardados rápidos | `/data/retroarch/savestates/` | `<nombre de la ROM>.state`, `.state1`… |
| Capturas de pantalla | Junto a la ROM (`<Content Directory>`) | Acaban en `/data/ROMS/<SISTEMA>/`; conviene apuntarlas a otra carpeta |
| Trucos de RetroArch (`.cht`) | `/data/retroarch/cheats/` | Distintos de los de GoldHEN (`/user/data/GoldHEN/cheats/`) |
| Configuración | `/data/retroarch/retroarch.cfg` y `/data/retroarch/config/` | Copiar `retroarch.cfg` al PC antes de cambiar ajustes en volumen |
| Listas de juegos, bases de datos, carátulas | `/data/retroarch/{playlists,database/rdb,thumbnails}/` | Ver `emu/RETROARCH/README.md` |
| Cores | `/data/self/retroarch/cores/` | Los pone el Core Installer; no se tocan por FTP |

Salir de RetroArch: menú rápido → *Cerrar contenido*, y después *Salir de RetroArch* en el menú principal, o el botón PS. Si se sale con el botón PS a mitad de juego sin autoguardado, la partida del cartucho no se escribe.

## Si algo falla

| Síntoma | Causa habitual |
|---|---|
| RetroArch no aparece tras instalar | GoldHEN no estaba activo al instalar (sin verificar) |
| El Package Installer no ve el PKG | *Package Source* está en `Usb`; cambiarlo a `Hdd` o `All` |
| El exploit falla al cargar GoldHEN | Reiniciar la consola y repetir. Comprobar HDCP activado y el USB en exFAT/FAT32 |
| RetroArch se cierra nada más abrirse, sin llegar al menú | Visto el 2026-09-13: `retroarch.cfg` tenía `input_driver = "null"` (debe ser `"ps4"`; el mando se crea desde ese driver y sin él RetroArch cae al iniciar el menú). Bajar `retroarch.cfg` por FTP, corregir la línea y subirlo. Para diagnosticar, `log_to_file = "true"` escribe un registro por arranque en `/data/retroarch/logs/` |
| Abre pero no hay cores | Falta el paso 2 |
| El core carga pero la ROM no | Extensión no soportada, o ROM comprimida en un formato que el core no lee |
| Va a tirones | Core pesado para el sistema; probar el alternativo (QuickNES en vez de Nestopia) |
| El FTP corta | Modo pasivo y una sola conexión simultánea |
| De golpe nada del PC llega a la consola, ni el ping, y las conexiones dan `WinError 10013` (acceso prohibido) al instante | **ESET** ha bloqueado la IP de la consola: su protección contra ataques de red toma una subida larga por FTP (cada archivo abre una conexión a un puerto distinto) por un escaneo de puertos. Visto el 16-09-2026 tras 38 000 archivos. Quitarla de *Protección de red → IDS → Direcciones IP bloqueadas temporalmente* y añadirla a las excepciones IDS o a la zona de confianza. La excepción del 16-09 es solo para `192.168.1.201` (la consola en el sistema de PS4); en Linux coge otra IP por DHCP (`.180` la última vez), así que conviene ampliarla a las dos o a toda la red `192.168.1.0/24` |
| *Load Content* muestra las carpetas vacías | Faltan los `.info` en `/data/retroarch/info/`: sin ellos RetroArch no reconoce ninguna extensión y oculta todo |
| "Failed to load content" | El core cargado no es de ese sistema (p. ej. Snes9x con un `.nes`). *Load Core* primero, o subir los `.info` para que lo elija solo |
| Un juego con tildes o ñ sale con símbolos raros, o su partida no carga | FileZilla lo subió en otra codificación y el nombre en la PS4 ya no coincide con el del PC. Usar nombres sin tildes |
| Un juego del historial ya no abre tras mover o renombrar carpetas | El historial guarda la ruta antigua. Abrirlo de nuevo desde *Load Content* en la ruta nueva |

## Fuentes

- [Files and Directories — ConsoleMods](https://consolemods.org/wiki/PS4:Files_and_Directories)
- [Guía Poops 12.52 — onejailbreak](https://onejailbreak.com/blog/how-to-jailbreak-ps4-12-52-with-poops-exploit/)
- [How To Install PS4 FPKGS on GoldHEN](https://github.com/DrYenyen/How-To-Install-PS4-FPKGS)
- [RetroArch en PS4: instalación y configuración](https://bytesnbits.co.uk/play-real-arcade-and-console-games-on-the-ps4-with-retroarch-full-installation-and-setup/)
- [PS4 RetroArch Port — GBAtemp](https://gbatemp.net/threads/release-ps4-retroarch-port-unofficial.555028/)

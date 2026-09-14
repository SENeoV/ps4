# Pendientes — lo que falta para un sistema retro 100% funcional

Lista completa y priorizada de lo que falta **conseguir, preparar o configurar**. Está verificada contra la consola por FTP (solo lectura) y contra los `.info` de libretro-core-info de los 74 cores instalados (2026-09-13); los cores son del port de 2020 y los `.info` actuales, así que algún nombre de BIOS puede diferir (ver `emu/RETROARCH/README.md`).

**Quién lo hace:**

- 🧑 **Tú:** BIOS, juegos y hardware. Son archivos con copyright o volcados de tus originales, así que solo puedes aportarlos tú.
- 🤖 **Yo:** software libre y datos abiertos que puedo descargar, preparar y verificar.
- 🎮 **En la consola:** ajustes y pruebas que se hacen con el mando.

Rutas de la PS4: BIOS en `/data/retroarch/system/`, ROMs en `/data/ROMS/<SISTEMA>/` y paquetes en `/data/pkg/`. Todo sin tildes ni ñ en los nombres.

---

## P0 — Dejar al 100% lo que ya está subido

8 sistemas y 5094 juegos: NES, SNES, GB, GBC, GBA, SMS, GG y MD.

### Pruebas

- [ ] 🎮 Probar un juego de **SNES, GB, GBC, GG y MD**. NES, GBA y SMS ya están probados
- [ ] 🎮 Cargar una partida de GBA subida (Castlevania, Pokemon Rojo fuego…) y comprobar que conserva el progreso
- [ ] 🎮 Borrar del historial las 2 entradas que apuntan a la ruta vieja `/data/roms`

### Ajustes que hoy faltan (verificado en `retroarch.cfg`)

- [ ] 🎮 **Autoguardado de partidas.** *Ajustes → Guardado → Intervalo de autoguardado de SaveRAM* = 10 s. Ahora no está definido: la partida solo se escribe al cerrar el juego, y si sales con el botón PS o se cuelga, se pierde
- [ ] 🎮 **Atajos de mando.** Ahora solo hay Start+Select para el menú. Asignar en *Ajustes → Entrada → Atajos* una tecla para habilitar atajos, y botones para guardar estado, cargar estado, avance rápido y salir del juego
- [ ] 🎮 **Core de GBA:** los juegos se abren con `mednafen_gba`. Cargar con **mGBA** y fijarlo como core por defecto del sistema. Las partidas `.srm` sirven igual. Si usas la lista de GBA ya generada, esta ya abre cada juego con mGBA
- [ ] 🎮 **Shaders:** están activados (`video_shader_enable = true`). Si algún juego va a tirones, desactivarlos es lo primero que hay que probar
- [ ] 🎮 **No usar el *Online Updater* ni el *Core Updater* de RetroArch:** apuntan a Bintray, que cerró. Todo se sube por FTP

### Listas de juegos y carátulas

Preparado el 2026-09-13 en `emu/RETROARCH/`. Detalle y resultados por sistema en [`emu/RETROARCH/README.md`](emu/RETROARCH/README.md).

- [x] 🤖 18 bases de datos `.rdb` de libretro-database, con formato comprobado frente a la versión de RetroArch 1.8.8
- [x] 🤖 18 listas con 6986 juegos: los 8 sistemas ya subidos y los 10 de la Tanda 1. Cada juego lleva su core; 6249 (89%) aparecen con su nombre oficial y el resto con el nombre de su archivo
- [x] 🤖 5400 carátulas (77%) del servidor oficial de libretro y de `emu/MEDIA/`, reducidas a 512 px
- [x] 🎮 **Subido y verificado por FTP el 2026-09-13:** las 18 bases de datos y las 18 listas coinciden por SHA-1 con las del PC, y las 5373 carátulas están completas
- [x] 🎮 Las 18 listas aparecen en la consola
- [ ] 🧑 Opcional: 1586 juegos no tienen carátula, sobre todo en SNES, NES, WonderSwan, Atari 2600 y Atari 7800 (del 7800 el servidor de libretro apenas tiene portadas; del resto son traducciones y variantes que no están en la base de datos). Aparecen igual, con su nombre; solo tendrían carátula añadiéndola a mano
- ⚠️ La lista de Game Boy Color en la consola tiene 497 entradas y la del PC 495: RetroArch añadió *Gameboy Gallery 3* y *DynaMike* por su cuenta, con el core en DETECT. Son juegos de la carpeta `GB` que ya salen en su propia lista, así que no falta nada; solo desaparecerían si se vuelve a subir esa lista desde el PC

### BIOS opcionales

- [x] 🤖 `bios_U.sms`: la marcada `[b]` era buena (mismo SHA-1 que la europea, que es el que libretro espera para las dos). Creada en `emu/BIOS/` como copia de `bios_E.sms`
- [x] 🎮 Las 9 BIOS de `emu/BIOS/` están en `/data/retroarch/system/`, verificadas por SHA-1
- [ ] 🧑 `gba_bios.bin`: opcional; mGBA funciona sin ella

### Registro y aspecto del menú

- [x] 🤖 Registro a archivo activado en `retroarch.cfg` el 2026-09-13 (`log_to_file`, `log_verbosity`): cada arranque deja un `.log` en `/data/retroarch/logs/`. Útil para diagnosticar; borrar los viejos de vez en cuando
- [ ] 🤖 `/data/retroarch/assets/` está vacío: el menú Ozone funciona pero sin iconos (el log lista 150 `Asset missing`). Los assets son libres (`assets.zip` de buildbot.libretro.com); prepararlos para la versión 1.8.8 y subirlos
- [x] 🤖 Copia de `retroarch.cfg` de la consola en `emu/RETROARCH/backup/` (local, no versionada) y en `/data/retroarch/retroarch.cfg.bak`

### Copias de seguridad

- [ ] 🧑 Disco externo para la colección: el repo solo guarda las referencias, no los juegos
- [x] 🤖 Las 15 partidas de la consola están copiadas en `emu/SAVES/` (2026-09-13). Repetir la copia de vez en cuando, sobre todo antes de subir cualquier `.srm` desde el PC, porque sobrescribe la de la consola
- [ ] 🎮🤖 Automatizarlo con un script que las descargue por FTP y las verifique

---

## P1 — Tanda 1: sistemas sin BIOS

Copiar y jugar. Lo recomendable son los sets **No-Intro** de cada sistema, porque sus hashes se pueden verificar con el catálogo.

| | Sistema | Carpeta | Formato | Core | En el PC |
|---|---|---|---|---|--:|
| [x] | Atari 2600 | `ATARI2600/` | `.a26`, `.bin` | stella2014 | 885 |
| [x] | Atari 7800 | `ATARI7800/` | `.a78` | prosystem | 170 |
| [x] | PC Engine / TurboGrafx-16 | `PCE/` | `.pce` | mednafen_pce_fast | 210 |
| [x] | Neo Geo Pocket | `NGP/` | `.ngp` | mednafen_ngp | 3 |
| [x] | Neo Geo Pocket Color | `NGPC/` | `.ngc` | mednafen_ngp | 72 |
| [x] | WonderSwan | `WS/` | `.ws` | mednafen_wswan | 214 |
| [x] | WonderSwan Color | `WSC/` | `.wsc` | mednafen_wswan | 131 |
| [x] | Atari Lynx | `LYNX/` | `.lnx` | handy | 136 |
| [x] | Sega 32X | `32X/` | `.32x` | picodrive | 45 |
| [x] | Virtual Boy | `VB/` | `.vb` (en zip) | mednafen_vb | 31 |

Ordenado el 2026-09-13, con cada movimiento en `cleanup-2026-09-13.tsv`. Neo Geo Pocket y WonderSwan están separados por la cabecera de cada ROM, no por la extensión: muchas venían en la carpeta o con la extensión del otro sistema.

- [x] **Atari 7800:** 2821 archivos de cinco colecciones superpuestas, reducidos a las **170 ROMs que reconoce la base de datos**. Las 1191 restantes (hacks, homebrew, versiones PAL y variantes) están en `EXTRAS/ATARI7800-variantes`
- [x] `lynxboot.img` verificada con `System.dat` de libretro y copiada a `emu/BIOS/`. La otra variante que traía la colección (`lynxboot.bin`) no es la oficial
- [ ] 🧑 Opcional: `7800 BIOS (U).rom`. La que venía en la colección es *7800 DEV OS*, homebrew, y no está en `System.dat`
- [x] 🎮 Las 1897 ROMs de la Tanda 1 (1,2 GB) están en `/data/ROMS/<SISTEMA>/`, verificadas por FTP una a una: mismo nombre y mismo tamaño que en el PC, sin faltantes ni sobrantes
- [x] 🎮 `lynxboot.img` y `bios_U.sms` subidas a `/data/retroarch/system/`
- [ ] 🎮 Probar un juego de cada sistema. Lynx tiene 13 prototipos sin cabecera `LYNX` que podrían no arrancar
- [ ] 🧑 Revisar lo apartado en `EXTRAS/` (4727 archivos): duplicados, las variantes de Atari 7800, 26 `.7z` de Virtual Boy que no se pudieron abrir para comprobarlos, BIOS descartadas, y el emulador OSwan y otros archivos que venían con las colecciones. Nada de esto se ha borrado

---

## P2 — Tanda 2: arcade

Los romsets tienen que ser **exactamente de la versión del core**. Un set de otra versión puede dar juegos que no arrancan sin ningún aviso claro.

- [x] 🧑 **Romset FB Alpha 2012:** conseguido el set *v0.2.97.24* de archive.org, con 2890 zips y `neogeo.zip`. Es más antiguo que los cores (v0.2.97.28 y .29)
- [x] 🤖 **DAT de los 5 cores**, sacados de su código fuente (commits de 2020), y **set verificado zip a zip** con la lógica de carga del core (`tools/fba2012.py`, 14-09):
  - 2775 juegos arrancan, repartidos por core en `ARCADE/FBNEO/`, `FBNEO/CPS1/`, `FBNEO/CPS2/`, `FBNEO/CPS3/` y `NEOGEO/`, cada carpeta con su lista;
  - 11 arrancan con alguna ROM de CRC distinta y 9 tienen el driver marcado como que no funciona. Detalle en [`emu/ROMS/ARCADE/FBNEO/README.md`](emu/ROMS/ARCADE/FBNEO/README.md)
- [ ] 🧑 Opcional: 47 juegos incompletos (`EXTRAS/ARCADE-incompletos/`, cada uno con las ROMs que le faltan) y 12 padres que no arrancan solos. Se completarían con un set v0.2.97.29
- [ ] 🎮 Subir las 5 carpetas y sus 5 listas, y probar un juego de cada core
- [ ] 🧑 **Romset MAME 2003-Plus**, para `ARCADE/MAME/` (pendiente de descargar). Solo juegos 2D; no mezclar con sets de otras versiones de MAME
- [ ] 🤖 Cuando lo tengas, lo cruzo con el DAT de MAME 2003-Plus para saber qué juegos están completos

---

## P3 — Tanda 3: sistemas que necesitan BIOS

| | BIOS | Sistema | Ruta en la PS4 | ¿Obligatoria? |
|---|---|---|---|---|
| [x] | `bios_CD_U.bin`, `bios_CD_E.bin`, `bios_CD_J.bin` | Sega CD | `system/` | sí — **ya subidas** |
| [ ] 🧑 | `syscard3.pce` | PC Engine CD | `system/` | sí |
| [ ] 🧑 | `disksys.rom` | Famicom Disk System | `system/` | sí |
| [ ] 🧑 | `5200.rom` | Atari 5200 | `system/` | sí |
| [ ] 🧑 | `MSX.ROM`, `MSX2.ROM`, `MSX2EXT.ROM`, `MSX2P.ROM`, `MSX2PEXT.ROM` | MSX / MSX2 | `system/` | sí, con fmsx |

Juegos:

- [ ] 🧑 Sega CD: `.cue` + `.bin` o `.chd`, en `SEGACD/`
- [ ] 🧑 PC Engine CD: `.cue` + `.bin` o `.chd`, en `PCECD/`
- [ ] 🧑 Famicom Disk System: `.fds`, en `FDS/`
- [ ] 🧑 Atari 5200: `.a52`, en `ATARI5200/`
- [ ] 🧑 MSX: `.rom`, `.dsk` o `.cas`, en `MSX/`

Formato CD:

- [ ] 🧑 Descargar **chdman**, que viene con MAME y es gratuito, para convertir `.cue`/`.bin` a `.chd`: un solo archivo por juego y menos espacio
- [ ] 🤖 Puedo prepararte un script que convierta una carpeta entera y verifique el resultado

---

## P4 — Tanda 4: PS1, como PS1 Classics

- [ ] 🧑 Tus discos de PS1 volcados en `.bin` + `.cue`. En juegos de varios discos, todos
- [ ] 🧑 Herramienta de conversión en el PC: **PSX-FPKG** (Jabu; `.bin/.cue` multi-bin e ISO, desde firmware 5.05) o **PS Classics fPKG Builder** (SvenGDK; solo `.bin`; funciona, pero su repositorio está archivado desde noviembre de 2025)
- [ ] 🤖 Puedo verificar la versión vigente de la herramienta y dejar escritos los pasos exactos antes de que conviertas nada
- [ ] 🧑 Opcional: imágenes de icono y fondo para cada juego
- [ ] 🎮 Consultar cada juego en la [lista de compatibilidad de PS1 Classics](https://www.psdevwiki.com/ps4/PS1_Classics_Emulator_Compatibility_List), instalar el paquete desde `/data/pkg/` y probarlo
- [ ] 🧑 Solo para la vía alternativa en RetroArch: `scph5501.bin` (USA), `scph5502.bin` (Europa) y `scph5500.bin` (Japón), en `system/`

---

## P5 — Tanda 5: PSP, como PSP Classics

- [ ] 🧑 Tus juegos de PSP en `.iso`
- [ ] 🧑 Herramienta **PSP-FPKG** (Jabu), que usa el emulador PSPHD de PS Plus
- [ ] 🎮 Consultar cada juego en la [lista de compatibilidad de PSP Classics](https://www.psdevwiki.com/ps4/Template:PSP_Classics_Emulator_Compatibility_List) **antes** de convertirlo: la compatibilidad es mixta
- [ ] 🤖 Solo para la vía alternativa en RetroArch: preparar la carpeta `assets` **completa** de PPSSPP (no solo `ppge_atlas.zim`), que es libre y el core `ppsspp` exige, para subirla a `system/PPSSPP/`

---

## P6 — Ordenadores

- [x] 🧑 **Teclado USB** (hecho según Javi, 14-09). C64, DOS, MSX y ScummVM se usan con teclado
- [x] 🧑 Colecciones de Commodore 64, DOS y ScummVM descargadas (14-09)
- [x] 🤖 **C64** ordenado (14-09):
  - 8427 imágenes de disco y cinta en `C64/`, con 509 `.m3u` para los juegos de varios discos (lista de 7522 juegos);
  - 11 023 `.prg` en `C64/PRG/`, con su propia lista. Detalle en [`emu/ROMS/C64/README.md`](emu/ROMS/C64/README.md)
- [x] 🤖 **DOS** (14-09): 956 juegos descomprimidos en `DOS/`, cada uno con un `.conf` que lo arranca (`tools/dos.py`), y los zips originales en `emu/ORIGINALES/DOS/`. Detalle en [`emu/ROMS/DOS/README.md`](emu/ROMS/DOS/README.md)
- [x] 🤖 **ScummVM** (14-09): 40 aventuras de la colección de DOS en `SCUMMVM/`, cada una con su `.scummvm` (id comprobado en ScummVM 2.2) y en su lista
- [ ] 🎮 Subir C64, DOS y ScummVM con sus 4 listas, y probar un juego de cada uno con teclado. Comprobar antes que el port reconoce el teclado
- [ ] 🎮 DOS: 254 lanzadores son `dudoso`. Si un juego abre el programa equivocado, se cambia la última línea de su `.conf` (alternativas en [`LANZADORES.md`](emu/ROMS/DOS/LANZADORES.md))
- [ ] 🧑 DOS: 11 juegos solo traen su instalador (*Discworld*, *Doom* shareware, *Colonization*…) y hay que instalarlos en DOSBox
- [ ] 🧑 DOS: faltan 778 de los 1778 juegos del `gamelist.xml` de la colección (pendiente de descargar). Cuando lleguen: `python tools/dos.py CARPETA`
- [ ] 🤖 ScummVM: datos de motores para `system/scummvm/extra/` (`kyra.dat` para *Eye of the Beholder*, `lure.dat` y `queen.tbl`) y temas, de la versión de ScummVM del core, que falta identificar
- [ ] 🤖 Carátulas de arcade, C64, DOS y ScummVM. De DOS hay 2901 imágenes de ScreenScraper en `emu/MEDIA/DOS/`
- [ ] 🤖 blueMSX, si se prefiere a fmsx: sus carpetas `Databases/` y `Machines/`, libres

---

## P7 — Probar después: rendimiento variable o sin datos

**Probar un juego de cada uno antes de conseguir la colección.**

| | Qué conseguir | Sistema | Ruta en la PS4 |
|---|---|---|---|
| [ ] 🧑 | `dc_boot.bin` + juegos `.gdi`/`.chd` | Dreamcast | BIOS en `system/dc/` |
| [ ] 🧑 | `naomi.zip` + romset compatible con Flycast | Sega NAOMI | BIOS en `system/dc/` |
| [ ] 🧑 | `awbios.zip` + romset compatible con Flycast | Sega Atomiswave | BIOS en `system/dc/` |
| [ ] 🧑 | `saturn_bios.bin` (yabause), o `sega_101.bin` + `mpr-17933.bin` (mednafen_saturn) + juegos `.cue`/`.chd` | Saturn | `system/` |
| [ ] 🧑 | `panafz10.bin` (u otra BIOS de 3DO) + juegos | 3DO | `system/` |
| [ ] 🧑 | `pcfx.rom` + juegos `.cue`/`.chd` | PC-FX | `system/` |

---

## P8 — Aparcados y más adelante

- [ ] 🧑 **PS2:** copiar al PC las 5 ISO de `/data/ROMS/PS2` para que queden en el catálogo; conseguir **PS2-FPKG** (Jabu) o **PS2 Classic GUI**; mirar cada juego en la [lista de compatibilidad de PS2 Classics](https://www.psdevwiki.com/ps4/PS2_Classics_Emulator_Compatibility_List); convertir, instalar y borrar las ISO de la consola
- [ ] N64 y DS: no invertir en ellos por ahora, porque se reportan lentos. Si quieres probar: ROMs `.z64` o `.nds`; en DS, `bios7.bin`, `bios9.bin` y `firmware.bin` son opcionales

---

## P9 — Mantenimiento de la colección en el PC

- [ ] 🧑 Decidir si se borran `EXTRAS/MD-duplicados/` (676) y `EXTRAS/MD-malos/` (6)
- [ ] 🧑 Decidir qué se hace con lo apartado el 14-09 en `EXTRAS/`: arcade incompleto y sin driver, variantes de PRG y el pack de Google Drive de C64 (244 MB, casi todo repetido), y los zips rotos de DOS
- [ ] 🧑 Espacio en el PC: quedan 6,7 GB libres en D: tras descomprimir DOS
- [ ] 🧑 Decidir si `ROMS/NES/Datach - Battle Rush….sav` va a `SAVES/`
- [ ] 🧑 Quitar `gamelist.xml` y `systeminfo.txt` de `ROMS/GBC` y `ROMS/GBA`, y `Lisezmoi.txt` de `ROMS/NES`
- [ ] 🧑 Decidir qué hacer con el `.rar` de 4,4 GB de la raíz del repo
- [ ] 🧑 Comprobar el espacio libre en la PS4 antes de subir las carátulas (1,4 GB) y antes de las tandas 4 y 5: los paquetes de PS1 y PSP ocupan GB
- [ ] 🧑 Descargar los DAT de **No-Intro** y **Redump** (gratuitos)
- [ ] 🤖 Hacer un verificador que cruce esos DAT con el `rom-sha1` del catálogo y marque cada volcado como bueno, malo o desconocido

---

## Linux — proyecto aparte, fuera de las tandas de RetroArch

Preparado el 2026-09-13 en [`linux/`](linux/README.md). La consola es **Baikal B1**: kernel 5.4.247, distro con Mesa ≤ 25.1 y solo disco externo. Nada probado aún en la consola.

- [x] 🤖 Loader v25, kernel 5.4.247 (Baikal) e initramfs externo de DionKill, verificados por SHA-1 contra su origen y catalogados en `catalogo/LINUX/`
- [x] 🧑 **La distro:** Arch de marzo de 2026 con KDE Plasma 6.6 y Mesa 25.1.0-devel, bajada de Mega el 2026-09-13, íntegra (`xz -t`) y catalogada como `linux/distros/ps4linux-arch-mesa25.1-2026-03-09.tar.xz`
- [x] 🤖 **Pendrive preparado** (2026-09-13): Kingston DataTraveler 3.0 de 30,9 GB, reparticionado de GPT a MBR, FAT32 `PS4LINUX`, con `bzImage`, `initramfs.cpio.gz` y `psxitarch.tar.gz` (2,73 GB, verificado)
- [ ] 🧑 Teclado y ratón USB para la consola
- [x] 🎮 Rescue shell, instalación y arranque de la distro (13-09): **solo con la tele**, el monitor Samsung no recibe señal
- [x] 🎮 GPU comprobada: `radeonsi, liverpool, ACO` en LXDE (13-09)
- [x] 🤖 `bootargs.txt` con `root=LABEL=psxitarch` en la FAT32 del pendrive (el instalador lo había borrado al reparticionar)
- [x] 🤖 Paquetes sin red en `linux/pkgs/` y en el pendrive: Dolphin, PPSSPP, `iw`, `wireless-regdb`, del Arch Linux Archive del 09-03-2026
- [x] 🎮 `instalar.sh` ejecutado: Dolphin 2509 abre (13-09)
- [x] 🎮 Wi-Fi: conecta con `hidden yes` (NetworkManager no lista la red aunque `iw` la ve). Probado con el hotspot del PC
- [x] 🤖 Payload Guest subido a `/data/pkg/` y los payloads a `/data/payloads/` (13-09): Linux se arranca desde la consola
- [x] 🎮 Payload Guest instalado; Linux arranca desde la consola (13-09)
- [x] 🧑 *Wind Waker* (Europe, RVZ, `GZLP01`, 870 MB) en `emu/ROMS/GC/` (13-09)
- [x] 🤖 Copiado por SFTP a `/home/ps4/Juegos/Zelda-Wind-Waker-Europe.rvz`, SHA-1 verificado; Dolphin configurado con OpenGL y esa carpeta (13-09)
- [x] 🤖 Autologin en LXDE, ZRAM desactivado (sin módulo en el 5.4) y `WIRELESS_REGDOM=ES`, por SSH (13-09)
- [ ] 🧑 Pendrive en el puerto trasero o con alargador: ahora va a USB 2.0
- [ ] 🧑 Probar el kernel `neocine-1.1` con la tele (más rendimiento en Pro y trae ZRAM); si va, se queda y se reactiva el `zram-generator.conf`
- [ ] 🧑 Apagar Linux siempre desde el menú (partición sin journal); algún día `e2fsck` en frío desde la rescue shell
- [ ] 🧑 *Wind Waker* en `.iso` o `.rvz` en un USB aparte en exFAT (la partición del pendrive es ext4 y Windows no la escribe), y un hub USB para teclado y ratón
- [x] 🎮 ***Wind Waker* a 30 fps en Dolphin 2509** (Vulkan), 13-09 a las 23:40
- [ ] 🎮 Lanzar `ps4-fan-threshold60.bin` antes de Linux en cada arranque: la CPU va a 71 °C jugando y en Baikal nadie mueve el ventilador
- [x] 🎮 DualShock 4 por cable mapeado en Dolphin (13-09); por Bluetooth pendiente (emparejar desde Linux, `linux/dolphin.md`)
- [x] 🤖 Aplicados por SSH los cambios de `linux/dolphin.md` con copia previa (13-09, 23:58)
- [ ] 🎮 Comprobar con la nueva configuración: fps en la cinemática del barco y mando (Z=R1, L=L2, R=R2, cámara). El 16:9 sin barras ya está comprobado en el USA (14-09)
- [x] 🧑 *Wind Waker* (USA, RVZ, `GZLE01`, 863 MB) y el pack de texturas *Hypatia WWHD v2.0* descargados (14-09)
- [x] 🤖 USA copiado a `emu/ROMS/GC/` con SHA-1 verificado; conjunto de prueba de texturas (`Characters` + `Items`, 846 archivos, 404 MB) extraído en `linux/texturas/GZL/` (14-09)
- [x] 🤖 Subidos por SFTP el USA (`/home/ps4/Juegos/Zelda-Wind-Waker-USA.rvz`) y `GZL/` a `~/.local/share/dolphin-emu/Load/Textures/`, con Dolphin cerrado y copia de la config (14-09)
- [x] 🤖 `GameSettings/GZLE01.ini`: texturas activadas, anisotrópico **1x** y *Prefetch* **no**, solo en el USA; 16:9 y sin desenfoque como el europeo (14-09)
- [x] 🤖 Pendrive terminó de escribir el 14-09: `tar` de 00:30 a 01:11 y `sync` hasta las 02:11 (1 h 40 min para ~1,3 GB)
- [x] 🎮 USA con texturas HD probado (14-09): Link en HD, 16:9, 30 fps en interiores y 25-27 mirando al mar. Ojo: los `GameSettings/*.ini` van en `~/.local/share/dolphin-emu/`, no en `~/.config/` (los del 13-09 nunca se aplicaron); corregidos el USA y el europeo
- [x] 🤖 Prueba A/B de `ArbitraryMipmapDetection = False` + `EnableGPUTextureDecoding = True`: 26,8 frente a 27,0 fps, sin efecto; descartados (`linux/dolphin.md`)
- [ ] 🧑 Pendrive o SSD con buena escritura sostenida: el Kingston DataTraveler 3.0 escribe a ~150 KB/s y el pack completo de texturas tardaría unas 17 h
- [x] 🧑 Originales de Descargas borrados tras verificar las copias del repo (14-09)
- [ ] 🎮 Si la prueba va bien: añadir `Effects` (140 MB) y luego decidir sobre `Environments` (8,2 GB). `HUD` solo sobre la versión USA (está en inglés)
- [ ] 🧑 El `.7z` de `linux/texturas/` (1,94 GB) es ya la única copia del pack: no borrarlo mientras se quiera extraer más carpetas
- [ ] 🧑 Comparar OpenGL y Vulkan en Dolphin (fps en la misma escena)
- [x] 🤖 **Resuelto (14-09): la CPU va a 1,6 GHz porque el kernel no tiene `cpufreq` y la deja en P2; P0 = 2,1 GHz está permitido.** `linux/cpu/ps4-cpu` lo pide por MSR: *Wind Waker* pasa de 26,8 a 29,95 fps en la misma escena. Instalado en la consola con dos iconos en el escritorio (*Rendimiento* / *Normal*)
- [ ] 🎮 **Pulsar "CPU 2,1 GHz — Rendimiento" en cada arranque de Linux antes de Dolphin** (se pierde al reiniciar). Vigilar la temperatura: 77-80 °C jugando a 2,1 GHz
- [ ] 🤖 Comprobar si `neocine-1.1` o los kernels de rmux traen `cpufreq` y arrancan ya en P0; entonces sobra el script
- [ ] 🎮 RPCS3, con su firmware (AUR, con red)
- [ ] 🤖 Vigilar [rmuxnet/linux](https://gitlab.com/rmuxnet/linux/-/releases): cuando publique un 7.x con Baikal, cambiar a CachyOS Light y actualizar `linux/README.md`

---

## Resumen de BIOS que faltan

Todas las BIOS deberían coincidir con los hashes que publica libretro. Cuando las tengas, las compruebo antes de subirlas.

| Archivo | Sistema | Ruta en la PS4 | Tanda | ¿Obligatoria? |
|---|---|---|---|---|
| ~~`bios_U.sms`~~ subida | Master System | `system/` | P0 | no |
| `gba_bios.bin` | GBA | `system/` | P0 | no |
| `7800 BIOS (U).rom` | Atari 7800 | `system/` | P1 | no |
| ~~`lynxboot.img`~~ subida | Lynx | `system/` | P1 | no, con handy |
| ~~`neogeo.zip` (FB Alpha 2012)~~ en `ROMS/NEOGEO/` del PC | Neo Geo | junto a las ROMs | P2 | sí |
| `syscard3.pce` | PC Engine CD | `system/` | P3 | sí |
| `disksys.rom` | Famicom Disk System | `system/` | P3 | sí |
| `5200.rom` | Atari 5200 | `system/` | P3 | sí |
| `MSX.ROM`, `MSX2.ROM`, `MSX2EXT.ROM`, `MSX2P.ROM`, `MSX2PEXT.ROM` | MSX | `system/` | P3 | sí, con fmsx |
| `scph5501.bin`, `scph5502.bin`, `scph5500.bin` | PS1 por RetroArch | `system/` | P4 | solo en esa vía |
| `dc_boot.bin` | Dreamcast | `system/dc/` | P7 | recomendada |
| `naomi.zip` | NAOMI | `system/dc/` | P7 | sí |
| `awbios.zip` | Atomiswave | `system/dc/` | P7 | sí |
| `saturn_bios.bin` | Saturn (yabause) | `system/` | P7 | no |
| `sega_101.bin`, `mpr-17933.bin` | Saturn (mednafen_saturn) | `system/` | P7 | sí, en ese core |
| `panafz10.bin` | 3DO | `system/` | P7 | sí |
| `pcfx.rom` | PC-FX | `system/` | P7 | sí |
| `bios7.bin`, `bios9.bin`, `firmware.bin` | Nintendo DS | `system/` | P8 | no |

## Lo que puedo preparar yo (🤖)

1. ~~Bases de datos `.rdb` para crear listas de juegos~~ — **hecho**
2. ~~Carátulas desde `emu/MEDIA/` o desde libretro-thumbnails~~ — **hecho**, junto con las listas ya generadas
3. Script de copia de seguridad de partidas por FTP
4. Script de conversión a `.chd` con verificación
5. Pasos verificados para PSX-FPKG y PSP-FPKG
6. Carpeta `PPSSPP/` de assets para el core de PSP
7. Temas y datos de ScummVM, y carpetas de blueMSX
8. Verificador de volcados contra los DAT de No-Intro y Redump
9. Comprobación de hashes de cada BIOS antes de subirla

## No hace falta conseguir

- **Sin core en esta PS4:** Pokémon Mini, Amiga, ZX Spectrum, Neo Geo CD, Sharp X68000 y CHIP-8
- **Solo con Linux:** GameCube, Wii, PS3 y PS Vita. Es el proyecto aparte de la sección "Linux" de arriba
- **No viables:** 3DS, Xbox / Xbox 360 y Switch. Motivos en [`emu/emuladores-ps4.md`](emu/emuladores-ps4.md)

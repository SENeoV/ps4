# Pendientes — lo que falta para un sistema retro 100% funcional

Lista completa y priorizada de lo que falta **conseguir, preparar o configurar**. Está verificada contra la consola por FTP (solo lectura) y contra los `.info` de los 74 cores instalados el 2026-09-13.

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
- [ ] 🎮 **Core de GBA:** los juegos se abren con `mednafen_gba`. Cargar con **mGBA** y fijarlo como core por defecto del sistema. Las partidas `.srm` sirven igual
- [ ] 🎮 **Shaders:** están activados (`video_shader_enable = true`). Si algún juego va a tirones, desactivarlos es lo primero que hay que probar
- [ ] 🎮 **No usar el *Online Updater* ni el *Core Updater* de RetroArch:** apuntan a Bintray, que cerró. Todo se sube por FTP

### Listas de juegos y carátulas

Ahora no hay ninguna lista, y la base de datos de RetroArch (`database/rdb`) está vacía, así que *Escanear directorio* no reconocerá los juegos.

- [ ] 🤖 Preparar los `.rdb` de [libretro-database](https://github.com/libretro/libretro-database) para cada sistema y subirlos a `/data/retroarch/database/rdb/`
- [ ] 🎮 Crear una lista por sistema: *Importar contenido → Escanear directorio* sobre `/data/ROMS/<SISTEMA>`. Sin los `.rdb`, usar *Escaneo manual* si tu versión lo muestra
- [ ] 🤖 Carátulas: `thumbnails/` está vacía. Se pueden montar con los 1555 PNG de `emu/MEDIA/` o con los packs libres de libretro-thumbnails, con el nombre de cada lista

### BIOS opcionales

- [ ] 🧑 `bios_U.sms` en buen estado: la única que tienes está marcada `[b]`. Sin ella el juego arranca igual
- [ ] 🧑 `gba_bios.bin`: opcional; mGBA funciona sin ella

### Copias de seguridad

- [ ] 🧑 Disco externo para la colección: el repo solo guarda las referencias, no los juegos
- [ ] 🎮🤖 Rutina de copia de `/data/retroarch/savefiles/` y `/data/retroarch/savestates/` al PC. Puedo hacer un script que la descargue por FTP y la verifique

---

## P1 — Tanda 1: sistemas sin BIOS

Copiar y jugar. Lo recomendable son los sets **No-Intro** de cada sistema, porque sus hashes se pueden verificar con el catálogo.

| | Sistema | Carpeta | Formato | Core |
|---|---|---|---|---|
| [ ] 🧑 | Atari 2600 | `ATARI2600/` | `.a26` | stella2014 |
| [ ] 🧑 | Atari 7800 | `ATARI7800/` | `.a78` | prosystem |
| [ ] 🧑 | PC Engine / TurboGrafx-16 | `PCE/` | `.pce` (`.sgx` para SuperGrafx) | mednafen_pce_fast |
| [ ] 🧑 | Neo Geo Pocket | `NGP/` | `.ngp` | mednafen_ngp |
| [ ] 🧑 | Neo Geo Pocket Color | `NGPC/` | `.ngc` | mednafen_ngp |
| [ ] 🧑 | WonderSwan | `WS/` | `.ws` | mednafen_wswan |
| [ ] 🧑 | WonderSwan Color | `WSC/` | `.wsc` | mednafen_wswan |
| [ ] 🧑 | Atari Lynx | `LYNX/` | `.lnx` | handy |
| [ ] 🧑 | Sega 32X | `32X/` | `.32x` | picodrive |
| [ ] 🧑 | Virtual Boy | `VB/` | `.vb` | mednafen_vb |

Opcionales: 🧑 `lynxboot.img` (handy no la exige) y 🧑 `7800 BIOS (U).rom`.

---

## P2 — Tanda 2: arcade

Los romsets tienen que ser **exactamente de la versión del core**. Un set de otra versión puede dar juegos que no arrancan sin ningún aviso claro.

- [ ] 🧑 **Romset FB Alpha 2012 `v0.2.97.29`**, para `ARCADE/FBNEO/` y `NEOGEO/`. Tiene que incluir las BIOS de placa que pidan los juegos; en Neo Geo, `neogeo.zip`, **junto a las ROMs** y no en `system/`
- [ ] 🧑 **Romset MAME 2003-Plus**, para `ARCADE/MAME/`. Solo juegos 2D; no mezclar con sets de otras versiones de MAME
- [ ] 🤖 Cuando los tengas, puedo cruzarlos con el DAT de cada versión para saber qué juegos están completos

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
- [ ] 🧑 Herramienta de conversión en el PC: **PS1-FPKG** (Jabu) o **PS Classics fPKG Builder** (SvenGDK; funciona, pero su repositorio está archivado)
- [ ] 🤖 Puedo verificar la versión vigente de la herramienta y dejar escritos los pasos exactos antes de que conviertas nada
- [ ] 🧑 Opcional: imágenes de icono y fondo para cada juego
- [ ] 🎮 Consultar cada juego en la [lista de compatibilidad de PS1 Classics](https://www.psdevwiki.com/ps4/PS1_Classics_Emulator_Compatibility_List), instalar el paquete desde `/data/pkg/` y probarlo
- [ ] 🧑 Solo para la vía alternativa en RetroArch: `scph5501.bin` (USA), `scph5502.bin` (Europa) y `scph5500.bin` (Japón), en `system/`

---

## P5 — Tanda 5: PSP, como PSP Classics

- [ ] 🧑 Tus juegos de PSP en `.iso`
- [ ] 🧑 Herramienta **PSP-FPKG** (Jabu), que usa el emulador PSPHD de PS Plus
- [ ] 🎮 Consultar cada juego en la [lista de compatibilidad de PSP Classics](https://www.psdevwiki.com/ps4/Template:PSP_Classics_Emulator_Compatibility_List) **antes** de convertirlo: la compatibilidad es mixta
- [ ] 🤖 Solo para la vía alternativa en RetroArch: preparar la carpeta `PPSSPP/` con sus assets (`ppge_atlas.zim`…), que es libre y el core `ppsspp` exige, para subirla a `system/PPSSPP/`

---

## P6 — Ordenadores

- [ ] 🧑 **Teclado USB.** C64, DOS, MSX y ScummVM se usan con teclado. Comprobar primero que el port de RetroArch lo reconoce
- [ ] 🧑 Commodore 64: `.d64`, `.t64`, `.tap`, `.prg` o `.crt`, en `C64/`. VICE lleva las ROMs del sistema integradas
- [ ] 🧑 DOS: una carpeta por juego, con su `.exe` o un `.conf`, en `DOS/`
- [ ] 🧑 ScummVM: los archivos de datos de tus juegos originales, uno por subcarpeta con su `.scummvm`, en `SCUMMVM/`
- [ ] 🤖 ScummVM: temas y archivos de datos de motores (`system/scummvm/theme/` y `extra/`), libres
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

- [ ] 🧑 **PS2:** copiar al PC las 5 ISO de `/data/ROMS/PS2` para que queden en el catálogo; conseguir la herramienta de PS2 Classics; convertir, instalar y borrar las ISO de la consola
- [ ] N64 y DS: no invertir en ellos por ahora, porque se reportan lentos. Si quieres probar: ROMs `.z64` o `.nds`; en DS, `bios7.bin`, `bios9.bin` y `firmware.bin` son opcionales

---

## P9 — Mantenimiento de la colección en el PC

- [ ] 🧑 Decidir si se borran `EXTRAS/MD-duplicados/` (676) y `EXTRAS/MD-malos/` (6)
- [ ] 🧑 Decidir si `ROMS/NES/Datach - Battle Rush….sav` va a `SAVES/`
- [ ] 🧑 Quitar `gamelist.xml` y `systeminfo.txt` de `ROMS/GBC` y `ROMS/GBA`
- [ ] 🧑 Decidir qué hacer con el `.rar` de 4,4 GB de la raíz del repo
- [ ] 🧑 Comprobar el espacio libre en la PS4 antes de las tandas 4 y 5: los paquetes de PS1 y PSP ocupan GB
- [ ] 🧑 Descargar los DAT de **No-Intro** y **Redump** (gratuitos)
- [ ] 🤖 Hacer un verificador que cruce esos DAT con el `rom-sha1` del catálogo y marque cada volcado como bueno, malo o desconocido

---

## Resumen de BIOS que faltan

Todas las BIOS deberían coincidir con los hashes que publica libretro. Cuando las tengas, las compruebo antes de subirlas.

| Archivo | Sistema | Ruta en la PS4 | Tanda | ¿Obligatoria? |
|---|---|---|---|---|
| `bios_U.sms` (en buen estado) | Master System | `system/` | P0 | no |
| `gba_bios.bin` | GBA | `system/` | P0 | no |
| `7800 BIOS (U).rom` | Atari 7800 | `system/` | P1 | no |
| `lynxboot.img` | Lynx | `system/` | P1 | no, con handy |
| `neogeo.zip` (FB Alpha 2012) | Neo Geo | junto a las ROMs | P2 | sí |
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

Solo tienes que pedirlo:

1. Bases de datos `.rdb` para crear listas de juegos
2. Carátulas desde `emu/MEDIA/` o desde libretro-thumbnails
3. Script de copia de seguridad de partidas por FTP
4. Script de conversión a `.chd` con verificación
5. Pasos verificados para PS1-FPKG y PSP-FPKG
6. Carpeta `PPSSPP/` de assets para el core de PSP
7. Temas y datos de ScummVM, y carpetas de blueMSX
8. Verificador de volcados contra los DAT de No-Intro y Redump
9. Comprobación de hashes de cada BIOS antes de subirla

## No hace falta conseguir

- **Sin core en esta PS4:** Pokémon Mini, Amiga, ZX Spectrum, Neo Geo CD, Sharp X68000 y CHIP-8
- **No viables:** 3DS, GameCube, Wii, PS Vita, PS3, Xbox / Xbox 360 y Switch. Motivos en [`emu/emuladores-ps4.md`](emu/emuladores-ps4.md)

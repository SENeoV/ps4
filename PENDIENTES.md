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

- [ ] 🧑 **PS2:** copiar al PC las 5 ISO de `/data/ROMS/PS2` para que queden en el catálogo; conseguir **PS2-FPKG** (Jabu) o **PS2 Classic GUI**; mirar cada juego en la [lista de compatibilidad de PS2 Classics](https://www.psdevwiki.com/ps4/PS2_Classics_Emulator_Compatibility_List); convertir, instalar y borrar las ISO de la consola
- [ ] N64 y DS: no invertir en ellos por ahora, porque se reportan lentos. Si quieres probar: ROMs `.z64` o `.nds`; en DS, `bios7.bin`, `bios9.bin` y `firmware.bin` son opcionales

---

## P9 — Mantenimiento de la colección en el PC

- [ ] 🧑 Decidir si se borran `EXTRAS/MD-duplicados/` (676) y `EXTRAS/MD-malos/` (6)
- [ ] 🧑 Decidir si `ROMS/NES/Datach - Battle Rush….sav` va a `SAVES/`
- [ ] 🧑 Quitar `gamelist.xml` y `systeminfo.txt` de `ROMS/GBC` y `ROMS/GBA`, y `Lisezmoi.txt` de `ROMS/NES`
- [ ] 🧑 Decidir qué hacer con el `.rar` de 4,4 GB de la raíz del repo
- [ ] 🧑 Comprobar el espacio libre en la PS4 antes de subir las carátulas (1,4 GB) y antes de las tandas 4 y 5: los paquetes de PS1 y PSP ocupan GB
- [ ] 🧑 Descargar los DAT de **No-Intro** y **Redump** (gratuitos)
- [ ] 🤖 Hacer un verificador que cruce esos DAT con el `rom-sha1` del catálogo y marque cada volcado como bueno, malo o desconocido

---

## Resumen de BIOS que faltan

Todas las BIOS deberían coincidir con los hashes que publica libretro. Cuando las tengas, las compruebo antes de subirlas.

| Archivo | Sistema | Ruta en la PS4 | Tanda | ¿Obligatoria? |
|---|---|---|---|---|
| `bios_U.sms` (ya en el PC, falta subir) | Master System | `system/` | P0 | no |
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
- **Solo con Linux, fuera de la hoja de ruta:** GameCube, Wii, PS3 y PS Vita. Linux arranca en 12.52, pero es un proyecto aparte
- **No viables:** 3DS, Xbox / Xbox 360 y Switch. Motivos en [`emu/emuladores-ps4.md`](emu/emuladores-ps4.md)

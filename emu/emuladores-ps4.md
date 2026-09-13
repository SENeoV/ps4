# Emuladores por plataforma — PS4 Pro + GoldHEN 12.52

Guía de referencia rápida para montar la retro-colección. ROMs y BIOS: originales, obtenidas por el usuario.

**Core** = el que está realmente instalado en esta PS4 (74 cores del Core Installer), comprobado contra sus `.info` el 2026-09-13. La columna *PS4 Pro* resume informes de la comunidad y no está probada juego a juego en esta consola. El orden de implantación está en la hoja de ruta de [`PLAN.md`](../PLAN.md), y el detalle de cada sistema en el `README.md` de su carpeta.

### Leyenda de compatibilidad

- 🟢 Excelente — prácticamente sin problemas
- 🟢/🟡 Muy buena — algunos juegos pueden necesitar ajustes
- 🟡 Buena/variable — depende bastante del juego/core
- 🟠 Experimental — reportado lento; no montar la colección alrededor
- 🐧 Solo con Linux — no hay emulador en el sistema de la PS4, pero sí arrancando Linux (sin probar en esta consola)
- 🔴 No viable — sin core en esta PS4 y sin emulador práctico ni siquiera en Linux
- ❔ Sin datos de rendimiento en PS4
- ⏸ Aplazado
- ✅ Probado en esta consola

## Tabla completa

| # | Plataforma | Año | Core en esta PS4 | ROM habitual | BIOS | PS4 Pro |
|--:|---|---|---|---|---|---|
| 1 | Atari 2600 | 1977 | stella2014 | `.a26` | No | 🟢 |
| 2 | Atari 5200 | 1982 | atari800 | `.a52` | `5200.rom` | 🟢 |
| 3 | Atari 7800 | 1986 | prosystem | `.a78` | `7800 BIOS (U).rom` (opcional) | 🟢 |
| 4 | Atari Lynx | 1989 | handy / mednafen_lynx | `.lnx` | `lynxboot.img` (opcional en handy) | 🟢 |
| 5 | NES / Famicom | 1983 | nestopia / fceumm / mesen / quicknes | `.nes` | No | 🟢 ✅ |
| 6 | Famicom Disk System | 1986 | nestopia / fceumm / mesen | `.fds` | `disksys.rom` | 🟢 |
| 7 | SNES / Super Famicom | 1990 | snes9x (2002/2005/2010) / mednafen_snes | `.sfc/.smc` | No | 🟢 |
| 8 | Virtual Boy | 1995 | mednafen_vb | `.vb` | No | 🟢 |
| 9 | Game Boy | 1989 | gearboy / sameboy / mgba | `.gb` | No | 🟢 |
| 10 | Game Boy Color | 1998 | gearboy / sameboy / mgba | `.gbc` | No | 🟢 |
| 11 | Game Boy Advance | 2001 | mgba / vba_next / vbam | `.gba` | `gba_bios.bin` (opcional) | 🟢 ✅ |
| 12 | Master System | 1985 | genesis_plus_gx | `.sms` | `bios_E/U/J.sms` (opcional) | 🟢 ✅ |
| 13 | Game Gear | 1990 | genesis_plus_gx | `.gg` | `bios.gg` (opcional) | 🟢 |
| 14 | Mega Drive / Genesis | 1988 | genesis_plus_gx / picodrive | `.md/.gen/.bin` | `bios_MD.bin` (opcional) | 🟢 |
| 15 | Sega CD / Mega CD | 1991 | genesis_plus_gx / picodrive | `.chd/.cue` | `bios_CD_U/E/J.bin` (la J es otra revisión que la de libretro) | 🟢 |
| 16 | 32X | 1994 | picodrive | `.32x` | No | 🟢 |
| 17 | PC Engine / TurboGrafx-16 | 1987 | mednafen_pce_fast / mednafen_supergrafx | `.pce/.sgx` | No | 🟢 |
| 18 | PC Engine CD | 1988 | mednafen_pce_fast | `.chd/.cue` | `syscard3.pce` | 🟢/🟡 |
| 19 | Neo Geo AES/MVS | 1990 | fbalpha2012_neogeo | `.zip` (romset FB Alpha 2012) | `neogeo.zip` junto a las ROMs | 🟢 |
| 20 | Neo Geo CD | 1994 | — (neocd no instalado) | `.chd/.cue` | — | 🔴 |
| 21 | Neo Geo Pocket | 1998 | mednafen_ngp | `.ngp` | No | 🟢 |
| 22 | Neo Geo Pocket Color | 1999 | mednafen_ngp | `.ngc` | No | 🟢 |
| 23 | WonderSwan | 1999 | mednafen_wswan | `.ws` | No | 🟢 |
| 24 | WonderSwan Color | 2000 | mednafen_wswan | `.wsc` | No | 🟢 |
| 25 | Arcade / MAME | — | mame2003_plus (+ 2000/2003/2010/2015) | `.zip` (romset de su versión) | dentro del romset | 🟢/🟡 solo 2D |
| 26 | Arcade / FB Alpha 2012 | — | fbalpha2012 (+ cps1/cps2/cps3) | `.zip` (romset FB Alpha 2012) | — | 🟢 |
| 27 | Nintendo 64 | 1996 | mupen64plus_next / parallel_n64 | `.z64/.n64/.v64` | No | 🟠 |
| 28 | Nintendo DS | 2004 | desmume / desmume2015 | `.nds` | `bios7/bios9/firmware.bin` (opcional) | 🟠 |
| 29 | Nintendo 3DS | 2011 | — | `.3ds/.cia` | — | 🔴 |
| 30 | Sega Saturn | 1994 | yabause / mednafen_saturn | `.chd/.cue` | `saturn_bios.bin`; `sega_101.bin` + `mpr-17933.bin` en mednafen | 🟡 algunos 2D |
| 31 | Dreamcast | 1998 | flycast | `.chd/.gdi/.cdi` | `dc/dc_boot.bin` | 🟡 probar |
| 32 | 3DO | 1993 | opera | `.chd/.cue/.iso` | `panafz10.bin` (u otra) | ❔ |
| 33 | PS1 | 1994 | **PS1 Classics** / pcsx_rearmed / mednafen_psx | `.bin/.cue/.chd` | `scph5501.bin` | 🟢 como Classics · 🟡 RetroArch |
| 34 | PS2 | 2000 | **PS2 Classics** (sin core) | `.iso` | — | ⏸ |
| 35 | PSP | 2004 | **PSP Classics** / ppsspp | `.iso/.cso` | carpeta `PPSSPP/` de assets (core) | 🟡 según juego |
| 36 | MSX / MSX2 | 1983 | fmsx / bluemsx | `.rom/.dsk` | `MSX.ROM`, `MSX2.ROM`… (fmsx) | 🟢 |
| 37 | PC-FX | 1994 | mednafen_pcfx | `.chd/.cue` | `pcfx.rom` | ❔ |
| 38 | Sharp X68000 | 1987 | — (px68k no instalado) | `.dim` | — | 🔴 |
| 39 | Commodore 64 | 1982 | vice_x64sc / vice_x64 | `.d64/.t64/.crt` | integradas en VICE | 🟢 |
| 40 | Amiga | 1985 | — (puae no instalado) | `.adf/.hdf` | Kickstart | 🔴 |
| 41 | ZX Spectrum | 1982 | — (fuse no instalado) | `.tzx/.tap/.z80` | — | 🔴 |
| 42 | DOS / PC | 1981 | dosbox_svn / dosbox | `.exe/.com/.bat` | No | 🟢/🟡 según juego |
| 43 | ScummVM | — | scummvm | `.scummvm` | temas opcionales | 🟢 |
| 44 | CHIP-8 | 1977 | — (sin core) | `.ch8` | — | 🔴 |
| 45 | Sega NAOMI (arcade) | 1998 | flycast | `.zip` | `dc/naomi.zip` | 🟡 probar |
| 46 | Sega Atomiswave (arcade) | 2003 | flycast | `.zip` | `dc/awbios.zip` | 🟡 probar |
| 47 | Pokémon Mini | 2001 | — (pokemini no instalado) | `.min` | — | 🔴 |
| 48 | GameCube | 2001 | — (Dolphin, solo en Linux) | `.iso/.gcm/.rvz` | — | 🐧 |
| 49 | Wii | 2006 | — (Dolphin, solo en Linux) | `.iso/.wbfs/.rvz` | — | 🐧 |
| 50 | PS Vita | 2011 | — (Vita3K, solo en Linux) | — | firmware de Vita | 🐧 sin informes |
| 51 | PS3 | 2006 | — (RPCS3, solo en Linux) | — | firmware de PS3 | 🐧 pocos juegos |
| 52 | Xbox / Xbox 360 | 2001/2005 | — | — | — | 🔴 |
| 53 | Nintendo Switch | 2017 | — | — | — | 🔴 |

Todas las BIOS van en `/data/retroarch/system/`, respetando la subcarpeta cuando la hay (`dc/`, `PPSSPP/`…). La excepción es `neogeo.zip`, que va junto a las ROMs.

### Otros cores instalados, sin carpeta en `ROMS/`

El Core Installer trae cores para sistemas que no están en la tabla. Ninguno tiene carpeta ni está en la hoja de ruta; se listan para saber que existen:

| Sistema | Core | ROM | BIOS |
|---|---|---|---|
| Atari ST / STE | `hatari` | `.st/.msa/.stx` | `tos.img` (obligatoria) |
| Atari Jaguar | `virtualjaguar` | `.j64/.jag` | no (CD: `[BIOS] Atari Jaguar CD (World).j64`) |
| Vectrex | `vecx` | `.vec/.bin` | no |
| ColecoVision / SG-1000 / SVI | `bluemsx` | `.col/.sg` | `Databases/` y `Machines/` de blueMSX |
| SG-1000 | `genesis_plus_gx` / `picodrive` | `.sg` | no |
| Commodore VIC-20, Plus/4, PET, C128, CBM-II, SuperCPU | `vice_xvic`, `vice_xplus4`, `vice_xpet`, `vice_x128`, `vice_xcbm2`, `vice_xscpu64` | como C64 | integradas |
| SuperGrafx | `mednafen_supergrafx` | `.sgx` (en `PCE/`) | no |
| Doom | `prboom` | `.wad` | no (hace falta el IWAD del juego) |
| Quake / Quake II | `tyrquake` / `vitaquake2` | `.pak` | no |
| Java ME (móviles) | `squirreljme` | `.jar/.jad` | `squirreljme.jar` |
| VMU de Dreamcast | `vemulator` | `.vms/.dci` | no |
| Mr.Boom (Bomberman libre) | `mrboom` | sin ROM | no |
| 2048 | `2048` | sin ROM | no |

## Orden de implantación

La hoja de ruta con casillas está en [`PLAN.md`](../PLAN.md). Resumen:

1. **Tanda 1, sin BIOS:** Atari 2600/7800, PC Engine, Neo Geo Pocket, WonderSwan, Lynx, 32X, Virtual Boy.
2. **Tanda 2, arcade:** Neo Geo y FB Alpha 2012, y MAME 2003-Plus. Romset de la versión exacta.
3. **Tanda 3, con BIOS:** Sega CD, PC Engine CD, Famicom Disk System, Atari 5200, MSX.
4. **Tanda 4, PS1** como PS1 Classics.
5. **Tanda 5, PSP** como PSP Classics.
6. **Ordenadores:** C64, DOS, ScummVM.
7. **Probar después:** Dreamcast, NAOMI, Atomiswave, Saturn, 3DO, PC-FX.
8. **Aparcados:** N64 y DS, reportados lentos; PS2 para más adelante.
9. **Solo con Linux, fuera de la hoja de ruta:** GameCube, Wii, PS3 y PS Vita.

### Solo con Linux — GameCube, Wii, PS3 y PS Vita

Dentro del sistema de la PS4 no hay emulador para ninguna de estas: Dolphin necesita OpenGL 3.3 / GLES 3.0 / Vulkan y el port de RetroArch (orbis) solo llega a OpenGL ES 2; RPCS3 y Vita3K solo existen para Linux, Windows y macOS.

Lo que sí hay es **Linux en esta consola**. En 12.52 está disponible: [ps4-linux-loader](https://github.com/ps4-linux/ps4-linux-loader) soporta de 5.05 a 13.52 y detecta la PS4 Pro, GoldHEN 2.4b18.9 arregló el arranque (kexec), y hay distribuciones recientes (Debian 13, Xubuntu 25.04, CachyOS, Manjaro, octubre de 2025) con kernel 6.6 y driver AMDGPU. Bajo Linux corren emuladores de PC, con el mismo hardware: 8 núcleos Jaguar a 2,1 GHz y una GPU tipo Polaris.

| Consola | Emulador en Linux | Informes en PS4 Pro |
|---|---|---|
| GameCube / Wii | Dolphin | Funciona; *Pikmin* a 50 fps en PS4 Pro. Con OpenGL: el backend Vulkan se cuelga en PS4 Pro con Mesa 22 o superior |
| PS3 | RPCS3 | *Demon's Souls* y *Folklore* reportados jugables; los juegos que cargan las SPU van cortos de CPU |
| PS Vita | Vita3K | Sin informes en PS4. El emulador sigue experimental incluso en PC |

Lo que cuesta, y por lo que **no está en la hoja de ruta**:

- Cada arranque de Linux exige GoldHEN cargado y luego el loader; al reiniciar vuelve el sistema de la PS4 intacto. No conviven: mientras está Linux no hay RetroArch ni PS1/PSP Classics.
- Linux vive en un USB o disco externo, con teclado y ratón. Es un PC con Linux que hay que administrar.
- Ninguno de estos informes está verificado en esta consola.

Si algún día se quiere probar, es un proyecto aparte: distro de [ps4linux.com](https://ps4linux.com/) y loader, en un disco propio.

### No viables

- **Xbox / Xbox 360** — pese a ser x86 como PS4, no existe ningún port de Cxbx-Reloaded ni Xenia para orbis. En Linux, xemu (Xbox original) es posible en teoría, pero no hay informes en PS4; Xenia necesita mucha más potencia (JIT + GPU DX12/Vulkan avanzada).
- **Nintendo Switch** — Yuzu/Ryujinx exigen mucha más CPU y una GPU con Vulkan avanzado de lo que ofrece PS4, también bajo Linux. Ningún proyecto lo intenta sobre orbis.
- **Nintendo 3DS** — sin emulador en orbis. En Linux (Azahar/Lime3DS) sería posible en teoría, sin informes en PS4.

Si aparece un port nuevo para orbis, revisar esta sección.

**Sin core en esta PS4:** Neo Geo CD, Amiga, ZX Spectrum, Sharp X68000, CHIP-8 y Pokémon Mini tienen emulador en RetroArch, pero su core no está entre los 74 instalados.

## PS1, PSP y Dreamcast en detalle

### PS1

La vía recomendada es **PS1 Classics**: el juego se convierte en el PC a un paquete que incluye el emulador oficial de Sony (`ps1hd`) y se instala como cualquier otro. Herramientas: **PSX-FPKG** (Jabu; `.bin/.cue` con varios `.bin`, e ISO; desde firmware 5.05) o PS Classics fPKG Builder (SvenGDK; solo `.bin`, repositorio archivado desde noviembre de 2025). Hay lista de compatibilidad en PSDevWiki.

En RetroArch los cores instalados son `pcsx_rearmed` (BIOS opcional) y `mednafen_psx` (BIOS obligatoria). *Beetle PSX HW* no está instalado. `pcsx_rearmed` solo tiene recompilador para x86-64 desde 2020 (Lightrec) y no está confirmado que el build de este port lo incluya; sin él va en intérprete y el 3D se arrastra.

### PSP

La vía recomendada es **PSP Classics** con PSP-FPKG, que usa el emulador PSPHD de PS Plus. La compatibilidad es mixta: unos juegos van perfectos y otros tienen fallos, así que conviene consultar cada juego en la lista de PSDevWiki antes de convertirlo.

Alternativa en RetroArch: el core `ppsspp`, que necesita la carpeta `assets` **completa** de PPSSPP en `system/PPSSPP/` (no solo `ppge_atlas.zim`, que es lo único que nombra el `.info`). Sin JIT en este port, así que va lento.

### PS2

No hay core de PS2 en RetroArch para PS4. La vía es **PS2 Classics**: un paquete con el emulador oficial de Sony que Jabu extrajo de los PS2 Classics de PS4. Herramientas de PC: **PS2-FPKG** (Jabu; convierte `.iso`/`.bin` y permite elegir el emulador base y añadir configuración) y **PS2 Classic GUI**, que incorpora una comprobación de compatibilidad. Los emuladores base más usados son el de *Jak* (v2, el más compatible, con opción "intentar mejorar compatibilidad" y soporte de parches Lua) y el *Rogue*; la compatibilidad va juego a juego y está en la [lista de PSDevWiki](https://www.psdevwiki.com/ps4/PS2_Classics_Emulator_Compatibility_List). No necesita BIOS: el emulador la lleva dentro. Funciona desde firmware 5.05.

Las 5 ISO de `/data/ROMS/PS2` de la consola no sirven ahí: RetroArch no las abre. Hay que bajarlas al PC, convertirlas y subir el paquete a `/data/pkg/`.

### Dreamcast

Core `flycast`, con la BIOS en `system/dc/dc_boot.bin`. Hay informes contradictorios sobre su rendimiento en PS4: probar un juego antes de meter la colección. NAOMI y Atomiswave usan el mismo core, con `dc/naomi.zip` y `dc/awbios.zip`.

## Arcade: no mezclar

MAME y FB Alpha no son intercambiables, y un romset de una versión puede no funcionar con otra versión del mismo emulador.

```
ARCADE/
├── FBNEO/        <- FB Alpha 2012 (+ CPS1/2/3); el nombre viene de la guía original
├── MAME/         <- MAME 2003-Plus recomendado
├── NAOMI/        <- Flycast
└── ATOMISWAVE/   <- Flycast
```

Cada colección debe corresponder a la versión exacta del core que la ejecuta.

## Dónde instalar

**Homebrew Store** en la PS4 con GoldHEN — permite descargar/instalar RetroArch y otros homebrew directamente desde la consola. Los cores de esta PS4 vienen del Core Installer (`SSNE20000`).

Qué va a cada ruta de la consola (PKG, ROMs, BIOS, `.info` y partidas) está en [`INSTALL.md`](../INSTALL.md).

**Nota:** no actualizar el firmware 12.52. Hay exploit público hasta 13.00; por encima no hay nada, y se perdería GoldHEN, RetroArch y Linux. Cómo se carga GoldHEN en 12.52, en [`INSTALL.md`](../INSTALL.md).

## Trucos

Dos sistemas distintos, no intercambiables:

- **GoldHEN (la consola):** menú de trucos integrado. Lee archivos `{TITLEID}_{versión}.json`, `.shn` o `.mc4` en `/user/data/GoldHEN/cheats/json/`, `/shn/` y `/mc4/` (un formato por juego y versión). El repositorio oficial es [GoldHEN_Cheat_Repository](https://github.com/GoldHEN/GoldHEN_Cheat_Repository), submódulo `goldhen_cheats/` de este repo. Se suben por FTP. Sirve para juegos de PS4, no para lo que corre dentro de RetroArch.
- **RetroArch:** trucos propios (`.cht`) en `/data/retroarch/cheats/`, para las ROMs emuladas. Se cargan desde el menú rápido del juego.

El submódulo `ps4_cheats/` (shadps4-emu) es el repositorio de trucos de **shadPS4, el emulador de PS4 para PC**: mismo formato JSON, pero no es lo que lee GoldHEN. Se conserva como histórico.

## Referencias

- [PS4 Emulators & Homebrew — ConsoleMods](https://consolemods.org/wiki/PS4%3AEmulators_and_Homebrew_Games)
- [PS4 Homebrew Store — ConsoleMods](https://consolemods.org/wiki/PS4%3AHomebrew_Store)
- [RetroArch — GitHub oficial](https://github.com/libretro/RetroArch) (incluye target `orbis` para PS4)
- [RetroArch PS4 R4 — PSX-Place](https://psx-place.com/threads/retroarch-ps4-r4-released-21-new-cores-added-ppsspp-mame-2015-new-dynarec-support-flycast.30137/)
- [PS4 RetroArch Port (Unofficial) — GBAtemp](https://gbatemp.net/threads/release-ps4-retroarch-port-unofficial.555028/)
- [PSP-FPKG v1.0 — PSXHAX](https://www.psxhax.com/threads/psp-fpkg-v1-0-app-to-convert-psp-isos-to-ps4-fpkgs-by-jabupl.13344/)
- [PS Classics fPKG Builder — GitHub](https://github.com/SvenGDK/PS-Classics-fPKG-Builder/releases)
- [PS1 Classics Emulator Compatibility List — PSDevWiki](https://www.psdevwiki.com/ps4/PS1_Classics_Emulator_Compatibility_List)
- [PSP Classics Emulator Compatibility List — PSDevWiki](https://www.psdevwiki.com/ps4/Template:PSP_Classics_Emulator_Compatibility_List)
- [PS2-FPKG — GameBrew](https://www.gamebrew.org/wiki/PS2-FPKG_PS4) · [PS2 Classics Emulator Compatibility List — PSDevWiki](https://www.psdevwiki.com/ps4/PS2_Classics_Emulator_Compatibility_List)
- [PSX-FPKG — PSX-Place](https://www.psx-place.com/threads/psx-fpkg-by-jabu-a-tool-to-convert-ps1-psx-games-for-use-on-ps4.30498/) · [PS1HD, notas del emulador oficial](https://github.com/andshrew/PlayStation-PS1HD)
- [GoldHEN_Cheat_Repository](https://github.com/GoldHEN/GoldHEN_Cheat_Repository) · [Menú de trucos de GoldHEN](https://github.com/GoldHEN/GoldHEN/blob/master/CHEATMENU.md)
- [ps4-linux-loader — GitHub](https://github.com/ps4-linux/ps4-linux-loader)
- [PS4Linux: distros y noticias](https://ps4linux.com/) · [Vulkan en PS4 Pro](https://ps4linux.com/ps4-pro-fix-vulkan-fix-crash/)
- [Dolphin on PS4 Pro — GBAtemp](https://gbatemp.net/threads/dolphin-on-ps4-pro.495799/) · [Linux games on PS4 Pro — GBAtemp](https://gbatemp.net/threads/linux-games-on-ps4-pro.576294/)

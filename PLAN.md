# Plan — PS4 Pro Retro Setup (GoldHEN 12.52)

Checklist maestra para preparar la carpeta `/emu` antes de copiarla a la PS4. Este archivo vive fuera de `/emu` a propósito — no se copia a la consola, es solo para seguimiento durante la preparación.

## Estructura

```
emu/
├── APPS/                 <- PKGs de emuladores
├── BIOS/                 <- BIOS (en la raíz, con el nombre que espera cada core)
├── ROMS/<SISTEMA>/       <- ROMs por sistema
├── RETROARCH/info/       <- .info de los cores (sí se versionan)
├── SAVES/                <- partidas guardadas (.srm)
├── MEDIA/<SISTEMA>/      <- carátulas, no se suben a la consola
└── EXTRAS/               <- apartado: no son juegos o son duplicados, no se sube
catalogo/                 <- un puntero .ref por juego (sí se versiona)
```

Todo el contenido binario de `emu/` está ignorado por git. `emu/` **no se copia tal cual** a la consola: cada subcarpeta tiene su destino. El mapeo y el procedimiento completo están en [`INSTALL.md`](INSTALL.md).

Del contenido binario solo se versiona la **referencia**, no el archivo:

- `catalogo/` — un `.ref` por archivo (SHA-1, tamaño y, en los zip, SHA-1 de la ROM interior). Cada commit lista los juegos añadidos, quitados o renombrados.
- `inventory.csv` — lo mismo en una tabla; `INVENTORY.md` — resumen por sistema.

Se regeneran solos en cada commit con el hook `tools/hooks/pre-commit`. A mano: `python tools/inventory.py`.

**Barrera anti-binarios:** `tools/guard.py`, llamado desde los hooks `pre-commit` y `pre-push`, bloquea cualquier binario o archivo de más de 5 MB antes de que llegue a GitHub. En un clon nuevo, instalar los hooks: `cp tools/hooks/pre-commit tools/hooks/pre-push .git/hooks/`.

## 0. Base del sistema

- [x] GoldHEN 12.52 instalado en la PS4 Pro
- [x] PKGs de RetroArch descargados y verificados (ver `emu/APPS/README.md`)
- [x] RetroArch (`SSNE10000`) instalado en la consola
- [x] RetroArch abierto una vez (crea `/data/retroarch/`)
- [x] Core Installer (`SSNE20000`) instalado y cores desplegados
- [x] **Smoke test superado** — Bomberman (NES) con imagen y sonido correctos
- [x] `emu/RETROARCH/info/` subido a `/data/retroarch/info/` (74 `.info`, verificado por FTP)
- [x] Filtro de extensiones reactivado (verificado en `retroarch.cfg`)
- [ ] Herramientas de conversión a paquete en el PC, para PS1 y PSP Classics (tandas 4 y 5)
- [ ] Homebrew Store instalado (opcional)
- [x] Repo local `D:\ps4` inicializado en git
- [x] `.gitmodules`: `ps4_cheats` (trucos de shadPS4, histórico) y `goldhen_cheats` (repositorio oficial de trucos de GoldHEN, 2026-09-13)
- [x] Guía `emu/emuladores-ps4.md` creada y corregida contra los cores instalados
- [x] Estructura de carpetas `/emu` creada, Arcade separado en MAME / FB Alpha 2012 / NAOMI / Atomiswave
- [x] Reestructurado en `APPS/` + `BIOS/` + `ROMS/`
- [x] `.gitignore`: se versiona la estructura y los `.md`, nunca los binarios
- [x] `tools/inventory.py` + `catalogo/` + hook pre-commit — juegos trackeados por referencia
- [x] `tools/guard.py` + hooks pre-commit/pre-push — ningún binario puede llegar a GitHub
- [x] Limpieza 2026-09-12 (registro en `cleanup-2026-09-12.tsv`): MD deduplicado, ROMs mal colocadas movidas, BIOS de trucos, carátulas y partidas apartadas, nombres con tildes pasados a ASCII
- [x] Revisión de consolas restantes y hoja de ruta (2026-09-13)
- [x] Bases de datos, listas y carátulas de 18 sistemas preparadas en `emu/RETROARCH/` con `tools/retroarch_lists.py`
- [x] Bases de datos, listas y carátulas subidas a la consola y verificadas por FTP (2026-09-13): 18 `.rdb` y 18 `.lpl` con el mismo SHA-1 que en el PC, y 5373 carátulas

## 1. Hecho — en la PS4

| Sistema | Carpeta | BIOS | ROMs | Probado en PS4 |
|---|---|---|---|---|
| NES | `NES/` | — | [x] 634 | [x] |
| SNES | `SNES/` | — | [x] 164 | [ ] |
| Game Boy | `GB/` | — | [x] 1542 | [ ] |
| Game Boy Color | `GBC/` | — | [x] 497 | [ ] |
| Game Boy Advance | `GBA/` | — | [x] 214 | [x] |
| Master System | `SMS/` | [x] opcional | [x] 333 | [x] |
| Game Gear | `GG/` | [x] opcional | [x] 373 | [ ] |
| Mega Drive | `MD/` | [x] opcional | [x] 1337 | [ ] |

## 2. Hoja de ruta

Orden acordado el 2026-09-13. Cores, extensiones y BIOS salen de los `.info` de libretro-core-info (uno por cada uno de los 74 cores instalados); los cores son del port de 2020 y los `.info` actuales, así que pueden diferir en algún detalle (ver `emu/RETROARCH/README.md`). El rendimiento sale de informes de la comunidad y aún no se ha probado en esta consola: **probar un juego antes de meter la colección entera**. Detalle de cada sistema en el `README.md` de su carpeta.

### Tanda 1 — sin BIOS, deberían ir al 100%

| Sistema | Carpeta | Core | ROMs | Probado en PS4 |
|---|---|---|---|---|
| Atari 2600 | `ATARI2600/` | stella2014 | [x] 885 | [ ] |
| Atari 7800 | `ATARI7800/` | prosystem | [x] 170 | [ ] |
| PC Engine | `PCE/` | mednafen_pce_fast | [x] 210 | [ ] |
| Neo Geo Pocket | `NGP/` | mednafen_ngp | [x] 3 | [ ] |
| Neo Geo Pocket Color | `NGPC/` | mednafen_ngp | [x] 72 | [ ] |
| WonderSwan | `WS/` | mednafen_wswan | [x] 214 | [ ] |
| WonderSwan Color | `WSC/` | mednafen_wswan | [x] 131 | [ ] |
| Atari Lynx | `LYNX/` | handy | [x] 136 | [ ] |
| 32X | `32X/` | picodrive | [x] 45 | [ ] |
| Virtual Boy | `VB/` | mednafen_vb | [x] 31 | [ ] |

ROMs copiadas y ordenadas el 2026-09-13 (registro en `cleanup-2026-09-13.tsv`): Neo Geo Pocket y WonderSwan separados por cabecera, duplicados, carátulas y archivos que no son juegos apartados. `lynxboot.img` verificada con `System.dat` de libretro y copiada a `emu/BIOS/`. **Subido y verificado por FTP el 2026-09-13:** las 1897 ROMs están en la consola con el mismo nombre y tamaño que en el PC. Falta probar un juego de cada sistema.

### Tanda 2 — arcade

El romset tiene que ser de la versión exacta del core.

| Sistema | Carpeta | Core | Romset | ROMs | Probado en PS4 |
|---|---|---|---|---|---|
| Neo Geo | `NEOGEO/` | fbalpha2012_neogeo | FB Alpha 2012 + `neogeo.zip` junto a las ROMs | [ ] | [ ] |
| Arcade FB Alpha 2012 | `ARCADE/FBNEO/` | fbalpha2012 (+ cps1/2/3) | FB Alpha 2012 | [ ] | [ ] |
| Arcade MAME | `ARCADE/MAME/` | mame2003_plus | MAME 2003-Plus; solo juegos 2D | [ ] | [ ] |

### Tanda 3 — necesitan BIOS

| Sistema | Carpeta | Core | BIOS | ROMs | Probado en PS4 |
|---|---|---|---|---|---|
| Sega CD | `SEGACD/` | genesis_plus_gx | [x] `bios_CD_U/E/J.bin` ya subidas | [ ] | [ ] |
| PC Engine CD | `PCECD/` | mednafen_pce_fast | [ ] `syscard3.pce` | [ ] | [ ] |
| Famicom Disk System | `FDS/` | nestopia | [ ] `disksys.rom` | [ ] | [ ] |
| Atari 5200 | `ATARI5200/` | atari800 | [ ] `5200.rom` | [ ] | [ ] |
| MSX / MSX2 | `MSX/` | fmsx | [ ] `MSX.ROM`, `MSX2.ROM`, `MSX2EXT.ROM`, `MSX2P.ROM`, `MSX2PEXT.ROM` | [ ] | [ ] |

### Tanda 4 — PS1, como PS1 Classics

| Sistema | Carpeta | Vía | ROMs | Probado en PS4 |
|---|---|---|---|---|
| PS1 | `PSX/` | PSX-FPKG: paquete con el emulador oficial de Sony. Alternativa en RetroArch: pcsx_rearmed + `scph5501.bin` | [ ] | [ ] |

### Tanda 5 — PSP, como PSP Classics

| Sistema | Carpeta | Vía | ROMs | Probado en PS4 |
|---|---|---|---|---|
| PSP | `PSP/` | PSP-FPKG, revisando cada juego en la lista de compatibilidad. Alternativa: ppsspp + carpeta `assets` de PPSSPP en `system/PPSSPP/` | [ ] | [ ] |

### Ordenadores

| Sistema | Carpeta | Core | ROMs | Probado en PS4 |
|---|---|---|---|---|
| Commodore 64 | `C64/` | vice_x64sc | [ ] | [ ] |
| DOS | `DOS/` | dosbox_svn | [ ] | [ ] |
| ScummVM | `SCUMMVM/` | scummvm | [ ] | [ ] |

### Probar después — rendimiento variable o sin datos

| Sistema | Carpeta | Core | BIOS | ROMs | Probado en PS4 |
|---|---|---|---|---|---|
| Dreamcast | `DC/` | flycast | [ ] `dc/dc_boot.bin` | [ ] | [ ] |
| Sega NAOMI | `ARCADE/NAOMI/` | flycast | [ ] `dc/naomi.zip` | [ ] | [ ] |
| Sega Atomiswave | `ARCADE/ATOMISWAVE/` | flycast | [ ] `dc/awbios.zip` | [ ] | [ ] |
| Saturn | `SATURN/` | yabause | [ ] `saturn_bios.bin` | [ ] | [ ] |
| 3DO | `3DO/` | opera | [ ] `panafz10.bin` | [ ] | [ ] |
| PC-FX | `PCFX/` | mednafen_pcfx | [ ] `pcfx.rom` | [ ] | [ ] |

### Aparcados

| Sistema | Carpeta | Motivo |
|---|---|---|
| Nintendo 64 | `N64/` | Reportado lento o injugable en el RetroArch de PS4 |
| Nintendo DS | `NDS/` | Reportado lento |
| PS2 | `PS2/` | Más adelante, como PS2 Classics. Hay 5 ISO en `/data/ROMS/PS2` de la consola |

### Sin core en la PS4

`POKEMINI/` (pokemini), `AMIGA/` (puae), `ZXSPECTRUM/` (fuse), `NEOGEOCD/` (neocd), `X68000/` (px68k) y `CHIP8/`. Ninguno de esos cores está entre los 74 instalados.

### Solo con Linux — proyecto aparte, en marcha

`GC/`, `WII/`, `PS3/` y `VITA/`: no hay emulador en el sistema de la PS4, pero Linux sí arranca en 12.52 y ahí corren Dolphin y RPCS3 (con informes en PS4 Pro) y Vita3K (sin informes). Desde el 2026-09-13 se prepara en [`linux/`](linux/README.md): la consola es Baikal B1, lo que obliga a kernel 5.4.247, distro con Mesa ≤ 25.1 y disco externo.

- [x] 🤖 Loader v25, kernel 5.4.247 (Baikal) e initramfs externo, verificados y catalogados
- [x] 🧑 Distro con Mesa ≤ 25.1 en `linux/distros/`: Arch de marzo de 2026 con KDE y Mesa 25.1.0-devel, verificada (2026-09-13)
- [x] 🤖 Pendrive Kingston DataTraveler 3.0 de 30,9 GB preparado el 2026-09-13: MBR, FAT32 `PS4LINUX`, con `bzImage`, `initramfs.cpio.gz` (SHA-1 comprobados) y `psxitarch.tar.gz` (2,73 GB, `gzip -t` correcto)
- [ ] 🎮 Llega a la rescue shell con el payload de 1 GB — **6 intentos el 13-09 sin señal de vídeo** en el monitor Samsung; probar con una tele (registro en `linux/README.md`)
- [ ] 🎮 `install-psxitarch.sh` instala y arranca la distro
- [ ] 🎮 Escritorio con GPU (`glxinfo`: `AMD Liverpool`, no `llvmpipe`)
- [ ] 🎮 Dolphin con *Wind Waker* a velocidad completa (OpenGL, resolución nativa); después RPCS3
- [ ] 🤖 Cuando salga el kernel 7.x para Baikal: cambiar a CachyOS Light y revisar `linux/README.md`

### No viables

`3DS/`, `XBOX/` y `SWITCH/`. Motivos en [`emu/emuladores-ps4.md`](emu/emuladores-ps4.md).

## 3. Rutina al añadir un sistema nuevo

1. Copiar las ROMs a `emu/ROMS/<SISTEMA>/` en el PC, **con nombres sin tildes ni ñ**.
2. Subir por FTP a `/data/ROMS/<SISTEMA>/` (puerto 2121, modo pasivo, 1 conexión).
3. Si el sistema necesita BIOS, subirla a `/data/retroarch/system/` con el nombre y la subcarpeta que indica su README.
4. Probar un juego y marcar la casilla "Probado en PS4".
5. Commit — el hook regenera inventario y catálogo, y el commit lista cada juego añadido.

## 4. Pendientes

La lista completa y priorizada de lo que falta conseguir, preparar o configurar está en [`PENDIENTES.md`](PENDIENTES.md).

**Subida a la PS4** — completada y verificada por FTP el 2026-09-12:

- [x] ROMs de NES, SNES, GB, GBC, GBA, GG, SMS y MD en `/data/ROMS/`: 5094 juegos, mismo nombre y tamaño que en el PC
- [x] 9 partidas de GBA en `/data/retroarch/savefiles/`: SHA-1 idéntico al del PC y cada una casa con su ROM
- [x] 7 BIOS en `/data/retroarch/system/`: SHA-1 idéntico al del PC
- [x] Borrados `/data/pkg/emu` (1,6 GB de PKG ya instalados) y `/data/emu`

**Pruebas en la PS4** (según el historial de RetroArch):

- [x] GBA — *Dragon Ball Z: The Legacy of Goku II*. Se abrió con `mednafen_gba`; el core recomendado es mGBA
- [x] SMS — *Indiana Jones and the Last Crusade*, que ya ha creado su partida guardada
- [ ] GB, GBC, GG y MD: un juego de cada
- [ ] Cargar una de las partidas de GBA subidas (Castlevania, Pokemon Rojo fuego…)
- [ ] Borrar del historial las 2 entradas que apuntan a la ruta vieja `/data/roms`

**Colección en el PC:**

- [ ] `EXTRAS/MD-duplicados/` (676) y `EXTRAS/MD-malos/` (6): decidir si se borran
- [ ] `ROMS/NES/Datach - Battle Rush….sav` suelto: decidir si va a `SAVES/`
- [ ] `gamelist.xml` y `systeminfo.txt` en `ROMS/GBC` y `ROMS/GBA`: restos de EmulationStation, no son juegos
- [ ] `.rar` de 4,4 GB en la raíz del repo (ignorado): decidir qué hacer con él
- [ ] Verificar espacio libre en la PS4 antes de subidas grandes
- [ ] Backup de la colección

## Notas

- No actualizar el firmware de la PS4 (12.52). Hay exploit público hasta 13.00 (Poops); por encima no hay nada. Cómo se carga GoldHEN en 12.52, en [`INSTALL.md`](INSTALL.md).
- No mezclar romsets de MAME y FB Alpha, ni entre versiones distintas del mismo emulador.
- Nombres de archivo sin tildes ni ñ: FileZilla los sube a la PS4 en otra codificación y dejan de coincidir con el PC (y con su partida).
- La PS4 distingue mayúsculas en las rutas: `/data/ROMS` y `/data/roms` son carpetas distintas.
- Detalle completo por sistema (core, extensiones, BIOS) en el `README.md` de cada subcarpeta de `emu/ROMS/` y en [`emu/emuladores-ps4.md`](emu/emuladores-ps4.md).

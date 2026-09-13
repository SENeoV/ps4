# APPS — Emuladores y homebrew (PKG)

Aquí van los `.pkg` que se instalan en la PS4. **Los PKG no se suben al repo** (están en `.gitignore`): pesan cientos de MB y GitHub rechaza archivos de más de 100 MB. Esta carpeta solo versiona esta documentación.

## Descargados (verificados)

Todos comprobados: cabecera PKG válida (`\x7FCNT`) y Content ID leído del propio archivo. Hashes en [`../../inventory.csv`](../../inventory.csv).

| PKG | Content ID | Tamaño | Qué es |
|---|---|--:|---|
| `PS4_SSNE10000_v4.00_Unofficial_RetroArch.pkg` | `UP0001-SSNE10000_00` | 27 MB | **RetroArch (la app).** v4.00 = la release R4 |
| `PS4_SSNE20000_v4.00_RetroArch_Core_Installer.pkg` | `UP0001-SSNE20000_00` | 1385 MB | **Core Installer.** Trae los cores offline, sin depender del Core Updater |
| `PS4_CUSB00000_v1.00_RetroArch_NES.pkg` | `UP9000-CUSB00000_00` | 64 MB | RetroArch + core NES, standalone |
| `PS4_CUSB99999_v1.00_RetroArch_QuickNES.pkg` | `UP9000-CUSB99999_00` | 25 MB | RetroArch + core QuickNES, standalone |
| `PS4_CUSB99997_v1.00_RetroArch_Picodrive.pkg` | `UP9000-CUSB99997_00` | 25 MB | RetroArch + core PicoDrive (MD/32X), standalone |
| `PS4_CUSB00001_v1.00_RetroArch_2048.pkg` | `UP9000-CUSB00001_00` | 65 MB | Juego 2048, no es un emulador |

### Lectura de esto

Los dos primeros son **justo el combo que hace falta**: la app + los cores. Con esos dos cubres la mayoría de `ROMS/`.

Los `CUSB*` son builds standalone de RetroArch con un core embebido. **Son redundantes** si instalas el Core Installer: NES, QuickNES y PicoDrive ya vienen ahí. Solo aportan un acceso directo desde el menú de la PS4 que arranca ya en ese core. El de 2048 es un juego, no pinta nada aquí.

### Falta por descargar

Nada crítico. Opcionales, para más adelante:

- Homebrew Store (`Store-R2.pkg` de pkg-zone), si prefieres instalar desde la consola en vez de por FTP
- Herramientas de PC para PS1/PS2/PSP Classics (PSX-FPKG, PS2-FPKG, PSP-FPKG): no son PKG de consola, van en el PC

## Orden recomendado de instalación

### 1. Homebrew Store (la vía fácil)

Es la forma más cómoda: instala un PKG una vez y desde ahí descargas el resto de emuladores directamente en la consola, sin USB.

- Con GoldHEN ya cargado, abre el navegador de la PS4 y ve a `pkg-zone.com/install`.
- Desde el Homebrew Store puedes instalar RetroArch y otros homebrew.

Tu firmware **12.52 está soportado por GoldHEN** (v2.4b18.9 lista 5.05, 6.71–6.72, 9.00, 9.60, 10.00–10.71, 11.00–11.52, 12.00/02, 12.50, **12.52** y 13.00). En 12.52 GoldHEN entra por el exploit Poops desde un Blu-ray; el procedimiento está en [`INSTALL.md`](../../INSTALL.md).

### 2. RetroArch (PS4) — el caballo de batalla

Port nativo de PS4 (target `orbis`). Cubre la gran mayoría de sistemas de `ROMS/`.

- Port no oficial de OsirisX, basado en RetroArch **1.8.8**. La release R4 (30-06-2020) añadió 21 cores (entre ellos PPSSPP y MAME 2015) y dynarec para Flycast. No ha habido más releases desde entonces: los cores son de 2020, aunque los `.info` de este repo sean los actuales de libretro.
- En esta consola hay **74 cores** en `/data/self/retroarch/cores/`.
- Gráficos por OpenGL ES 2 (liborbis/piglet). Sin JIT en la mayoría de cores: N64, DS, Saturn y PSP van lentos.

### 3. RetroArch Core Installer — imprescindible

RetroArch en PS4 **viene sin cores**. La única forma de conseguirlos es la app **Cores Installer** (PKG aparte, en pkg-zone con ID `SSNE20000`). El *Core Updater* de dentro de RetroArch no sirve: apunta a Bintray, que cerró en 2021.

Sin este paso RetroArch se abre pero no ejecuta nada.

### 4. Standalone

**No existe** ningún PPSSPP, Flycast ni ScummVM standalone para PS4; la petición de Flycast standalone sigue abierta ([flycast #942](https://github.com/flyinghead/flycast/issues/942)). Para PSP y PS1 la vía buena es la de los *Classics* (paquete con el emulador oficial de Sony); ver `ROMS/PSP/README.md` y `ROMS/PSX/README.md`.

## Por dónde empezar (fricción cero)

Los sistemas sin BIOS son los que funcionan nada más copiar la ROM: **NES, SNES, GB, GBC, GBA, Master System, Game Gear, Mega Drive**. Empieza por ahí para validar que RetroArch y los cores están bien antes de pelearte con BIOS o con Saturn/PS2.

## Fuentes

- [PS4 Homebrew Store — ConsoleMods](https://consolemods.org/wiki/PS4:Homebrew_Store)
- [PS4 Emulators & Homebrew — ConsoleMods](https://consolemods.org/wiki/PS4:Emulators_and_Homebrew_Games)
- [GoldHEN — GitHub](https://github.com/GoldHEN/GoldHEN)
- [RetroArch (ps4) — PSX-Place](https://www.psx-place.com/resources/retroarch-ps4.889/)
- [RetroArch PS4 R4 (cores nuevos + dynarec Flycast) — PSX-Place](https://psx-place.com/threads/retroarch-ps4-r4-released-21-new-cores-added-ppsspp-mame-2015-new-dynarec-support-flycast.30137/)
- [RetroArch Core Installer — pkg-zone](https://pkg-zone.com/details/SSNE20000)
- [RetroArch — GitHub oficial](https://github.com/libretro/RetroArch)

## Pendiente de verificar en la consola

- [x] Lista real de `/data/self/retroarch/cores/` leída por FTP el 2026-09-13: 74 cores, uno por cada `.info` del repo, 1372,5 MB en total (tabla en `emu/RETROARCH/README.md`)
- [x] El Core Installer (`SSNE20000`) ya no está instalado en `/user/app` (se desinstaló tras desplegar los cores), así que no se puede leer su versión. Los 1372,5 MB de cores casan con el PKG `r4` (1385 MB) y no con el `r4.1` "Fixed Speed" (1,27 GB): lo instalado es el `r4`. Si algún core va acelerado, la solución es el `r4.1`

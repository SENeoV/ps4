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

- PPSSPP standalone (PSP) — el core de PPSSPP ya entra con el Core Installer
- Flycast standalone (Dreamcast) — verificar build antes
- ScummVM standalone
- Homebrew Store, si prefieres instalar desde la consola en vez de por USB

## Orden recomendado de instalación

### 1. Homebrew Store (la vía fácil)

Es la forma más cómoda: instala un PKG una vez y desde ahí descargas el resto de emuladores directamente en la consola, sin USB.

- Con GoldHEN ya cargado, abre el navegador de la PS4 y ve a `pkg-zone.com/install`.
- Desde el Homebrew Store puedes instalar RetroArch y otros homebrew.

Tu firmware **12.52 está soportado por GoldHEN** (v2.4b18.9 lista 5.05, 6.71–6.72, 9.00, 9.60, 10.00–10.71, 11.00–11.52, 12.00/02, 12.50, **12.52** y 13.00).

### 2. RetroArch (PS4) — el caballo de batalla

Port nativo de PS4 (target `orbis`). Cubre la gran mayoría de sistemas de `ROMS/`.

- Es un port no oficial; la base del port es RetroArch v1.8.8 y la release R4 añadió cores nuevos (entre ellos PPSSPP y MAME 2015) y dynarec para Flycast.
- Reporta del orden de 72 cores disponibles en PS4.

### 3. RetroArch Core Installer — imprescindible

RetroArch en PS4 **viene sin cores**. Hay dos formas de conseguirlos:

- La app **Cores Installer** (PKG aparte, en pkg-zone con ID `SSNE20000`), o
- La opción **Core Updater** desde dentro de RetroArch.

Sin este paso RetroArch se abre pero no ejecuta nada.

### 4. Standalone (opcional, más adelante)

Para PSP y Dreamcast la guía recomienda standalone antes que el core, pero conviene comprobar la build concreta antes de instalar:

| App | Sistema | Estado |
|---|---|---|
| PPSSPP | PSP | Preferir standalone si hay build PS4 funcional; si no, el core de RetroArch |
| Flycast / Reicast | Dreamcast | El standalone ha tenido limitaciones históricas en PS4; verificar build |
| ScummVM | Aventuras gráficas | Standalone |

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

- [ ] Versión exacta de RetroArch instalada (condiciona qué romsets de MAME/FBNeo valen)
- [ ] Si el Homebrew Store de tu firmware ofrece PPSSPP/Flycast standalone o solo los cores

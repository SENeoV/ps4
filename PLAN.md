# Plan — PS4 Pro Retro Setup (GoldHEN 12.52)

Checklist maestra para preparar la carpeta `/emu` antes de copiarla a la PS4. Este archivo vive fuera de `/emu` a propósito — no se copia a la consola, es solo para seguimiento durante la preparación.

## Estructura

```
emu/
├── APPS/                 <- PKGs de emuladores
├── BIOS/                 <- BIOS
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
- [ ] Subir `emu/RETROARCH/info/` a `/data/retroarch/info/` (arregla la selección
      automática de core; sin esto hay que cargar el core a mano cada vez)
- [ ] Reactivar el filtro de extensiones una vez subidos los `.info`
- [ ] Homebrew Store instalado (opcional)
- [ ] PPSSPP standalone instalado (opcional)
- [ ] Flycast/Reicast standalone instalado (opcional, verificar build)
- [ ] ScummVM standalone instalado (opcional)
- [x] Repo local `D:\ps4` inicializado en git
- [x] `.gitmodules` para `ps4_cheats` configurado
- [x] Guía `emu/emuladores-ps4.md` creada
- [x] Estructura de carpetas `/emu` creada (44 plataformas, nombres cortos, Arcade separado en MAME/FBNEO)
- [x] Reestructurado en `APPS/` + `BIOS/` + `ROMS/`
- [x] `.gitignore`: se versiona la estructura y los `.md`, nunca los binarios
- [x] `tools/inventory.py` + `catalogo/` + hook pre-commit — juegos trackeados por referencia
- [x] Limpieza 2026-09-12 (registro en `cleanup-2026-09-12.tsv`): MD deduplicado, ROMs mal colocadas movidas, BIOS de trucos, carátulas y partidas apartadas

## 1. Nivel 1 — imprescindibles

| Sistema | Carpeta | BIOS lista | ROMs copiadas | Probado en PS4 |
|---|---|---|---|---|
| NES | `NES/` | — | [x] 634 | [x] |
| SNES | `SNES/` | — | [x] 164 | [ ] |
| Game Boy | `GB/` | — | [x] 1542 | [ ] |
| Game Boy Color | `GBC/` | — | [x] 497 | [ ] |
| Game Boy Advance | `GBA/` | — | [x] 214 | [ ] |
| Master System | `SMS/` | — | [x] 333 | [ ] |
| Game Gear | `GG/` | — | [x] 373 | [ ] |
| Mega Drive | `MD/` | — | [x] 1337 | [ ] |
| PC Engine | `PCE/` | — | [ ] | [ ] |
| Neo Geo AES/MVS | `NEOGEO/` | [ ] | [ ] | [ ] |
| Arcade (FBNeo) | `ARCADE/FBNEO/` | [ ] | [ ] | [ ] |
| PS1 | `PSX/` | [ ] | [ ] | [ ] |
| PSP | `PSP/` | — | [ ] | [ ] |
| Dreamcast | `DC/` | [ ] | [ ] | [ ] |
| N64 | `N64/` | — | [ ] | [ ] |
| MSX | `MSX/` | [ ] | [ ] | [ ] |
| DOS | `DOS/` | — | [ ] | [ ] |

## 2. Nivel 2 — requieren configuración

| Sistema | Carpeta | BIOS lista | ROMs copiadas | Probado en PS4 |
|---|---|---|---|---|
| Sega CD | `SEGACD/` | [ ] | [ ] | [ ] |
| 32X | `32X/` | — | [ ] | [ ] |
| PC Engine CD | `PCECD/` | [ ] | [ ] | [ ] |
| Neo Geo CD | `NEOGEOCD/` | [ ] | [ ] | [ ] |
| 3DO | `3DO/` | [ ] | [ ] | [ ] |
| Commodore 64 | `C64/` | [ ] | [ ] | [ ] |
| Amiga | `AMIGA/` | [ ] Kickstart | [ ] | [ ] |
| ZX Spectrum | `ZXSPECTRUM/` | — | [ ] | [ ] |
| Nintendo DS | `NDS/` | — | [ ] | [ ] |
| Saturn | `SATURN/` | [ ] | [ ] | [ ] |

## 3. Nivel 3 — experimental / raros

| Sistema | Carpeta | BIOS lista | ROMs copiadas | Probado en PS4 |
|---|---|---|---|---|
| Arcade (MAME) | `ARCADE/MAME/` | [ ] | [ ] | [ ] |
| PS2 | `PS2/` | [ ] | [ ] | [ ] |
| Atari 2600 | `ATARI2600/` | — | [ ] | [ ] |
| Atari 5200 | `ATARI5200/` | [ ] | [ ] | [ ] |
| Atari 7800 | `ATARI7800/` | — | [ ] | [ ] |
| Atari Lynx | `LYNX/` | — | [ ] | [ ] |
| Famicom Disk System | `FDS/` | [ ] | [ ] | [ ] |
| Virtual Boy | `VB/` | — | [ ] | [ ] |
| Neo Geo Pocket | `NGP/` | — | [ ] | [ ] |
| Neo Geo Pocket Color | `NGPC/` | — | [ ] | [ ] |
| WonderSwan | `WS/` | — | [ ] | [ ] |
| WonderSwan Color | `WSC/` | — | [ ] | [ ] |
| PC-FX | `PCFX/` | [ ] | [ ] | [ ] |
| Sharp X68000 | `X68000/` | [ ] | [ ] | [ ] |
| ScummVM | `SCUMMVM/` | — | [ ] | [ ] |
| CHIP-8 | `CHIP8/` | — | [ ] | [ ] |
| Nintendo 3DS | `3DS/` | — | 🔴 no viable | 🔴 no viable |

## 4. Rutina al añadir un sistema nuevo

1. Copiar las ROMs a `emu/ROMS/<SISTEMA>/` en el PC.
2. Subir por FTP a `/data/roms/<SISTEMA>/` (puerto 2121, modo pasivo, 1 conexión).
3. Si el sistema necesita BIOS, subirla a `/data/retroarch/system/` con el nombre que espera el core (lo indica su `.info`).
4. Probar un juego y marcar la casilla "Probado en PS4".
5. Commit — el hook regenera inventario y catálogo, y el commit lista cada juego añadido.

## 5. Pendientes generales

- [ ] Probar en la PS4 GB, GBC, GBA, SMS, GG y MD (un juego de cada)
- [ ] Subir `emu/SAVES/` a `/data/retroarch/savefiles/` y comprobar que carga una partida de GBA
- [ ] BIOS de Sega CD, Master System y Game Gear están en subcarpetas con su nombre original: renombrar y dejar en la raíz antes de subir
- [ ] `EXTRAS/MD-duplicados/` (676) y `EXTRAS/MD-malos/` (6): decidir si se borran
- [ ] `ROMS/NES/Datach - Battle Rush….sav` suelto: decidir si va a `SAVES/`
- [ ] `gamelist.xml` y `systeminfo.txt` en `ROMS/GBC` y `ROMS/GBA`: restos de EmulationStation, no son juegos
- [ ] `.rar` de 4,4 GB en la raíz del repo (ignorado): decidir qué hacer con él
- [ ] Verificar espacio libre en la PS4 antes de subidas grandes
- [ ] Backup de la colección

## Notas

- No actualizar el firmware de la PS4 (12.52) solo para tener una versión más nueva de un emulador — GoldHEN depende de esa versión exacta.
- No mezclar ROM sets de MAME y FBNeo entre versiones distintas del emulador.
- Detalle completo por sistema (emulador, extensión, BIOS) en [`emu/emuladores-ps4.md`](emu/emuladores-ps4.md) y en el `README.md` de cada subcarpeta de `/emu`.

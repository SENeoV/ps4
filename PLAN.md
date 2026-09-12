# Plan — PS4 Pro Retro Setup (GoldHEN 12.52)

Checklist maestra para preparar la carpeta `/emu` antes de copiarla a la PS4. Este archivo vive fuera de `/emu` a propósito — no se copia a la consola, es solo para seguimiento durante la preparación.

## Estructura

```
emu/                      <- esto es lo que se copia a la PS4
├── APPS/                 <- PKGs de emuladores (ignorados por git)
├── BIOS/                 <- BIOS, = carpeta "system" de RetroArch (ignoradas por git)
└── ROMS/<SISTEMA>/       <- ROMs por sistema (ignoradas por git)
```

Del contenido binario solo se versiona el **hash**, no el archivo. Tras copiar ROMs o BIOS:

```bash
bash tools/inventory.sh
```

Eso regenera `inventory.csv` (detalle, SHA-1 por archivo) e `INVENTORY.md` (resumen por sistema). El `git diff` de `inventory.csv` muestra exactamente qué contenido se añadió. SHA-1 es el hash de los DATs de No-Intro/Redump, así que sirve también para verificar volcados.

## 0. Base del sistema

- [x] GoldHEN 12.52 instalado en la PS4 Pro
- [ ] Homebrew Store instalado
- [ ] RetroArch (build orbis/PS4) instalado vía Homebrew Store
- [ ] PPSSPP standalone instalado
- [ ] Flycast/Reicast standalone instalado (verificar build actualizada)
- [ ] ScummVM standalone instalado
- [x] Repo local `D:\ps4` inicializado en git
- [x] `.gitmodules` para `ps4_cheats` configurado
- [x] Guía `emu/emuladores-ps4.md` creada
- [x] Estructura de carpetas `/emu` creada (44 plataformas, nombres cortos, Arcade separado en MAME/FBNEO)
- [x] Reestructurado en `APPS/` + `BIOS/` + `ROMS/`
- [x] `.gitignore`: se versiona la estructura y los `.md`, nunca los binarios
- [x] `tools/inventory.sh` — inventario por hash SHA-1

## 1. Nivel 1 — imprescindibles

| Sistema | Carpeta | BIOS lista | ROMs copiadas | Probado en PS4 |
|---|---|---|---|---|
| NES | `NES/` | — | [ ] | [ ] |
| SNES | `SNES/` | — | [ ] | [ ] |
| Game Boy | `GB/` | — | [ ] | [ ] |
| Game Boy Color | `GBC/` | — | [ ] | [ ] |
| Game Boy Advance | `GBA/` | — | [ ] | [ ] |
| Master System | `SMS/` | — | [ ] | [ ] |
| Game Gear | `GG/` | — | [ ] | [ ] |
| Mega Drive | `MD/` | — | [ ] | [ ] |
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

## 4. Antes de copiar a la PS4

- [ ] Revisar que cada carpeta tenga al menos 1 ROM antes de copiar (evitar carpetas vacías innecesarias)
- [ ] Confirmar que los `README.md` por carpeta no interfieren con los scrapers/frontends usados (si molestan, quitarlos antes de copiar)
- [ ] Verificar espacio libre en el USB/HDD destino
- [ ] Copiar `/emu` completo a la PS4
- [ ] Configurar rutas de contenido en RetroArch/PPSSPP/Flycast/ScummVM apuntando a las carpetas copiadas
- [ ] Probar 1 juego por sistema de Nivel 1 como humo (smoke test)
- [ ] Backup del USB/HDD final

## Notas

- No actualizar el firmware de la PS4 (12.52) solo para tener una versión más nueva de un emulador — GoldHEN depende de esa versión exacta.
- No mezclar ROM sets de MAME y FBNeo entre versiones distintas del emulador.
- Detalle completo por sistema (emulador, extensión, BIOS) en [`emu/emuladores-ps4.md`](emu/emuladores-ps4.md) y en el `README.md` de cada subcarpeta de `/emu`.

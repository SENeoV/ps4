# Plan — PS4 Pro Retro Setup (GoldHEN 12.52)

Checklist maestra para preparar la carpeta `/emu` antes de copiarla a la PS4. Este archivo vive fuera de `/emu` a propósito — no se copia a la consola, es solo para seguimiento durante la preparación.

## Estructura

```
emu/
├── APPS/                 <- PKGs de emuladores (ignorados por git)
├── BIOS/                 <- BIOS (ignoradas por git)
└── ROMS/<SISTEMA>/       <- ROMs por sistema (ignoradas por git)
```

`emu/` **no se copia tal cual** a la consola: cada subcarpeta tiene su destino
(`/data/`, `/data/retroarch/system/`, `/data/roms/`). El mapeo y el
procedimiento completo están en [`INSTALL.md`](INSTALL.md).

Del contenido binario solo se versiona el **hash**, no el archivo. Tras copiar ROMs o BIOS:

```bash
bash tools/inventory.sh
```

Eso regenera `inventory.csv` (detalle, SHA-1 por archivo) e `INVENTORY.md` (resumen por sistema). El `git diff` de `inventory.csv` muestra exactamente qué contenido se añadió. SHA-1 es el hash de los DATs de No-Intro/Redump, así que sirve también para verificar volcados.

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
- [x] `tools/inventory.sh` — inventario por hash SHA-1

## 1. Nivel 1 — imprescindibles

| Sistema | Carpeta | BIOS lista | ROMs copiadas | Probado en PS4 |
|---|---|---|---|---|
| NES | `NES/` | — | [x] 634 | [x] |
| SNES | `SNES/` | — | [x] 164 | [ ] |
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

## 4. Rutina al añadir un sistema nuevo

1. Copiar las ROMs a `emu/ROMS/<SISTEMA>/` en el PC.
2. `bash tools/inventory.sh` para registrar los hashes.
3. Subir por FTP a `/data/roms/<SISTEMA>/` (puerto 2121, modo pasivo, 1 conexión).
4. Si el sistema necesita BIOS, subirla a `/data/retroarch/system/`.
5. Probar un juego y marcar la casilla "Probado en PS4".
6. Commit — el diff de `inventory.csv` deja constancia de lo añadido.

## 5. Pendientes generales

- [ ] Verificar espacio libre en la PS4 antes de subidas grandes
- [ ] Comprobar si los `README.md` dentro de `ROMS/<SISTEMA>/` molestan en el navegador
      de RetroArch una vez reactivado el filtro de extensiones (no deberían: `.md` no
      está en ninguna lista de extensiones soportadas)
- [ ] Backup de la colección

## Notas

- No actualizar el firmware de la PS4 (12.52) solo para tener una versión más nueva de un emulador — GoldHEN depende de esa versión exacta.
- No mezclar ROM sets de MAME y FBNeo entre versiones distintas del emulador.
- Detalle completo por sistema (emulador, extensión, BIOS) en [`emu/emuladores-ps4.md`](emu/emuladores-ps4.md) y en el `README.md` de cada subcarpeta de `/emu`.

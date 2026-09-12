# BIOS

Carpeta única de BIOS. En RetroArch esto corresponde a la carpeta **`system`** — hay que apuntar *Settings → Directory → System/BIOS* a la ruta donde acabe esta carpeta en la PS4.

**Los archivos de BIOS no se suben al repo** (están en `.gitignore`). Solo se versiona esta documentación. Las BIOS las aportas tú desde tu hardware original.

## Sistemas que NO necesitan BIOS

Empieza por estos, no requieren nada extra:

`NES` · `SNES` · `GB` · `GBC` · `GBA` · `MD` · `SMS` · `GG` · `PCE` (cartuchos) · `N64` · `PSP` · `DOS` · `ZXSPECTRUM` · `VB` · `LYNX` · `NGP` · `NGPC` · `WS` · `WSC` · `ATARI2600` · `ATARI7800` · `CHIP8`

## Sistemas que SÍ necesitan BIOS

| Sistema | Carpeta ROMS | Notas |
|---|---|---|
| PS1 | `PSX/` | BIOS SCPH. RetroArch documenta nombres y hashes esperados. Beetle PSX HW la exige |
| Saturn | `SATURN/` | Obligatoria |
| Dreamcast | `DC/` | Obligatoria |
| 3DO | `3DO/` | Obligatoria |
| Sega CD | `SEGACD/` | Una por región (US / EU / JP) |
| PC Engine CD | `PCECD/` | Syscard |
| Neo Geo CD | `NEOGEOCD/` | Obligatoria |
| Neo Geo | `NEOGEO/` | Depende de la configuración del core |
| PS2 | `PS2/` | BIOS + configuración |
| Amiga | `AMIGA/` | Kickstart |
| C64 | `C64/` | ROMs del sistema |
| MSX | `MSX/` | Depende del core (fMSX / blueMSX) |
| Famicom Disk System | `FDS/` | BIOS del disk system |
| Atari 5200 | `ATARI5200/` | Según el core |
| 32X | `32X/` | Según el juego |
| PC-FX | `PCFX/` | Obligatoria |
| X68000 | `X68000/` | Obligatoria |
| Nintendo DS | `NDS/` | Solo para ciertas funciones |
| Arcade (MAME/FBNeo) | `ARCADE/` | No es "BIOS" al uso: son ROM sets de BIOS dentro del propio set |

## Consejo

Las BIOS son sensibles al nombre de archivo y al hash. Si un sistema no arranca y la ROM es buena, el 90 % de las veces es que la BIOS tiene el nombre incorrecto o es una revisión distinta a la que espera el core. Revisa el log de RetroArch, que dice qué archivo exacto está buscando.

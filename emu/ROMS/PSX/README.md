# PSX — PlayStation (1994)

- **Estado:** Tanda 4 — PS1
- **Cores instalados en la PS4:** `pcsx_rearmed` (recomendado), `mednafen_psx`
- **Extensiones:** `.chd` `.cue` `.pbp`
- **BIOS** (en `/data/retroarch/system/`, salvo que se indique otra cosa):
  - `scph5501.bin` — USA; `scph5500.bin` Japón y `scph5502.bin` Europa. Opcional en `pcsx_rearmed`, obligatoria en `mednafen_psx`

**Recomendada: PS1 Classics.** Se convierte el juego en el PC a un paquete que lleva dentro el emulador oficial de Sony (`ps1hd`) y se instala como un juego. Herramientas: **PSX-FPKG** (Jabu; acepta `.bin/.cue` con varios `.bin`, e ISO; desde firmware 5.05) o PS Classics fPKG Builder (SvenGDK; solo `.bin`, archivado en noviembre de 2025). Antes de convertir, mirar el juego en la [lista de compatibilidad de PSDevWiki](https://www.psdevwiki.com/ps4/PS1_Classics_Emulator_Compatibility_List).

Esta carpeta es para la vía RetroArch, que va peor: `pcsx_rearmed` solo tiene recompilador en x86-64 desde 2020 (Lightrec) y no está confirmado que el build de este port lo lleve; sin él corre en intérprete y el 3D se arrastra.

_Cores, extensiones y BIOS según los `.info` de libretro-core-info (uno por core instalado, 2026-09-13). Los cores son del port R4 de 2020 y los `.info` son los actuales, así que en los cores que siguen en desarrollo (mGBA, VICE, ScummVM, PPSSPP, Flycast, atari800…) extensiones y BIOS pueden no coincidir con el core real; en los contrastados con el binario de la consola (stella2014, prosystem, gearboy, mednafen_wswan, mGBA) las extensiones coinciden. El rendimiento sale de informes de la comunidad y aún no se ha probado en esta consola._

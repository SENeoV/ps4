# EXTRAS — apartado, no se sube a la PS4

Archivos que venían con las ROMs pero no son juegos jugables, o que son duplicados, variantes o volcados rotos. Están **movidos, no borrados**.

| Carpeta | Contenido |
|---|---|
| `EXTRAS/GB/` | BIOS de dispositivos: trucos (Game Genie, Game Shark, Action Replay), copiadores (Smart Card, Backup Station, Challenger) y utilidades (Work Master) |
| `EXTRAS/GBA/` | `.sgm`: savestate de VisualBoyAdvance. RetroArch no lo lee |
| `EXTRAS/<SISTEMA>-duplicados`, `-malos`, `-otros`, `-variantes`, `-7z`… | Lo apartado de la Tanda 1 el 13-09-2026 |
| `EXTRAS/BIOS-candidatas/` | BIOS descartadas al elegir las buenas |
| `EXTRAS/ARCADE-incompletos/` | 47 juegos del set FB Alpha 2012 v0.2.97.24 a los que les faltan ROMs de la versión del core. Su README lista lo que falta a cada uno |
| `EXTRAS/ARCADE-sin-driver/` | 44 zips del set que no existen en FB Alpha 2012 |
| `EXTRAS/ARCADE-otros/` | `neocdz` (Neo Geo CDZ sin CD), el DAT v0.2.97.24 y los metadatos del set |
| `EXTRAS/C64-PRG-variantes/` | 4550 `.prg`: las otras versiones de los juegos de `ROMS/C64/PRG/` |
| `EXTRAS/C64-gdrive/` | El pack *Roms Commodore 64* de Google Drive entero (5752 zips y sus listas); lo que no estaba en Ghostware ya se extrajo a `ROMS/C64/` |
| `EXTRAS/C64-duplicados/` | 10 imágenes de Ghostware con el mismo contenido que otra y `PRG test`, copia de `PRG/` |
| `EXTRAS/C64-otros/` | Audio y espectrogramas de archive.org, *Last Ninja* en `.prg` sueltos y los `.tcrt` de THEC64 |
| `EXTRAS/DOS-malos/` | 6 zips rotos: cuatro de 0 bytes, `Liverpool.zip` cortado y `Metal Gear.zip` con CRC incorrecta |
| `EXTRAS/DOS-otros/` | *Microsoft Arcade* y *SimFarm*, que son de Windows 3.x, y los `.p2k.cfg` de Recalbox |

Cada movimiento está registrado con origen, destino y motivo, así que se puede deshacer: [`cleanup-2026-09-12.tsv`](../../cleanup-2026-09-12.tsv), [`cleanup-2026-09-13.tsv`](../../cleanup-2026-09-13.tsv) y, partidos por áreas, [`cleanup-2026-09-14-arcade.tsv`](../../cleanup-2026-09-14-arcade.tsv), [`-c64.tsv`](../../cleanup-2026-09-14-c64.tsv), [`-c64-prg.tsv`](../../cleanup-2026-09-14-c64-prg.tsv) y [`-dos.tsv`](../../cleanup-2026-09-14-dos.tsv).

No se suben al repo: son binarios ignorados por git.

# C64 — Commodore 64 (1982)

- **Estado:** Ordenadores — ROMs en el PC (14-09-2026), sin probar en la consola
- **Cores instalados en la PS4:** `vice_x64sc` (recomendado), `vice_x64`
- **Extensiones:** `.d64` `.t64` `.tap` `.prg` `.crt` `.g64` `.d81` `.m3u`
- **BIOS** (en `/data/retroarch/system/`, salvo que se indique otra cosa):
  - `vice/JiffyDOS_C64.bin` — opcional

**Notas:** VICE lleva integradas las ROMs del sistema. Se usa con teclado.

## Contenido

| Dónde | Qué | Lista de RetroArch |
|---|---|---|
| `C64/` | 8427 imágenes de disco y cinta con nombres No-Intro: 8229 de *C64 Rom Collection by Ghostware* (archive.org) y 198 que solo traía el pack *Roms Commodore 64* de Google Drive | *Commodore - 64*, 7522 entradas |
| `C64/*.m3u` | 509 listas de discos, una por juego de varios discos o caras (1414 imágenes). La lista de RetroArch apunta al `.m3u` y no a cada disco; los discos se cambian desde el menú rápido | (en la anterior) |
| `C64/PRG/<letra>/` | 11 023 programas `.prg` con nombres TOSEC, la mejor versión de cada juego: la limpia si existe; si no, la crackeada, la de trainer, etc. El volcado malo (`[b]`) solo entra cuando no hay otra | *Commodore - 64 (PRG)*, 11 023 entradas |

- **Nombres cambiados:** 20 pasados a ASCII (`720°` → `720`, `Mühle` → `Muhle`…). A 146 volcados del pack de Google Drive se les añadió « (Alt)», porque Ghostware trae otro volcado con el mismo nombre.
- **Nombres en las listas:** la base de datos de libretro (`Commodore - 64.rdb`) no reconoce estas imágenes, así que los juegos salen con el nombre del archivo, que ya es el oficial.
- **Sin probar:** que el VICE de 2020 del port lea `.m3u` y `.g64`. Los `.info` actuales los listan, pero son de un VICE más nuevo.

## Apartado en `emu/EXTRAS/`

Nada borrado. Los movimientos están en `cleanup-2026-09-14-c64.tsv` y `cleanup-2026-09-14-c64-prg.tsv`.

| Carpeta | Archivos | Qué |
|---|--:|---|
| `C64-PRG-variantes/` | 4550 | Las otras versiones (cracks, trainers, alternativas) de los juegos de `PRG/` |
| `C64-gdrive/` | 5755 | El pack de Google Drive entero, en zip; 5553 de sus volcados ya estaban en Ghostware |
| `C64-duplicados/` | 30 | 10 archivos de Ghostware con el mismo contenido que otro, y la carpeta `PRG test`, copia idéntica de `PRG/` |
| `C64-otros/` | 102 | Audio y espectrogramas que generó archive.org, *Last Ninja* en `.prg` sueltos (el juego está en disco en `C64/`) y los `.tcrt` de THEC64, que VICE no lee |

_Cores y extensiones según los `.info` de libretro-core-info, más nuevos que los cores del port R4 de 2020. Rendimiento sin probar en esta consola._

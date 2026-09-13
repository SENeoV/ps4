# RETROARCH — archivos de configuración

| En el PC | En la PS4 |
|---|---|
| `emu/RETROARCH/info/*.info` | `/data/retroarch/info/` |
| `emu/RETROARCH/playlists/*.lpl` | `/data/retroarch/playlists/` |
| `emu/RETROARCH/database/rdb/*.rdb` | `/data/retroarch/database/rdb/` |
| `emu/RETROARCH/thumbnails/<lista>/` | `/data/retroarch/thumbnails/<lista>/` |

## Por qué existe esta carpeta

**Síntoma:** RetroArch abre, hay cores instalados, las ROMs están en la consola con permisos correctos — pero *Load Content* muestra las carpetas **vacías**.

**Causa raíz:** el navegador de RetroArch filtra los archivos por extensión soportada:

```
menu_navigation_browser_filter_supported_extensions_enable = "true"
libretro_info_path = "/data/retroarch/info"
```

Las extensiones que soporta cada core **no salen del core**, salen de su archivo `.info`. El Core Installer (`SSNE20000`) despliega los cores en `/data/self/retroarch/cores/` pero **deja `/data/retroarch/info/` vacío**.

Resultado: RetroArch no conoce ni una sola extensión válida → filtra absolutamente todos los archivos → cada carpeta se ve vacía aunque esté llena.

Diagnóstico que lo confirmó:

| Comprobación | Resultado |
|---|---|
| ROMs en `/data/roms/NES/` | 635 archivos, permisos 0777, tamaños correctos |
| Cores en `/data/self/retroarch/cores/` | 74 cores presentes |
| Archivos en `/data/retroarch/info/` | **0 — vacío** |

## Contenido

74 archivos `.info`, uno por core instalado, de [libretro-core-info](https://github.com/libretro/libretro-core-info).

`mupen64plus_libretro.info` es una copia del `mupen64plus_next_libretro.info` de upstream: el core de PS4 se llama `mupen64plus_libretro_ps4.self` y RetroArch empareja core con `.info` **por nombre de archivo**. Ojo: el port trae `mupen64plus` y `mupen64plus_next` como dos cores distintos (el primero entró en R2, el segundo después), así que ese `.info` probablemente describe el core equivocado (el antiguo Mupen64Plus no lee `.ndd` ni `IPL.n64`). Se deja así porque N64 está aparcado; si se prueba, usar `mupen64plus_next`.

Los `.info` son los actuales de libretro-core-info y los cores del port son de 2020: donde el core sigue en desarrollo (mGBA 0.8.1 en la consola frente a 0.10-dev en el `.info`) pueden diferir en extensiones, BIOS o versión.

## Cómo aplicarlo

Subir por FTP el contenido de `info/` a `/data/retroarch/info/` y reiniciar RetroArch.

## Alternativas sin subir nada

- **Cargar el core primero:** *Load Core → Nestopia* y **después** *Load Content*. Con un core ya cargado RetroArch le pregunta las extensiones directamente, sin pasar por los `.info`.
- **Desactivar el filtro:** *Settings → File Browser → Filter Unknown Extensions* → OFF. Ojo: en la config está `menu_show_advanced_settings = "false"`, así que puede que haya que activar antes las opciones avanzadas para que aparezca.

Ambas sirven para salir del paso, pero sin los `.info` seguirán fallando el escaneo de contenido, las playlists y la asociación automática core↔sistema.

---

## Listas de juegos, bases de datos y carátulas

La consola no tenía ninguna lista y su base de datos (`database/rdb`) estaba vacía, así que *Escanear directorio* no podía reconocer ningún juego. Además, el *Online Updater* apunta a Bintray, que ya no existe. Estos archivos se preparan en el PC y se suben por FTP.

### Bases de datos (`database/rdb/`)

Descargadas de [libretro-database](https://github.com/libretro/libretro-database), rama `master` (commit `ff28a5e5bca2`, 2026-09-09):

| SHA-1 | Archivo |
|---|---|
| `bce56eba1eab172c5912e4db6920cd9ba9e2d263` | `Atari - 2600.rdb` |
| `e4860847575ca2d67f5293d754f17089265aff30` | `Atari - 7800.rdb` |
| `eb22afc9a8fba4bb64cd925923af9747696e29f7` | `Atari - Lynx.rdb` |
| `a2df574f342b8683a8e8afad708a623bfecd88f2` | `Bandai - WonderSwan Color.rdb` |
| `ee588e64e757e9ac30e6c1fe3afcbe316b339072` | `Bandai - WonderSwan.rdb` |
| `c1ffeba0447d930ac11c8d00d0a366833d845e9d` | `NEC - PC Engine - TurboGrafx 16.rdb` |
| `8d6df35369b31e1e1125d910dda55a6d19ae1398` | `Nintendo - Game Boy Advance.rdb` |
| `66a4b9a358e64359fe9664e713582623bda47638` | `Nintendo - Game Boy Color.rdb` |
| `455c0cb0877877103ab1debdcf0af2352394c425` | `Nintendo - Game Boy.rdb` |
| `ce8bad3ed41cc0011bf05a4e6175cf4b003ec910` | `Nintendo - Nintendo Entertainment System.rdb` |
| `57ba637b6c158e4200f057e0e41b0980ffbbbd6b` | `Nintendo - Super Nintendo Entertainment System.rdb` |
| `ede3ce69f9d0c5209ae7f1e6e8f9cfac4abf7328` | `Nintendo - Virtual Boy.rdb` |
| `728d262e0b1b8c0f13cdc58d3a4f9d8587d302be` | `Sega - 32X.rdb` |
| `2d5dead78cfb09b8dc1307d80bc7174a7fab1a98` | `Sega - Game Gear.rdb` |
| `a4d39817eef5c618fbb225a4ac6c64f05999de59` | `Sega - Master System - Mark III.rdb` |
| `29d931e44bc859e75e9fe8c05d3c42a8d0da8822` | `Sega - Mega Drive - Genesis.rdb` |
| `cfb7fbc10d19e479f7486f4a8f332c9d1d95cbfd` | `SNK - Neo Geo Pocket Color.rdb` |
| `7fdb69a7b39bb66dbe6e0816861ca8df3280c02d` | `SNK - Neo Geo Pocket.rdb` |

**Compatibilidad con RetroArch 1.8.8:** se compararon con las mismas bases de la etiqueta `v1.8.8`. La cabecera de formato es idéntica (`RARCHDB` + desplazamiento de metadatos) y ambas traen los campos `crc` y `name` que usa el escaneo. Las actuales solo tienen más juegos (Game Boy: 4399 frente a 1672).

### Listas (`playlists/*.lpl`)

Generadas con `python tools/retroarch_lists.py`, con la misma estructura JSON (versión 1.4) que el historial de la consola. Una por sistema con juegos:

| Carpeta | Lista | Core por defecto |
|---|---|---|
| `NES/` | `Nintendo - Nintendo Entertainment System` | nestopia |
| `SNES/` | `Nintendo - Super Nintendo Entertainment System` | snes9x2010 |
| `GB/` | `Nintendo - Game Boy` | gearboy |
| `GBC/` | `Nintendo - Game Boy Color` | gearboy |
| `GBA/` | `Nintendo - Game Boy Advance` | mgba |
| `SMS/` | `Sega - Master System - Mark III` | genesis_plus_gx |
| `GG/` | `Sega - Game Gear` | genesis_plus_gx |
| `MD/` | `Sega - Mega Drive - Genesis` | genesis_plus_gx |
| `ATARI2600/` | `Atari - 2600` | stella2014 |
| `ATARI7800/` | `Atari - 7800` | prosystem |
| `PCE/` | `NEC - PC Engine - TurboGrafx 16` | mednafen_pce_fast |
| `NGP/` | `SNK - Neo Geo Pocket` | mednafen_ngp |
| `NGPC/` | `SNK - Neo Geo Pocket Color` | mednafen_ngp |
| `WS/` | `Bandai - WonderSwan` | mednafen_wswan |
| `WSC/` | `Bandai - WonderSwan Color` | mednafen_wswan |
| `LYNX/` | `Atari - Lynx` | handy |
| `32X/` | `Sega - 32X` | picodrive |
| `VB/` | `Nintendo - Virtual Boy` | mednafen_vb |

Cómo se construyen:

- **Entran todos los juegos**, no solo los reconocidos: los que no están en la base de datos (traducciones, hacks, variantes, volcados alterados) aparecen con el nombre de su archivo.
- **Reconocimiento por CRC32**, igual que el escaneo de RetroArch. En los zip se usa la ROM interior, y también se prueba sin cabecera: iNES de 16 bytes (NES), copiador de 512 bytes (SNES, PC Engine), 64 bytes (Lynx) y 128 bytes (Atari 7800).
- Los juegos reconocidos muestran el **nombre oficial** de la base de datos, que puede no coincidir con el del archivo: por ejemplo, `Battle Bull (E) [!].gb` aparece como *Battle Bull (USA)* porque es el mismo volcado.
- Cada juego lleva su core, así que se abre directamente, sin preguntar cuál usar.

### Carátulas (`thumbnails/`)

- Portadas (`Named_Boxarts`) del servidor oficial `thumbnails.libretro.com`, buscadas por el nombre oficial de cada juego reconocido.
- Si el servidor no la tiene, se usa la carátula de `emu/MEDIA/` con el mismo nombre que la ROM.
- Reducidas a 512 px como máximo, para que ocupen menos al subirlas.
- Tu consola ya las muestra: en `retroarch.cfg` está `menu_thumbnails = "3"` (portadas).

### Resultado de la generación (2026-09-13)

Comprobado en disco: cada carátula coincide exactamente con el nombre del juego en su lista, no sobra ninguna y todas las rutas apuntan a una ROM que existe.

| Sistema | Juegos | Reconocidos en la base de datos | Con carátula | Tamaño carátulas |
|---|--:|--:|--:|--:|
| NES | 632 | 519 (82%) | 352 (56%) | 97,5 MB |
| SNES | 164 | 77 (47%) | 25 (15%) | 6,2 MB |
| Game Boy | 1542 | 1495 (97%) | 1281 (83%) | 330,8 MB |
| Game Boy Color | 495 | 490 (99%) | 463 (94%) | 87,9 MB |
| Game Boy Advance | 213 | 171 (80%) | 168 (79%) | 38,2 MB |
| Master System | 333 | 331 (99%) | 333 (100%) | 72,4 MB |
| Game Gear | 373 | 369 (99%) | 372 (100%) | 118,2 MB |
| Mega Drive | 1337 | 1284 (96%) | 1159 (87%) | 342,8 MB |
| Atari 2600 | 885 | 710 (80%) | 621 (70%) | 112,0 MB |
| PC Engine | 210 | 206 (98%) | 210 (100%) | 80,5 MB |
| Neo Geo Pocket | 3 | 2 (67%) | 3 (100%) | 0,4 MB |
| Neo Geo Pocket Color | 72 | 51 (71%) | 57 (79%) | 11,9 MB |
| WonderSwan | 214 | 107 (50%) | 107 (50%) | 37,2 MB |
| WonderSwan Color | 131 | 80 (61%) | 78 (60%) | 23,4 MB |
| Atari Lynx | 136 | 121 (89%) | 94 (69%) | 15,1 MB |
| 32X | 45 | 36 (80%) | 35 (78%) | 9,5 MB |
| Virtual Boy | 31 | 30 (97%) | 31 (100%) | 11,9 MB |
| Atari 7800 | 170 | 170 (100%) | 11 (6%) | 3,2 MB |
| **Total** | **6986** | **6249 (89%)** | **5400 (77%)** | **1399,2 MB** |

A subir en total: bases de datos 14,1 MB + listas 2,3 MB + carátulas 1399,2 MB ≈ **1,4 GB**.

Atari 7800 se quedó con las 170 ROMs que reconoce la base de datos, así que su lista sale al 100% con nombre oficial, pero el servidor de libretro apenas tiene portadas de este sistema: solo 11.

**Extensiones comprobadas contra los cores reales de la consola** (leídas de los propios `.self` por FTP): mgba, stella2014, gearboy y mednafen_wswan coinciden con su `.info`. Los `.info` actuales declaran alguna extensión de más que el core de 2020 no tiene (`cdf` en prosystem, `pcv2` en mednafen_wswan), pero ninguna se usa en las listas.

- Los juegos **sin carátula aparecen igual** en su lista, con su nombre.
- SNES tiene cifras bajas porque 87 de sus ROMs son traducciones, versiones parcheadas o volcados alterados que no están en la base de datos: no se pueden reconocer por CRC. En WonderSwan pasa lo mismo con las variantes `[o]`, `[b]` y `[f]` de la colección GoodWSx.
- En NES y Lynx, parte de los juegos reconocidos no tienen portada en el servidor de libretro. En Lynx, 89 de las 94 carátulas vienen de `emu/MEDIA/`.

### Subirlas a la consola

1. **Primero las ROMs** de cada sistema en `/data/ROMS/<SISTEMA>/`: las listas apuntan ahí, y si una ROM no está, su entrada no abre. Ojo con las de la Tanda 1, que todavía no están en la consola.
2. `database/rdb/*.rdb` → `/data/retroarch/database/rdb/`
3. `playlists/*.lpl` → `/data/retroarch/playlists/`
4. Las carpetas de `thumbnails/` completas → `/data/retroarch/thumbnails/`
5. Reiniciar RetroArch: aparecen las listas en el menú principal.

### Al añadir ROMs

Volver a ejecutar `python tools/retroarch_lists.py --thumbs`. Regenera las listas y descarga solo las carátulas que falten. Después, subir de nuevo la lista del sistema y su carpeta de carátulas.

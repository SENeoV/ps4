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

<details><summary>Los 74 cores de <code>/data/self/retroarch/cores/</code>, leídos por FTP el 2026-09-13 (1372,5 MB; cada uno se llama <code>&lt;core&gt;_libretro_ps4.self</code>)</summary>

| Core | Tamaño |
|---|--:|
| `2048` | 12.3 MB |
| `atari800` | 11.6 MB |
| `bluemsx` | 14.0 MB |
| `desmume` | 15.5 MB |
| `desmume2015` | 14.5 MB |
| `dosbox` | 12.8 MB |
| `dosbox_svn` | 13.5 MB |
| `fbalpha2012` | 37.4 MB |
| `fbalpha2012_cps1` | 13.1 MB |
| `fbalpha2012_cps2` | 12.8 MB |
| `fbalpha2012_cps3` | 12.5 MB |
| `fbalpha2012_neogeo` | 14.3 MB |
| `fceumm` | 13.0 MB |
| `flycast` | 30.7 MB |
| `fmsx` | 12.4 MB |
| `gearboy` | 12.5 MB |
| `genesis_plus_gx` | 21.2 MB |
| `handy` | 12.4 MB |
| `hatari` | 13.6 MB |
| `mame2000` | 30.3 MB |
| `mame2003` | 54.3 MB |
| `mame2003_plus` | 56.1 MB |
| `mame2010` | 71.9 MB |
| `mame2015` | 120.9 MB |
| `mednafen_gba` | 11.6 MB |
| `mednafen_lynx` | 12.4 MB |
| `mednafen_ngp` | 11.4 MB |
| `mednafen_pce_fast` | 11.4 MB |
| `mednafen_pcfx` | 12.8 MB |
| `mednafen_psx` | 18.3 MB |
| `mednafen_saturn` | 20.0 MB |
| `mednafen_snes` | 12.0 MB |
| `mednafen_supergrafx` | 12.7 MB |
| `mednafen_vb` | 11.3 MB |
| `mednafen_wswan` | 12.4 MB |
| `mesen` | 15.2 MB |
| `mesen-s` | 14.0 MB |
| `mgba` | 13.7 MB |
| `mrboom` | 19.8 MB |
| `mupen64plus` | 13.2 MB |
| `mupen64plus_next` | 14.7 MB |
| `nestopia` | 13.3 MB |
| `opera` | 12.4 MB |
| `parallel_n64` | 14.4 MB |
| `pcsx_rearmed` | 13.3 MB |
| `picodrive` | 13.3 MB |
| `ppsspp` | 18.6 MB |
| `prboom` | 12.1 MB |
| `prosystem` | 12.3 MB |
| `quicknes` | 11.4 MB |
| `sameboy` | 12.4 MB |
| `scummvm` | 60.1 MB |
| `snes9x` | 13.4 MB |
| `snes9x2002` | 13.0 MB |
| `snes9x2005` | 13.2 MB |
| `snes9x2010` | 14.1 MB |
| `squirreljme` | 12.3 MB |
| `stella2014` | 14.0 MB |
| `tyrquake` | 13.1 MB |
| `vba_next` | 13.1 MB |
| `vbam` | 12.4 MB |
| `vecx` | 12.3 MB |
| `vemulator` | 12.3 MB |
| `vice_x128` | 16.2 MB |
| `vice_x64` | 15.9 MB |
| `vice_x64sc` | 16.0 MB |
| `vice_xcbm2` | 14.7 MB |
| `vice_xpet` | 14.8 MB |
| `vice_xplus4` | 15.0 MB |
| `vice_xscpu64` | 16.7 MB |
| `vice_xvic` | 14.9 MB |
| `virtualjaguar` | 13.5 MB |
| `vitaquake2` | 14.0 MB |
| `yabause` | 13.3 MB |

</details>

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

Añadidas el 2026-09-14, de la rama `master` (commit `0eee396a0f5d`):

| SHA-1 | Archivo |
|---|---|
| `8abad092629556b8d99f367e488ab9db0e34af5f` | `Commodore - 64.rdb` |
| `b686a3544370bb437605e153c828a9d75466ed5d` | `DOS.rdb` |
| `07e9656b9d32fb07b77318000d2737c38381a521` | `ScummVM.rdb` |

`database/dat/` no se sube. Guarda los DAT de FB Alpha 2012 que genera `tools/fba2012.py` desde el código fuente de los cores, y un `fba2012.json` con las tablas de ROMs para verificar sin volver a clonar.

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
| `C64/` | `Commodore - 64` | vice_x64sc |
| `C64/PRG/` (con subcarpetas) | `Commodore - 64 (PRG)`, con la base de datos `Commodore - 64` | vice_x64sc |
| `DOS/` | `DOS` (los `.conf` de la raíz) | dosbox_svn |
| `SCUMMVM/` (con subcarpetas) | `ScummVM` (los `.scummvm`) | scummvm |

Las de arcade salen de `python tools/fba2012.py listas`, con el nombre de cada juego sacado del DAT de su core. Cada carpeta tiene su propia lista y su propio core:

| Carpeta | Lista | Core |
|---|---|---|
| `ARCADE/FBNEO/` | `FB Alpha 2012` | fbalpha2012 |
| `ARCADE/FBNEO/CPS1/` | `FB Alpha 2012 CPS-1` | fbalpha2012_cps1 |
| `ARCADE/FBNEO/CPS2/` | `FB Alpha 2012 CPS-2` | fbalpha2012_cps2 |
| `ARCADE/FBNEO/CPS3/` | `FB Alpha 2012 CPS-3` | fbalpha2012_cps3 |
| `NEOGEO/` | `FB Alpha 2012 Neo Geo` | fbalpha2012_neogeo |

Cómo se construyen:

- **Entran todos los juegos**, no solo los reconocidos: los que no están en la base de datos (traducciones, hacks, variantes, volcados alterados) aparecen con el nombre de su archivo.
- **Reconocimiento por CRC32**, igual que el escaneo de RetroArch. En los zip se usa la ROM interior, y también se prueba sin cabecera: iNES de 16 bytes (NES), copiador de 512 bytes (SNES, PC Engine), 64 bytes (Lynx) y 128 bytes (Atari 7800).
- Los juegos reconocidos muestran el **nombre oficial** de la base de datos, que puede no coincidir con el del archivo: por ejemplo, `Battle Bull (E) [!].gb` aparece como *Battle Bull (USA)* porque es el mismo volcado.
- Cada juego lleva su core, así que se abre directamente, sin preguntar cuál usar.

### Iconos y fuentes del menú (`assets/`)

`/data/retroarch/assets/` está vacío en la consola: el menú Ozone funciona, pero sin iconos, y el registro lista 150 `Asset missing`. Preparados el 2026-09-14 en `assets/` (101 MB, 4879 archivos) desde [retroarch-assets](https://github.com/libretro/retroarch-assets), **commit `8827a81` del 28-06-2020**, dos días antes del port R4 que tiene la consola, así que son exactamente los de esa versión.

Se copiaron `ozone/`, `xmb/`, `rgui/`, `glui/`, `nxrgui/`, `menu_widgets/`, `sounds/`, `pkg/` y `branding/`. Quedaron fuera `src/` (los SVG de origen, 113 MB) y `wallpapers/` (26 MB), que no hacen falta.

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

### Listas añadidas el 2026-09-14 (subidas y verificadas el 15-09, con sus carátulas)

| Lista | Juegos | Reconocidos en la base de datos | Con carátula | Tamaño carátulas |
|---|--:|--:|--:|--:|
| FB Alpha 2012 | 2032 | nombre del DAT del core | 1315 (65 %) | 363 MB |
| FB Alpha 2012 CPS-1 | 154 | nombre del DAT del core | 67 (44 %) | 18 MB |
| FB Alpha 2012 CPS-2 | 273 | nombre del DAT del core | 124 (45 %) | 34 MB |
| FB Alpha 2012 CPS-3 | 32 | nombre del DAT del core | 23 (72 %) | 8 MB |
| FB Alpha 2012 Neo Geo | 284 | nombre del DAT del core | 219 (77 %) | 62 MB |
| Commodore - 64 | 7522 | 2 (0 %) | 1029 (14 %) | 360 MB |
| Commodore - 64 (PRG) | 11 023 | 0 | 0 | |
| DOS | 956 | 0 | 951 (99 %) | 210 MB |
| ScummVM | 40 | 40 (100 %) | 23 (58 %) | 9 MB |
| **Total** | **22 316** | | **3751** | **1064 MB** |

- **C64:** `Commodore - 64.rdb` no trae los CRC de estas imágenes de disco y cinta, así que salen con el nombre de archivo, que ya es el de No-Intro en los discos y el de TOSEC en los `.prg`. Los juegos de varios discos aparecen una sola vez, con su `.m3u`; `retroarch_lists.py` no lista sueltos los discos que ya están en un `.m3u`. Las carátulas se piden al servidor por ese nombre aunque el juego no esté en la base de datos: así salen las 1029. A los `.prg` no se les piden, porque el servidor va con nombres No-Intro y los suyos son TOSEC.
- **Arcade:** las carátulas están en el servidor bajo *FBNeo - Arcade Games*, con el nombre completo del juego; `fba2012.py listas --thumbs` las pide con la descripción del DAT del core. Donde FBNeo cambió el nombre respecto a FB Alpha 2012, no hay carátula.
- **DOS:** los `.conf` no se reconocen por CRC, así que el nombre es el de la carpeta del juego. Las carátulas salen de las imágenes de ScreenScraper de `emu/MEDIA/DOS/images/` (836) y del servidor (115).
- **ScummVM:** la base de datos reconoce los `.scummvm` por su contenido (el id del juego).

### Subirlas a la consola

1. **Primero las ROMs** de cada sistema en `/data/ROMS/<SISTEMA>/`: las listas apuntan ahí, y si una ROM no está, su entrada no abre. Ojo con las de la Tanda 1, que todavía no están en la consola.
2. `database/rdb/*.rdb` → `/data/retroarch/database/rdb/`
3. `playlists/*.lpl` → `/data/retroarch/playlists/`
4. Las carpetas de `thumbnails/` completas → `/data/retroarch/thumbnails/`
5. Reiniciar RetroArch: aparecen las listas en el menú principal.

### Al añadir ROMs

Volver a ejecutar `python tools/retroarch_lists.py --thumbs` (o `python tools/fba2012.py listas --thumbs` en arcade). Regenera las listas y descarga solo las carátulas que falten. Después, subir de nuevo la lista del sistema y su carpeta de carátulas.

### Segunda pasada de carátulas (2026-09-16)

`python tools/caratulas.py` busca las que la primera pasada no encuentra por nombre exacto: baja el índice de cada carpeta del servidor y casa por título, quitando etiquetas (`[cr X]`, `(Alt)`, `(Disk 1)`, `[!]`…), traduciendo regiones de GoodTools (`(U)` → USA) y eligiendo la región más parecida cuando hay varias. En arcade pasa del nombre corto del zip al de FBNeo con `FBNeo - Arcade Games.rdb`, y un clon sin carátula hereda la de su padre. Encontró 4283 más:

| Lista | Con carátula | | Lista | Con carátula |
|---|--:|---|---|--:|
| NES | 567 / 632 | | FB Alpha 2012 | 1758 / 2032 |
| SNES | 133 / 164 | | FB Alpha 2012 CPS-1 | 152 / 154 |
| Game Boy | 1445 / 1542 | | FB Alpha 2012 CPS-2 | 270 / 273 |
| Game Boy Color | 473 / 495 | | FB Alpha 2012 CPS-3 | 32 / 32 |
| Game Boy Advance | 195 / 213 | | FB Alpha 2012 Neo Geo | 258 / 284 |
| Master System | 327 / 333 | | Commodore - 64 | 2072 / 7522 |
| Game Gear | 373 / 373 | | Commodore - 64 (PRG) | 1576 / 11 023 |
| Mega Drive | 1252 / 1337 | | DOS | 954 / 956 |
| Atari 2600 | 715 / 885 | | ScummVM | 30 / 40 |
| Atari 7800 | 122 / 170 | | PC Engine | 210 / 210 |
| Lynx | 126 / 136 | | Neo Geo Pocket / Color | 3 / 3 y 67 / 72 |
| WonderSwan / Color | 133 / 214 y 98 / 131 | | 32X, Virtual Boy | 38 / 45 y 31 / 31 |

En total 13 409 carátulas (3,8 GB): los 18 sistemas antiguos al 90 % y arcade al 89 %. Lo que falta son hacks, traducciones y variantes que el servidor no tiene; de C64 no hay más. Subirlas: `python tools/ps4ftp.py subir IP emu\RETROARCH\thumbnails /data/retroarch/thumbnails --hacer --remoto-existe` sube solo las que falten.

Para comprobar los volcados contra los DAT de No-Intro: `python tools/verificar_dumps.py`. Resultado del 2026-09-15 en [`docs/volcados-2026-09-15.md`](../../docs/volcados-2026-09-15.md): 5877 de 6986 (84 %) coinciden con No-Intro.

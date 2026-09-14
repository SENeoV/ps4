# BIOS — índice

Carpeta única de BIOS. En la PS4 va a **`/data/retroarch/system/`**, la carpeta *system* de RetroArch (ruta fija en este port, verificada en *Ajustes → Carpeta*). Cada archivo con el nombre exacto que pide su core; cuando el core espera una subcarpeta (`dc/`, `PPSSPP/`, `vice/`, `scummvm/`), se respeta.

**Los archivos no se suben al repo** (`.gitignore`); solo sus referencias en `catalogo/BIOS/`. Las BIOS con copyright las aporta el usuario desde su hardware.

Leyenda: **PC** = está en `emu/BIOS/` · **PS4** = subida y verificada por SHA-1 · **hash** = coincide con `System.dat` de libretro.

## Lo que hay

| Archivo | Sistema | Core | ¿Obligatoria? | PC | PS4 | Hash |
|---|---|---|---|:-:|:-:|:-:|
| `bios_MD.bin` | Mega Drive | genesis_plus_gx | no (arranque con logo TMSS) | ✅ | ✅ | ✅ |
| `bios_E.sms` | Master System (EU) | genesis_plus_gx | no | ✅ | ✅ | ✅ |
| `bios_J.sms` | Master System (JP) | genesis_plus_gx | no | ✅ | ✅ | ✅ |
| `bios_U.sms` | Master System (US) | genesis_plus_gx | no | ✅ | ✅ | ✅ |
| `bios.gg` | Game Gear | genesis_plus_gx | no | ✅ | ✅ | ✅ |
| `bios_CD_U.bin` | Sega CD (US) | genesis_plus_gx / picodrive | sí, para juegos US | ✅ | ✅ | ✅ |
| `bios_CD_E.bin` | Mega CD (EU) | genesis_plus_gx / picodrive | sí, para juegos EU | ✅ | ✅ | ✅ |
| `bios_CD_J.bin` | Mega CD (JP) | genesis_plus_gx / picodrive | sí, para juegos JP | ✅ | ✅ | ⚠️ |
| `lynxboot.img` | Atari Lynx | handy (opcional) / mednafen_lynx (obligatoria) | según core | ✅ | ✅ | ✅ |

- `bios_U.sms`: es una copia de `bios_E.sms` (hecha el 2026-09-13). La BIOS US y la EU son el mismo binario: libretro espera el SHA-1 `c315672807d8…` para las dos, y es el que tiene también `Master System/[BIOS] Sega Master System (USA) (v1.3) [b].sms`, cuya marca `[b]` es falsa. Subida a `/data/retroarch/system/` el 2026-09-13.
- ⚠️ `bios_CD_J.bin`: es `jp_mcd1_9112` (SHA-1 `e4193c6ae44c…`). libretro espera `4846f448160059…` (otra revisión del Mega CD japonés). Genesis Plus GX no comprueba el hash, así que debería arrancar; si un juego japonés falla, es lo primero que hay que cambiar.
- `32x/32X_G_BIOS.BIN`, `32X_M_BIOS.BIN`, `32X_S_BIOS.BIN`: BIOS reales de 32X que venían con la colección. **PicoDrive no las usa** (lleva las suyas), así que no se suben.
- Las subcarpetas `Game Gear/`, `Master System/`, `Sega CD/` y `Sega Genesis/` son los mismos archivos con su nombre original de No-Intro; son duplicados de los de la raíz.

### Software libre preparado el 2026-09-14 (no son BIOS, pero van en `system/`)

| Carpeta | Para | Qué es | Origen |
|---|---|---|---|
| `PPSSPP/` | ppsspp | Los 59 archivos de `assets` que el core exige (`ppge_atlas.zim`, fuentes, shaders, idiomas), 12 MB | [ppsspp](https://github.com/hrydgard/ppsspp), commit `9aab3d986` del 30-06-2020, el mismo día que el port R4 |
| `bluemsx/Databases/`, `bluemsx/Machines/` | bluemsx | 302 archivos con las máquinas MSX y su base de datos, 9 MB. Las ROMs de MSX siguen faltando (las pide fmsx o bluemsx) | [blueMSX-libretro](https://github.com/libretro/blueMSX-libretro), commit `1d441d9` de 2020 |
| `scummvm/extra/` | scummvm | `kyra.dat` (*Eye of the Beholder*), `lure.dat` (*Lure of the Temptress*) y `queen.tbl` (*Flight of the Amazon Queen*): sin ellos esos tres no arrancan | [scummvm](https://github.com/scummvm/scummvm), rama `branch-2-2` |
| `scummvm/theme/` | scummvm | `scummmodern.zip`, el tema del menú de ScummVM | ídem |

Los `.dat` de ScummVM tienen que ser de la misma versión que el core. El core del port es de 2020 y no está identificada su versión exacta, así que se cogió la rama 2.2; si ScummVM se queja de la versión del archivo, hay que probar con la de otra rama.

## Lo que falta, por tanda

| Archivo | Sistema | Core | ¿Obligatoria? | Tanda |
|---|---|---|---|---|
| `7800 BIOS (U).rom` | Atari 7800 | prosystem | no | 1 |
| `gba_bios.bin` | Game Boy Advance | mgba / vba_next / vbam | no | 0 |
| `neogeo.zip` | Neo Geo | fbalpha2012_neogeo | **sí, junto a las ROMs**, no en `system/` | 2 |
| `syscard3.pce` | PC Engine CD | mednafen_pce_fast / mednafen_supergrafx | sí | 3 |
| `disksys.rom` | Famicom Disk System | nestopia / fceumm / mesen | sí | 3 |
| `5200.rom` | Atari 5200 | atari800 | sí | 3 |
| `MSX.ROM`, `MSX2.ROM`, `MSX2EXT.ROM`, `MSX2P.ROM`, `MSX2PEXT.ROM` | MSX / MSX2 | fmsx | sí (las cinco) | 3 |
| ~~`bluemsx/Databases/`, `bluemsx/Machines/`~~ ya están | MSX | bluemsx | sí, si se usa bluemsx | 3 |
| `scph5501.bin` (US), `scph5502.bin` (EU), `scph5500.bin` (JP) | PS1 en RetroArch | pcsx_rearmed (opcional) / mednafen_psx (obligatoria) | según core; PS1 Classics no la necesita | 4 |
| ~~`PPSSPP/` (carpeta `assets` de PPSSPP)~~ ya está | PSP en RetroArch | ppsspp | sí; es software libre, no una BIOS | 5 |
| `vice/JiffyDOS_*.bin` | C64 | vice_* | no; VICE lleva las ROMs del sistema integradas | ordenadores |
| ~~`scummvm/theme/`, `scummvm/extra/`~~ ya están | ScummVM | scummvm | obligatorias para tres juegos; software libre | ordenadores |
| `dc/dc_boot.bin` | Dreamcast | flycast | no (tiene BIOS HLE), pero recomendada | después |
| `dc/naomi.zip` | NAOMI | flycast | **sí**, sin HLE | después |
| `dc/awbios.zip` | Atomiswave | flycast | **sí**, sin HLE | después |
| `saturn_bios.bin` | Saturn | yabause | no | después |
| `sega_101.bin` (JP), `mpr-17933.bin` (US/EU) | Saturn | mednafen_saturn | sí | después |
| `panafz10.bin` (u otra de la lista del `.info`) | 3DO | opera | sí, al menos una | después |
| `pcfx.rom` | PC-FX | mednafen_pcfx | sí | después |
| `firmware.bin`, `bios7.bin`, `bios9.bin` | Nintendo DS | desmume | no | aparcado |
| `Mupen64plus/IPL.n64` | N64 (solo 64DD) | mupen64plus_next | no | aparcado |

Los sistemas que no necesitan nada: NES, SNES, GB, GBC, GBA, VB, PCE (cartuchos), NGP/NGPC, WS/WSC, Atari 2600, 32X, N64, DOS y arcade (las BIOS de placa van dentro del romset). PS1, PS2 y PSP como *Classics* tampoco: el emulador de Sony va dentro del paquete.

## Comprobar antes de subir

Las BIOS son sensibles al nombre y a la revisión. Si un sistema no arranca con una ROM buena, casi siempre es la BIOS: nombre distinto o revisión que el core no espera. El log de RetroArch dice qué archivo busca.

Los hashes esperados están en [`System.dat` de libretro-database](https://github.com/libretro/libretro-database/blob/master/dat/System.dat) y en la tabla de cada core en [docs.libretro.com](https://docs.libretro.com/). Al añadir una BIOS a `emu/BIOS/`, el commit siguiente la registra en `catalogo/BIOS/` con su SHA-1, y ahí se contrasta.

Ojo con la antigüedad: los cores de esta PS4 son del port R4 de 2020, así que los nombres de BIOS que declara un `.info` actual pueden no ser los que pide el core real. Si el log de RetroArch busca otro nombre, manda el log.

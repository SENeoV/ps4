# Auditoría de la documentación — 2026-09-13

Revisión de toda la documentación del repo contrastada con internet y con los datos del propio repo (`.info` de los cores y hashes del catálogo). Sirve de registro de qué se corrigió y por qué; cada punto enlaza a la fuente.

Leyenda: 🔴 falso u obsoleto · 🟡 impreciso o sin base · ⚪ no verificable desde aquí · ✅ corregido

## Hallazgos

### Jailbreak y GoldHEN

- 🔴 ✅ No estaba documentado cómo se carga GoldHEN en 12.52. Es Poops + BD-JB: Blu-ray grabado con `Poops.iso`, USB exFAT/FAT32 con el payload, HDCP activado, internet una vez para activar el Blu-ray, pop-ups de vídeo sin desactivar. Hay que repetirlo tras cada reinicio. Si falla, reiniciar la consola, no reabrir la app BD-J. Fuentes: [henloader_lp](https://github.com/GoldHEN/henloader_lp), [BD-JB-1252](https://github.com/DefKorns/BD-JB-1252), [guía Poops 12.52](https://onejailbreak.com/blog/how-to-jailbreak-ps4-12-52-with-poops-exploit/).
- 🔴 ✅ "El jailbreak público llega a 11.00" (VITA, PS3, emuladores-ps4): Poops llega a 13.00. GoldHEN 2.4b18.9 (12-02-2026) añade 13.00 y arregla el kexec de Linux. Fuente: [BiteYourConsole](https://www.biteyourconsole.net/2026/02/12/scena-ps4-goldhen-si-aggiorna-alla-versione-2-4b18-9-con-supporto-per-il-firmware-13-00/).
- 🔴 ✅ "GoldHEN depende de esa versión exacta de firmware" (PLAN, emuladores-ps4): GoldHEN soporta muchas versiones. El riesgo real es actualizar por encima de 13.00, donde hoy no hay exploit.
- 🟡 ✅ GoldHEN 2.4b18.9 no está en los releases de GitHub (el último ahí es 2.4b18, 28-10-2024); se distribuye aparte. Fuente: [releases](https://github.com/GoldHEN/GoldHEN/releases).
- 🟡 ✅ "GoldHEN 2.4b18.9 es el actual" (INSTALL, APPS, CLAUDE): la consola lleva **2.4b18.10** (foto de *Información del sistema*, 13-09-2026 03:37). Corregido. La guía de DionKill avisa de que la 2.4b18.8 no arranca Linux.
- 🔴 ✅ INSTALL.md: el Package Installer lee por defecto solo del USB. Para `/data/pkg` hay que poner *Package Source* en `Hdd` o `All`. Fuente: [How-To-Install-PS4-FPKGS](https://github.com/DrYenyen/How-To-Install-PS4-FPKGS).
- ⚪ "RetroArch no aparece tras instalar → GoldHEN no estaba activo": plausible, sin fuente.

### Linux

- 🔴 ✅ "Nada confirmado para 12.5x; con GoldHEN 12.52 esta consola no tiene Linux" (emuladores-ps4, VITA, PS3): falso. [ps4-linux-loader](https://github.com/ps4-linux/ps4-linux-loader) soporta 12.50/12.52 (hasta 13.52) y detecta PS4 Pro. Bajo Linux hay informes de Dolphin ([GBAtemp](https://gbatemp.net/threads/dolphin-on-ps4-pro.495799/)) y RPCS3 ([GBAtemp](https://gbatemp.net/threads/linux-games-on-ps4-pro.576294/)) con algunos juegos. Vulkan da problemas en PS4 Pro con Mesa ≥ 22; OpenGL va bien ([PS4Linux](https://ps4linux.com/ps4-pro-fix-vulkan-fix-crash/)). Kernel 6.6 con AMDGPU desde 02-2025 ([PS4Linux](https://ps4linux.com/)).
- 🟡 ✅ "Dolphin necesita OpenGL 3.0+": el mínimo es OpenGL 3.3 / GLES 3.0 / D3D 11.1. Fuente: [Dolphin](https://en.wikipedia.org/wiki/Dolphin_(emulator)).
- 🟡 ✅ "Distribuciones recientes (Debian 13, Xubuntu 25.04, CachyOS, Manjaro) con kernel 6.6 y AMDGPU" (emuladores-ps4): vale para Aeolia y Belize, no para esta consola, que es **Baikal B1 (0x30201)** (foto de *Información del sistema* con GoldHEN, 13-09-2026 03:37). En Baikal el kernel es el 5.4.247 ([guía de DionKill](https://dionkill.github.io/ps4-linux-tutorial/files.html), corregida el 10-09-2026: ["7.1.7 does *not* support Baikal"](https://github.com/DionKill/ps4-linux-tutorial/commit/f4fb573); [rmux, 04-09-2026](https://gitlab.com/rmuxnet/linux/-/releases): "Baikal will be soon merged in"), la GPU solo funciona con Mesa ≤ 25.1 ([feeRnt, issue #8](https://github.com/feeRnt/ps4-linux-12xx/issues/8)) y no hay instalación en el disco interno. Corregido en `emu/emuladores-ps4.md`; detalle en `linux/README.md`.
- 🟡 ✅ Propuesta de ChatGPT (2026-09-13): "payload Linux específico para 12.50/12.52 y PS4 Pro", `archlinux-on-ps4` de 7coil y psxitarch. El loader v25 es un solo payload para 5.05–13.52 que detecta southbridge y Pro en tiempo de ejecución ([release v25](https://github.com/ps4-linux/ps4-linux-loader/releases/tag/v25)); el rootfs de 7coil es Arch de 2022-06 sin escritorio y con `mesa-ps4 21.3.2` (leído del tar). Sirve para una primera prueba, no como distro.
- 🔴 ✅ El `initramfs.cpio.gz` descargado (feeRnt v1.0, 29-01-2026) no vale: su [release](https://github.com/feeRnt/ps4-linux-initramfs/releases/tag/v1.0) dice "Missing support for: External installation". Sustituido por el "External HDD" de la guía de DionKill, cuyo `install-psxitarch.sh` (leído del cpio) exige pendrive MBR ≥ 22 GB y la distro como `psxitarch.tar.gz` (gzip), no `.tar.xz` como dice la guía.

### RetroArch (port de OsirisX)

- 🔴 ✅ El sello "verificado contra los `.info` de los cores instalados" no es exacto: los `.info` son del libretro actual (VICE 3.10, ScummVM 2.8.0git, mGBA 0.10-dev…), pero los binarios son del port R4 (30-06-2020, RetroArch 1.8.8). Extensiones y BIOS pueden no coincidir con los cores de 2020. Fuente: [hilo de OsirisX](https://www.psxhax.com/threads/ps4-retroarch-native-emulator-port-unofficial-pkg-via-osirisx.7243/).
- 🟡 ✅ *Core Updater* como alternativa al Core Installer (INSTALL, APPS): desde R3 los cores solo se instalan con el Cores Installer; el Online Updater apunta a Bintray, cerrado.
- 🟡 ✅ "72 cores" (APPS) frente a 74 (PLAN): en la consola hay 74.
- ⚪ El Core Installer del PC pesa 1385 MB = `Cores_Installer_r4.pkg` (1,35 GB). Existe `r4.1` (1,27 GB, "Fixed Speed"). Sin confirmar cuál está instalado; hay un hilo [Retroarch on PS4 too fast?](https://www.psx-place.com/threads/retroarch-on-playstation-4-too-fast.37068/).
- 🟡 ✅ `mupen64plus_libretro.info` es el de *Next* renombrado, pero desde R2 el port trae `mupen64plus` y `mupen64plus_next` por separado, así que ese `.info` probablemente describe el core equivocado. Fuente: [R2 en PSX-Place](https://www.psx-place.com/threads/updated-retroarch-unofficial-ps4-r2-now-includes-37-libretro-cores-yabause-mupen64-addded.27573/). Solo se documenta; el archivo no se toca.
- 🟡 ✅ `pcsx_rearmed` "más ligero": en x86-64 solo tiene dynarec desde 2020 (Lightrec); sin confirmar si el build R4 lo lleva. Fuente: [libretro](https://www.libretro.com/index.php/pcsx-rearmed-now-has-dynarec-support-across-multiple-platforms/).
- 🟡 ✅ PPSSPP standalone y Flycast standalone "si hay build": no existe ninguno para PS4. Fuente: [flycast #942](https://github.com/flyinghead/flycast/issues/942).
- 🔴 ✅ Faltaban sistemas con core instalado: Atari ST (hatari), Jaguar (virtualjaguar), Vectrex (vecx), ColecoVision/SG-1000 (bluemsx), VIC-20/Plus4/PET/C128 (vice), Doom (prboom), Quake (tyrquake, vitaquake2), Java ME (squirreljme), VMU (vemulator).

### BIOS

- 🟡 ✅ `bios_CD_J.bin` del PC es `jp_mcd1_9112` (SHA-1 `e4193c…`); libretro espera `4846f448…`. Genesis Plus GX no comprueba el hash, así que debería arrancar. Fuente: [System.dat](https://github.com/libretro/libretro-database/blob/master/dat/System.dat). EU, US, SMS, GG y MD sí coinciden.
- 🔴 ✅ `emu/BIOS/README.md` obsoleto: pedía BIOS para sistemas sin core, "BIOS + config" para PS2 Classics (no hace falta), citaba Beetle PSX HW (no instalado), PSP sin nada (el core necesita assets), 32X "según juego", Lynx sin BIOS (mednafen_lynx la exige), y "apuntar Directory → System" (la ruta es fija).
- 🔴 ✅ PSP: el core necesita **toda** la carpeta `assets` de PPSSPP en `system/PPSSPP/`, no solo `ppge_atlas.zim`. Fuente: [docs libretro](https://github.com/libretro/docs/blob/master/docs/library/ppsspp.md).
- ✅ Verificado correcto: `5200.rom` obligatoria ([atari800](https://github.com/libretro/docs/blob/master/docs/library/atari800.md)); NAOMI/Atomiswave sin BIOS HLE, `naomi.zip`/`awbios.zip` obligatorias en `system/dc/` ([flycast](https://github.com/libretro/docs/blob/master/docs/library/flycast.md)); `neogeo.zip` junto a las ROMs ([RetroBIOS](https://abdess.github.io/retrobios/emulators/fbalpha2012_neogeo/)); BIOS de GPGX ([docs](https://github.com/libretro/docs/blob/master/docs/library/genesis_plus_gx.md)).
- 🟡 ✅ `emu/BIOS/32x/` tiene 3 BIOS de 32X que nadie documentaba; PicoDrive no las usa.

### Classics (PS1, PS2, PSP)

- 🔴 ✅ "PS1-FPKG": la herramienta se llama **PSX-FPKG** (Jabu). Acepta ISO y bin/cue (varios `.bin`), desde firmware 5.05. Fuente: [PSX-Place](https://www.psx-place.com/threads/psx-fpkg-by-jabu-a-tool-to-convert-ps1-psx-games-for-use-on-ps4.30498/). El emulador es `ps1hd`, incluido en cada paquete ([PS1HD](https://github.com/andshrew/PlayStation-PS1HD)).
- ✅ PSP-FPKG (Jabu), emulador PSPHD de PS Plus, desde 5.05 ([PSXHAX](https://www.psxhax.com/threads/psp-fpkg-v1-0-app-to-convert-psp-isos-to-ps4-fpkgs-by-jabupl.13344/)).
- ✅ PS2: PS2-FPKG (Jabu) y PS2 Classic GUI; emuladores Jak v2 y Rogue; lista en [PSDevWiki](https://www.psdevwiki.com/ps4/PS2_Classics_Emulator_Compatibility_List). Fuente: [GameBrew](https://www.gamebrew.org/wiki/PS2-FPKG_PS4).
- ✅ PS Classics fPKG Builder archivado el 14-11-2025, correcto ([GitHub](https://github.com/SvenGDK/PS-Classics-fPKG-Builder)).

### Otros

- 🔴 ✅ El submódulo `ps4_cheats` es de shadPS4 (emulador de PC), no de GoldHEN. GoldHEN usa [GoldHEN_Cheat_Repository](https://github.com/GoldHEN/GoldHEN_Cheat_Repository), en `/user/data/GoldHEN/cheats/{json,shn,mc4}/`, con nombre `{titleid}_{version}.{ext}`.
- 🔴 ✅ `emu/init.md` era la respuesta original de ChatGPT y contradecía el resto (melonDS, Gambatte, Beetle PSX HW, N64 🟢…). Movido a `docs/historico/`.
- 🟡 ✅ 15 README por sistema en formato antiguo ("Prioridad Nivel 1", "BIOS: No" en SMS/GG/MD con BIOS opcional ya subida, MD solo `.md/.gen`).
- 🟡 ✅ ARCADE/FBNEO: romset `v0.2.97.29` para todo, pero CPS1 y CPS2 son `v0.2.97.28` según sus `.info`.
- 🟡 ✅ Columna "PS4 Pro" 🟢 en casi todo sin fuente; solo NES, GBA y SMS probados.
- 🟡 ✅ README raíz de dos líneas, sin índice.

## Verificado en la consola (capturas de Ajustes → Carpeta, 13-09-2026 02:06)

- *Información del sistema* (03:37): `HEN 12.52`, IP 192.168.1.201, **Southbridge Baikal B1 (0x30201)**, **GoldHEN v2.4b18.10**.

- Rutas: `system`, `info`, `playlists`, `database/rdb`, `thumbnails`, `savefiles`, `savestates`, `cheats`, `config`, `downloads`, `assets`, `shaders`, `overlays`, `remaps`, `layouts`, `temp` cuelgan de `/data/retroarch/`; cores en `/data/self/retroarch/cores`; explorador en `/data/ROMS`; capturas en la carpeta del contenido. Coincide con `INSTALL.md` y `emu/RETROARCH/README.md`.
- La barra de estado muestra `1.8.8 - mGBA (0.8.1 7ad318f5)`: el core instalado es **mGBA 0.8.1**, mientras `mgba_libretro.info` del repo declara `0.10-dev`. Prueba directa de que los `.info` son más nuevos que los cores.
- Otra sesión extrajo de los `.self` de `/data/self/retroarch/cores/` (por FTP) las versiones y extensiones que declara cada binario: `prosystem 1.3e`, `gearboy 3.4.1`, `mednafen_wswan 0.9.35.1` y `stella2014 3.9.3` coinciden con sus `.info`; las extensiones coinciden en los cinco comprobados (mGBA incluido; el `.info` de prosystem añade `cdf` y el de wswan `pcv2`, siempre de más, nunca de menos). De `handy` no se pudo leer. Conclusión: el desfase afecta a los cores en desarrollo activo (mGBA y previsiblemente VICE, ScummVM, PPSSPP, Flycast, atari800), y a las listas `.lpl` no les afecta.

## Documentación añadida

- Cómo se carga GoldHEN en 12.52 (`INSTALL.md`) y uso diario de RetroArch: menú, partidas, guardados rápidos, capturas, trucos y configuración, con las rutas verificadas en la consola.
- Sección "Solo con Linux" (GameCube, Wii, PS3, Vita) con lo que cuesta y por qué no está planificado.
- PS2 Classics (PS2-FPKG, PS2 Classic GUI, Jak v2/Rogue) y PS1 Classics (PSX-FPKG, `ps1hd`), con las listas de compatibilidad de PSDevWiki.
- Cores instalados sin carpeta (Atari ST, Jaguar, Vectrex, ColecoVision, VIC-20/Plus4/PET/C128, Doom, Quake, Java ME, VMU).
- Trucos: GoldHEN (`goldhen_cheats/`, `/user/data/GoldHEN/cheats/`) frente a RetroArch (`.cht`) y shadPS4 (`ps4_cheats/`, histórico).
- Índice de BIOS con hashes; `bios_U.sms` creada a partir de la europea (mismo SHA-1).
- README raíz con índice; `emu/init.md` a `docs/historico/`.
- `linux/README.md`: Linux en esta consola (Baikal B1): archivos verificados, restricciones, procedimiento por pendrive y problemas; `linux/ps4-linux-tutorial.md`, copia de la guía de DionKill. Loader, kernel e initramfs catalogados en `catalogo/LINUX/`; fuentes como submódulos en `linux/src/`.

## Incidencia resuelta: RetroArch se cerraba al arrancar (2026-09-13, 03:28–03:44)

Tras abrir un juego de PC Engine desde su lista, RetroArch dejó de llegar al menú. Diagnóstico por FTP (solo lectura) más dos escrituras confirmadas: (1) vaciar `libretro_path` no lo arregló, descartado; (2) activar `log_to_file` mostró que el arranque moría al elegir el driver de entrada; `retroarch.cfg` tenía `input_driver = "null"` con `input_joypad_driver = "ps4"`. Con `input_driver = "ps4"` arranca y el mando responde. No se sabe cómo llegó a `null` (Javi no tocó la lista de drivers). Registro en `INSTALL.md`, "Si algo falla".

## No verificable desde aquí

ConsoleMods, PSX-Place, PSXHAX, GBAtemp, PSDevWiki y GameBrew devuelven 403 al acceso automático, y archive.org no es accesible. Para esas fuentes se usaron los extractos de búsqueda. Pendiente de comprobar en la consola: lista real de `/data/self/retroarch/cores/`, versión del Core Installer (r4 o r4.1), y de qué versión de MAME tienen que ser los romsets de NAOMI/Atomiswave para el Flycast de 2020. La combinación del menú (Start + Select) sí está confirmada en `retroarch.cfg`.

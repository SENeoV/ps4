# Linux en la PS4 Pro — 12.52, Baikal B1

Proyecto aparte de RetroArch: arrancar Linux en esta consola para usar emuladores de PC (Dolphin para GameCube/Wii, RPCS3 para PS3) que no existen en el sistema de la PS4. **Estado: preparado en el PC, sin probar todavía en la consola** (checklist en [`../PLAN.md`](../PLAN.md), tareas en [`../PENDIENTES.md`](../PENDIENTES.md)).

Este documento cubre lo específico de **esta** consola y de **estos** archivos. La guía general de la escena, con todos los métodos y sus problemas, es la de DionKill: copia en [`ps4-linux-tutorial.md`](ps4-linux-tutorial.md), original en [dionkill.github.io/ps4-linux-tutorial](https://dionkill.github.io/ps4-linux-tutorial/). Los textos antiguos (psxitarch, `archlinux-on-ps4`, kernels 4.14/5.3, ps4linux.com) están superados; no seguirlos.

## Esta consola

Leído en *Ajustes → Sistema → Información del sistema* con GoldHEN cargado y en la etiqueta de la consola (fotos, 13-09-2026):

| Dato | Valor |
|---|---|
| Modelo | **PS4 Pro CUH-7116B** (etiqueta; serie 7100, 1 TB). Aparece en la [tabla de sony-jaguar-devs](https://github.com/sony-jaguar-devs/ps4-linux#console-models-and-southbridge) como *Pro - Baikal B1*, kernel compatible 5.4.247 |
| Firmware | 12.52 (`HEN 12.52`) |
| **Southbridge** | **Baikal B1 (0x30201)** |
| GoldHEN | v2.4b18.10 |
| IP | 192.168.1.201 (cambia; confirmarla antes de conectar) |
| Pantalla | **Tele LG por HDMI.** El monitor Samsung de 22" 1080p no recibe señal con los kernels 5.4 (sacan 1080p60 fijo sin leer el EDID); la tele sí. La PS4 en 1080p, HDR y Deep Colour desactivados |

Lo que implica ser **Baikal**, y además Pro, según la guía y los mantenedores del kernel (septiembre de 2026):

- Es el southbridge **con menos soporte** de los tres (Aeolia, Belize, Baikal), y "con problemas, especialmente en PS4 Pro". Menos usuarios, menos desarrolladores.
- **No hay instalación en el disco interno.** Solo en un disco externo por USB.
- **Kernel: 5.4.247.** Es el único con soporte de Baikal hoy; el kernel moderno 7.1.7 **no** lo soporta (la guía lo corrigió el 10-09-2026; rmux, su autor, dice que Baikal "se incorporará pronto"). Probado por otros en Pro Baikal B1 (CUH-7116B, CUH-7202B).
- **Mesa ≤ 25.1.** Con el kernel 5.4, una Mesa más nueva no encuentra la GPU (`libdrm` incompatible) y el escritorio va por software (`llvmpipe`): arranca, pero sin aceleración no hay emuladores. Las distros que la escena recomienda hoy (CachyOS Light, Arch de Erkkola) llevan Mesa 26 y sirven solo cuando llegue el kernel 7.x de Baikal.
- Ethernet puede no funcionar en Pro Baikal. El Wi-Fi (MediaTek MT7668) viene en el kernel 5.4.247.
- GoldHEN **2.4b18.8 no arranca Linux**; 2.4b18.9 y 2.4b18.10 sí.

## Qué hay en `linux/`

Todo verificado por SHA-1 contra su origen y catalogado en [`../catalogo/LINUX/`](../catalogo/LINUX/). Los binarios no entran en git.

| Archivo | Qué es | Origen | Uso |
|---|---|---|---|
| `loader/PS4-Linux-Loader-v25.zip` | Loader v25 (25-07-2026): payloads `.bin` y `.elf` de 32 MB a 4 GB de VRAM. Un solo payload para 5.05–13.52, detecta southbridge y Pro en tiempo de ejecución | [ps4-linux/ps4-linux-loader](https://github.com/ps4-linux/ps4-linux-loader/releases/tag/v25) | ✅ |
| `loader/linux-1024mb.bin`, `linux-2048mb.bin` (y `.elf`) | Extraídos del zip. **1 GB para instalar y el primer arranque, 2 GB después.** La VRAM se resta de los 8 GB de RAM | ídem | ✅ |
| `loader/ps4-linux-loader-25-src.zip` | Código fuente del loader v25 | ídem | referencia |
| `kernel/bzImage_Clang` | **Kernel 5.4.247 neocine-1.1 para Baikal** (10-03-2026): AMDGPU con registros Gladius arreglados (Pro), MT7668, ZRAM, `-O3` | [feeRnt/ps4-linux-12xx](https://github.com/feeRnt/ps4-linux-12xx/releases/tag/v5.4.247__neocine-1.1) | ✅ va al USB como `bzImage` |
| `kernel/bzImage_GCC-11` | Misma versión compilada con GCC 11 | ídem | alternativa si el Clang da problemas |
| `kernel/config_Clang`, `config_GCC-11` | Configuración de compilación de cada uno | ídem | referencia |
| `initramfs/initramfs.cpio.gz` | initramfs **"External HDD"** de la guía de DionKill: rescue shell con `install-psxitarch.sh` (instala en USB) y `start-psxitarch.sh` (arranca lo instalado) | [DionKill/ps4-linux-tutorial](https://github.com/DionKill/ps4-linux-tutorial/blob/main/PS4%20Linux/initramfs.zip), carpeta `External HDD` | ✅ va al USB tal cual |
| `initramfs/initramfs-dionkill.zip` | El zip completo, con las variantes internas (Aeolia, Belize) que aquí no sirven | ídem | referencia |
| `initramfs/feernt-1.0/initramfs.cpio.gz` | initramfs v1.0 de feeRnt (29-01-2026). Su release avisa: **sin soporte de instalación externa** | [feeRnt/ps4-linux-initramfs](https://github.com/feeRnt/ps4-linux-initramfs/releases/tag/v1.0) | ❌ no vale en Baikal |
| `initramfs/feernt-1.0/ps4-linux-initramfs-1.0-src.zip` | Su código fuente | ídem | referencia |
| `distros/ps4linux-arch-mesa25.1-2026-03-09.tar.xz` | **La distro elegida.** Arch Linux (5–9 de marzo de 2026) con KDE Plasma 6.6, SDDM, Firefox, NetworkManager, Bluetooth y PipeWire; **Mesa 25.1.0-devel** (`libgallium-25.1.0-devel.so`; el paquete se llama `mesa-git 22.1-1`, "repacked from known-good PS4 rootfs") y `libdrm-git 2.4.124` "compiled for PS4 Baikal". Usuario `ps4`/`ps4`, `fstab` ya con `LABEL=psxitarch`. 2,03 GB, 6,3 GB instalada | [Mega](https://mega.nz/file/JNkUgZLY#q-XwRcz81SLyMBE_-RIpbtRZIi2pGaH-8xCc6-uFXRI), enlazada por feeRnt en el [issue #8](https://github.com/feeRnt/ps4-linux-12xx/issues/8); descargada el 13-09-2026 como `ps4linux.tar.xz`, `xz -t` correcto | ✅ va al USB recomprimida como `psxitarch.tar.gz` |
| `distros/psxitarch-7coil-2022-06-26.tar.xz` | Rootfs de 7coil: Arch 2022.06.01 **sin escritorio**, `mesa-ps4 21.3.2`, usuario `pi`/`raspberry`, root `raspberry` | [7coil/archlinux-on-ps4](https://github.com/7coil/archlinux-on-ps4/releases/tag/2022-06-26) | ⚠️ vale para probar que la cadena arranca (Mesa vieja, compatible con el 5.4). De 2022: no actualizarla ni usarla como distro final |
| `distros/archlinux-on-ps4-2022-06-26.zip` | Documentación de 7coil (sin binarios) | ídem | referencia |
| `pkgs/` | **Paquetes para instalar sin red**: `dolphin-emu 1:2509-1`, `ppsspp 1.19.3-3` con sus 6 dependencias (`ppsspp-assets`, `qt5-base`, `qt5-multimedia`, `qt5-translations`, `openal`, `sdl2_ttf`), `iw` y `wireless-regdb`. Bajados del [Arch Linux Archive](https://archive.archlinux.org/packages/) con las versiones exactas de las bases de datos de sync que trae la distro (`extra.db` del 09-03-2026), verificados por SHA-256 contra ellas, así que casan con las librerías instaladas sin `pacman -Syu`. El de Dolphin va renombrado (`1_2509`) porque FAT32 no admite `:`. `instalar.sh` los instala con `pacman -U`: ver "Dolphin" | Arch Linux Archive | ✅ van a `pkgs/` de la FAT32 del pendrive |
| `src/` | Submódulos con el código de [ps4-linux-loader](https://github.com/ps4-linux/ps4-linux-loader), [ps4-linux-initramfs](https://github.com/feeRnt/ps4-linux-initramfs), [archlinux-on-ps4](https://github.com/7coil/archlinux-on-ps4) y [ps4-linux-12xx](https://github.com/feeRnt/ps4-linux-12xx) (fuentes del kernel, 6,4 GB de historial). Se traen con `git submodule update --init linux/src/<repo>`. El kernel queda en su rama por defecto (6.15.4): la rama de Baikal, `5.4.247-baikal-dfaus`, **no se puede extraer en Windows** (archivos `aux.c` y nombres que solo difieren en mayúsculas); hace falta Linux o WSL | — | referencia; no se cataloga |

### La distro

Hace falta una distro para PS4 **con Mesa ≤ 25.1**. Solo hay dos, ambas en descargas directas que no se pueden automatizar; la primera es la que está en `distros/`:

| Distro | Mesa | Descarga | Acceso | Pega |
|---|---|---|---|---|
| **Arch limpio con Mesa 25.1** (08-03-2026) | 25.1 | [Mega](https://mega.nz/file/JNkUgZLY#q-XwRcz81SLyMBE_-RIpbtRZIi2pGaH-8xCc6-uFXRI), 2,03 GB | `ps4` / `ps4` | Autor anónimo; la enlaza y la da por buena el mantenedor del kernel Baikal ([issue #8](https://github.com/feeRnt/ps4-linux-12xx/issues/8)). Se llama `ps4linux.tar.xz`: hay que renombrarla |
| Xubuntu 25.04 (25-05-2025) | 25.0.5 | [1fichier](https://1fichier.com/?at7ccs9f5rb9spzkm8h9) o [Mediafire](https://www.mediafire.com/folder/lmcwkxf915jqm/ps4-xubuntu), en varias partes | `ps4linux` / `ps4linux` | Trae Steam, Wine y emuladores, pero su autor (triki1) está señalado en la guía de DionKill como no fiable, y no publica fuentes |

Cuando rmux publique el kernel 7.x para Baikal, la distro a usar pasa a ser [CachyOS Light](https://ps4linux.com/forums/d/422-cachyos-light-lxqt-a-light-and-fast-distro) (Mesa 26, se actualiza con `pacman`) y este documento cambia.

## Cómo arranca

1. GoldHEN cargado en la PS4 (Poops desde el Blu-ray; [`../INSTALL.md`](../INSTALL.md)).
2. Se envía a la consola el **payload del loader** (`linux-1024mb.bin`). El loader busca `bzImage` e `initramfs.cpio.gz` **en el USB** y, si no hay, en `/data/linux/boot/` del disco interno (o `/user/system/boot/`); reserva la VRAM y hace `kexec` del kernel.
3. El initramfs abre una **rescue shell** en pantalla (teclado USB). `install-psxitarch.sh` particiona el USB, extrae la distro y la arranca; en arranques siguientes `start-psxitarch.sh` monta la partición `psxitarch` y arranca. Si no arranca solo, `resume-boot` (nunca más de dos veces; a la tercera, Ctrl+Alt+Supr).
4. Al reiniciar la consola vuelve el sistema de la PS4 intacto. Linux no toca el disco interno; para volver a Linux hay que repetir 1 y 2.

## Procedimiento (pendrive, método por script)

### 1. Preparar el pendrive en el PC

- Pendrive USB 3.0 de **32 GB o más** (el instalador exige **22 GB** como mínimo y **tabla de particiones MBR**, no GPT). **Se borra entero.**
- Formatear en **FAT32**. Windows no ofrece FAT32 por encima de 32 GB: usar [Rufus](https://rufus.ie) con *Non bootable*, *MBR*, *FAT32*. Ojo con la tabla de particiones: el Kingston de 32 GB venía **GPT** y el instalador aborta si no es MBR; se convirtió desde PowerShell como administrador (`Clear-Disk`, `Set-Disk -PartitionStyle MBR`, `New-Partition -MbrType FAT32`, `Format-Volume -FileSystem FAT32`), sin Rufus porque son 28,8 GiB.
- Copiar en la raíz, con estos nombres exactos:

| En el pendrive | Copia de |
|---|---|
| `bzImage` | `linux/kernel/bzImage_Clang` |
| `initramfs.cpio.gz` | `linux/initramfs/initramfs.cpio.gz` |
| `psxitarch.tar.gz` | la distro, **recomprimida en gzip** (abajo) |

- El instalador solo acepta **`psxitarch.tar.gz`** (gzip): busca ese nombre y extrae con `tar -xvpzf`. Un `.tar.xz` no sirve aunque se renombre. Recomprimir en el PC sin descomprimir en disco, por ejemplo la de 7coil:

  ```
  python -c "import lzma,gzip,shutil,sys; shutil.copyfileobj(lzma.open(sys.argv[1]), gzip.open(sys.argv[2], 'wb', 6))" linux/distros/ps4linux-arch-mesa25.1-2026-03-09.tar.xz E:\psxitarch.tar.gz
  ```

  (`E:` es el pendrive; salen unos 2,5 GB y tarda unos minutos. Para la prueba con la de 7coil, el mismo comando con su archivo. Si una distro ya es `.tar.gz`, solo renombrar.)

- **Preparado el 2026-09-13** (Kingston DataTraveler 3.0, 30,9 GB, etiqueta `PS4LINUX`): `bzImage` y `initramfs.cpio.gz` con el mismo SHA-1 que el catálogo, y `psxitarch.tar.gz` de 2.729.779.909 bytes recomprimido desde el Arch Mesa 25.1 (`gzip -t` correcto, 6.630.072.320 bytes descomprimidos, los mismos que el `.xz`).
- **`bootargs.txt` sí hace falta**, por el initramfs: sin `root=LABEL=psxitarch` cae siempre en la rescue shell pidiendo `resume-boot`. Línea completa: `panic=0 clocksource=tsc consoleblank=0 net.ifnames=0 radeon.dpm=0 amdgpu.dpm=0 drm.debug=0 console=tty0 video=HDMI-A-1:1920x1080@60 drm.edid_firmware=edid/1920x1080.bin root=LABEL=psxitarch`.
- Sin `vram.txt`: el kernel 5.4.247 ya pone 1920x1080 a 60 Hz y la VRAM la fija el payload elegido. Solo si hace falta, `bootargs.txt` junto al `bzImage` (ver "Problemas").

### 2. Preparar la consola

- Cargar GoldHEN. Comprobar que el Blu-ray de Poops **ha salido** de la bandeja (suele expulsarse solo): un disco dentro corrompe la instalación.
- En el menú de GoldHEN, con **FTP** y **BinLoader** (puerto 9090) activados. Sin ninguna aplicación suspendida ni RetroArch abierto.
- *Ajustes → Sonido y pantalla → Ajustes de salida de vídeo*: resolución **1080p** (no *Automático*); *Gama de colores RGB* en *Limitado* si la imagen sale oscura; **desactivar** *Salida Deep Colour* (color de más de 8 bits) o no hay señal. HDCP se queda activado.
- Conectados: pendrive, **teclado y ratón USB**. Sin hub para el pendrive. Si hay un monitor y una tele, la tele suele dar menos pantallas negras.

### 3. Enviar el payload

**Desde la consola, sin PC** (lo normal desde el 13-09-2026): abrir **Payload Guest** (`pkg/utils/PS4_AZIF00003_v0.98_Payload_Guest.pkg`, instalado desde `/data/pkg/`) y elegir *Linux 2 GB VRAM (uso normal)*; el primer arranque tras instalar, *1 GB*. Lee `/data/payloads/` (los nueve `linux-*.bin` del loader v25, de 32 MB a 4 GB, más las herramientas del host webkitty; copia y tabla en [`pkg/payloads/`](../pkg/payloads/README.md)) y se los pasa al BinLoader de GoldHEN.

Desde el PC, con la PS4 en el menú principal:

```
python -c "import socket,sys; s=socket.create_connection(('192.168.1.201', 9090)); s.sendall(open(sys.argv[1], 'rb').read()); s.close()" linux/loader/linux-1024mb.bin
```

La pantalla se queda negra unos segundos y aparece la rescue shell. Si no responde, apagar y encender la tele o el monitor; si sigue negra, reiniciar la consola y repetir (puede costar dos o tres intentos; LED blanco fijo = fallo, reiniciar).

Alternativas: en el navegador de la PS4, `http://webkitty.arabpixel.net` → pestaña *Linux* → esperar a que se cachee → payload 1 GB (o `http://uar.no/ps4/linux` si el primero no está); o subir `linux-1024mb.elf` por FTP a `/data/payloads/` y lanzarlo con la aplicación *Payload Guest*.

### 4. Instalar (una vez)

En la rescue shell:

```
eject /dev/sr0          # solo si quedó un disco dentro
install-psxitarch.sh
```

Busca el pendrive, copia los tres archivos a RAM, lo reparticiona (80 MB FAT32 con `bzImage` e `initramfs.cpio.gz` + el resto en ext4 con etiqueta `psxitarch`), extrae la distro y arranca. Tarda. Errores típicos en "Problemas".

### 5. Arranques siguientes

GoldHEN → payload **`linux-2048mb.bin`** → arranca la distro sola desde el pendrive. Si se queda en la rescue shell: `resume-boot` o `start-psxitarch.sh`.

### 6. Después de instalar

- **No actualizar Mesa ni libdrm**: la actualización trae Mesa 26 y se pierde la GPU con el 5.4. En Arch, `IgnorePkg = mesa libdrm lib32-mesa lib32-libdrm llvm-libs lib32-llvm-libs` en `/etc/pacman.conf` (sección "Legacy" de la guía). En Debian/Ubuntu, `apt-mark hold`.
- Comprobar la aceleración: `glxinfo | grep renderer` tiene que decir `AMD Liverpool (PlayStation 4)`, no `llvmpipe`.
- Teclado en español, idioma, usuario y contraseña, swap y ZRAM: sección "Post install setup" de la guía.
- Rendimiento de CPU: `mitigations=off` en `bootargs.txt` (desactiva las mitigaciones de Spectre/Meltdown; la consola ya está abierta).
- El mando DualShock 4 hay que emparejarlo por Bluetooth en cada arranque de Linux.

## Dolphin (GameCube y Wii): el objetivo

**Configuración actual, cambios recomendados, mando y Bluetooth: [`dolphin.md`](dolphin.md).**

La meta del proyecto es jugar a GameCube (*Wind Waker*) con Dolphin. Lo que hace falta y lo que cabe esperar:

- **GPU activa antes que nada.** `glxinfo | grep renderer` → `AMD Liverpool`. Con `llvmpipe` Dolphin va a pocos fps y no hay nada que ajustar: es la distro (Mesa) o el kernel. Dolphin necesita OpenGL 3.3; Mesa 25.1 da OpenGL 4.6 en esta GPU.
- **Instalar sin red, desde el pendrive** (la Pro Baikal no tiene Ethernet en Linux y el Wi-Fi MediaTek de este kernel escanea mal): los paquetes de `linux/pkgs/` van en `pkgs/` de la partición FAT32 del pendrive. En LXTerminal (clave `ps4`): `sudo mkdir -p /mnt`, `sudo mount /dev/sda1 /mnt`, `sudo sh /mnt/pkgs/instalar.sh`, `sudo umount /mnt`. Dolphin y PPSSPP quedan en el menú *Juegos*.
- **Con red**, la vía normal sería `sudo pacman -Syu dolphin-emu`. El `pacman.conf` de esta distro ya trae `IgnorePkg` con `mesa-git`, `libdrm-git` y `llvm`, `IgnoreGroup = mesa` y `DisableSandbox` (el 5.4 no tiene Landlock), así que la actualización no rompe la GPU. Pero es un Arch de marzo: `-Syu` baja y escribe medio sistema, y en un pendrive a USB 2.0 es más de una hora.
- **Backend OpenGL**, no Vulkan: Vulkan se cuelga en PS4 Pro con Mesa ≥ 22. Resolución interna 1x (nativa) para empezar; la GPU sobra y se puede subir a 2x, el límite es la CPU (8 Jaguar a 2,1 GHz). `mitigations=off` en `bootargs.txt` ayuda.
- **Expectativa.** No hay informe de *Wind Waker* en PS4; la referencia es *Pikmin* a 50 fps en PS4 Pro con OpenGL (GBAtemp) y, en la guía, Cemu (Wii U, mucho más pesado) a 50-55 fps. *Wind Waker* es un juego ligero para Dolphin: lo previsible es velocidad completa con alguna bajada.
- **Los juegos (🧑).** Dolphin lee `.iso`, `.gcm` y `.rvz` (RVZ es el formato comprimido de Dolphin, sin pérdida; *Wind Waker* ocupa 1,4 GB en ISO). La partición de Linux del pendrive es ext4 y Windows no la escribe, así que las ISO van en **otro USB en exFAT** (Linux lo lee) o se copian por red (Wi-Fi) una vez arrancado. Hace falta un hub USB para teclado y ratón: pendrive, USB de juegos y mando ocupan los tres puertos.
- **Ya configurado por SSH (13-09):** `GFXBackend = OGL`, carpeta de juegos `/home/ps4/Juegos` con `Zelda-Wind-Waker-Europe.rvz`.
- **Mando.** DualShock 4 **por cable USB: mapeado y funcionando** (13-09; `SDL/0/PS4 Controller`). **Por Bluetooth aún no**: hay que emparejarlo desde Linux en cada arranque (procedimiento en `dolphin.md`). Para Wii, *Emulated Wii Remote* con el mismo mando.
- **Wii** funciona igual (mismo Dolphin), con el puntero del Wiimote mapeado al stick derecho. Menos cómodo, pero para juegos sin puntero va bien.

## Otros emuladores en este Linux

Mismo hardware para todos: 8 Jaguar a 2,1 GHz y una GPU con OpenGL 4.6 (Mesa 25.1). Vulkan da problemas en Pro: **backend OpenGL** siempre que se pueda elegir. Todo por `pacman` o AUR (`yay`), **nunca por Flatpak**: el Flatpak trae su propia Mesa 26 y con el kernel 5.4 va por software. Y antes de instalar nada, `IgnorePkg` para Mesa (sección Dolphin).

| Emulador | Sistema | Expectativa en esta Pro | Instalación |
|---|---|---|---|
| Dolphin | GameCube, Wii | Buena (*Pikmin* a 50 fps reportado) | `pacman -S dolphin-emu` |
| PPSSPP | PSP | Muy buena | `pacman -S ppsspp` |
| PCSX2 | PS2 | Correcta en muchos juegos; la PS4 ya tiene PS2 Classics nativo, así que solo para lo que ahí no funcione | `pacman -S pcsx2` |
| RetroArch | retro | Como en la PS4, pero con los cores que al port de 2020 le faltan (Pokémon Mini, Amiga, Spectrum, Neo Geo CD, X68000) y N64 con OpenGL | `pacman -S retroarch` + cores |
| Cemu | Wii U | Según la guía, *Super Mario 3D World* a 50-55 fps con ajustes | AUR `cemu-bin` |
| RPCS3 | PS3 | Justa: *Demon's Souls* y *Folklore* jugables; lo que exprime las SPU se arrastra. Necesita el firmware de PS3 (🧑) | AUR `rpcs3-bin` |
| Azahar | 3DS | Sin informes en PS4; la guía pone 3DS en "Low" | AUR |
| Yuzu / Ryujinx | Switch | No: 8-20 fps según la guía | — |
| xemu | Xbox | Solo en teoría, sin informes | AUR |

Fuera de emuladores: Steam con Proton, Lutris y Heroic; la guía trae una tabla de compatibilidad de juegos de PC.

## Rutina de cada día

1. GoldHEN (Poops), con el pendrive en un puerto **frontal**, teclado y mando por cable conectados, la **tele** como pantalla.
2. Payload Guest → `ps4-fan-threshold60.bin` (ventilador) → `linux-2048mb.bin`.
3. Entra solo en LXDE (autologin). Dolphin en el menú *Juegos*; *Wind Waker* en la lista.
4. **Apagar desde el menú de LXDE**, nunca con el botón: la partición no tiene journal.

Desde el PC, con la PS4 en Linux: `python tools/ps4linux.py ip` y luego `MSYS_NO_PATHCONV=1 python tools/ps4linux.py <ip> "comando"`.

## Errores de este proyecto y qué aprender de ellos

| Qué pasó | Qué hacer la próxima vez |
|---|---|
| Seis lanzamientos sin señal (05:35–06:11) antes de probar otra pantalla; se probaron EDID forzado y otro kernel | Con kernels 5.4 de Baikal, **tele primero**: sacan 1080p60 fijo sin EDID y hay monitores que no lo aceptan. Está en el foro desde 2025 |
| Sondeé el puerto 9090 con una conexión vacía y GoldHEN apagó el BinLoader; hubo que reactivarlo dos veces | No sondear 9090: enviar el payload y ya. El FTP (2121) sí se puede sondear |
| Los apagones "de la nada" eran la protección térmica: 71 °C con el ventilador parado en Baikal | `ps4-fan-threshold60.bin` antes de Linux; `sensors` para vigilar |
| El initramfs descargado no valía (solo interno) y el "psxitarch" era un rootfs de 2022 | Leer la release y verificar por SHA-1 cada archivo antes de usarlo; los nombres engañan |
| El instalador borró el `bootargs.txt` y hubo que hacer `resume-boot` en cada arranque | `root=LABEL=psxitarch` en `bootargs.txt`, recreado tras instalar |
| Pantalla negra al cambiar el pendrive al puerto trasero | Solo `/mnt/usb0` y `/mnt/usb1`: puertos frontales |
| Plasma se quedaba en el splash desde el pendrive a USB 2.0 | LXDE (autologin); Plasma cuando haya SSD |
| `meta.json` para Payload Guest sin `icon`: "No se pudo leer" | Sin `meta.json`, o con `icon` en cada entrada |
| Dos copias por SFTP fallaron con *No such file*: Git Bash convertía `/home/ps4/...` en `C:/Program Files/Git/home/ps4/...` | `MSYS_NO_PATHCONV=1` con cualquier argumento que empiece por `/` |
| Un SHA-1 calculado mientras Chrome aún cerraba la descarga salió mal | Hashear cuando tamaño y `mtime` llevan un rato sin cambiar |
| `inventory.py` cataloga lo que encuentra: un clon de git a medias (hasheó un pack de 5 GB) y 759 texturas sueltas | Mirar el disco antes de commitear; `SKIP_DIRS` para árboles que no son binarios de referencia |
| Estimé la instalación en 15-45 min y fueron 1 h 40 | Medir la posición en el tar antes de estimar; el pendrive escribe 30 archivos/s en librerías y 130/s en archivos pequeños |
| `dolphin-emu-1:2509-1…` con `:` en el nombre desapareció en FAT32/NTFS | Renombrar los paquetes con epoch antes de copiarlos |

## Registro de pruebas

### 2026-09-13, madrugada — seis intentos, ninguno con imagen

Pendrive Kingston DataTraveler 3.0 (MBR, FAT32) con `initramfs.cpio.gz` de DionKill y `psxitarch.tar.gz` (Arch Mesa 25.1). Payload `linux-1024mb.bin` enviado desde el PC al BinLoader (9090) con GoldHEN 2.4b18.10, disco de Poops fuera, teclado y ratón conectados.

| Hora | Kernel | `bootargs.txt` | Resultado |
|---|---|---|---|
| 05:35 | 5.4.247 neocine-1.1 (Clang) | no | La PS4 deja de responder en red (el kexec se hace). Pantalla negra, LED azul/blanco parpadeando; apagar y encender el monitor y Ctrl+Alt+F2/F1 no cambian nada |
| 05:45, 05:50, 05:59 | ídem | no | Igual. En el cuarto, LED apagado, consola encendida, monitor "sin señal"; al rato la consola se cae |
| 06:07 | ídem | sí: línea por defecto + `drm.edid_firmware=edid/1920x1080.bin` | Sin señal |
| 06:11 | 5.4.247 baikal_mt76 (09-2025, "possible fix for the No signal issue") | sí | Sin señal; la consola se apaga entera al poco |

Lecciones:

- El BinLoader de GoldHEN se cierra si recibe una conexión vacía (un `connect` de prueba); no sondear el puerto 9090, enviar directamente. El FTP (2121) sí se puede sondear.
- Forzar el EDID no sirve con estos kernels: según el foro, [no usan el EDID del monitor](https://ps4linux.com/forums/d/388-baikal-ps4-slim-no-signal-after-loading-linux-payload) y sacan 1080p a 60 Hz fijo. En ese hilo (10-2025), un Baikal B1 con el mismo kernel y el mismo síntoma **funcionó al cambiar el monitor por una tele**; su monitor era un MSI a 100 Hz. Siguiente prueba: una tele.
- Pendiente de aclarar si la consola se apaga por temperatura (sin control del ventilador en Baikal) o por un cuelgue del kernel: medir cuánto tarda y si el ventilador gira.

### 2026-09-13, tarde — con la tele funciona; instalado y con GPU

| Hora | Qué | Resultado |
|---|---|---|
| 16:25 | Tele LG en vez del monitor. Kernel `5.4.247 baikal_mt76`, `bootargs.txt` con EDID forzado, payload v25 de 1 GB | **Rescue shell en pantalla** a la primera. Era el monitor |
| 16:35 | `install-psxitarch.sh` | Encuentra `/dev/sda` (29 GB), copia a RAM, particiona, extrae. **1 h 40 min** para 249.000 archivos: 30/s en las librerías grandes, 130/s en los pequeños. El pendrive iba a **USB 2.0** (`480` en `/sys/bus/usb/devices/*/speed`): no entraba del todo en el puerto frontal |
| 18:17 | Fin de la instalación | `Psxitarch linux installed with success!`, pero el `switch_root` final del script falla ("PID must be 1") y vuelve a la rescue shell. `resume-boot` arranca la distro |
| 18:21 | Payload de 2 GB, arranque normal | Vuelve a caer en la rescue shell (*"root" variable is empty*): falta `root=LABEL=psxitarch` en `bootargs.txt`. Con `resume-boot` arranca. Pendiente añadirlo |
| 18:25 | Login en SDDM, sesión Plasma (Wayland) | Negro con cursor |
| 18:40 | Sesión Plasma (X11) | Se queda en el splash de KDE más de 3 minutos (pendrive a USB 2.0) |
| 18:45 | Sesión **LXDE** | Escritorio en segundos. `glxinfo`: **`AMD Radeon Graphics (radeonsi, liverpool, ACO, DRM 3.35, 5.4.247-DFAUS-blkscrn_Fix_mt7668_hdmia)`** — aceleración GPU real |

Lecciones:

- El kernel 5.4.247 `baikal_mt76` + loader v25 + distro Arch Mesa 25.1 funcionan en esta CUH-7116B. El `neocine-1.1` queda por probar con la tele.
- El teclado es US: la `|` es Shift + `\` (encima de Intro). En la rescue shell no hay distribución española.
- `glxinfo` solo funciona dentro del escritorio; en una consola de texto da *unable to open display*.
- Plasma 6 en un pendrive a USB 2.0 no es viable; LXDE sí. Para Dolphin da igual el escritorio.
- El loader solo busca el pendrive en `/mnt/usb0` y `/mnt/usb1`: en el puerto trasero no lo encuentra (20:00, pantalla negra); en el frontal original sí.
- El instalador borra el `bootargs.txt` al reparticionar: hay que recrearlo con `root=LABEL=psxitarch` (20:08, arranque directo a SDDM sin `resume-boot`).
- La Pro Baikal no tiene Ethernet en Linux. El Wi-Fi MediaTek escanea bien con `iw dev wlan2 scan`, pero NetworkManager lista solo dos redes: conectar con `nmcli device wifi connect "RED" password "…" hidden yes`. Funcionó con el punto de acceso móvil del PC (`JFK-963`, red 192.168.137.x); el router Digi de casa, mejor por su SSID de 2,4 GHz (`DIGIFIBRA-938F`; el `-PLUS-` es 5 GHz). `hostname` e `ifconfig` no existen: `ip -4 a`.
- `instalar.sh` (20:25): los 10 paquetes entran; el `ERROR` de `mkinitcpio` (`/boot/vmlinuz-linux`) es inofensivo, el kernel viene del pendrive. **Dolphin 2509 abre.**
- El SSH de la distro solo escucha en socket local hasta hacer `sudo systemctl start sshd` (ya está `enabled`). Desde el PC entra `paramiko` con `ps4`/`ps4`; ojo con Git Bash, que convierte los argumentos que empiezan por `/` en rutas de Windows (`MSYS_NO_PATHCONV=1`).

### 2026-09-13, noche — Payload Guest, ajustes por SSH y el juego en la consola

- **Payload Guest** instalado y `/data/payloads/` con los 30 `.bin` de `pkg/payloads/`; el `meta.json` sin `icon` lo rompía y se quitó. Linux se arranca desde la consola eligiendo `linux-2048mb.bin`.
- La IP de Linux en la red de casa fue **192.168.1.180** (Wi-Fi `DIGIFIBRA-PLUS-938F`, conectada con `hidden yes`); cambia con DHCP, se localiza por la MAC del Wi-Fi (`e8:9e:b4:9e:bd:6f`).
- Por SSH: **autologin en LXDE** (`/etc/sddm.conf.d/autologin.conf`, `Session=LXDE`; las sesiones disponibles son `LXDE`, `openbox` y `plasmax11`), `Dolphin.ini` con `GFXBackend = OGL` e `ISOPath0 = /home/ps4/Juegos`, y ***Wind Waker* copiado** por SFTP como `/home/ps4/Juegos/Zelda-Wind-Waker-Europe.rvz` (SHA-1 igual al catálogo). SFTP no aceptó el nombre largo con comas y paréntesis.
- Revisión del log de arranque (`journalctl -b -p warning`): ningún servicio fallido. Se arregló lo que hacía ruido: **ZRAM** (la distro lo configura pero el kernel `baikal_mt76` no trae el módulo: `dev-zram0.device` agotaba el tiempo cada 90 s y alargaba el arranque a 3:30; desactivado renombrando `/etc/systemd/zram-generator.conf`) y **dominio regulatorio** (`WIRELESS_REGDOM="ES"` en `/etc/conf.d/wireless-regdom`). Lo demás es normal en PS4 con 5.4: sin ACPI ni IOAPIC, `pci=biosirq`, `over-current` falso en los puertos USB (lo de Baikal), `ahci probe failed` (sin SATA, por eso no hay disco interno), systemd pidiendo kernel ≥ 5.7, y la partición ext4 sin journal ("mounting unchecked fs": apagar siempre desde el menú).
- El disco interno de la PS4 aparece en Linux como `sdb` con sus 16 particiones cifradas. No tocar.
- `pacman -S` funciona con red; `ifconfig`/`iwconfig`/`nslookup` no existen como paquetes (son `net-tools`, `wireless_tools`, `bind`); con `ip`, `iw` y `getent hosts` sobra.

### 2026-09-13, 23:40 — *Wind Waker* jugable

- **Dolphin 2509 con *Wind Waker* (GZLP01) a 30 fps** (velocidad completa: el juego es de 30 nativos) en menús y juego; 23-24 fps en alguna cinemática. Backend **Vulkan** (`JIT64 DC | Vulkan | HLE`): Dolphin lo eligió (o Javi) por encima del `OGL` del `Dolphin.ini`, y funciona; el aviso de la escena de que Vulkan se cuelga en Pro era de Mesa 22. OpenGL queda por comparar.
- **CPU a 1,59 GHz**, no a 2,13: el kernel dice *"Unable to measure TSC frequency, assuming default"* (1594 MHz) y el *uptime* cuadra con el reloj real, así que la frecuencia es esa de verdad. Es el P-state que deja el loader antes del kexec y/o este kernel 5.4; pregunta abierta para `neocine-1.1` y los kernels de rmux.
- **Temperatura: CPU a 71 °C jugando, con "high" en 70** (`sensors`, `k10temp`). En Baikal ningún kernel controla el ventilador: se queda como lo dejó el sistema de la PS4. Explica los apagones de la madrugada (protección térmica del Syscon). **Antes de lanzar Linux, lanzar `ps4-fan-threshold60.bin` en Payload Guest**: el umbral vive en el microcontrolador del ventilador y sobrevive al kexec.
- Zona horaria puesta a `Europe/Madrid` (venía en UTC; la hora ya la sincroniza NTP).
- Estado de Dolphin guardado por SSH (`xdotool`, Shift+F1), Dolphin cerrado por SSH y **configuración recomendada aplicada** con copia previa (`dolphin.md`): ubershaders híbridos, V-Sync off, MSAA 4x, mando sin conflicto, 16:9 real y sin desenfoque de lejanía en *Wind Waker*.
- **DualShock 4 mapeado por USB** en Dolphin; por Bluetooth no funciona todavía. Revisada la configuración de Dolphin y del juego (`Dolphin.ini`, `GFX.ini`, `GCPadNew.ini`, `sys/GameSettings/GZL.ini`) y recomendaciones en [`dolphin.md`](dolphin.md): ubershaders híbridos, V-Sync off, MSAA 4x, Z/L/R sin conflicto en el mando, 16:9 por código Gecko.

## Problemas conocidos

| Síntoma | Qué hacer |
|---|---|
| `The "root" variable is empty` al arrancar antes de instalar | Normal: no hay nada instalado. Seguir con `install-psxitarch.sh` |
| `No valid usb device found` | Conectar solo el pendrive y reiniciar; conectar teclado y ratón cuando ya esté la rescue shell. Comprobar que es MBR + FAT32 y que los tres archivos tienen el nombre exacto (`psxitarch.tar.gz`, no `.xz`). `fdisk -l` para ver si aparece |
| `Not enough space in RAM available` | Payload de 1 GB, no de 2 o más: la distro se copia a RAM antes de particionar |
| `mount -o ro /newroot failed` | initramfs equivocado (tiene que ser el "External HDD") o distro mal nombrada |
| Pantalla negra o gris tras el payload | Otra tele; apagar y encender la pantalla; reiniciar y repetir hasta dos o tres veces. En 5.4 con monitor, Ctrl+Alt+F2 y luego Ctrl+Alt+F1 o F7 recupera la señal. `bootargs.txt` de emergencia (legacy): `panic=0 clocksource=tsc consoleblank=0 net.ifnames=0 radeon.dpm=0 amdgpu.dpm=0 drm.debug=0 console=tty0 drm.edid_firmware=edid/1920x1080.bin` |
| LED blanco fijo, no arranca | Fallo del kexec: reiniciar y repetir. Si se subieron `bzImage` o `initramfs` por FTP, resubirlos en modo binario |
| Escritorio muy lento, juegos a 10 fps | `glxinfo` dice `llvmpipe`: Mesa demasiado nueva para el 5.4. Distro con Mesa ≤ 25.1 |
| `clock recovery tried 5 times` en `dmesg` | Normal en kernels 5.x, no afecta |
| Sin Ethernet | Conocido en Pro Baikal. Wi-Fi |
| Glitches en juegos con Vulkan | `RADV_DEBUG=nocompute` en `/etc/environment`, o `amdgpu.abmlevel=0` en `bootargs.txt`. OpenGL va mejor que Vulkan en Pro |
| `pacman` falla por *Landlock* | Descomentar `DisableSandbox` en `/etc/pacman.conf` |

## Rutas en la consola

| Ruta | Para qué |
|---|---|
| USB, raíz (FAT32) | `bzImage`, `initramfs.cpio.gz`, `psxitarch.tar.gz`; opcionales `bootargs.txt`, `vram.txt`. Tiene prioridad sobre el disco interno |
| `/data/linux/boot/` | Alternativa por FTP para `bzImage` e `initramfs.cpio.gz`: permite llegar a la rescue shell sin USB. El loader los copia ahí solo desde el USB la primera vez |
| `/data/payloads/` | Los nueve `linux-*.bin` (32 MB a 4 GB de VRAM) y las herramientas de `pkg/payloads/` para *Payload Guest*, subidos el 13-09-2026 |

## Fuentes

- [ps4-linux-loader](https://github.com/ps4-linux/ps4-linux-loader) — README y [release v25](https://github.com/ps4-linux/ps4-linux-loader/releases/tag/v25) (25-07-2026)
- [Guía de DionKill](https://dionkill.github.io/ps4-linux-tutorial/) (copia: [`ps4-linux-tutorial.md`](ps4-linux-tutorial.md)); commit del 10-09-2026 ["7.1.7 does *not* support Baikal"](https://github.com/DionKill/ps4-linux-tutorial/commit/f4fb573)
- [feeRnt/ps4-linux-12xx, release 5.4.247 neocine-1.1](https://github.com/feeRnt/ps4-linux-12xx/releases/tag/v5.4.247__neocine-1.1) y su [issue #8: Baikal 5.4, no GPU acceleration with newer Mesa](https://github.com/feeRnt/ps4-linux-12xx/issues/8)
- [sony-jaguar-devs/ps4-linux](https://github.com/sony-jaguar-devs/ps4-linux) — tabla de modelos: Pro Baikal B1 con 5.4.247
- [rmuxnet/linux, release 7.1.7](https://gitlab.com/rmuxnet/linux/-/releases) (04-09-2026): "This release is for Aeolia Belize. Baikal will be soon merged in"
- [CachyOS Light](https://ps4linux.com/forums/d/422-cachyos-light-lxqt-a-light-and-fast-distro) (Mesa 26.0.4; "For Baikal systems, use the 7.0 kernel")
- [GoldHEN](https://github.com/GoldHEN/GoldHEN) — FTP en 2121 y BinLoader en 9090
- `install-psxitarch.sh` y `start-psxitarch.sh`, leídos del `initramfs.cpio.gz` de DionKill (variante External HDD)

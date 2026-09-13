# Linux en la PS4 Pro — 12.52, Baikal B1

Proyecto aparte de RetroArch: arrancar Linux en esta consola para usar emuladores de PC (Dolphin para GameCube/Wii, RPCS3 para PS3) que no existen en el sistema de la PS4. **Estado: preparado en el PC, sin probar todavía en la consola** (checklist en [`../PLAN.md`](../PLAN.md), tareas en [`../PENDIENTES.md`](../PENDIENTES.md)).

Este documento cubre lo específico de **esta** consola y de **estos** archivos. La guía general de la escena, con todos los métodos y sus problemas, es la de DionKill: copia en [`ps4-linux-tutorial.md`](ps4-linux-tutorial.md), original en [dionkill.github.io/ps4-linux-tutorial](https://dionkill.github.io/ps4-linux-tutorial/). Los textos antiguos (psxitarch, `archlinux-on-ps4`, kernels 4.14/5.3, ps4linux.com) están superados; no seguirlos.

## Esta consola

Leído en *Ajustes → Sistema → Información del sistema* con GoldHEN cargado (foto, 13-09-2026):

| Dato | Valor |
|---|---|
| Modelo | PS4 Pro |
| Firmware | 12.52 (`HEN 12.52`) |
| **Southbridge** | **Baikal B1 (0x30201)** |
| GoldHEN | v2.4b18.10 |
| IP | 192.168.1.201 (cambia; confirmarla antes de conectar) |

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
| `distros/psxitarch-7coil-2022-06-26.tar.xz` | Rootfs de 7coil: Arch 2022.06.01 **sin escritorio**, `mesa-ps4 21.3.2`, usuario `pi`/`raspberry`, root `raspberry` | [7coil/archlinux-on-ps4](https://github.com/7coil/archlinux-on-ps4/releases/tag/2022-06-26) | ⚠️ vale para probar que la cadena arranca (Mesa vieja, compatible con el 5.4). De 2022: no actualizarla ni usarla como distro final |
| `distros/archlinux-on-ps4-2022-06-26.zip` | Documentación de 7coil (sin binarios) | ídem | referencia |
| `src/` | Submódulos con el código de [ps4-linux-loader](https://github.com/ps4-linux/ps4-linux-loader), [ps4-linux-initramfs](https://github.com/feeRnt/ps4-linux-initramfs), [archlinux-on-ps4](https://github.com/7coil/archlinux-on-ps4) y [ps4-linux-12xx](https://github.com/feeRnt/ps4-linux-12xx) (fuentes del kernel, 6,4 GB de historial). Se traen con `git submodule update --init linux/src/<repo>`. El kernel queda en su rama por defecto (6.15.4): la rama de Baikal, `5.4.247-baikal-dfaus`, **no se puede extraer en Windows** (archivos `aux.c` y nombres que solo difieren en mayúsculas); hace falta Linux o WSL | — | referencia; no se cataloga |

### Lo que falta: la distro (🧑)

Una distro para PS4 **con Mesa ≤ 25.1**. Las dos que hay, ambas en descargas directas que no se pueden automatizar:

| Distro | Mesa | Descarga | Acceso | Pega |
|---|---|---|---|---|
| **Arch limpio con Mesa 25.1** (08-03-2026) | 25.1 | [Mega](https://mega.nz/file/JNkUgZLY#q-XwRcz81SLyMBE_-RIpbtRZIi2pGaH-8xCc6-uFXRI), 2,03 GB | `ps4` / `ps4` | Autor anónimo; la enlaza y la da por buena el mantenedor del kernel Baikal ([issue #8](https://github.com/feeRnt/ps4-linux-12xx/issues/8)). Se llama `ps4linux.tar.xz`: hay que renombrarla |
| Xubuntu 25.04 (25-05-2025) | 25.0.5 | [1fichier](https://1fichier.com/?at7ccs9f5rb9spzkm8h9) o [Mediafire](https://www.mediafire.com/folder/lmcwkxf915jqm/ps4-xubuntu), en varias partes | `ps4linux` / `ps4linux` | Trae Steam, Wine y emuladores, pero su autor (triki1) está señalado en la guía de DionKill como no fiable, y no publica fuentes |

La que elijas, a `linux/distros/` con su nombre original; el commit siguiente la catalogará. Cuando rmux publique el kernel 7.x para Baikal, la distro a usar pasa a ser [CachyOS Light](https://ps4linux.com/forums/d/422-cachyos-light-lxqt-a-light-and-fast-distro) (Mesa 26, se actualiza con `pacman`) y este documento cambia.

## Cómo arranca

1. GoldHEN cargado en la PS4 (Poops desde el Blu-ray; [`../INSTALL.md`](../INSTALL.md)).
2. Se envía a la consola el **payload del loader** (`linux-1024mb.bin`). El loader busca `bzImage` e `initramfs.cpio.gz` **en el USB** y, si no hay, en `/data/linux/boot/` del disco interno (o `/user/system/boot/`); reserva la VRAM y hace `kexec` del kernel.
3. El initramfs abre una **rescue shell** en pantalla (teclado USB). `install-psxitarch.sh` particiona el USB, extrae la distro y la arranca; en arranques siguientes `start-psxitarch.sh` monta la partición `psxitarch` y arranca. Si no arranca solo, `resume-boot` (nunca más de dos veces; a la tercera, Ctrl+Alt+Supr).
4. Al reiniciar la consola vuelve el sistema de la PS4 intacto. Linux no toca el disco interno; para volver a Linux hay que repetir 1 y 2.

## Procedimiento (pendrive, método por script)

### 1. Preparar el pendrive en el PC

- Pendrive USB 3.0 de **32 GB o más** (el instalador exige **22 GB** como mínimo y **tabla de particiones MBR**, no GPT). **Se borra entero.**
- Formatear en **FAT32**. Windows no ofrece FAT32 por encima de 32 GB: usar [Rufus](https://rufus.ie) con *Non bootable*, *MBR*, *FAT32*.
- Copiar en la raíz, con estos nombres exactos:

| En el pendrive | Copia de |
|---|---|
| `bzImage` | `linux/kernel/bzImage_Clang` |
| `initramfs.cpio.gz` | `linux/initramfs/initramfs.cpio.gz` |
| `psxitarch.tar.gz` | la distro, **recomprimida en gzip** (abajo) |

- El instalador solo acepta **`psxitarch.tar.gz`** (gzip): busca ese nombre y extrae con `tar -xvpzf`. Un `.tar.xz` no sirve aunque se renombre. Recomprimir en el PC sin descomprimir en disco, por ejemplo la de 7coil:

  ```
  python -c "import lzma,gzip,shutil,sys; shutil.copyfileobj(lzma.open(sys.argv[1]), gzip.open(sys.argv[2], 'wb', 6))" linux/distros/psxitarch-7coil-2022-06-26.tar.xz E:\psxitarch.tar.gz
  ```

  (`E:` es el pendrive; tarda unos minutos. Si la distro ya es `.tar.gz`, solo renombrar.)

- Sin `bootargs.txt` ni `vram.txt`: el kernel 5.4.247 ya pone 1920x1080 a 60 Hz y la VRAM la fija el payload elegido. Solo si hace falta, `bootargs.txt` junto al `bzImage` (ver "Problemas").

### 2. Preparar la consola

- Cargar GoldHEN. Comprobar que el Blu-ray de Poops **ha salido** de la bandeja (suele expulsarse solo): un disco dentro corrompe la instalación.
- En el menú de GoldHEN, con **FTP** y **BinLoader** (puerto 9090) activados. Sin ninguna aplicación suspendida ni RetroArch abierto.
- *Ajustes → Sonido y pantalla → Ajustes de salida de vídeo*: resolución **1080p** (no *Automático*); *Gama de colores RGB* en *Limitado* si la imagen sale oscura; **desactivar** *Salida Deep Colour* (color de más de 8 bits) o no hay señal. HDCP se queda activado.
- Conectados: pendrive, **teclado y ratón USB**. Sin hub para el pendrive. Si hay un monitor y una tele, la tele suele dar menos pantallas negras.

### 3. Enviar el payload

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
| `/data/payloads/` | Payloads `.elf`/`.bin` para *Payload Guest* |

## Fuentes

- [ps4-linux-loader](https://github.com/ps4-linux/ps4-linux-loader) — README y [release v25](https://github.com/ps4-linux/ps4-linux-loader/releases/tag/v25) (25-07-2026)
- [Guía de DionKill](https://dionkill.github.io/ps4-linux-tutorial/) (copia: [`ps4-linux-tutorial.md`](ps4-linux-tutorial.md)); commit del 10-09-2026 ["7.1.7 does *not* support Baikal"](https://github.com/DionKill/ps4-linux-tutorial/commit/f4fb573)
- [feeRnt/ps4-linux-12xx, release 5.4.247 neocine-1.1](https://github.com/feeRnt/ps4-linux-12xx/releases/tag/v5.4.247__neocine-1.1) y su [issue #8: Baikal 5.4, no GPU acceleration with newer Mesa](https://github.com/feeRnt/ps4-linux-12xx/issues/8)
- [sony-jaguar-devs/ps4-linux](https://github.com/sony-jaguar-devs/ps4-linux) — tabla de modelos: Pro Baikal B1 con 5.4.247
- [rmuxnet/linux, release 7.1.7](https://gitlab.com/rmuxnet/linux/-/releases) (04-09-2026): "This release is for Aeolia Belize. Baikal will be soon merged in"
- [CachyOS Light](https://ps4linux.com/forums/d/422-cachyos-light-lxqt-a-light-and-fast-distro) (Mesa 26.0.4; "For Baikal systems, use the 7.0 kernel")
- [GoldHEN](https://github.com/GoldHEN/GoldHEN) — FTP en 2121 y BinLoader en 9090
- `install-psxitarch.sh` y `start-psxitarch.sh`, leídos del `initramfs.cpio.gz` de DionKill (variante External HDD)

# ps4-cpu — modo rendimiento / modo normal de la CPU en Linux

El kernel 5.4.247 de Baikal **no lleva `cpufreq`** y ni siquiera mide el reloj (`ps4: Unable to measure TSC frequency, assuming default` → `tsc: Detected 1594.000 MHz`). Deja la CPU donde la deja el arranque: **P2, 1,6 GHz**, en los 8 núcleos, aunque el P-state **P0 a 2,1 GHz está permitido** (`PstateCurLim = 0`). Leído de los MSR el 14-09-2026:

| P-state | MHz | |
|---|---|---|
| P0 | 2100 | permitido, nadie lo pide |
| P1 | 1800 | |
| **P2** | **1600** | **donde arranca** |
| P3–P5 | 1400 / 1200 / 800 | |

Pedir P0 escribiendo en `PstateCtl` (MSR `0xC0010062`) de cada núcleo es lo que hace este script. Medido en *Wind Waker* (Dolphin 2509, misma escena con estado guardado, Outset mirando al mar): **26,8 fps a 1,6 GHz → 29,95 a 2,1 GHz**, velocidad completa. Temperatura de 74-76 a 77-80 °C. Se pierde al reiniciar: **hay que volver a pedirlo en cada arranque de Linux**, hasta que haya un kernel con `cpufreq`.

## Uso

Dos iconos en el escritorio y en el menú *Juegos* / *Sistema*:

| Icono | Hace | Cuándo |
|---|---|---|
| **CPU 2,1 GHz — Rendimiento** (naranja, aguja arriba) | `ps4-cpu rendimiento` → P0 | Antes de lanzar Dolphin |
| **CPU 1,6 GHz — Normal** (verde, aguja abajo) | `ps4-cpu normal` → P2 | Escritorio, o si sube demasiado la temperatura |

Al pulsarlos sale un aviso arriba a la derecha, encima del juego, con el modo, la frecuencia y la temperatura; se cierra solo. En terminal, además: `ps4-cpu estado` y `ps4-cpu alternar`.

La temperatura viene de `/sys/class/hwmon/*/temp1_input`. **Lanzar `ps4-fan-threshold60.bin` antes de Linux** sigue siendo necesario: a 2,1 GHz jugando se llega a 80 °C.

## Archivos

| Aquí | En la consola |
|---|---|
| `ps4-cpu` | `/usr/local/bin/ps4-cpu` (root, 755). La parte que toca los MSR corre como root; el aviso, como usuario |
| `rendimiento.svg`, `normal.svg` | `/usr/local/share/ps4-cpu/` |
| `ps4-cpu-*.desktop` | `/usr/share/applications/` (menú) y `~/Desktop/` (escritorio, con permiso de ejecución para que `pcmanfm` no pregunte) |
| `instalar.sh` | crea además `/etc/sudoers.d/ps4-cpu`: `ps4 ALL=(root) NOPASSWD: /usr/local/bin/ps4-cpu`, solo para ese script (que el usuario no puede editar) |

Instalar o actualizar: copiar la carpeta a la consola y `sudo sh instalar.sh`. Desde el PC, `tools/ps4linux.py --put` archivo a archivo (con finales de línea Unix) y luego el `sh`.

El aviso usa GTK 3 desde Python (viene con la distro); la distro no trae `notify-send` ni `zenity`. La ventana es de tipo `POPUP` y `keep_above`, y se ve encima de la ventana de render de Dolphin.

## Cómo se supo

`/dev/cpu/*/msr` existe en este kernel (el módulo `msr` va compilado dentro). Los MSR de P-state de la familia 16h: `0xC0010061` límite, `0xC0010062` control, `0xC0010063` estado, `0xC0010064+n` definición de cada P-state (`CoreCOF = 100 MHz × (CpuFid + 0x10) / 2^CpuDid`). El reloj del sistema no se desajusta al cambiar (`constant_tsc`): la hora de la consola siguió igual a la del PC.

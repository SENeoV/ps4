# Dolphin en la PS4 — configuración y *Wind Waker*

Dolphin **2509** (paquete `dolphin-emu 1:2509-1` de Arch, instalado sin red desde `linux/pkgs/`) sobre el Arch de `linux/distros/` (Mesa 25.1, RADV), kernel 5.4.247, en la PS4 Pro CUH-7116B (Baikal B1). Primer juego: *The Legend of Zelda: The Wind Waker* (Europe, `GZLP01`, RVZ), el 13-09-2026, **a 30 fps (velocidad completa) con Vulkan**, 3x de resolución interna, y bajones a 23-24 fps en cinemáticas por la compilación de shaders.

Hardware visto desde Linux: 8 núcleos Jaguar **a 1,6 GHz al arrancar, 2,1 GHz con [`cpu/ps4-cpu`](cpu/README.md)** (icono *Rendimiento* en el escritorio; pulsarlo antes de Dolphin en cada arranque), GPU "AMD Radeon Graphics (RADV LIVERPOOL)", Vulkan 1.3 (RADV) y OpenGL 4.6 (radeonsi), 5,8 GiB de RAM con el payload de 2 GB de VRAM. **El cuello de botella es la CPU**: la GPU tiene margen para resolución y antialiasing, la CPU no lo tiene para compilar shaders ni para juegos exigentes.

Los archivos viven en `/home/ps4/.config/dolphin-emu/`: `Dolphin.ini` (general), `GFX.ini` (gráficos), `GCPadNew.ini` (mando). Dolphin los reescribe al cerrarse: **editarlos solo con Dolphin cerrado**.

**Los ajustes por juego van en otro sitio: `~/.local/share/dolphin-emu/GameSettings/<ID>.ini`** (es donde Dolphin los escribe desde *Properties*). Un `GameSettings/` dentro de `~/.config/dolphin-emu/` **no lo lee**: los `GZLP01.ini` y `GZLE01.ini` que se escribieron ahí el 13 y el 14-09 nunca se aplicaron (comprobado el 14-09: el juego salía en 4:3 y sin texturas). Dolphin los lee al arrancar cada juego, así que un cambio necesita *Stop* y volver a lanzar, no cerrar Dolphin.

El resto del archivo es el diario de lo que se hizo, por fechas. Al final están las dos secciones de referencia, que son lo que hay que leer antes de tocar nada: **[reglas de configuración](#reglas-de-configuración-qué-se-lee-dónde-y-cuándo)** (qué archivo gana, cómo se llaman las secciones, cuándo se relee cada cosa, qué no se toca) y **[protocolo de pruebas](#protocolo-de-pruebas-en-la-consola)** (cómo medir en esta consola sin sacar una conclusión falsa).

## Configuración a 13-09-2026, 23:50 (leída por SSH)

| Archivo | Clave | Valor | Comentario |
|---|---|---|---|
| `Dolphin.ini` `[Core]` | `CPUThread` | `True` | Dual core, imprescindible aquí |
| | `GFXBackend` | `Vulkan` | Puesto desde la interfaz; el `OGL` inicial no se conservó. Funciona |
| | `SIDevice0` | `6` | Mando estándar en el puerto 1 |
| `Dolphin.ini` `[DSP]` | `DSPThread` | `True` | Audio HLE en su hilo |
| `Dolphin.ini` `[General]` | `ISOPath0` | `/home/ps4/Juegos` | Carpeta de juegos |
| `GFX.ini` `[Settings]` | `InternalResolution` | `3` | 3x = 1920x1584, ≈ 1080p |
| | `MSAA` / `SSAA` | `1` / `False` | Sin antialiasing |
| | `ShowFPS` | `True` | Contador arriba a la derecha |
| `GFX.ini` `[Enhancements]` | `MaxAnisotropy` | `4` | 16x (0 = 1x … 4 = 16x) |
| `GFX.ini` `[Hardware]` | `VSync` | `True` | |
| `GCPadNew.ini` `[GCPad1]` | `Device` | `SDL/0/PS4 Controller` | DualShock 4 **por cable USB** |

Lo que Dolphin impone al juego desde su `sys/GameSettings/GZL.ini` y que no hay que tocar: `EFBAccessEnable = True`, `EFBToTextureEnable = False` (copias de EFB a RAM, las necesita el juego), `VISkip = False` (incompatible con el juego), `ArbitraryMipmapDetection = True`, `EnableGPUTextureDecoding = False`. Y trae códigos listos: el Gecko **"16:9 Widescreen"** y el AR **"Remove Distance Blur"**, ambos marcados como verificados.

## Cambios recomendados

| Ajuste | Dónde (interfaz) | Clave en el archivo | Por qué |
|---|---|---|---|
| **Hybrid Ubershaders** y **compilar antes de empezar** | *Graphics → Advanced → Shader Compilation* | `GFX.ini [Settings] ShaderCompilationMode = 2`, `WaitForShadersBeforeStarting = True` | Los tirones de las cinemáticas son shaders compilándose en una CPU a 1,6 GHz; los ubershaders los pintan mientras tanto con la GPU, que sobra |
| **V-Sync off** | *Graphics → General* | `GFX.ini [Hardware] VSync = False` | Dolphin ya limita a la velocidad del juego; con V-Sync cada bajón se nota el doble |
| **MSAA 4x** (nunca SSAA) | *Graphics → Enhancements → Anti-Aliasing* | `GFX.ini [Settings] MSAA = 4`, `SSAA = False` | Casi gratis en GCN; SSAA multiplica por 4 el coste |
| Resolución interna **3x** | *Graphics → Enhancements* | `InternalResolution = 3` | Dejar como está: ya es 1080p. 4x solo con el payload de 3 GB y para comprobar que la GPU aguanta |
| **Mando: Z = R1, L = L2, R = R2** | *Controllers → Port 1 → Configure* | `GCPadNew.ini` (abajo) | Ahora L1 es a la vez `Z` (tercer objeto) y `L` (fijar objetivo). L y R de GameCube son gatillos analógicos: L2/R2 |
| **16:9 con el código Gecko** | *Propiedades del juego → Gecko Codes → 16:9 Widescreen*; y *Graphics → General → Aspect Ratio: Auto* | `Dolphin.ini [Core] EnableCheats = True`; `GameSettings/GZLP01.ini [Gecko_Enabled] $16:9 Widescreen` | Parche del juego, no el *Widescreen Hack* de Dolphin: sin recortes de geometría en los bordes |
| *Remove Distance Blur* (opcional) | *Propiedades → AR Codes* | `GameSettings/GZLP01.ini [ActionReplay_Enabled] $Remove Distance Blur` | Quita el desenfoque de lejanía; cuestión de gusto |
| `mitigations=off` | `bootargs.txt` del pendrive | al final de la línea | Algo de CPU (Spectre/Meltdown); la consola ya está abierta |
| Texturas HD (*Hypatia WWHD v2.0*) | *Graphics → Advanced → Load Custom Textures* | `GFX.ini [Settings] HiresTextures = True` | **Prueba parcial primero**: ver "Texturas HD" abajo. El pack entero son 9,1 GB y el pendrive va a USB 2.0 |

No tocar: *Skip EFB Access*, *Store EFB Copies to Texture Only*, *VBI Skip* (el INI del juego los fija por necesidad), ni el reloj de CPU emulada.

### `GCPadNew.ini` recomendado (DualShock 4 por USB)

```ini
[GCPad1]
Device = SDL/0/PS4 Controller
Buttons/A = `Button S`
Buttons/B = `Button E`
Buttons/X = `Button W`
Buttons/Y = `Button N`
Buttons/Z = `Shoulder R`
Buttons/Start = Start
Main Stick/Up = `Left Y+`
Main Stick/Down = `Left Y-`
Main Stick/Left = `Left X-`
Main Stick/Right = `Left X+`
Main Stick/Calibration = 100.00 141.42 100.00 141.42 100.00 141.42 100.00 141.42
C-Stick/Up = `Right Y+`
C-Stick/Down = `Right Y-`
C-Stick/Left = `Right X-`
C-Stick/Right = `Right X+`
C-Stick/Calibration = 100.00 141.42 100.00 141.42 100.00 141.42 100.00 141.42
Triggers/L = `Trigger L`
Triggers/R = `Trigger R`
Triggers/L-Analog = `Trigger L`
Triggers/R-Analog = `Trigger R`
D-Pad/Up = `Pad N`
D-Pad/Down = `Pad S`
D-Pad/Left = `Pad W`
D-Pad/Right = `Pad E`
```

Cruz = A, círculo = B, cuadrado = X, triángulo = Y, R1 = Z, L2/R2 = L/R. En el archivo actual el C-Stick está con Left y Right cruzados (`Right X+` para Left): si es a propósito, para llevar la cámara invertida, dejarlo; si no, esta versión lo pone recto.

## DualShock 4

- **Por cable USB: funciona** (13-09-2026). Dolphin lo ve como `SDL/0/PS4 Controller`.
- **Por Bluetooth: no, de momento.** Es el problema conocido de la guía: el mando guarda el emparejamiento con el Bluetooth del sistema de la PS4 y Linux usa el mismo chip con otra pila, así que hay que emparejarlo desde Linux, y en cada arranque de Linux. Procedimiento para probarlo: mando apagado, mantener **Share + PS** hasta que la barra parpadee rápido (modo emparejamiento); en LXTerminal `bluetoothctl`, y dentro: `power on`, `agent on`, `scan on`, esperar a `Wireless Controller`, `pair <MAC>`, `trust <MAC>`, `connect <MAC>`. Al volver al sistema de la PS4 hay que volver a emparejarlo allí con el cable. Con `bluetoothd` en el arranque salen dos avisos (`Failed to reset Adv Monitors`, `Set device flags`) que son de kernel 5.4 y no impiden emparejar; si el chip no lo encuentra, es el driver MediaTek y no hay más.

## Aplicado el 13-09-2026 a las 23:58 (por SSH, con Dolphin cerrado)

Copia previa completa en `~/.config/dolphin-emu.bak-2026-09-13`. Aplicado todo lo de la tabla salvo las texturas HD: `EnableCheats`, MSAA 4x (`MSAA = 0x00000004`, Dolphin lo guarda en hexadecimal), ubershaders híbridos con compilación previa, V-Sync off, mando con `Z = R1`, `L = L2`, `R = R2` y C-Stick recto, y `GameSettings/GZLP01.ini` con el Gecko *16:9 Widescreen*, el AR *Remove Distance Blur* y `AspectRatio = 1` (16:9 forzado solo en este juego). Para volver atrás: `rm -r ~/.config/dolphin-emu && cp -a ~/.config/dolphin-emu.bak-2026-09-13 ~/.config/dolphin-emu`.

**Corrección del 14-09:** ese `GZLP01.ini` se escribió en `~/.config/dolphin-emu/GameSettings/`, que Dolphin no lee, así que no se aplicó. Lo que el europeo usaba de verdad era un `~/.local/share/dolphin-emu/GameSettings/GZLP01.ini` creado desde la interfaz el 13-09 a las 23:10, con el *Widescreen Hack* **y** el código Gecko a la vez, `MSAA = 1`, anisotrópico 8x, `EnableGPUTextureDecoding = True`, `ArbitraryMipmapDetection = False` y los parches `$Max health` y `$Current health`. El 14-09 se sustituyó por la versión limpia (Gecko 16:9, AR sin desenfoque, `AspectRatio = 1`) y el resto lo hereda de la configuración global; el original está en `~/.config/dolphin-emu.bak-2026-09-14/GameSettings-local-share/GZLP01.ini`.

Trucos de manejo remoto que sirvieron: Dolphin no tiene control remoto, pero con `xdotool` (`DISPLAY=:0`) se le mandan atajos: *Shift+F1* guarda estado en la ranura 1 (queda en `~/.local/share/dolphin-emu/StateSaves/GZLP01.s01`, se carga con F1) y *Ctrl+Q* en la ventana principal (no en la de render) lo cierra, previo diálogo *Confirm* que se acepta con *Alt+Y*. Dolphin solo reescribe los `.ini` si algo cambió.

## Cómo aplicar los cambios (a mano)

Con Dolphin cerrado, por SSH (`ps4`/`ps4`, IP por la MAC del Wi-Fi) o en LXTerminal:

```sh
cd ~/.config/dolphin-emu
sed -i 's/^VSync = .*/VSync = False/' GFX.ini
sed -i 's/^MSAA = .*/MSAA = 4/' GFX.ini
grep -q ShaderCompilationMode GFX.ini || sed -i '/^\[Settings\]/a ShaderCompilationMode = 2\nWaitForShadersBeforeStarting = True' GFX.ini
grep -q EnableCheats Dolphin.ini || sed -i '/^\[Core\]/a EnableCheats = True' Dolphin.ini
printf '[Gecko_Enabled]\n$16:9 Widescreen\n' > ~/.local/share/dolphin-emu/GameSettings/GZLP01.ini
```

y el `GCPadNew.ini` de arriba tal cual. Después, arrancar el juego una vez y esperar la compilación inicial de shaders (una barra al principio); las siguientes veces sale de la caché.

## Texturas HD (*Hypatia WWHD v2.0*)

Pack de texturas que rehace *Wind Waker* al aspecto del remaster de Wii U, en `.dds` con mipmaps. Archivo `Hypatia WWHD Mod v2.0 (DDS-Full).7z`, **1,94 GB comprimido**, en `linux/texturas/` (no se versiona; el `.7z` está catalogado, el árbol extraído no).

El pack principal es la carpeta `GZL/`, **5.747 archivos y 9,14 GB** descomprimidos:

| Carpeta | Archivos | Tamaño | Qué es |
|---|---|---|---|
| `Environments` | 2.010 | 8.159,9 MB | Suelos, paredes, mar, cielo. **El 87 % del pack** |
| `HUD` | 2.534 | 627,6 MB | Menús, iconos, tipografías. **Solo en inglés** |
| `Characters` | 758 | 380,5 MB | Link, Tetra, enemigos, NPC |
| `Effects` | 175 | 140,1 MB | Fuego, humo, magia |
| `Additions` | 182 | 28,0 MB | Añadidos del autor |
| `Items` | 88 | 19,7 MB | Bombas, boomerang, hoja Deku, arco… |

Aparte trae `-[Optional Textures]-` con variantes sueltas (boomerang de *A Link to the Past*, etc.) que se copian encima si se quieren.

**Requisitos del readme del mod y cómo quedan aquí:**

| Pide el mod | Estado |
|---|---|
| Dolphin 5.0-6199 o superior | ✅ tenemos 2509 |
| *Load Custom Textures* activado | ⬜ `HiresTextures` ni siquiera está en `GFX.ini` (por defecto `False`) |
| **Filtrado anisotrópico a 1x** | ⬜ ahora está en 16x (`MaxAnisotropy = 4`); hay que ponerlo a `0`. Con 16x el mod muestra costuras en los bordes de las texturas |
| Versión **inglesa** del juego | ⬜ por eso se añade la copia USA (`GZLE01`); ver [`emu/ROMS/GC/README.md`](../emu/ROMS/GC/README.md) |
| Copiar las carpetas dentro de una carpeta `GZL` | El nombre `GZL` es el prefijo del ID, así que **vale para `GZLE01` y para `GZLP01`**: las mismas texturas sirven a las dos versiones |

Que el pack sea "solo inglés" afecta de verdad a `HUD` (textos y menús dibujados en las texturas): sobre la versión europea en español, el HUD saldría en inglés. `Characters`, `Items`, `Effects` y `Environments` no llevan texto y sirven igual en cualquier idioma.

### Resultado final: el pack entero, a velocidad completa (15-09-2026, 00:25)

**Los 5.747 archivos (9,2 GB) están en la consola**, verificados por hash conjunto carpeta a carpeta, y *Wind Waker* USA va a **29,95-29,98 fps** (ocho muestras seguidas en Outset), con la CPU al 150 % y a **62-65 °C**. Es decir: velocidad completa con el pack completo, siempre que la CPU esté a 2,1 GHz.

| | Antes | Con el pack entero |
|---|---|---|
| fps (Outset) | 26,8 a 1,6 GHz · 29,95 a 2,1 GHz | **29,97** |
| Memoria de Dolphin | 526 MB | **1,98 GB** (quedan 2,7 GB libres de 5,9) |
| Pendrive | 8,9 GB usados | 18 GB usados, **9,2 GB libres** |

La memoria es lo único que hay que vigilar: con `CacheHiresTextures = False` Dolphin carga cada `.dds` cuando aparece y no lo suelta, así que en una partida larga que recorra muchas islas puede seguir subiendo. Si algún día se queda sin RAM, la salida es quitar `Environments` (el 87 % del pack) o el payload de 3 GB de VRAM, que hoy no arranca.

Subido con [`tools/subir_texturas.py`](../tools/subir_texturas.py) por SFTP archivo a archivo, ~2,4 MiB/s: `Additions` 14 s, `Effects` 57 s, `HUD` ~5 min, `Environments` (8,2 GB) ~70 min. Cada carpeta termina comparando el hash conjunto del PC con el de la consola.

### Conjunto de prueba (extraído el 14-09-2026)

Antes de mover 9 GB por Wi-Fi a un pendrive a USB 2.0, se prueba con lo que más se ve y menos pesa: **`Characters` + `Items`, 846 archivos y 404 MB**, en `linux/texturas/GZL/`. Si el rendimiento aguanta, se añade `Effects` (140 MB), luego `Environments` (8,2 GB, el que decidirá) y `HUD` solo sobre la versión USA.

Sitio: el pendrive tiene **20 GB libres de 29** (`/dev/sda2`, 7,5 GB usados), así que cabe hasta el pack entero. Lo que no cabe es en RAM: 4,2 GB disponibles de 5,9, así que ***Prefetch Custom Textures* se queda desactivado** (cargaría todo el pack a RAM al arrancar). Con prefetch off Dolphin carga cada `.dds` cuando aparece, y ahí es donde el USB 2.0 puede dar tirones la primera vez que se entra a una zona.

### Pasos para instalarlas

Con **Dolphin cerrado** (reescribe los `.ini` al salir) y por SSH/SFTP a la IP de Linux (`ps4`/`ps4`):

```sh
# 1. Juego USA (desde el PC, por SFTP; sin comas ni paréntesis en el nombre)
#    emu/ROMS/GC/Legend of Zelda, The - The Wind Waker (USA).rvz
#    ->  /home/ps4/Juegos/Zelda-Wind-Waker-USA.rvz

# 2. Texturas: linux/texturas/GZL/  ->  ~/.local/share/dolphin-emu/Load/Textures/GZL/
mkdir -p ~/.local/share/dolphin-emu/Load/Textures/GZL

# 3. Activarlas y bajar el anisotrópico a 1x, solo en el USA (ver el GZLE01.ini de abajo)
```

En la interfaz es lo mismo, desde *Propiedades del juego*: *Anisotropic Filtering: 1x* y *Load Custom Textures* sí, *Prefetch Custom Textures* no.

Para comprobar que las coge basta con que Link se vea distinto (o mirar `~/.local/share/dolphin-emu/Logs/dolphin.log`). Si no cambia nada, casi siempre es que la carpeta no se llama exactamente `GZL` o que los `.dds` quedaron un nivel de más (`Load/Textures/GZL/GZL/...`).

### Aplicado el 14-09-2026, 00:15-00:30 (por SSH, con Dolphin cerrado)

- Partida europea guardada antes de cerrar (Shift+F1 → `StateSaves/GZLP01.s01`, 00:15) y Dolphin cerrado con Ctrl+Q. El segundo `xdotool` dio `BadWindow` porque la ventana ya se había cerrado: no es un error.
- Copia previa de la configuración en `~/.config/dolphin-emu.bak-2026-09-14`.
- `Legend of Zelda, The - The Wind Waker (USA).rvz` subido como `/home/ps4/Juegos/Zelda-Wind-Waker-USA.rvz`.
- Juego y `.tar` del conjunto de prueba (`Characters` + `Items`) verificados en la consola por SHA-1; el `.tar` se extrajo en `~/.local/share/dolphin-emu/Load/Textures/GZL/` y se borró.
- **Verificado en el pendrive tras el `sync`, con la caché vaciada** (02:15): `.rvz` USA con el SHA-1 del catálogo, y `GZL/` con 846 archivos, 419.597.016 B y el mismo hash conjunto que en el PC (`6961f340…`: SHA-1 de la lista de SHA-1 de cada archivo, ordenados por ruta con `LC_ALL=C`; se compara solo la columna del hash, porque el `sha1sum` de Git Bash pone `*` delante de la ruta y el de Linux no).

**El pendrive escribe a ~150 KB/s sostenidos** (medido en `/sys/block/sda/stat`, sin errores USB en `dmesg`, enlace a 480 Mb/s). Por SFTP los primeros ~700 MB llegan a 7-8 MB/s porque van a la caché de RAM; al llenarse (`Dirty` ≈ 1 GB) todo se frena al ritmo real del pendrive, y el `tar` extrae un archivo por minuto. Consecuencias:

- **No apagar Linux ni la consola mientras `grep Dirty /proc/meminfo` pase de unos MB**: lo copiado aún no está en el pendrive, y la partición no tiene journal.
- Un `sha1sum` justo después de subir lee de la caché, no del pendrive: comprueba la transferencia, no la escritura.
- No subir un `.tar` para extraerlo allí: duplica lo que hay que escribir. Mejor archivo a archivo, o subirlo a un USB aparte.
- **El pack entero (9,1 GB) a 150 KB/s son unas 17 horas de escritura**: con este pendrive no es viable. Hace falta un SSD o un pendrive con buena escritura sostenida.
- El `install-psxitarch.sh` de 1 h 40 min del 13-09 fue esto mismo.

Tiempos reales del 14-09: subida por SFTP del juego y del `.tar` hasta las 00:30; `tar` hasta las 01:11 (846 archivos, con `Dirty` clavado en ~990 MB todo el rato); `sync` hasta las 02:11. **Una hora y cuarenta minutos para ~1,3 GB.** Para esperar sin que se corte la sesión SSH, un script con `setsid nohup` que registra `dds` y `Dirty` cada minuto y hace el `sync` al final.

**La lectura, en cambio, va bien: 13 MiB/s** (SHA-1 del `.rvz` USA con la caché vaciada, `echo 1 > /proc/sys/vm/drop_caches`: 823 MiB en 61 s). Eso es lo que cuenta al jugar: un `.dds` de personaje, de 0,5 MB de media, se lee en unas centésimas. El pendrive es malo para copiar cosas, no necesariamente para cargar texturas.

**Todo por juego, sin tocar la configuración global ni la versión europea**: `~/.local/share/dolphin-emu/GameSettings/GZLE01.ini` activa las texturas y el anisotrópico a 1x solo en el USA, y copia del europeo el 16:9 y el desenfoque:

```ini
[Gecko_Enabled]
$16:9 Widescreen
[ActionReplay_Enabled]
$Remove Distance Blur
[Video_Settings]
AspectRatio = 1
HiresTextures = True
CacheHiresTextures = False
[Video_Enhancements]
MaxAnisotropy = 0
```

Los nombres de los códigos son iguales en `sys/GameSettings/GZLE01.ini` y `GZLP01.ini`, los dos verificados para RetroAchievements. Así el europeo sigue en 16x y sin texturas (las ignora porque `HiresTextures` está desactivado globalmente), y el USA las carga. Para quitarlo: `rm ~/.local/share/dolphin-emu/GameSettings/GZLE01.ini`.

### Resultado (14-09-2026, 18:40-19:10)

El primer arranque del USA salió en **4:3 con barras y sin texturas**: el `GZLE01.ini` estaba en `~/.config/dolphin-emu/GameSettings/`, que Dolphin no lee (ver arriba). Movido a `~/.local/share/dolphin-emu/GameSettings/`, el juego sale en 16:9 y **las texturas HD de personajes entran**: Link nítido a 1080p de cara y de espaldas.

Rendimiento, con las texturas activas y el contador de Dolphin (`ShowFPS`), leído con capturas de pantalla por SSH (`ffmpeg -f x11grab`, que sí incluye el OSD; la captura de Dolphin con F9 no lo lleva y sale a la resolución interna):

| Escena | fps |
|---|---|
| Interior (casa de la abuela), título | 29,9-30 |
| Outset mirando a la casa de Link | 29,98 |
| Outset, camino de la playa mirando al mar con toda la bahía | **25,2-27,2** |

Depende de lo que hay en pantalla: el mar y el horizonte con toda la isla son lo más caro del juego, y todo lo que se dibuja pasa por la CPU. En interiores va a velocidad completa; navegando es donde más se notará.

**Prueba A/B de los ajustes "de rendimiento"** que llevaba el `GZLP01.ini` de la interfaz (`ArbitraryMipmapDetection = False` y `EnableGPUTextureDecoding = True`), en la misma escena exacta (estado guardado en la ranura 2, cámara idéntica, Link quieto), 6 muestras en un minuto:

| | fps | Media |
|---|---|---|
| A: `GZLE01.ini` limpio | 26,36 · 27,17 · 26,49 · 27,20 · 26,78 · 27,02 | 26,8 |
| B: + los dos ajustes | 26,32 · 27,48 · 27,11 · 27,49 · 27,03 · 26,69 | 27,0 |

Diferencia dentro del ruido: **no dan rendimiento aquí**, y anulan lo que Dolphin fija para el juego. Se quedan fuera. El MSAA no se probó porque es GPU y el cuello es la CPU. Lo que movería estos fps es la frecuencia de la CPU, no ajustes de vídeo. CPU entre 72 y 76 °C durante todo esto, con `ps4-fan-threshold60` lanzado antes de Linux.

**Y la frecuencia lo resolvió** (19:18): con la CPU en P0 (2,1 GHz) por MSR, misma escena y mismo estado cargado:

| CPU | fps | Temp |
|---|---|---|
| 1,6 GHz (P2, como arranca) | 26,36 · 27,17 · 26,49 · 27,20 · 26,78 · 27,02 → 26,8 | 74-76 °C |
| **2,1 GHz (P0)** | 29,98 · 29,97 · 29,96 · 29,84 · 29,97 · 29,97 → **29,95** | 77-80 °C |

Velocidad completa en el peor caso. Detalle, script e iconos del escritorio en [`cpu/README.md`](cpu/README.md).

Para medir: `ffmpeg -loglevel error -y -f x11grab -video_size 1920x1080 -i :0 -frames:v 1 cap.png` y recortar el contador con `-vf 'crop=110:24:1810:36'`.

## Automatizar el juego por SSH: qué funciona y qué no

Probado el 16-09-2026 intentando llegar a una mazmorra sin jugar, para medir el rendimiento allí. **Se puede pulsar botones del juego por SSH; no se puede saltar de fase con los códigos de Dolphin.**

### Simular pulsaciones: sí, con dos condiciones

1. **El mando 1 tiene que estar mapeado a teclado, entero.** La sintaxis de Dolphin para combinar dos dispositivos en una misma acción (`` Buttons/X = `Button W` | `XInput2/0/Virtual core pointer:U` ``) **se acepta sin error pero no funciona**: el DualShock sigue respondiendo y el teclado no. Hay que poner `Device = XInput2/0/Virtual core pointer` y nombres de tecla a secas.
2. **Hay que mantener la tecla pulsada.** `xdotool key X` pulsa y suelta en unos 12 ms y Dolphin, que sondea a 60 Hz, se lo pierde. Lo que funciona es `xdotool keydown x; sleep 1; xdotool keyup x`.

Comprobado sin ambigüedad: con el mapeo de teclado y `keydown Return` durante un segundo, se abrió el menú de objetos del juego.

Mapeo de teclado usado (se restaura después con la copia de `GCPadNew.ini`): A=Espacio, B=B, X=U, Y=I, Z=P, Start=Return, cruceta=O/K/J/L, stick=W/A/S/D, L=Q, R=E.

### Saltar a una mazmorra: no, con este Dolphin

`sys/GameSettings/GZLE01.ini` trae 14 códigos *Test room* y un *Hidden dungeon* que cambian de fase escribiendo el nombre en `0x803C9D48` y una bandera en `0x803C9D44`; el activador es por botones (`8A3ED84A <máscara>`). Los nombres reales de las mazmorras están en el propio binario del juego (`M_NewD2` Dragon Roost, `kindan` Bosque Prohibido, `M_Dai` Templo de la Tierra, `kaze` Templo del Viento; se ven en el mapa de símbolos de `linux/src/Wind-Waker-60FPS-Hack/EXTRA STUFF/`).

Pero **ninguno de esos códigos se dispara en Dolphin 2509**, ni los míos ni los que trae Dolphin: con *Test room 1* habilitado y L+Z mantenido tres segundos, la pulsación llega (la cámara se reorienta, que es lo que hace Z) y la fase no cambia. Son códigos heredados de hace más de una década; el activador por botones de Action Replay parece no estar implementado ya.

Para medir en una mazmorra hacen falta otras vías: una partida guardada avanzada, o jugar hasta allí. Queda pendiente.

### Errores míos en esta prueba, para no repetirlos

| Error | Qué pasó | Cómo evitarlo |
|---|---|---|
| Copiar un código al apartado equivocado | Metí los códigos de salto en `[Gecko]` cuando el opcode `8A` es de **Action Replay**. El manejador de códigos de Gecko intentó ejecutarlos y el juego murió con *"Invalid read from 0x00000000, PC = 0x80001f00"*. Perdí dos intentos creyendo que fallaba el salto | Mirar en qué sección del INI vive el código antes de copiar su formato. Un `PC` dentro de `0x80001800-0x80002000` señala al manejador de Gecko, no al juego |
| Dar por buena la sintaxis `\|` entre dispositivos | Falla en silencio: ni error ni aviso | Comprobar siempre el efecto en pantalla con algo inequívoco (Start abre el menú) antes de seguir construyendo encima |
| `xdotool key` para pulsar un botón | Demasiado corto para el sondeo de Dolphin | `keydown` + `sleep` + `keyup` |
| Heredocs (`<<'PY'`) a través de `tools/ps4linux.py` | El texto llega literal y no se ejecuta; la orden parece funcionar y no hace nada | Subir el script con `--put` y ejecutarlo, o editar desde el PC por SFTP |
| `sed -i` para editar los INI | Varias veces no cambió nada, sin error | Verificar el archivo después de cada edición; para INI, mejor Python por SFTP |
| Órdenes compuestas muy largas por SSH | Algunas no llegaron a ejecutarse y no dieron salida | Partirlas y comprobar el resultado de cada parte |

Ver también el error de la ruta de `GameSettings` (arriba) y el de medir con el juego en pausa (abajo): ambos costaron una conclusión equivocada antes de detectarlos.

## El hack de 60 fps: no

`linux/src/Wind-Waker-60FPS-Hack/` (submódulo desde el 15-09, [Meowmaritus](https://github.com/Meowmaritus/Wind-Waker-60FPS-Hack), 2016-2017) son 39 códigos Gecko `FPSHack_*` que hacen correr *Wind Waker* a 60 fps. Es **solo para la versión USA** (`GZLE01`), que es justo la que tenemos con las texturas.

**El motivo de fondo para descartarlo es la CPU, no el software.** El hack exige *CPU Clock Override* **al 200 %**: el PowerPC emulado ejecuta el doble de instrucciones por segundo, porque el bucle del juego pasa de 30 a 60 Hz. Es decir, **hace falta el doble de CPU anfitriona**. Lo que tenemos, medido en la escena de la playa de Outset:

| | |
|---|---|
| A 1,593 GHz (P2) | 26,8 fps — por debajo del tope, así que ahí la CPU está saturada |
| A 2,092 GHz (P0) | 29,95 fps — en el tope de 30 |
| Capacidad estimada a 2,1 GHz | 26,8 × (2,092 / 1,593) = **~35 fps**, y es una cota superior: la latencia de memoria no escala con el reloj |

O sea, **un 17 % de margen sobre los 30 fps, cuando hacen falta un 100 %.** Nos quedamos cortos por un factor de ~1,7. El resultado esperado serían unos 35 fps de los 60, es decir el juego a poco más de la mitad de velocidad, que es justo el *"super slowmo"* del que avisa el autor. **Medido el 16-09 y confirmado: 33 fps** (ver abajo).

Y el margen no se puede sacar de los gráficos: el cuello es el hilo de emulación de la CPU (Dolphin usa ~1,5 núcleos de los 8; los otros 6 no ayudan, porque el PowerPC se emula en un solo hilo). Bajar la resolución interna, el MSAA o las texturas alivia la GPU, que ya va sobrada. Y 2,1 GHz es el P-state máximo (P0): no hay más reloj que pedir.

A esto se suma que **rompe la partida**. El propio README lista bloqueos sin salida: Niko no llega a la plataforma en el barco (principio del juego), el slime del Templo de la Tierra se libera antes de tiempo, y la sala de Molgera se cuelga en negro. Los enemigos, además, atacan el doble de a menudo.

**Corrección (15-09):** en la primera versión de esta nota puse que el *CPU Clock Override* ya no funcionaba en las versiones nuevas de Dolphin. **Es falso.** Lo decía el README del hack refiriéndose a 5.0-4792, un fallo de 2017 que se arregló: en Dolphin actual sigue existiendo como `OverclockEnable` / `Overclock` en `[Core]`, y admite valor por juego desde el INI. Ese motivo no vale; el que manda es el de la CPU.

### Estado del hack en internet (revisado el 16-09-2026)

Buscado a fondo para descartar que hubiera algo más nuevo o mejor. No lo hay:

- **El repositorio original está abandonado desde 2017.** 7 commits, 34 estrellas, 1 incidencia abierta, 0 *pull requests*. El aviso de copyright dice "Meowmaritus 2016-2017" y el README no menciona ningún sucesor.
- **El único fork reciente no aporta nada.** [`EleventhLucas/Wind-Waker-FPS-Hacks`](https://github.com/EleventhLucas/Wind-Waker-FPS-Hacks), creado el 14-08-2026, se anuncia como "parches para *Wind Waker* a distintas tasas de refresco, arreglando el código que depende de la tasa"; pero su README es **copia literal del original**, con los mismos tres bloqueos sin salida y la misma firma de Meowmaritus. Sin commits propios.
- **No existe versión PAL** de este hack ni de ningún otro equivalente, en ningún sitio.
- **El *clock override* sigue vivo** en Dolphin moderno (`OverclockEnable` / `Overclock` en `[Core]`, también por juego desde el INI). Lo del 5.0-4792 fue un fallo puntual de 2017.
- La referencia que maneja la comunidad para mover *Wind Waker* a 60 fps es **un x86 moderno rápido de un solo hilo**, tipo i3 Skylake o Haswell bien subido. Los Jaguar de la PS4 a 2,1 GHz son una arquitectura de bajo consumo de 2013, muy por debajo de eso.

### La versión europea (`GZLP01`): no, y no es cuestión de probar

Los 39 códigos son direcciones absolutas del binario USA (`C2006410`, `C20251A0`, … `C25F0228`): cada uno inyecta código en una función concreta de `GZLE01`. La compilación PAL coloca esas mismas funciones en **otras direcciones**, así que aplicarlos al europeo no daría 60 fps: parchearía instrucciones al azar y lo más probable es que se cuelgue. Por eso el autor escribe que *"no es compatible con ninguna otra región del juego"*.

Portarlo significaría localizar las 39 funciones en el binario PAL —con el mapa de símbolos que viene en `EXTRA STUFF`, que es del USA— y reescribir cada código. Es trabajo de ingeniería inversa, no de configuración, y aun así chocaría con el mismo muro de CPU.

### Medido el 16-09-2026: confirmado, no llega

Dos pruebas en la consola, con el pack de texturas puesto, la CPU a 2,1 GHz y el estado guardado de la playa de Outset (ranura 2), para no depender de estimaciones:

| Prueba | Configuración | fps | Lectura |
|---|---|---|---|
| **A — capacidad real** | `EmulationSpeed = 0.0` (sin límite) | 32,2 · 34,4 · 33,9 · 34,8 · 28,9 | **~33 fps de un juego de 30 → 110 % de tiempo real** |
| **B — reloj emulado al doble** | `OverclockEnable = True`, `Overclock = 2.0`, sin límite | 27,4 · 34,6 · 27,8 · 27,7 · 33,8 · 27,6 | ~30 fps: el *overclock* solo cuesta un **10 %** |

**La prueba A es la que decide.** La capacidad de esta consola es del **110 % del tiempo real** con *Wind Waker* a 30 Hz. El hack lo pone a 60 Hz, o sea **200 %**. Con el hack instalado saldrían unos 33 fps de los 60: el juego a la mitad de velocidad, en cámara lenta. La estimación previa (~35 fps) se confirmó con dos décimas de diferencia.

La prueba B sale engañosamente barata y conviene entender por qué, para no sacar la conclusión contraria: subir el reloj emulado **sin** el hack no duplica el trabajo, porque el juego sigue a 30 Hz y lo único que hace es terminar antes su cálculo y quedarse esperando el barrido de pantalla; Dolphin detecta esos bucles de espera y los salta. El coste real llega cuando el bucle del juego corre 60 veces por segundo, que es lo que hacen los códigos Gecko, y eso es lo que no cabe en el 110 %.

Método: `ffmpeg -f x11grab` para leer el contador, y `top` para la CPU, que llegó al 200 % (dos núcleos saturados: el hilo de emulación y el de GPU) a 61-68 °C. La configuración se restauró al terminar.

Mientras tanto se queda en el repo como referencia: los `.asm` comentados y el mapa de símbolos demangled de *Wind Waker* (2 MB, en `EXTRA STUFF`) son buen material si algún día hace falta trastear con la memoria del juego. Para jugar, **30 fps con las texturas HD**, que es el ritmo para el que se hizo.

Si aun así se quiere probar: los códigos van al `[Gecko]` de `~/.local/share/dolphin-emu/GameSettings/GZLE01.ini` y se activan en `[Gecko_Enabled]`; hay que **desactivar los demás códigos de inyección ASM** (el hack agota el espacio que Gecko reserva para el código inyectado), lo que incluye el *16:9 Widescreen* que tenemos puesto.

## Reglas de configuración: qué se lee, dónde y cuándo

Casi todos los errores de configuración de este proyecto han sido de *sitio* (editar el archivo que Dolphin no mira) o de *momento* (editarlo cuando Dolphin lo va a sobrescribir). Esto es lo aprendido, puesto como referencia.

### Los tres niveles, y cuál gana

| Nivel | Dónde | Qué es |
|---|---|---|
| Global | `~/.config/dolphin-emu/` → `Dolphin.ini`, `GFX.ini`, `GCPadNew.ini` | Lo que vale para todos los juegos |
| Del juego, de fábrica | `sys/GameSettings/` de la instalación → `GZL.ini`, `GZLE01.ini`, `GZLP01.ini` | Lo que Dolphin sabe que este juego necesita, más su lista de códigos. **No editar**: se pierde al actualizar el paquete y además está bien |
| Del juego, nuestro | `~/.local/share/dolphin-emu/GameSettings/<ID>.ini` | Lo único que tocamos por juego. **Gana sobre los dos anteriores** |

Dolphin carga el INI de **3 letras y el de 6**: para `GZLE01` lee `GZL.ini` y `GZLE01.ini`, en los dos niveles. Por eso los ajustes de fábrica del juego están en `GZL.ini` y valen para las dos regiones. Un `~/.local/share/dolphin-emu/GameSettings/GZL.ini` nuestro sería la forma de poner algo común al europeo y al USA (igual que la carpeta de texturas se llama `GZL`); aquí no se ha usado: cada versión tiene su INI de 6 letras porque llevan cosas distintas.

### Los nombres de las secciones **no** son los mismos arriba y abajo

Este es el fallo silencioso más fácil de cometer: copiar una clave de `GFX.ini` al INI del juego tal cual. No da error, simplemente no hace nada.

| En `GFX.ini` (global) | En el INI del juego | Claves que usamos |
|---|---|---|
| `[Settings]` | `[Video_Settings]` | `InternalResolution`, `MSAA`, `AspectRatio`, `HiresTextures`, `CacheHiresTextures`, `ShaderCompilationMode` |
| `[Enhancements]` | `[Video_Enhancements]` | `MaxAnisotropy`, `ForceFiltering` |
| `[Hacks]` | `[Video_Hacks]` | `EFBAccessEnable`, `EFBToTextureEnable` (los que fija el juego) |
| `[Hardware]` | `[Video_Hardware]` | `VSync` |
| `[Core]` de `Dolphin.ini` | `[Core]` (igual) | `CPUThread`, `OverclockEnable`, `Overclock`, `EmulationSpeed` |

Los apartados de códigos (`[Gecko]`, `[Gecko_Enabled]`, `[ActionReplay]`, `[ActionReplay_Enabled]`) solo existen en el INI del juego.

### Cuándo se relee cada cosa

| Qué se cambia | Qué hace falta para que surta efecto |
|---|---|
| INI del juego: códigos, texturas, aspecto, *overclock* | **Stop y volver a lanzar el juego.** No hace falta cerrar Dolphin |
| `GFX.ini`, `Dolphin.ini`, `GCPadNew.ini` a mano | **Dolphin cerrado antes de editar.** Al salir los reescribe enteros con lo que tiene en memoria y se lleva por delante la edición |
| Cualquier cosa desde la interfaz | Al momento, y se guarda al salir |

Dolphin solo reescribe los `.ini` si algo cambió durante la sesión; aun así, la regla práctica es no editarlos nunca con Dolphin abierto.

### Números que no se entienden solos

| Clave | Qué significa el número |
|---|---|
| `MaxAnisotropy` | 0 = 1x, 1 = 2x, 2 = 4x, 3 = 8x, 4 = 16x. **No** son las veces |
| `AspectRatio` | 0 = Auto, 1 = forzar 16:9, 2 = forzar 4:3, 3 = estirar |
| `ShaderCompilationMode` | 0 = síncrona, 1 = ubershaders síncronos, 2 = **ubershaders híbridos** (el nuestro), 3 = asíncrona saltando dibujado |
| `InternalResolution` | múltiplo de la nativa: 3 = 3x ≈ 1080p |
| `MSAA` | número de muestras; 1 = sin AA. Dolphin lo guarda en hexadecimal (`0x00000004` = 4x) y lo lee también en decimal |
| `SIDevice0` | 6 = mando estándar en el puerto 1 |
| `EmulationSpeed` | 1.0 = velocidad normal, **0.0 = sin límite** (solo para medir, ver el protocolo) |

### Códigos: lo que hay que cumplir para que uno se active

1. `EnableCheats = True` en `Dolphin.ini [Core]`. Es **global**: sin eso no se aplica ningún código de ningún juego, por muy habilitado que esté en su INI.
2. El código, en **su** apartado: los Gecko (`04…`, `C2…`) en `[Gecko]`, los de Action Replay en `[ActionReplay]`. Mezclarlos no da error de sintaxis, revienta en ejecución (ver "Errores míos en esta prueba", arriba).
3. El nombre en `[Gecko_Enabled]` / `[ActionReplay_Enabled]`, con `$` delante y **exactamente igual** al del apartado del código o al que trae el `sys/GameSettings`; un espacio o una tilde de más y no se activa, sin aviso.
4. *Stop* y relanzar el juego: la lista se lee al arrancar.
5. Los Gecko de inyección de código (`C2…`) comparten un espacio reservado limitado: varios a la vez se pisan. Por eso el hack de 60 fps exigiría quitar el *16:9 Widescreen*.

### Lo que no se toca en esta consola

| Ajuste | Por qué |
|---|---|
| `EFBAccessEnable`, `EFBToTextureEnable`, `VISkip`, `ArbitraryMipmapDetection`, `EnableGPUTextureDecoding` | Los fija el `GZL.ini` de fábrica porque el juego los necesita. Los dos últimos, probados en A/B el 14-09: no dan fps |
| DSP **LLE** | HLE en su hilo es lo que hace que quepa. LLE emula el DSP instrucción a instrucción: es CPU, que es justo lo que falta |
| **Dual Core** (`CPUThread = False`) | Recurso típico para arreglar cuelgues en otros juegos; aquí partiría el rendimiento por la mitad. Antes de desactivarlo, probar todo lo demás |
| **MMU** | Solo lo piden unos pocos juegos y cuesta mucha CPU |
| **SSAA** | Cuadruplica el coste por píxel. MSAA sí, que en esta GPU es casi gratis |
| *Online Updater* de Dolphin, o actualizar el paquete | La distro está clavada al archivo de Arch del 09-03-2026 (ver [`README.md`](README.md)); además, cambiar de versión de Dolphin invalida los estados guardados |

**Ojo con los iconos de juego del escritorio:** lanzan `dolphin-emu -b -e <imagen>`, y `-b` es *batch*, es decir **sin ventana principal**. La receta de cerrar por SSH con *Ctrl+Q* en la ventana principal y *Alt+Y* en el diálogo supone Dolphin abierto de la forma normal, con sus dos ventanas. Lanzado desde el icono del juego solo debería estar la de render (es lo que significa la opción; **sin comprobar en la consola**): conviene mirar qué ventanas hay con `xdotool search --name Dolphin` y cómo se cierra esa, **antes** de necesitarlo con una partida sin guardar.

## Protocolo de pruebas en la consola

Medir aquí es fácil de hacer mal: hay un tope de 30 fps que disimula cualquier diferencia, una CPU que arranca a otra frecuencia, un pendrive lento y un escritorio que se comparte por VNC. Esta es la rutina que hace comparables dos medidas.

### Antes de medir, en este orden

1. **Pedir la consola.** Es de uno: si hay otra sesión trabajando en ella, esperar. Tocarla lo decide Javi.
2. **`ps4-fan-threshold60.bin` en Payload Guest, antes de arrancar Linux.** Sin él, a 2,1 GHz se llega a 80 °C y el Syscon acaba apagando la consola.
3. **CPU a 2,1 GHz**: icono *CPU 2,1 GHz — Rendimiento*, o `ps4-cpu rendimiento`; comprobar con `ps4-cpu estado`. Arrancando por Payload Guest la CPU viene en P2 (1,6 GHz) y **todas las cifras salen un 12 % bajas**; por BinLoader ya viene en P0.
4. **Visor VNC desconectado.** x11vnc lee la pantalla a base de sondeos y gasta la CPU que se está midiendo ([`vnc.md`](vnc.md)).
5. **Nada copiando al pendrive.** Escribe a 1,7 MB/s: una subida por SFTP en marcha falsea la prueba entera.
6. **Cargar siempre el mismo estado guardado**, con el personaje quieto y la cámara idéntica.
7. **Descartar la primera pasada** por una zona: ahí se compilan los shaders y se leen por primera vez las `.dds` del pendrive. Se mide a partir de la segunda.
8. **Al menos cinco muestras**, y apuntarlas una a una, no solo la media: la dispersión dice tanto como el valor (en la prueba del reloj emulado del 16-09 alternaban 27,4 y 34,6, y esa bimodalidad era el dato).

### Cómo se lee el número

```sh
# fotograma completo (para ver qué había en pantalla) y recorte del contador
ffmpeg -loglevel error -y -f x11grab -video_size 1920x1080 -i :0 -frames:v 1 escena.png
ffmpeg -loglevel error -y -f x11grab -video_size 1920x1080 -i :0 -frames:v 1 -vf 'crop=110:24:1810:36' fps.png
```

- El contador es el `ShowFPS` de Dolphin, arriba a la derecha, y solo sale en una captura **de la pantalla X**. La captura propia de Dolphin (F9) **no lleva el OSD** y además sale a la resolución interna: no sirve para medir.
- **Guardar siempre el fotograma completo, no solo el recorte.** El recorte no distingue el juego corriendo de una pausa, de un menú abierto o de un diálogo de Dolphin tapando la escena; más de una conclusión falsa ha salido de un número creíble sobre una pantalla que no era la que se creía.
- A la vez, CPU y temperatura: `top -bn1 | head` (el hilo de emulación y el de GPU saturados son ~200 %) y `cat /sys/class/hwmon/hwmon*/temp1_input`.

### Los seis errores que ya han falseado una medida

| Error | Cómo se nota | Qué hacer |
|---|---|---|
| **Medir contra el tope de 30 fps** | Sale 29,9x en las dos ramas del A/B y se concluye "no hay diferencia" | Si el número roza 30, se está midiendo el limitador, no la máquina. Para capacidad, `EmulationSpeed = 0.0`, y devolverlo a `1.0` al terminar |
| **Medir con la CPU en P2** | Todo un 12 % bajo, de forma coherente | `ps4-cpu estado` antes de empezar |
| **Medir con el visor VNC conectado** | Fps más bajos y más irregulares | Desconectar el visor; para mirar sin medir da igual |
| **Medir solo el recorte del contador** | Un número perfectamente creíble de una escena que no es | Capturar también el fotograma entero |
| **Medir la primera pasada por la zona** | Bajones que no se repiten después | Entrar, salir y volver antes de contar |
| **Comparar en escenas distintas** | Diferencias grandes que no vienen del ajuste | Estado guardado, cámara quieta, la escena patrón |

### La escena patrón y las cifras conocidas

La referencia del proyecto es el **estado de la ranura 2 del USA (`StateSaves/GZLE01.s02`): playa de Outset mirando al mar**, con toda la bahía y el horizonte en pantalla, que es lo más caro que se ha encontrado en el juego. **No guardar encima de esa ranura** (la 1 es la partida europea del 13-09).

| Escena | Condiciones | fps |
|---|---|---|
| Interior (casa de la abuela), título | texturas HD, 1,6 GHz | 29,9-30 |
| Outset mirando a la casa de Link | texturas HD, 1,6 GHz | 29,98 |
| **Playa de Outset mirando al mar** | texturas HD, 1,6 GHz (P2) | 26,8 (26,36-27,20) |
| **Playa de Outset mirando al mar** | texturas HD, 2,1 GHz (P0) | **29,95** (29,84-29,98) |
| Playa de Outset, **sin límite de velocidad** | texturas HD, 2,1 GHz | ~33 → **capacidad = 110 % del tiempo real** |

Cifras que acompañan a una medida buena: memoria de Dolphin 526 MB sin texturas y **1,98 GB con el pack entero** (de 5,9 GiB totales), CPU al 150 % jugando y hasta 200 % sin límite, temperatura 62-65 °C con el pack a 2,1 GHz y 77-80 °C en las pruebas largas.

**Sin medir todavía:** navegando en barco y dentro de una mazmorra, los dos escenarios que faltan por ver y los candidatos a ser peores que la playa. Llegar allí sin jugar no se pudo (arriba); hará falta una partida avanzada o jugar hasta ahí. Tampoco está hecha la comparación OpenGL frente a Vulkan, que sí es un A/B con sentido porque cambia el hilo de GPU y el coste de compilar shaders.

### Qué anotar de cada prueba

Fecha y hora, versión del juego (`GZLE01` / `GZLP01`), frecuencia de la CPU, backend, si estaban las texturas, el estado guardado usado, **las muestras una a una**, temperatura y CPU, y qué se restauró al terminar. Sin la frecuencia y el estado guardado, una medida no se puede comparar con nada.

### Antes de dar por buena una conclusión

- **Cambiar un ajuste de GPU y no ver diferencia no significa que el ajuste no haga nada**: significa que el cuello es la CPU, que es lo que pasa aquí con MSAA, resolución interna y anisotrópico. Esos se prueban para ver si **rompen algo** o para ganar imagen, no para ganar fps.
- **Lo que mueve los fps en esta consola es la frecuencia de la CPU**, y poco más. Antes de montar un A/B de vídeo, preguntarse si el ajuste toca el hilo de emulación.
- **Un resultado que sale demasiado barato hay que explicarlo**, no celebrarlo: el *overclock* al 200 % costó solo un 10 % porque el juego seguía a 30 Hz y Dolphin salta los bucles de espera. Sin esa explicación, la conclusión habría sido la contraria.
- **Deshacer siempre lo que se tocó para medir** (`EmulationSpeed`, *overclock*, mando mapeado a teclado, códigos de prueba) y dejarlo dicho por escrito. Que conste es parte del resultado.

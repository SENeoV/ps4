# Dolphin en la PS4 — configuración y *Wind Waker*

Dolphin **2509** (paquete `dolphin-emu 1:2509-1` de Arch, instalado sin red desde `linux/pkgs/`) sobre el Arch de `linux/distros/` (Mesa 25.1, RADV), kernel 5.4.247, en la PS4 Pro CUH-7116B (Baikal B1). Primer juego: *The Legend of Zelda: The Wind Waker* (Europe, `GZLP01`, RVZ), el 13-09-2026, **a 30 fps (velocidad completa) con Vulkan**, 3x de resolución interna, y bajones a 23-24 fps en cinemáticas por la compilación de shaders.

Hardware visto desde Linux: 8 núcleos Jaguar **a 1,6 GHz al arrancar, 2,1 GHz con [`cpu/ps4-cpu`](cpu/README.md)** (icono *Rendimiento* en el escritorio; pulsarlo antes de Dolphin en cada arranque), GPU "AMD Radeon Graphics (RADV LIVERPOOL)", Vulkan 1.3 (RADV) y OpenGL 4.6 (radeonsi), 5,8 GiB de RAM con el payload de 2 GB de VRAM. **El cuello de botella es la CPU**: la GPU tiene margen para resolución y antialiasing, la CPU no lo tiene para compilar shaders ni para juegos exigentes.

Los archivos viven en `/home/ps4/.config/dolphin-emu/`: `Dolphin.ini` (general), `GFX.ini` (gráficos), `GCPadNew.ini` (mando). Dolphin los reescribe al cerrarse: **editarlos solo con Dolphin cerrado**.

**Los ajustes por juego van en otro sitio: `~/.local/share/dolphin-emu/GameSettings/<ID>.ini`** (es donde Dolphin los escribe desde *Properties*). Un `GameSettings/` dentro de `~/.config/dolphin-emu/` **no lo lee**: los `GZLP01.ini` y `GZLE01.ini` que se escribieron ahí el 13 y el 14-09 nunca se aplicaron (comprobado el 14-09: el juego salía en 4:3 y sin texturas). Dolphin los lee al arrancar cada juego, así que un cambio necesita *Stop* y volver a lanzar, no cerrar Dolphin.

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

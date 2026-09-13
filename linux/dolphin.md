# Dolphin en la PS4 — configuración y *Wind Waker*

Dolphin **2509** (paquete `dolphin-emu 1:2509-1` de Arch, instalado sin red desde `linux/pkgs/`) sobre el Arch de `linux/distros/` (Mesa 25.1, RADV), kernel 5.4.247, en la PS4 Pro CUH-7116B (Baikal B1). Primer juego: *The Legend of Zelda: The Wind Waker* (Europe, `GZLP01`, RVZ), el 13-09-2026, **a 30 fps (velocidad completa) con Vulkan**, 3x de resolución interna, y bajones a 23-24 fps en cinemáticas por la compilación de shaders.

Hardware visto desde Linux: 8 núcleos Jaguar **a 1,59 GHz** (no a los 2,13 de la Pro; ver `README.md`, "Registro"), GPU "AMD Radeon Graphics (RADV LIVERPOOL)", Vulkan 1.3 (RADV) y OpenGL 4.6 (radeonsi), 5,8 GiB de RAM con el payload de 2 GB de VRAM. **El cuello de botella es la CPU**: la GPU tiene margen para resolución y antialiasing, la CPU no lo tiene para compilar shaders ni para juegos exigentes.

Los archivos viven en `/home/ps4/.config/dolphin-emu/`: `Dolphin.ini` (general), `GFX.ini` (gráficos), `GCPadNew.ini` (mando), `GameSettings/<ID>.ini` (por juego, se crea desde *Properties*). Dolphin los reescribe al cerrarse: **editarlos solo con Dolphin cerrado**.

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
| Texturas HD (*Hypatia WWHD*, 1,9 GB en Descargas) | *Graphics → Advanced → Load Custom Textures* | — | **No ahora**: desde un pendrive a USB 2.0 daría tirones al cargar y 1,9 GB de DDS piden el payload de 3-4 GB. Con SSD, sí |

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

Trucos de manejo remoto que sirvieron: Dolphin no tiene control remoto, pero con `xdotool` (`DISPLAY=:0`) se le mandan atajos: *Shift+F1* guarda estado en la ranura 1 (queda en `~/.local/share/dolphin-emu/StateSaves/GZLP01.s01`, se carga con F1) y *Ctrl+Q* en la ventana principal (no en la de render) lo cierra, previo diálogo *Confirm* que se acepta con *Alt+Y*. Dolphin solo reescribe los `.ini` si algo cambió.

## Cómo aplicar los cambios (a mano)

Con Dolphin cerrado, por SSH (`ps4`/`ps4`, IP por la MAC del Wi-Fi) o en LXTerminal:

```sh
cd ~/.config/dolphin-emu
sed -i 's/^VSync = .*/VSync = False/' GFX.ini
sed -i 's/^MSAA = .*/MSAA = 4/' GFX.ini
grep -q ShaderCompilationMode GFX.ini || sed -i '/^\[Settings\]/a ShaderCompilationMode = 2\nWaitForShadersBeforeStarting = True' GFX.ini
grep -q EnableCheats Dolphin.ini || sed -i '/^\[Core\]/a EnableCheats = True' Dolphin.ini
mkdir -p GameSettings && printf '[Gecko_Enabled]\n$16:9 Widescreen\n' > GameSettings/GZLP01.ini
```

y el `GCPadNew.ini` de arriba tal cual. Después, arrancar el juego una vez y esperar la compilación inicial de shaders (una barra al principio); las siguientes veces sale de la caché.

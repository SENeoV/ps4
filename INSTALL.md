# Instalación en la PS4 (vía FTP / FileZilla)

Procedimiento para instalar RetroArch y validar la cadena completa con una ROM de NES o SNES.

## Mapeo de carpetas: importante

`emu/` **no se copia tal cual** a la consola. Cada subcarpeta tiene su destino:

| En el PC | En la PS4 | Notas |
|---|---|---|
| `emu/APPS/*.pkg` | `/data/pkg/` | Es la ruta donde el instalador los detecta. Temporal: tras instalar se pueden borrar |
| `emu/BIOS/*` | `/data/retroarch/system/` | **Ruta obligatoria.** Es la carpeta "system" de RetroArch |
| `emu/ROMS/<SISTEMA>/` | `/data/roms/<SISTEMA>/` | RetroArch puede navegar a cualquier ruta; `/data/roms` mantiene el mismo esquema que el PC |

La carpeta `/data/retroarch/` no existirá hasta que RetroArch se haya ejecutado al menos una vez.

## Antes de empezar

1. Cargar **GoldHEN** en la consola (hay que hacerlo tras cada reinicio, no es CFW permanente).
2. Activar el **servidor FTP** desde el menú de GoldHEN.
3. Anotar la IP de la PS4 (Ajustes → Red → Ver estado de la conexión).

En FileZilla:

```
Servidor:  <IP de la PS4>
Puerto:    2121
Modo:      anónimo, sin usuario ni contraseña
```

Conviene poner FileZilla en **modo pasivo** y **1 sola conexión simultánea** — el FTP de GoldHEN es frágil con transferencias en paralelo y el Core Installer son 1,4 GB.

## Paso 1 — RetroArch (la app)

1. Subir por FTP a `/data/pkg/`:
   ```
   emu/APPS/PS4_SSNE10000_v4.00_Unofficial_RetroArch.pkg   (27 MB)
   ```
2. En la consola: **Ajustes → Debug Settings → Game → Package Installer**, seleccionar el PKG e instalar.
3. Comprobar que aparece el icono de RetroArch en el menú principal.
4. **Abrir RetroArch una vez** y cerrarlo. Esto crea `/data/retroarch/`, que hace falta para los pasos siguientes.

## Paso 2 — Core Installer

RetroArch en PS4 **viene sin cores**: sin este paso se abre pero no ejecuta nada.

1. Subir a `/data/pkg/`:
   ```
   emu/APPS/PS4_SSNE20000_v4.00_RetroArch_Core_Installer.pkg   (1385 MB)
   ```
   Es una subida larga. Si FileZilla corta a mitad, reanudar en vez de reiniciar.
2. Instalar igual que el paso 1.
3. Ejecutar la app **Core Installer** desde el menú de la PS4 e instalar los cores.

Alternativa sin esta app: *Core Updater* desde dentro de RetroArch (requiere que la consola tenga red).

## Paso 3 — ROM de prueba

Se empieza por NES o SNES a propósito: **no necesitan BIOS**, así que si algo falla, el fallo está en RetroArch o el core, no en una BIOS mal nombrada.

1. Subir la ROM a `/data/roms/NES/` (o `/data/roms/SNES/`).
2. En RetroArch: **Load Content** → navegar a esa ruta → seleccionar la ROM.
3. Elegir el core:
   - NES → *Nestopia* o *QuickNES*
   - SNES → *Snes9x*

## Paso 4 — Validación

La cadena está bien si:

- [ ] RetroArch arranca
- [ ] Aparecen cores en la lista (si está vacía, falló el paso 2)
- [ ] La ROM carga y se ve imagen
- [ ] Hay sonido
- [ ] El mando responde
- [ ] Guardar y cargar un save state funciona

Con eso validado, ya se puede meter contenido en volumen y pasar a los sistemas que sí necesitan BIOS.

## Si algo falla

| Síntoma | Causa habitual |
|---|---|
| RetroArch no aparece tras instalar | GoldHEN no estaba activo al instalar |
| Abre pero no hay cores | Falta el paso 2 |
| El core carga pero la ROM no | Extensión no soportada, o ROM comprimida en un formato que el core no lee |
| Va a tirones | Core pesado para el sistema; probar el alternativo (QuickNES en vez de Nestopia) |
| El FTP corta | Modo pasivo y una sola conexión simultánea |

## Fuentes

- [Files and Directories — ConsoleMods](https://consolemods.org/wiki/PS4:Files_and_Directories)
- [How To Install PS4 FPKGS on GoldHEN](https://github.com/DrYenyen/How-To-Install-PS4-FPKGS)
- [RetroArch en PS4: instalación y configuración](https://bytesnbits.co.uk/play-real-arcade-and-console-games-on-the-ps4-with-retroarch-full-installation-and-setup/)
- [PS4 RetroArch Port — GBAtemp](https://gbatemp.net/threads/release-ps4-retroarch-port-unofficial.555028/)

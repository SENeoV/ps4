# pkg/payloads — payloads para Payload Guest

Copia de todo lo que sirve el host web de ArabPixel ([webkitty.arabpixel.net](http://webkitty.arabpixel.net/), la referencia que usa la guía de Linux), bajado el 13-09-2026 de `includes/payloads/` con la lista y las compatibilidades de su `payloadsList.js`. Los `.bin` de esta carpeta van a **`/data/payloads/`** de la consola y los lista [Payload Guest](https://github.com/Al-Azif/ps4-payload-guest) (`pkg/utils/PS4_AZIF00003_v0.98_Payload_Guest.pkg`), que se los pasa al BinLoader de GoldHEN. Así se lanza cualquiera con el mando, sin PC. Payload Guest solo lista `.bin` en la raíz; no lee subcarpetas, y un `meta.json` sin el campo `icon` lo rompe (probado), así que no hay `meta.json`.

Los `.bin` de Linux son los del zip del loader v25 (`linux/loader/`); comprobado que los `.elf` del host son byte a byte los del zip.

## Linux (loader v25, firmware 5.05–13.52, detecta southbridge y Pro)

| Archivo | VRAM | Para qué |
|---|---|---|
| `linux-1024mb.bin` | 1 GB | Instalar y primer arranque (la distro se copia a RAM) |
| `linux-2048mb.bin` | 2 GB | **Uso normal**: escritorio y emuladores |
| `linux-3072mb.bin`, `linux-4096mb.bin` | 3-4 GB | Juegos con mucha VRAM; quedan 5 o 4 GB de RAM |
| `linux-32mb.bin` … `linux-512mb.bin` | 32-512 MB | Servidor sin gráficos. Con 32 o 64 hay pantallas que no dan imagen; 128 es el mínimo razonable |

## Herramientas (sin restricción de firmware según el host)

| Archivo | Nombre en el host | Autor | Qué hace |
|---|---|---|---|
| `ps4-ftp.bin` | FTP | Scene Collective | Servidor FTP. Redundante con el de GoldHEN (2121) |
| `ps4-disable-updates.bin` | Disable-Updates | Scene Collective | Bloquea las actualizaciones del sistema. Redundante con GoldHEN |
| `ps4-fan-threshold60/70/80/85.bin` | Fan-Threshold | Scene Collective | Temperatura a la que el ventilador entra en turbo (60, 70, 80 u 85 °C) |
| `ps4-history-blocker.bin` | History-Blocker | Stooged | El navegador no vuelve a la última página al abrirse. Otra vez para desactivar |
| `np-fake-signin-ps4.bin` | NP Fake Signin | earthonion | Marca PSN como "conectado" tras una activación falsa. Es un `.elf` renombrado |
| `ps4-backup.bin` / `ps4-restore.bin` | Backup-DB / Restore-DB | Stooged | Copia y restaura bases de datos, licencias y datos de usuario |
| `db-rebuilder-v0.1.bin` | DB-Rebuilder | 4GAMER | Reconstruye la base de datos de fPKG: devuelve los iconos de homebrew al menú |
| `ps4-exit-idu.bin` | ExitIDU | Scene Collective | Sale del modo tienda (IDU) y reinicia |
| `ps4-app2usb.bin` | App2USB | Stooged | Mueve aplicaciones instaladas a un USB externo |
| `ps4-app-dumper.bin` | App Dumper | — | Vuelca juegos instalados a USB (no aparece en la lista del host, pero está en `payloads.js`) |
| `ps4-websrv.bin` | PS4-Websrv | ArabPixel | Servidor web en el puerto 80 de la PS4 para cargar payloads desde otros dispositivos |
| `ps4-pup-decrypt.bin` | PUP-Decrypt | andy-man | Descifra un PUP de firmware |
| `ps4-module-dumper.bin` | Module-Dumper | — | Vuelca a USB los módulos descifrados de `/system`, `/system_ex`, `/update` |
| `ps4-kernel-dumper.bin` | Kernel-Dumper | — | Vuelca el kernel |
| `ps4-disable-aslr.bin` | Disable-ASLR | — | Desactiva el ASLR (para trabajar con memoria) |
| `ps4-permanent-uart.bin` | Permanent-UART | — | UART por hardware sin parche de kernel; persiste tras actualizar |
| `ps4-rif-renamer.bin` | RIF-Renamer | — | Renombra RIF "fake" a "free" para PKG que solo van con Mira+HEN |

## `no-12.52/` — no se suben: su firmware máximo queda por debajo de 12.52

| Archivo | Firmware según el host |
|---|---|
| `Orbis-Toolbox-900.bin` (OSM-Made) | 5.05, 6.72, 7.02, 7.55, 9.00 |
| `ps4debug.bin` (CTN & SiSTR0) | hasta 12.02 |
| `WebRTE.bin` (golden, EchoStretch) | 5.05, 6.72, 7.00–11.00 |

`BinLoader` (7.00–9.60) y `ElfLoader` del host son `elfldr.bin/.elf`, que llegan vacíos (0 bytes) y son de la era sin GoldHEN: no se guardan.

## `no-subir/` — peligroso en esta consola

`ps4-enable-updates.bin` **reactiva las actualizaciones del sistema**. Por encima de 13.00 no hay exploit: nunca en `/data/payloads/`.

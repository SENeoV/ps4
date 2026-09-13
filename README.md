# ps4

Todo lo que rodea a una **PS4 Pro con firmware 12.52 y GoldHEN**: la colección retro para RetroArch, los paquetes de homebrew y los trucos. Los binarios (ROMs, BIOS, PKG) viven solo en el PC y en la consola; aquí se versionan la documentación, los scripts y una referencia (SHA-1) de cada archivo.

## Por dónde empezar

| Documento | Para qué |
|---|---|
| [`INSTALL.md`](INSTALL.md) | Cargar GoldHEN en 12.52, instalar RetroArch y sus cores, y qué carpeta del PC va a qué ruta de la consola |
| [`PLAN.md`](PLAN.md) | Checklist maestra: qué está hecho, qué está probado y la hoja de ruta por tandas |
| [`PENDIENTES.md`](PENDIENTES.md) | Lista priorizada de lo que falta conseguir, preparar o configurar, y quién lo hace |
| [`emu/emuladores-ps4.md`](emu/emuladores-ps4.md) | Matriz de 53 sistemas: core en esta PS4, extensiones, BIOS y compatibilidad; qué no es viable y por qué |
| [`emu/ROMS/<SISTEMA>/README.md`](emu/ROMS/) | Detalle de cada sistema |
| [`emu/BIOS/README.md`](emu/BIOS/README.md) | Índice de BIOS: cuáles hay, cuáles faltan y sus hashes |
| [`emu/RETROARCH/README.md`](emu/RETROARCH/README.md) | `.info`, listas de juegos, bases de datos y carátulas |
| [`INVENTORY.md`](INVENTORY.md) · [`catalogo/`](catalogo/) | Inventario y punteros por archivo, regenerados en cada commit |
| [`CLAUDE.md`](CLAUDE.md) | Guía del repo para Claude Code |
| [`docs/`](docs/) | Auditorías y documentos históricos |
| [`linux/ps4-linux-tutorial.md`](linux/ps4-linux-tutorial.md) | Guía completa de instalación de Linux en PS4 (copia de dionkill.github.io, en inglés) |

## Estructura

```
emu/            colección: APPS (PKG), BIOS, ROMS/<SISTEMA>, RETROARCH, SAVES, MEDIA, EXTRAS
pkg/            homebrew, juegos y herramientas en PKG (ignorado por git, catalogado)
catalogo/       un .ref (SHA-1, tamaño) por cada archivo binario
tools/          inventory.py, guard.py, retroarch_lists.py y los hooks de git
ps4_cheats/     submódulo: trucos de shadPS4 (histórico, no válido para GoldHEN)
goldhen_cheats/ submódulo: trucos oficiales de GoldHEN
docs/           auditoría de la documentación e histórico
linux/          Linux en la PS4: copia de la guía de DionKill (proyecto aparte, no planificado)
```

Los hooks de `tools/hooks/` regeneran el catálogo en cada commit y bloquean cualquier binario o archivo de más de 5 MB. En un clon nuevo: `cp tools/hooks/pre-commit tools/hooks/pre-push .git/hooks/` y `git submodule update --init`.

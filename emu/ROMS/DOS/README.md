# DOS — DOS / PC (1981)

- **Estado:** Ordenadores — juegos en el PC (14-09-2026), sin probar en la consola
- **Cores instalados en la PS4:** `dosbox_svn` (recomendado, lista *DOS*), `dosbox`
- **Extensiones:** `.exe` `.com` `.bat` `.conf`
- **BIOS:** no necesita

**Notas:** Se usa con teclado. El rendimiento depende del juego: los más exigentes pueden ir lentos.

## Cómo está organizado

- `DOS/<Juego>/`: el juego descomprimido tal como venía en su zip. Hay dos arreglos:
  - si el zip traía una única carpeta con nombre largo, se quitó, porque DOS no ve nombres largos;
  - si traía zips dentro, cada uno se descomprimió en una subcarpeta con su nombre.
- `DOS/<Juego>.conf`: su lanzador. Monta la carpeta del juego como `C:` con la ruta de la consola (`/data/ROMS/DOS/<Juego>`), entra en su subcarpeta y ejecuta el programa. La lista *DOS* de RetroArch apunta a estos `.conf`.
- El zip original de cada juego está en `emu/ORIGINALES/DOS/`, y es lo que se cataloga. Las carpetas descomprimidas no se catalogan: son 87 054 archivos.

**Se sube a la consola:** las 956 carpetas y sus `.conf`, a `/data/ROMS/DOS/` (5,2 GB). En otra ruta no arrancan, porque la línea `mount` de cada `.conf` apunta ahí.

## Contenido (14-09-2026)

Salen de una colección preparada para Recalbox o Batocera: 1000 zips, 2 `.dosz` y 2 `.rar`. El `gamelist.xml` que traía lista 1778 juegos, así que faltan 778.

| Estado del lanzador | Juegos | Qué significa |
|---|--:|---|
| `seguro` | 690 | Un único ejecutable claro |
| `dudoso` | 254 | Hay otros candidatos; el `.conf` los lista en `# Alternativas:` |
| `instalar` | 11 | El zip solo trae el instalador: el `.conf` deja la consola de DOS en la carpeta del juego |
| `disquete` | 1 | *Championship Lode Runner* arranca de una imagen de disquete |

El ejecutable lo elige `tools/dos.py` por su nombre, sin probarlo. [`LANZADORES.md`](LANZADORES.md) lista los que no son `seguro` con sus alternativas. Si un juego abre el programa equivocado, se cambia la última línea de su `.conf`.

- **Instaladores** (hay que instalarlos en DOSBox, en el PC o en la consola): *Airbucks*, *Alien Rampage*, *Brett Hull Hockey '95*, *Colonization*, *Discworld*, *Doom* (shareware), *Entombed*, *Fields of Glory*, *Fuzzy's World of Miniature Space Golf*, *Litil Divil* y *Traffic Department 2192*.
- **Warcraft II - Tides of Darkness:** venía en `.rar` junto con los mapas de *Armory Campaigns*, que están en su subcarpeta `ARMORY/`.
- **Lode Runner:** trae tres versiones (`LRSLOW/`, `V1/` y `V2/`); arranca la primera.
- **Alias de DOS:** *Football Limited* y *Mickey's Space Adventure* entran en carpetas de nombre largo con el alias `~1` que genera DOSBox. No se ha podido comprobar en el PC.
- **Nombres cambiados:** 8 archivos con nombres no ASCII dentro de los juegos pasaron a ASCII; casi todos eran NFO de grupos de cracks.
- **ScummVM:** 40 aventuras de esta colección están en `emu/ROMS/SCUMMVM/`, no aquí.

**Apartado:**

- en `emu/EXTRAS/DOS-malos/`, 6 zips rotos: cuatro de 0 bytes, `Liverpool.zip`, que está cortado, y `Metal Gear.zip`, con CRC incorrecta;
- en `emu/EXTRAS/DOS-otros/`, *Microsoft Arcade* y *SimFarm*, que son de Windows 3.x, y los `.p2k.cfg` de Recalbox.

Las carátulas, capturas, logos, vídeos y el `gamelist.xml` de ScreenScraper están en `emu/MEDIA/DOS/`. Los movimientos están en `cleanup-2026-09-14-dos.tsv`.

## Añadir más juegos

```bash
python tools/dos.py CARPETA            # simula: estado y ejecutable elegido para cada zip
python tools/dos.py CARPETA --hacer    # descomprime, crea los lanzadores, guarda los originales y lo registra
python tools/dos.py --informe          # regenera LANZADORES.md a partir de los .conf
python tools/retroarch_lists.py --only DOS SCUMMVM
```

_Cores y extensiones según los `.info` de libretro-core-info, más nuevos que los cores del port R4 de 2020._

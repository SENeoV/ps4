# ARCADE

| Carpeta | Core en la PS4 | Romset | Juegos | Lista de RetroArch |
|---|---|---|--:|---|
| `FBNEO/` | `fbalpha2012` | FB Alpha 2012 `v0.2.97.29` | 2032 | *FB Alpha 2012* |
| `FBNEO/CPS1/` | `fbalpha2012_cps1` | FB Alpha 2012 `v0.2.97.28` | 154 | *FB Alpha 2012 CPS-1* |
| `FBNEO/CPS2/` | `fbalpha2012_cps2` | FB Alpha 2012 `v0.2.97.28` | 273 | *FB Alpha 2012 CPS-2* |
| `FBNEO/CPS3/` | `fbalpha2012_cps3` | FB Alpha 2012 `v0.2.97.29` | 32 | *FB Alpha 2012 CPS-3* |
| `../NEOGEO/` | `fbalpha2012_neogeo` | FB Alpha 2012 `v0.2.97.29` | 284 | *FB Alpha 2012 Neo Geo* |
| `MAME/` | MAME 2003-Plus (y otras 4 versiones) | el de la versión elegida; recomendado MAME 2003-Plus | — | — |
| `NAOMI/`, `ATOMISWAVE/` | Flycast | BIOS en `system/dc/` | — | — |

**Cada carpeta de FB Alpha 2012 va con un core.** Su lista abre cada juego con ese core. Si se carga a mano con *Load Content*, hay que elegir el core que corresponde a la carpeta. El padre de un clon y la BIOS de placa tienen que estar en la misma carpeta que el juego, porque el core solo los busca ahí.

Los juegos de FB Alpha 2012 salen del set *v0.2.97.24* de archive.org, verificado zip a zip el 14-09-2026 con `tools/fba2012.py` contra los DAT de cada core. El detalle está en [`FBNEO/README.md`](FBNEO/README.md).

No mezclar romsets entre emuladores ni entre versiones del mismo emulador: un romset de una versión puede no funcionar en otra. Cada colección debe corresponder exactamente al core que la va a ejecutar.

# SCUMMVM — ScummVM — aventuras gráficas

- **Estado:** Ordenadores — juegos en el PC (14-09-2026), sin probar en la consola
- **Cores instalados en la PS4:** `scummvm` (lista *ScummVM*)
- **Extensiones:** `.scummvm`
- **BIOS** (en `/data/retroarch/system/`, salvo que se indique otra cosa):
  - `scummvm/extra/`: datos de algunos motores. Aún no están, y sin ellos no arrancan *Eye of the Beholder* (`kyra.dat`), *Lure of the Temptress* (`lure.dat`) ni *Flight of the Amazon Queen* (`queen.tbl`)
  - `scummvm/theme/`: temas del menú, opcionales

**Notas:** Cada juego va en su propia subcarpeta. Su `.scummvm` está junto a los archivos de datos y contiene el id del juego en ScummVM.

## Contenido

40 aventuras sacadas de la colección de DOS el 14-09-2026 con `tools/dos.py`. Sus zips originales están en `emu/ORIGINALES/DOS/`. Las 40 aparecen con su nombre oficial en la lista, porque `ScummVM.rdb` las reconoce.

Los ids se comprobaron en las tablas de detección de ScummVM 2.2. No está identificada la versión exacta de ScummVM del core del port (2020).

| Motor | Juegos (id) |
|---|---|
| SCI (Sierra) | *Castle of Dr. Brain* (`castlebrain`), *Codename: Iceman* (`iceman`), *Conquests of the Longbow* (`longbow`), *EcoQuest* (`ecoquest`), *Freddy Pharkas* (`freddypharkas`), *Jones in the Fast Lane* (`jones`), *King's Quest 4* (`kq4sci`), *5* (`kq5`) y *6* (`kq6`), *Laura Bow* (`laurabow`), *Leisure Suit Larry 2* (`lsl2`) y *3* (`lsl3`), *Mixed-Up Fairy Tales* (`fairytales`), *Pepper's Adventures in Time* (`pepper`), *Police Quest 2* (`pq2`) y *3* (`pq3`), *Quest for Glory II* (`qfg2`) y *III* (`qfg3`), *Space Quest 3* (`sq3`), *4* (`sq4`) y *5* (`sq5`) |
| AGI (Sierra) | *Donald Duck's Playground* (`ddp`), *Gold Rush!* (`goldrush`), *King's Quest 2* (`kq2`) y *3* (`kq3`), *Leisure Suit Larry* (`lsl1`), *Manhunter: New York* (`mh1`), *Mixed-Up Mother Goose* (`mixedup`), *Space Quest 2* (`sq2`), *The Black Cauldron* (`bc`) |
| SCUMM (LucasArts) | *Loom* (`loom`), *Zak McKracken* (`zak`) |
| Gob (Coktel Vision) | *Gobliiins* (`gob1`), *Gobliins 2* (`gob2`), *Ween* (`ween`) |
| Otros | *DreamWeb* (`dreamweb`), *Eye of the Beholder* (`eob`), *Flight of the Amazon Queen* (`queen`), *Future Wars* (`fw`), *Lure of the Temptress* (`lure`) |

Otros tres juegos traen archivos que parecen de un motor de ScummVM, pero se quedaron en DOS con un aviso en su `.conf`: *Asterix - Operation Getafix*, *The Incredible Machine* y *The Even More Incredible Machine*. *Discworld*, que ScummVM también ejecuta, solo trae su instalador; está en DOS como `instalar`.

## Añadir juegos

`python tools/dos.py CARPETA` manda a esta carpeta los títulos que conoce (tabla `SCUMMVM_IDS` del script). Otro juego nuevo se añade a esa tabla con su id de ScummVM.

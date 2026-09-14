# ARCADE/FBNEO — Arcade — FB Alpha 2012

- **Estado:** Tanda 2 — ROMs en el PC (14-09-2026), sin probar en la consola
- **Core:** `fbalpha2012` para esta carpeta. CPS-1, CPS-2 y CPS-3 van en `CPS1/`, `CPS2/` y `CPS3/` con su core dedicado, y Neo Geo en `emu/ROMS/NEOGEO/`
- **Extensiones:** `.zip`
- **BIOS:** `pgm.zip` e `isgsm.zip`, **junto a los juegos**, no en `system/`. Ya están
- **Romset:** FB Alpha 2012 `v0.2.97.29`

**Notas:** La carpeta se llama FBNEO por la guía original, pero en la PS4 el core es **FB Alpha 2012**, no FinalBurn Neo: los romsets de FBNeo actual no valen.

## De dónde salen y cómo se verificaron

Del set *Final Burn Alpha 2012 (Split) (v0.2.97.24)* de archive.org: 2890 zips, **más antiguo que el core**. Para saber cuáles arrancan, `tools/fba2012.py`:

1. Saca el DAT de cada core de su código fuente en libretro. Usa el último commit anterior a julio de 2020, la fecha del port de la consola, y las tablas de ROMs de esos commits coinciden con las de 2026 salvo cuatro BIOS Universe opcionales.
2. Repite la búsqueda de ROMs de `libretro.cpp`: cada ROM se busca primero por CRC y, si no aparece, por nombre, con el tamaño exacto. La busca en el zip del juego, en el de su placa y en los de sus padres. Las ROMs marcadas como opcionales no cuentan.
3. Coloca cada juego en la carpeta de su core, junto con los zips que necesita.

Los cinco DAT (`FB Alpha 2012 - <core> (v0.2.97.2x).dat`) quedan en `emu/RETROARCH/database/dat/`, sin versionar. Los movimientos están en `cleanup-2026-09-14-arcade.tsv`.

## Esta carpeta

| | Zips |
|---|--:|
| Juegos en la lista *FB Alpha 2012* | 2032 |
| · con alguna ROM de CRC distinta: arrancan, pero pueden fallar (`ambush`, `cninja1`, `sjryuko`, `sjryuko1`) | 4 |
| · con el driver marcado como que no funciona; salen con «[no funciona bien]» (`aceattac`, `downtown`, `dsoccr94`, `kbash`, `mwalk`, `nob`, `tekipaki`, `tokio`, `whoopee`) | 9 |
| Padres que no arrancan porque les faltan ROMs de la v0.2.97.29, pero sus clones sí (`dblaxle`, `driftout`, `fantzn2x`, `gradius3`, `karnov`, `puckman`, `raiden`, `rastan`, `smgp`, `superchs`, `thndzone`) | 11 |
| Padres de relleno sin driver propio, que necesitan sus clones (`8ballact`, `ckong`, `dockman`, `hunchbak`, `huncholy`, `maniacsq`, `phoenix`, `thepit`) | 8 |
| BIOS de placa (`pgm.zip`, `isgsm.zip`) | 2 |
| **Total** | **2053** |

El resto del set está en `CPS1/` (154 zips), `CPS2/` (275), `CPS3/` (32) y `emu/ROMS/NEOGEO/` (285). Lo apartado en `emu/EXTRAS/` incluye lo que le falta a cada zip:

- `ARCADE-incompletos/`: 47 juegos a los que les faltan ROMs de la v0.2.97.29. Se completarían con un set de la versión del core.
- `ARCADE-sin-driver/`: 44 zips cuyo nombre no existe en FB Alpha 2012.
- `ARCADE-otros/`: `neocdz` (la Neo Geo CDZ sin CD), el DAT v0.2.97.24 y los metadatos del set.

## Comprobar o añadir juegos

```bash
python tools/fba2012.py dat                                   # DAT de los 5 cores (clona libretro en %TEMP%)
python tools/fba2012.py verificar CARPETA --tsv informe.tsv   # zip a zip: core, estado, ROMs que faltan y carpeta
python tools/fba2012.py listas                                # verifica estas carpetas y regenera las 5 listas
```

_Las listas de arcade no salen de `tools/retroarch_lists.py`: en arcade el nombre de cada juego sale del DAT del core, no del CRC. Rendimiento sin probar en esta consola._

# ARCADE/FBNEO/CPS2 — Capcom CPS-2

- **Estado:** Tanda 2 — ROMs en el PC (14-09-2026), sin probar en la consola
- **Core:** `fbalpha2012_cps2` (lista *FB Alpha 2012 CPS-2*)
- **Extensiones:** `.zip`
- **BIOS:** no necesita
- **Romset:** FB Alpha 2012 `v0.2.97.28`

275 zips, de ellos 273 juegos en la lista:

- 272 arrancan tal cual.
- `vsav2d` arranca con dos ROMs de CRC distinta (`vs2j_d.03` y `vs2j_d.04`) y puede fallar.

Los otros dos zips no salen en la lista, pero no se pueden quitar:

- `xmcota` no arranca, porque le faltan `xmne.03f`, `xmne.04f`, `xmne.05b` y `xmne.10b` de la v0.2.97.28, pero es el padre de 10 clones que sí arrancan.
- `megaman.zip` es una copia del de `../CPS1/` y hace de padre de `mmancp2u` y `rmancp2j`.

Verificado con `tools/fba2012.py`; detalle en [`../README.md`](../README.md).

# ARCADE/FBNEO/CPS1 — Capcom CPS-1

- **Estado:** Tanda 2 — ROMs en el PC (14-09-2026), sin probar en la consola
- **Core:** `fbalpha2012_cps1` (lista *FB Alpha 2012 CPS-1*)
- **Extensiones:** `.zip`
- **BIOS:** no necesita
- **Romset:** FB Alpha 2012 `v0.2.97.28`

154 zips, todos en la lista:

- 148 arrancan tal cual.
- 6 arrancan con una ROM de CRC distinta (`s224b.1a`) y pueden fallar: las seis versiones de *Final Fight* (`ffight`, `ffighta`, `ffightu`, `ffightu1`, `ffightua` y `ffightub`).

`megaman.zip` también está copiado en `../CPS2/`, porque lo necesitan dos clones de CPS-2.

Verificado con `tools/fba2012.py`; detalle en [`../README.md`](../README.md).

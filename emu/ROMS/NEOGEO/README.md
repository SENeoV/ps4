# NEOGEO — Neo Geo AES/MVS (1990)

- **Estado:** Tanda 2 — ROMs en el PC (14-09-2026), sin probar en la consola
- **Core:** `fbalpha2012_neogeo` (lista *FB Alpha 2012 Neo Geo*)
- **Extensiones:** `.zip`
- **BIOS:** `neogeo.zip` — obligatoria, **en esta misma carpeta**, no en `/data/retroarch/system/`. Ya está
- **Romset:** FB Alpha 2012 `v0.2.97.29`

**Notas:** Los romsets de FBNeo actual pueden no funcionar.

285 zips: 284 juegos, que arrancan todos según `tools/fba2012.py`, y `neogeo.zip`. Salen del set FB Alpha 2012 v0.2.97.24; cómo se verificó está en [`../ARCADE/FBNEO/README.md`](../ARCADE/FBNEO/README.md).

Del mismo set quedaron fuera, en `emu/EXTRAS/`:

- `samsh5sph`, que está incompleto;
- `garouo` y `samsh5spn`, que no tienen driver;
- `neocdz`, la Neo Geo CDZ sin CD, que no es un juego.

_Rendimiento sin probar en esta consola._

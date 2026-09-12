# SAVES — partidas guardadas

| En el PC | En la PS4 |
|---|---|
| `emu/SAVES/*.srm` | `/data/retroarch/savefiles/` |

Configuración leída de la consola:

```
savefile_directory = "/data/retroarch/savefiles"
sort_savefiles_enable = "false"
savefiles_in_content_dir = "false"
```

Por eso la carpeta es **plana**, sin subcarpetas por core. Si algún día se activa `sort_savefiles_enable`, RetroArch buscará las partidas en una subcarpeta con el nombre del core y habrá que moverlas.

## Nombre de archivo

RetroArch busca `<nombre de la ROM sin extensión>.srm` (así lo confirma el `Bomberman2.srm` que ya creó en la consola). Las partidas de GBA venían como `.sav`: se han renombrado a `.srm` sin tocar el contenido.

## Antes de subir

- Si ese juego ya se ha jugado en la PS4, allí existe su `.srm` y subir este lo **sobrescribe**. Descargar antes el de la consola.
- Todavía sin probar en consola. Comprobar una partida antes de dar por buenas todas.

Los `.srm` no se suben al repo (binarios, ignorados por git).

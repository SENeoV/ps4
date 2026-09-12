# MEDIA — carátulas (no se suben a la PS4)

Imágenes que venían mezcladas con las ROMs, con el mismo nombre que el juego (carátulas estilo EmulationStation). Se apartaron porque:

- ningún core las lee (ningún `.info` declara `png`),
- casi duplicaban el número de archivos a subir por FTP,
- con el filtro de extensiones desactivado aparecían en *Load Content*.

Estructura: `MEDIA/<SISTEMA>/<nombre del juego>.png`.

Para usarlas como miniaturas en RetroArch no basta con copiarlas: van en `/data/retroarch/thumbnails/<nombre de la playlist>/Named_Boxarts/` y hace falta tener playlists creadas.

No se suben al repo (binarios, ignorados por git).

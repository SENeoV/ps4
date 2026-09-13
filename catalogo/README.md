# catalogo — los juegos, por referencia

Git versiona aquí **un puntero por cada archivo** de `emu/ROMS`, `emu/BIOS`, `emu/APPS` y `pkg/`. El contenido real nunca entra en el repo ni se sube a GitHub: se queda en el PC.

Así cada commit muestra, archivo a archivo, qué juegos se añadieron, se quitaron o se renombraron.

## Formato

La ruta imita a la de `emu/` y añade `.ref`; `pkg/` va bajo `PKG/`, con sus subcarpetas:

```
emu/ROMS/GB/Tetris (World).gb   ->   catalogo/ROMS/GB/Tetris (World).gb.ref
pkg/stores/Store-R2.pkg         ->   catalogo/PKG/stores/Store-R2.pkg.ref
```

Contenido:

```
sha1 <SHA-1 del archivo>
size <bytes>
rom-sha1 <SHA-1 de la ROM interior>   (solo en .zip)
content-id <Content ID de la cabecera>   (solo en .pkg)
```

Para verificar un volcado contra los DAT de No-Intro o Redump se usa `rom-sha1` si el juego está en zip, y `sha1` si no lo está.

El `content-id` se lee del propio PKG (magic `\x7FCNT`, 36 bytes en el offset `0x40`), porque el nombre del archivo no siempre coincide: `PS4_CUSA01116_v2.32.pkg` contiene `CUSA01015`.

## Cómo se actualiza

Solo, en cada `git commit`, mediante el hook `tools/hooks/pre-commit`: ejecuta `python tools/inventory.py` y añade `catalogo/`, `inventory.csv` e `INVENTORY.md` al commit.

A mano: `python tools/inventory.py` (con `--force` recalcula todos los hashes).

Los hooks viven en `.git/hooks/`, que no se versiona. En un clon nuevo hay que instalarlos una vez:

```bash
cp tools/hooks/pre-commit tools/hooks/pre-push .git/hooks/
```

Además de regenerar el catálogo, bloquean cualquier commit o push que añada un binario o un archivo de más de 5 MB (`tools/guard.py`).

**No editar los `.ref` a mano**: se regeneran desde los archivos reales.

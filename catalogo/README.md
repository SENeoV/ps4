# catalogo — los juegos, por referencia

Git versiona aquí **un puntero por cada archivo** de `emu/ROMS`, `emu/BIOS` y `emu/APPS`. El contenido real nunca entra en el repo ni se sube a GitHub: se queda en el PC.

Así cada commit muestra, archivo a archivo, qué juegos se añadieron, se quitaron o se renombraron.

## Formato

La ruta imita a la de `emu/` y añade `.ref`:

```
emu/ROMS/GB/Tetris (World).gb   ->   catalogo/ROMS/GB/Tetris (World).gb.ref
```

Contenido:

```
sha1 <SHA-1 del archivo>
size <bytes>
rom-sha1 <SHA-1 de la ROM interior>   (solo en .zip)
```

Para verificar un volcado contra los DAT de No-Intro o Redump se usa `rom-sha1` si el juego está en zip, y `sha1` si no lo está.

## Cómo se actualiza

Solo, en cada `git commit`, mediante el hook `tools/hooks/pre-commit`: ejecuta `python tools/inventory.py` y añade `catalogo/`, `inventory.csv` e `INVENTORY.md` al commit.

A mano: `python tools/inventory.py` (con `--force` recalcula todos los hashes).

Los hooks viven en `.git/hooks/`, que no se versiona. En un clon nuevo hay que instalarlos una vez:

```bash
cp tools/hooks/pre-commit tools/hooks/pre-push .git/hooks/
```

Además de regenerar el catálogo, bloquean cualquier commit o push que añada un binario o un archivo de más de 5 MB (`tools/guard.py`).

**No editar los `.ref` a mano**: se regeneran desde los archivos reales.

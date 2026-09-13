# GC — GameCube (2001)

- **Estado:** Solo con Linux — **funciona**: *Wind Waker* a 30 fps en Dolphin 2509 el 13-09-2026 ([`linux/`](../../../linux/README.md))
- **Core en la PS4:** ninguno. Dolphin necesita OpenGL 3.3 / GLES 3.0 / Vulkan y el port de RetroArch para PS4 solo llega a OpenGL ES 2
- **Extensiones:** `.iso` `.gcm` `.rvz` (Dolphin)
- **BIOS:** no necesita

**Notas:** Arrancando Linux en esta PS4 (disponible en 12.52) Dolphin funciona: hay informes de *Pikmin* a 50 fps en PS4 Pro con OpenGL. Qué implica y cómo va el proyecto, en [`../../emuladores-ps4.md`](../../emuladores-ps4.md#solo-con-linux--gamecube-wii-ps3-y-ps-vita). Sin probar en esta consola.

**Juegos (14-09-2026):** *The Legend of Zelda: The Wind Waker*, en RVZ (Dolphin lo lee sin descomprimir), en dos versiones:

| Versión | ID | Tamaño | En la consola | Para qué |
|---|---|---|---|---|
| Europe (En,Fr,De,Es,It) | `GZLP01` | 870.001.784 B | Sí, `/home/ps4/Juegos/Zelda-Wind-Waker-Europe.rvz` | **En español.** El que se juega |
| USA | `GZLE01` | 863.379.372 B | Sí, `/home/ps4/Juegos/Zelda-Wind-Waker-USA.rvz` (14-09) | Con las texturas HD, que el mod diseñó para la versión inglesa |

Es el juego objetivo del proyecto Linux; cómo llega a la consola y cómo se lanza, en [`linux/README.md`](../../../linux/README.md#dolphin-gamecube-y-wii-el-objetivo). Las texturas HD y por qué hacen falta las dos versiones, en [`linux/dolphin.md`](../../../linux/dolphin.md#texturas-hd-hypatia-wwhd-v20).

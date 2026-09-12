# RETROARCH — archivos de configuración

| En el PC | En la PS4 |
|---|---|
| `emu/RETROARCH/info/*.info` | `/data/retroarch/info/` |

## Por qué existe esta carpeta

**Síntoma:** RetroArch abre, hay cores instalados, las ROMs están en la consola con permisos correctos — pero *Load Content* muestra las carpetas **vacías**.

**Causa raíz:** el navegador de RetroArch filtra los archivos por extensión soportada:

```
menu_navigation_browser_filter_supported_extensions_enable = "true"
libretro_info_path = "/data/retroarch/info"
```

Las extensiones que soporta cada core **no salen del core**, salen de su archivo `.info`. El Core Installer (`SSNE20000`) despliega los cores en `/data/self/retroarch/cores/` pero **deja `/data/retroarch/info/` vacío**.

Resultado: RetroArch no conoce ni una sola extensión válida → filtra absolutamente todos los archivos → cada carpeta se ve vacía aunque esté llena.

Diagnóstico que lo confirmó:

| Comprobación | Resultado |
|---|---|
| ROMs en `/data/roms/NES/` | 635 archivos, permisos 0777, tamaños correctos |
| Cores en `/data/self/retroarch/cores/` | 74 cores presentes |
| Archivos en `/data/retroarch/info/` | **0 — vacío** |

## Contenido

74 archivos `.info`, uno por core instalado, de [libretro-core-info](https://github.com/libretro/libretro-core-info).

`mupen64plus_libretro.info` es el `mupen64plus_next_libretro.info` de upstream renombrado: el core de PS4 se llama `mupen64plus_libretro_ps4.self` y RetroArch empareja core con `.info` **por nombre de archivo**.

## Cómo aplicarlo

Subir por FTP el contenido de `info/` a `/data/retroarch/info/` y reiniciar RetroArch.

## Alternativas sin subir nada

- **Cargar el core primero:** *Load Core → Nestopia* y **después** *Load Content*. Con un core ya cargado RetroArch le pregunta las extensiones directamente, sin pasar por los `.info`.
- **Desactivar el filtro:** *Settings → File Browser → Filter Unknown Extensions* → OFF. Ojo: en la config está `menu_show_advanced_settings = "false"`, así que puede que haya que activar antes las opciones avanzadas para que aparezca.

Ambas sirven para salir del paso, pero sin los `.info` seguirán fallando el escaneo de contenido, las playlists y la asociación automática core↔sistema.

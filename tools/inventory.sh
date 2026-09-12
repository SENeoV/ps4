#!/bin/bash
# Genera el inventario de ROMs y BIOS por hash SHA-1.
#
#   bash tools/inventory.sh           # incremental (reutiliza hashes si path+tamaño no cambian)
#   bash tools/inventory.sh --force   # recalcula todos los hashes
#
# Salida:
#   inventory.csv  -> detalle completo (una línea por archivo), es lo que hace visible el diff en git
#   INVENTORY.md   -> resumen legible por sistema
#
# SHA-1 es el hash que usan los DATs de No-Intro y Redump, así que estos valores
# se pueden contrastar directamente contra esas bases de datos.

set -euo pipefail
cd "$(dirname "$0")/.."

CSV="inventory.csv"
MD="INVENTORY.md"
FORCE=0
[ "${1:-}" = "--force" ] && FORCE=1

# Cache de la ejecución anterior: "system/ruta|tamaño" -> sha1
declare -A CACHE
if [ $FORCE -eq 0 ] && [ -f "$CSV" ]; then
  while IFS=, read -r sys file bytes sha1; do
    [ "$sys" = "system" ] && continue
    CACHE["$sys/$file|$bytes"]="$sha1"
  done < "$CSV"
fi

TMP=$(mktemp)
echo "system,file,bytes,sha1" > "$TMP"

reused=0
hashed=0

# Recorre ROMS/ y BIOS/, ignorando la documentación
while IFS= read -r -d '' path; do
  case "$path" in
    *.md) continue ;;
  esac

  rel="${path#./emu/}"
  case "$rel" in
    ROMS/*) sys="${rel#ROMS/}"; sys="${sys%%/*}"; file="${rel#ROMS/$sys/}" ;;
    BIOS/*) sys="BIOS"; file="${rel#BIOS/}" ;;
    APPS/*) sys="APPS"; file="${rel#APPS/}" ;;
    *) continue ;;
  esac

  bytes=$(stat -c%s "$path")
  key="$sys/$file|$bytes"

  if [ -n "${CACHE[$key]:-}" ]; then
    sha1="${CACHE[$key]}"
    reused=$((reused + 1))
  else
    sha1=$(sha1sum "$path" | cut -d' ' -f1)
    hashed=$((hashed + 1))
    echo "  hash: $sys/$file" >&2
  fi

  echo "$sys,$file,$bytes,$sha1" >> "$TMP"
done < <(find ./emu/ROMS ./emu/BIOS ./emu/APPS -type f -print0 2>/dev/null | sort -z)

# Ordena por sistema y nombre para que el diff de git sea estable
{ head -1 "$TMP"; tail -n +2 "$TMP" | sort; } > "$CSV"
rm -f "$TMP"

total=$(( $(wc -l < "$CSV") - 1 ))

# --- Resumen legible ---
{
  echo "# Inventario"
  echo
  echo "Generado por \`tools/inventory.sh\`. Detalle completo en [\`inventory.csv\`](inventory.csv)."
  echo
  echo "Hash: **SHA-1** (el mismo que usan los DATs de No-Intro y Redump, así que se puede verificar contra ellos)."
  echo
  if [ "$total" -eq 0 ]; then
    echo "_Todavía no hay contenido. Copia ROMs a \`emu/ROMS/<SISTEMA>/\` y BIOS a \`emu/BIOS/\`, y vuelve a ejecutar el script._"
  else
    echo "**Total: $total archivos**"
    echo
    echo "| Sistema | Archivos | Tamaño |"
    echo "|---|--:|--:|"
    tail -n +2 "$CSV" | awk -F, '
      { count[$1]++; size[$1] += $3; tc++; ts += $3 }
      END {
        n = asorti(count, sorted)
        for (i = 1; i <= n; i++) {
          s = sorted[i]
          printf "| %s | %d | %.1f MB |\n", s, count[s], size[s] / 1048576
        }
        printf "| **TOTAL** | **%d** | **%.1f MB** |\n", tc, ts / 1048576
      }'
  fi
} > "$MD"

echo "OK  ->  $CSV ($total archivos)  |  $MD"
echo "    hashes nuevos: $hashed, reutilizados: $reused"

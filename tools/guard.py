#!/usr/bin/env python
# Bloquea commits y pushes que añadan o modifiquen un binario o un archivo grande. Los borrados no cuentan.
#   python tools/guard.py pre-commit   revisa lo preparado
#   python tools/guard.py pre-push     revisa los commits que se van a subir (lee el stdin del hook)

import subprocess
import sys

MAX_BYTES = 5 * 1024 * 1024
EMPTY_TREE = "4b825dc642cb6eb9a060e54bf8d69288fbee4904"
ZERO = "0" * 40

HOW_TO_FIX = {
    "pre-commit": "Sácalos de lo preparado con  git restore --staged <archivo>  y añádelos a .gitignore.",
    # En un push el archivo ya está dentro de un commit: quitarlo en un commit nuevo no lo saca del historial que se sube
    "pre-push": "Están en commits aún no subidos. Rehazlos:  git reset --soft origin/main,  "
                "git restore --staged <archivo>,  añádelo a .gitignore  y vuelve a hacer commit.",
}


def git(*args, stdin=b""):
    return subprocess.run(["git", *args], input=stdin, capture_output=True, check=True).stdout


def offenders(diff_args):
    fields = git("diff", "--raw", "-z", "--no-renames", "--diff-filter=ACM", "--abbrev=40", *diff_args).split(b"\0")
    entries = {}
    for meta, path in zip(fields[0::2], fields[1::2]):
        if not meta:
            continue
        _, new_mode, _, new_sha, _ = meta.decode().split()
        if new_mode != "160000":
            entries[path.decode("utf-8", "replace")] = new_sha
    if not entries:
        return []

    sizes = {}
    batch = git("cat-file", "--batch-check=%(objectname) %(objectsize)", stdin="\n".join(entries.values()).encode())
    for line in batch.decode().splitlines():
        sha, size = line.split()
        sizes[sha] = int(size) if size.isdigit() else 0

    # git marca como "-\t-" en numstat los archivos que detecta como binarios por su contenido
    binary = set()
    for record in git("diff", "--numstat", "-z", "--no-renames", "--diff-filter=ACM", *diff_args).split(b"\0"):
        parts = record.split(b"\t", 2)
        if len(parts) == 3 and parts[0] == b"-" and parts[1] == b"-":
            binary.add(parts[2].decode("utf-8", "replace"))

    bad = []
    for path, sha in sorted(entries.items()):
        if path in binary:
            bad.append(f"binario    {path}")
        elif sizes.get(sha, 0) > MAX_BYTES:
            bad.append(f"{sizes[sha] / 1048576:5.1f} MB   {path}")
    return bad


def main():
    # En Windows Python escribe en cp1252 y la terminal de git espera UTF-8
    sys.stderr.reconfigure(encoding="utf-8")
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode not in HOW_TO_FIX:
        sys.exit("uso: python tools/guard.py pre-commit | pre-push")
    try:
        if mode == "pre-commit":
            bad = offenders(["--cached"])
        else:
            bad = []
            for line in sys.stdin.read().splitlines():
                _, local_sha, _, remote_sha = line.split()
                if local_sha == ZERO:
                    continue
                bad += offenders([EMPTY_TREE if remote_sha == ZERO else remote_sha, local_sha])
    except subprocess.CalledProcessError as e:
        sys.exit(f"BLOQUEADO ({mode}): no se pudo revisar ({e.stderr.decode(errors='replace').strip()}). ¿Falta un git fetch?")

    if bad:
        print(f"BLOQUEADO ({mode}): ni binarios ni archivos de más de {MAX_BYTES // 1048576} MB entran en el repo:", file=sys.stderr)
        for entry in bad[:30]:
            print("   " + entry, file=sys.stderr)
        if len(bad) > 30:
            print(f"   ... y {len(bad) - 30} más", file=sys.stderr)
        print(HOW_TO_FIX[mode], file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

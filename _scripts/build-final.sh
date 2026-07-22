#!/bin/bash
# Concatenation brute des blocs -> 99-bilan-final.md
# usage: bash _scripts/build-final.sh p06
BASE="$(cd "$(dirname "$0")/.." && pwd)"
cd "$BASE/$1" || exit 1
{
  echo "# Bilan final $1"; echo
  echo "*Fichier généré par concaténation des blocs. Ne pas l'éditer, éditer les blocs sources.*"
  echo "*Généré le $(date +%Y-%m-%d).*"; echo; echo "---"; echo
  for f in 00-cadrage.md 01-journal.md 02-bugs.md 03-connaissances.md 04-choix-techniques.md 05-bilan.md 06-git.md 07-synthese.md 08-soutenance.md 09-memo.md 10-point-de-reprise.md 11-a-verifier.md; do
    [ -f "$f" ] || continue
    cat "$f"; echo; echo "---"; echo
  done
} > 99-bilan-final.md
echo "genere $1/99-bilan-final.md ($(wc -l < 99-bilan-final.md) lignes)"

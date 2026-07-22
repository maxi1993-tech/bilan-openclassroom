# Journal du dépôt

Ce qui est arrivé à `bilan-oc` lui-même : mises en dépôt, corrections de scripts, leçons d'outillage. Rien sur les projets, qui vivent dans `pXX/`.

Rempli par Claude au rangement, sur faits observés. Une ligne résolue est barrée, pas supprimée.

Format : `[date] type : constat → correction`

---

## 2026-07-22 · mise en dépôt Git du dossier de notes

- ~~`[2026-07-22] doublon` : `fiche-p6-sophie-bluel.md` est resté à la racine du dépôt alors que son contenu existe déjà en deux endroits.~~ **Résolu le 22-07** : supprimé après vérification ligne à ligne, contenu intégralement retrouvé dans les blocs de `p06/`.

- ~~`[2026-07-22] doublon` : `_template/04-bilan.md` ne contient plus qu'une note "fichier remplacé".~~ **Résolu le 22-07** : supprimé.

- ~~`[2026-07-22] doublon` : douze fichiers `.sauv*` hors convention dans `p06/_deltas/`.~~ **Résolu le 22-07** : supprimés après vérification ligne à ligne.

> **Leçon de la session du 22-07.** Ces douze `.sauv*` étaient couverts par `.gitignore`, donc jamais suivis par Git. Claude les a présentés comme récupérables depuis l'historique : c'était faux. Avant d'annoncer qu'une suppression est réversible, vérifier que le fichier est réellement suivi, avec `git ls-files`.

---

## 2026-07-22 · audit général du dépôt

- ~~`[2026-07-22] renvoi cassé` : `sophie-bluel-design-tokens.md` est cité comme fiche existante dans `00-cadrage.md` et dans `10-point-de-reprise.md`, sans exister dans ce dépôt.~~ **Résolu le 22-07** : la fiche vit dans le dépôt du projet P6, avec le code. Les deux renvois précisent maintenant où elle est.

- ~~`[2026-07-22] séparateurs` : `fusionne-sous-sections.py` supprimait les `---` entre entrées, alors que le format de référence de `CLAUDE.md` les exige.~~ **Résolu le 22-07**, commit `080fe72`.

- ~~`[2026-07-22] contenu perdu à la génération` : `build-lisible.py` n'exportait aucune ligne de `02-bugs.md`, 95 lignes absentes, et annonçait 58 bugs au lieu de 30.~~ **Résolu le 22-07**, commit `c925252`.

- ~~`[2026-07-22] compteurs faux` : la page "En une page" du bilan lisible annonçait 0 connaissance acquise et 0 décision technique justifiée, sur 65 et 30 réelles. Le script comptait des puces `- `, absentes des blocs écrits en mots-clés.~~ **Résolu le 22-07**, commit `5687f1c`.

---

## 2026-07-22 · second audit, mesures de contrôle

> Contrôles rejoués en copie, sans modifier le dépôt. Détail des commandes dans la session Cowork du 22-07.

- `build-final.sh` · 0 ligne perdue sur 1202 lignes source significatives.

- `build-lisible.py` · 3 lignes non exportées, toutes issues de `État Git` de `06-git.md`, exclusion volontaire documentée dans le script.

- Régénération des deux bilans finaux · 0 écart avec les versions commitées, hors ligne de date.

- 0 doublon de sous-section `###` dans les douze blocs de `p06/`, après quatre deltas rangés.

- 0 écart de structure entre les titres de `p06/` et `templates/fiche-template-complet.md`, dans les deux sens.

- 0 écart entre `_template/` et le template complet, sur les douze fichiers.

- `[2026-07-22] sentinelle inopérante` : `build-lisible.py` masque le bloc `📐 Formule` s'il contient la chaîne `Non applicable`. Le bloc de `p06` disait "Aucune formule sur ce projet pour l'instant", donc restait exporté. **Résolu le 22-07** : texte remplacé par `Non applicable`.

- `[2026-07-22] procédure jamais exercée` : cinq projets sont déclarés validés dans `README.md`, aucun n'est clôturé. `p04/bilan-ohmyfood.md` est un fichier monolithique hors format, avec onze tirets cadratins. `p01`, `p02`, `p03`, `p05` ne contiennent qu'un `_deltas/` vide. À trancher.

---

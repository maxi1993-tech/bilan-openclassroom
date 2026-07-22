# bilan-oc, instructions de dossier

Ce fichier décrit **où et comment écrire**. Le comportement pédagogique (intégrité OC, barème d'indice, ton) reste dans les instructions du projet Claude "Intégrateur Web". Ne pas dupliquer ici.

## Ce que contient ce dossier

```
CLAUDE.md        ce fichier
ETAT.md          état du projet actif, court, à coller en Chat
README.md        index des 12 projets
_scripts/        génération des bilans, à réutiliser, ne pas réécrire
_template/       blocs vierges à copier pour un nouveau projet
_archive/        fiches d'origine avant découpage
p01/ ... p12/    un dossier par projet
```

## Fichiers d'un projet

| Fichier | Contenu |
| --- | --- |
| `00-cadrage.md` | mission, specs, todo, pièges, ce qu'il faut maîtriser |
| `01-journal.md` | 🧩 Pseudocode, 🗣️ Explication ligne par ligne |
| `02-bugs.md` | bug → cause réelle → correction |
| `03-connaissances.md` | 🧠 Nouvelles connaissances, 📚 Théorie non pratiquée |
| `04-choix-techniques.md` | 🔍 Choix techniques, format `décision → pourquoi` |
| `05-bilan.md` | 📐 Formule, 📊 Validation outils, 🔍 Vérification, 📋 Bilan mentor, ❓ Questions |
| `06-git.md` | commits, état git |
| `07-synthese.md` | 🧭 Bilan technique : ce que je maîtrise, erreurs récurrentes, découvertes |
| `08-soutenance.md` | seulement si le projet est évalué en soutenance |
| `09-memo.md` | 💡 Tips par concept, 📖 Lexique |
| `10-point-de-reprise.md` | où j'en suis, détaillé |
| `11-a-verifier.md` | incohérences et savoirs douteux relevés au rangement |
| `_inbox.md` | zone de dépôt brute, vidée après rangement |
| `_deltas/` | deltas d'origine archivés, numérotés |

Un projet peut demander un bloc en plus. Le proposer à Max, jamais l'ajouter en silence.

## Une information, un seul endroit

Trois blocs parlent de ce qui reste à apprendre. Ils ne se répètent pas, ils ont chacun un rôle :

| Bloc | Rôle |
| --- | --- |
| `03-connaissances.md`, 📚 Théorie non pratiquée | **le catalogue** des notions non acquises, avec ce qui a été vu |
| `05-bilan.md`, ➡️ À revoir par priorité | **le plan d'action**, l'ordre dans lequel les traiter |
| `07-synthese.md`, Ce qui reste à revoir | **un renvoi**, jamais une liste |

Même principe pour les tips :

| Bloc | Rôle |
| --- | --- |
| `03-connaissances.md` | **explique** la notion, une fois pour toutes |
| `09-memo.md`, 💡 Tips | **prescrit** un réflexe, à éviter et à faire. N'explique jamais. |

Quand une information existe déjà ailleurs, renvoyer au bloc source plutôt que la recopier.

## Mise en page, format de référence

Le format ci-dessous s'applique à tous les blocs sauf `01-journal.md`, qui contient les mots de Max et ne se reformate pas.

### Entrée de connaissance ou de tip

Mot-clé français, point médian, mot-clé anglais, les deux en `code`. Puis une ou deux phrases en prose. Puis un séparateur `---`.

```
`portée des variables` · `scope`

Une variable déclarée dans un bloc n'existe pas en dehors. L'instruction qui l'utilise doit vivre dans le même bloc.

> **Vu, pas acquis.** À reprendre sur exo dédié.

---
```

### Entrée de bug

Symptôme en gras avec le message d'erreur exact en `code`, puis cause et correction en puces, preuve en encadré.

```
**`Cannot read properties of null`**

- **Cause** · le `querySelector` s'exécute avant que l'élément existe.
- **Correction** · déplacer la récupération après la création.

> Preuve en console · un `console.log` immédiat affiche `null`.

---
```

### Puces et numérotation

- **Puce** dès qu'il y a une liste de plus d'un élément.
- **Numérotation** quand l'ordre compte : étapes, priorités, chronologie, questions mentor.
- **Prose** pour les explications sous un mot-clé, jamais de puce à cet endroit.
- **Une ligne vide entre chaque puce** quand l'entrée fait plus d'une ligne.

### Éléments de mise en page

| Élément | Usage |
| --- | --- |
| `---` | entre chaque entrée, jamais entre deux puces d'une même liste |
| `>` encadré | piège, preuve obtenue, avertissement, décision à défendre |
| `**gras**` | titre d'entrée, étiquette de puce (`- **Cause** ·`) |
| `` `code` `` | tout mot-clé, nom de fichier, classe, méthode, message d'erreur, couleur |
| tableau | données parallèles : specs, commits, scores, lexique, positions |
| `·` | séparateur à l'intérieur d'une ligne |
| `→` | conséquence, résultat, renvoi |

### Ce qui est interdit

- Tiret cadratin `—` et demi-cadratin `–`, partout.
- Pavé de plus de cinq lignes sans respiration.
- Mention répétée à chaque ligne (`[à valider]` fois soixante). La poser une fois en tête de bloc.
- Sous-section `### Étape N` qui redécoupe des sous-sections déjà existantes.

## Règles d'écriture

**Jamais de tiret cadratin ni demi-cadratin** (`—`, `–`), dans les fichiers comme dans les réponses. Utiliser `→`, le point médian `·`, la virgule, les deux-points ou les parenthèses.

**Mots-clés en français puis en anglais**, séparés par un point médian, entourés de `code` : `portée des variables` · `scope`. Le français pour comprendre, l'anglais pour chercher sur MDN.

**Une ligne vide entre chaque entrée.** Pas de listes compactes.

**Additionner, jamais écraser.** Un nouveau contenu s'ajoute à la suite du bloc existant. Rien de ce qui est déjà écrit ne disparaît.

**Un seul fichier par bloc, jamais de doublon daté.** Pas de `01-journal-v2.md`, pas de `bilan-2026-07-21.md`.

**Qui tient le stylo :**

- `01-journal.md` : mots de Max uniquement, orthographe corrigée, jamais reformulés. Claude pose la question, Max écrit. Pas de réponse, le bloc reste vide.
- `02-bugs.md`, `03-connaissances.md`, `06-git.md`, les vérifications : Claude remplit seul, faits observés uniquement, rien d'inventé.
- `00-cadrage.md`, `05-bilan.md` : Claude propose, Max valide.

**En continu, pas en fin de projet.** Le pseudocode s'écrit avant l'étape, le bug au moment où il est résolu, la connaissance quand elle est acquise.

## Cycle de session

1. Max travaille en **Chat** sur le projet OC (code, indices, pseudocode). C'est là qu'il apprend.
2. Fin de session Chat, Claude produit le delta. Max le colle brut dans `pXX/_inbox.md`, sans classer.
3. Session **Cowork** courte, Max dit "range l'inbox de PXX". Claude :
   - lit l'inbox **en entier** avant de classer, jamais au fil de l'eau
   - archive le brut dans `_deltas/NN-AAAA-MM-JJ-sujet.md`, numérotation à 2 chiffres, séquentielle par projet
   - répartit chaque bloc dans son fichier, en ajoutant à la suite
   - **fusionne par sous-section, jamais par étape.** Une nouvelle puce "JavaScript, bases" rejoint le `### JavaScript, bases` existant. Ne jamais créer un `### Étape N` qui redécoupe les mêmes sous-sections : au douzième delta il y aurait douze fois chaque titre. La traçabilité par étape est assurée par `_deltas/`, pas par la structure des blocs.
   - note dans `11-a-verifier.md` toute incohérence rencontrée
   - régénère `ETAT.md`
   - vide `_inbox.md` (le fichier reste, seul le contenu part)

En cas de doute sur la destination d'un passage, demander plutôt que deviner.

## _scripts/

Les scripts de génération existent déjà, les réutiliser plutôt que d'en réécrire :

- `bash _scripts/build-final.sh pXX` → `99-bilan-final.md`, concaténation brute
- `python3 _scripts/build-lisible.py pXX` → `99-bilan-final-lisible.md`, version réorganisée
- `python3 _scripts/fusionne-sous-sections.py pXX/03-connaissances.md` → fusionne les `###` de même nom

À lancer après chaque rangement d'inbox.

## 99-bilan-final.md

Généré par Claude en fin de projet, sur demande, par concaténation des blocs dans l'ordre numérique. Sert à la soutenance, au bilan mentor, ou à un export Notion en une fois.

**C'est une sortie, pas une source.** Max ne l'édite jamais : une correction se fait dans le bloc concerné, puis on régénère. Régénérable autant de fois que voulu.

Après génération, vérifier qu'aucune ligne des blocs sources n'est absente du final.

## 11-a-verifier.md

Rempli par Claude seul, pendant le rangement, sur faits observés uniquement.

Ce qui s'y note : contradiction entre deux passages, affirmation technique douteuse ou fausse, tâche annoncée jamais faite, doublon, écart avec les pratiques pro.

Ce qui ne s'y note pas : une notion que Max n'a pas encore vue (ça va dans `📚 Théorie non pratiquée`), un bug résolu (ça va dans `02-bugs.md`).

Une ligne résolue est barrée, jamais supprimée. Ce fichier alimente `❓ Questions pour le mentor`.

## ETAT.md

Court, 20 lignes maximum. Régénéré par Claude en fin de session à partir des fichiers du projet actif. Max ne l'écrit jamais lui-même, il le colle en Chat quand sa question dépend du contexte.

Contient : projet actif et étape, projets validés, dernier commit, en cours, bloqué sur, dettes, prochaine action.

## Git

Dépôt de notes, séparé des dépôts de projets OC. Commits conventionnels, message en anglais avec traduction française. Ouvrir le skill `git-commit` avant tout commit.

Avant toute commande destructive (`Remove-Item`, `git reset --hard`, `git restore`, `git clean`, `>`) : expliquer ce qui sera perdu, demander confirmation, proposer une alternative non destructive.

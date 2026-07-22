# bilan-oc, instructions de dossier

Ce fichier décrit **où et comment écrire**. Le comportement pédagogique, intégrité OC, niveau d'aide, ton, reste dans `prompt-OC/prompt-oc-v8.md`, chargé comme instructions du projet Claude "Intégrateur Web". Ne pas dupliquer ici.

## Ma mission

Ce fichier gouverne les sessions Cowork, où Claude range les notes. Il n'enseigne pas et ne guide aucun code : c'est le rôle du Chat. `prompt-OC/prompt-oc-v8.md` est un fichier de ce dépôt, pas des instructions.

1. Ranger `_inbox.md` : le lire en entier avant de classer, archiver le brut dans `_deltas/NN-AAAA-MM-JJ-sujet.md`, répartir chaque passage dans son bloc.

2. Ajouter à la suite, jamais écraser. Fusionner par sous-section, jamais par étape.

3. Lancer `fusionne-sous-sections.py` sur les blocs touchés, régénérer `ETAT.md`, vider `_inbox.md`.

4. Noter les incohérences observées dans `11-a-verifier.md`, faits seulement.

5. Générer `99-bilan-final.md` et `99-bilan-final-lisible.md` sur demande.

6. Clôturer un projet uniquement quand Max le déclare terminé, sous les trois conditions décrites plus bas, avec confirmation fichier par fichier.

7. Méta-travail : prompt, templates, audits, `CLAUDE.md`, `README.md`.

8. Réutiliser les scripts de `_scripts/`, ne pas les réécrire.

9. `01-journal.md` ne contient que les mots de Max, orthographe corrigée, jamais reformulés.

10. Une information, un seul endroit : renvoyer au bloc source plutôt que recopier.

11. Respecter le format de référence : pas de tiret cadratin, mots-clés `français` · `english`, une ligne vide entre les entrées.

12. Ouvrir le skill `git-commit` avant tout commit.

13. Protocole complet avant toute commande destructive. Vérifier avec `git ls-files` avant d'annoncer qu'une suppression est réversible.

14. Ne rien modifier sans demander. En cas de doute, demander plutôt que deviner.

> **Commandes Git.** Ne pas les lancer depuis le sandbox, elles laissent un `.git/index.lock` que Max doit supprimer à la main. Les lui donner à lancer dans PowerShell.

## Ce que contient ce dossier

```
CLAUDE.md        ce fichier
ETAT.md          état du projet actif, court, à coller en Chat
README.md        index des 12 projets
.gitattributes   fins de ligne, LF dans le dépôt, natif sur le disque
_scripts/        génération des bilans, à réutiliser, ne pas réécrire
_template/       blocs vierges à copier pour un nouveau projet
_archive/        vide. Réservé aux fiches d'origine d'un futur découpage.
prompt-OC/       le prompt du projet Claude et son histoire, rien d'autre
templates/       ce qui décrit la fiche projet, chargé en contexte
preferences/     préférences Claude, tous projets confondus
p01/ ... p12/    un dossier par projet
```

> **`_template/` et `templates/` ne sont pas la même chose.** `_template/` contient les blocs vierges à copier sur le disque pour démarrer un projet. `templates/` décrit ces blocs, ce qui va dedans et qui les remplit : il se charge en contexte, il ne se copie pas.

## prompt-OC/

Le prompt qui gouverne les sessions Chat, et rien d'autre. Ce dossier n'est pas un dossier projet. Ce qui n'est pas du prompt en est sorti : les templates de fiche dans `templates/`, les préférences dans `preferences/`.

| Fichier | Rôle | Où il sert |
| --- | --- | --- |
| `prompt-oc-v8.md` | **version active** | instructions du projet Claude |
| `prompt-oc-v1.md` à `v7` | archives | ici, ne jamais modifier |
| `audits.md` | journal des échecs mesurés en session | ici, jamais chargé en contexte |
| `evolution.md` | historique v1 à v8 | ici, jamais chargé en contexte |

## templates/ et preferences/

| Fichier | Rôle | Où il sert |
| --- | --- | --- |
| `templates/fiche-template-minimal.md` | liste des blocs, qui les remplit | documents de contexte du projet |
| `templates/fiche-template-complet.md` | format exact de chaque bloc | documents de contexte du projet |
| `preferences/preferences-personnalisees.md` | copie des préférences Claude | réglages Claude, tous projets |

**Une seule version active.** Une correction se fait dans `prompt-oc-v8.md`, jamais dans une archive. Une refonte crée `prompt-oc-v9.md` et laisse la v8 intacte.

**`audits.md` ne se charge jamais en contexte.** Me donner mes échecs passés avant de m'auto-évaluer biaiserait l'audit. Max colle le résultat lui-même.

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
| `05-bilan.md`, ➡️ À revoir, par priorité | **le plan d'action**, l'ordre dans lequel les traiter |
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

**Qui tient le stylo.** La répartition bloc par bloc est dans `templates/fiche-template-minimal.md`, colonne "Qui écrit". Source unique, ne pas la recopier ici.

Une seule règle mérite d'être rappelée : `01-journal.md` ne contient que les mots de Max, orthographe corrigée, jamais reformulés. Claude pose la question, Max écrit. Pas de réponse, le bloc reste vide.

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
   - lance `fusionne-sous-sections.py` sur les blocs touchés
   - régénère `ETAT.md`
   - vide `_inbox.md` (le fichier reste, seul le contenu part)

En cas de doute sur la destination d'un passage, demander plutôt que deviner.

## _scripts/

Les scripts de génération existent déjà, les réutiliser plutôt que d'en réécrire :

| Script | Sortie | Quand |
| --- | --- | --- |
| `python3 _scripts/fusionne-sous-sections.py pXX/03-connaissances.md` | fusionne les `###` de même nom | après chaque rangement d'inbox |
| `bash _scripts/build-final.sh pXX` | `99-bilan-final.md`, concaténation brute | sur demande, et à la clôture |
| `python3 _scripts/build-lisible.py pXX` | `99-bilan-final-lisible.md`, version réorganisée | sur demande, et à la clôture |

Les deux derniers produisent une sortie régénérable : inutile de les lancer à chaque session.

## 99-bilan-final.md

Généré par Claude en fin de projet, sur demande, par concaténation des blocs dans l'ordre numérique. Sert à la soutenance, au bilan mentor, ou à un export Notion en une fois.

**C'est une sortie, pas une source.** Max ne l'édite jamais : une correction se fait dans le bloc concerné, puis on régénère. Régénérable autant de fois que voulu.

Le contrôle des lignes manquantes est décrit à la clôture d'un projet, il vaut à chaque génération.

## Clôture d'un projet

Quand un projet est terminé et validé, il ne reste que `99-bilan-final.md` et `99-bilan-final-lisible.md`. Tout le reste est supprimé : les douze blocs, `_inbox.md`, `_deltas/`.

**Trois conditions, dans cet ordre. Aucune ne se saute.**

1. **Max le déclare terminé explicitement.** Claude ne décide jamais qu'un projet est fini, même si tout semble coché.
2. **Les deux fichiers finaux sont suivis par Git.** Vérifier avec `git ls-files pXX/` avant toute suppression. Ils ont été retirés du `.gitignore` le 22 juillet 2026, précisément pour que la clôture archive le projet au lieu de le faire disparaître.
3. **Régénérer puis vérifier.** Lancer `build-final.sh` et `build-lisible.py`, puis contrôler qu'aucune ligne des blocs sources n'est absente des deux finaux. Comparaison ligne à ligne, pas au jugé.

Ensuite seulement, suppression, avec confirmation de Max fichier par fichier.

> **Le contrôle du point 3 n'est pas une formalité.** Une fois les blocs supprimés, ce qui manque au final est perdu.

---

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

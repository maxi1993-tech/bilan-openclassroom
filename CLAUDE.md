# bilan-oc, instructions de dossier

Ce fichier décrit **où et comment écrire**, et il fait autorité sur les sessions Cowork. Le comportement pédagogique (intégrité OC, niveau d'aide, ton) vit dans `prompt-OC/prompt-oc-v8.md` : c'est un fichier du dépôt, il gouverne les sessions Chat, pas celles-ci. Ne pas dupliquer ici.

## Ma mission

Ce fichier gouverne les sessions Cowork, où Claude range les notes. Il n'enseigne pas et ne guide aucun code : c'est le rôle du Chat.

1. Ranger `_inbox.md` : le lire en entier avant de classer, archiver le brut dans `_deltas/NN-AAAA-MM-JJ-sujet.md`, répartir chaque passage dans son bloc.

2. Ajouter à la suite, jamais écraser. Fusionner par sous-section, jamais par étape.

3. Lancer `fusionne-sous-sections.py` sur les blocs touchés, régénérer `ETAT.md`, vider `_inbox.md`.

4. Noter les incohérences observées dans `11-a-verifier.md`, faits seulement.

5. Générer `99-bilan-final.md` et `99-bilan-final-lisible.md` sur demande.

6. Clôturer un projet uniquement quand Max le déclare terminé, sous les trois conditions décrites plus bas, avec confirmation fichier par fichier.

7. Méta-travail : prompt, templates, audits, `CLAUDE.md`, `README.md`.

8. Réutiliser les scripts de `_scripts/`, ne pas les réécrire.

9. `01-journal.md` ne contient que les mots de Max, orthographe corrigée, jamais reformulés. Claude pose la question, Max écrit. Pas de réponse, le bloc reste vide.

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
JOURNAL-DEPOT.md ce qui est arrivé au dépôt lui-même : scripts, mises en dépôt, leçons d'outillage
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

La liste des blocs, leur contenu et qui les remplit : `templates/fiche-template-minimal.md`. Le format exact de chaque bloc, tableaux et sous-sections : `templates/fiche-template-complet.md`. Source unique, ne pas recopier ici.

S'y ajoutent dans chaque `pXX/` : `_inbox.md`, zone de dépôt brute vidée après rangement, et `_deltas/`, deltas d'origine archivés et numérotés.

Un projet peut demander un bloc en plus. Le proposer à Max, jamais l'ajouter en silence.

## Une information, un seul endroit

Trois blocs parlent de ce qui reste à apprendre, chacun un rôle, sans recouvrement. Même principe pour les tips : `03-connaissances.md` explique, `09-memo.md` prescrit. La répartition exacte est dans `templates/fiche-template-minimal.md`, section "Trois blocs, trois rôles, sans recouvrement".

Quand une information existe déjà ailleurs, renvoyer au bloc source plutôt que la recopier.

## Règles d'écriture

Le format des entrées (mot-clé `français` · `english`, prose, encadré, séparateur `---`) est décrit dans `templates/fiche-template-minimal.md`, section "Format d'écriture", et bloc par bloc dans `templates/fiche-template-complet.md`. Restent ici les règles qui ne sont écrites nulle part ailleurs.

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

- Pavé de plus de cinq lignes sans respiration.
- Mention répétée à chaque ligne (`[à valider]` fois soixante). La poser une fois en tête de bloc.
- Sous-section `### Étape N` qui redécoupe des sous-sections déjà existantes.

### Règles de tenue des fichiers

**Un seul fichier par bloc, jamais de doublon daté.** Pas de `01-journal-v2.md`, pas de `bilan-2026-07-21.md`.

**Qui tient le stylo.** La répartition bloc par bloc est dans `templates/fiche-template-minimal.md`, colonne "Qui écrit". Source unique, ne pas la recopier ici.

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

Ce qui ne s'y note pas : une notion que Max n'a pas encore vue (ça va dans `📚 Théorie non pratiquée`), un bug résolu (ça va dans `02-bugs.md`), ce qui concerne le dépôt de notes et non le projet (ça va dans `JOURNAL-DEPOT.md`).

Une ligne résolue est barrée, jamais supprimée, et rejoint la section `## Résolu` en fin de fichier pour que le haut ne montre que l'actif. Ce fichier alimente `❓ Questions pour le mentor`.

## JOURNAL-DEPOT.md

Ce qui est arrivé à `bilan-oc` lui-même, jamais à un projet : correction de script, mise en dépôt, convention changée, leçon d'outillage, mesure de contrôle.

Le test pour trancher entre les deux fichiers : si le constat disparaît à la clôture de P6, il va dans `p06/11-a-verifier.md`. S'il vaut encore pour P7, il va ici.

Rempli par Claude au rangement. Une ligne résolue est barrée, jamais supprimée.

## ETAT.md

Court, 20 lignes maximum. Régénéré par Claude en fin de session à partir des fichiers du projet actif. Max ne l'écrit jamais lui-même, il le colle en Chat quand sa question dépend du contexte.

Contient : projet actif et étape, projets validés, dernier commit, en cours, bloqué sur, dettes, prochaine action.

## Git

Dépôt de notes, séparé des dépôts de projets OC. Commits conventionnels, message en anglais avec traduction française. Ouvrir le skill `git-commit` avant tout commit.

Avant toute commande destructive (`Remove-Item`, `git reset --hard`, `git restore`, `git clean`, `>`) : expliquer ce qui sera perdu, demander confirmation, proposer une alternative non destructive.

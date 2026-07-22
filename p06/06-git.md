## Commit

> Relevé avec `git log --oneline`. Message en anglais, traduction française à côté.

| Hash | Type | Message | Traduction |
| --- | --- | --- | --- |
| `87ea86d` | `feat` | add style to filter buttons | ajouter le style des boutons de filtre |
| `3e1f4e5` | `refactor` | split filter script into two functions | séparer le script des filtres en deux fonctions |
| `4c23113` | `feat` | add filter buttons from API | ajouter les boutons de filtre depuis l'API |
| `2fd429c` | `feat` | display works from API | afficher les travaux depuis l'API |
| `85f4ea2` | `chore` | untrack .env | sortir .env du suivi |
| `0d5d46d` | `chore` | initial project setup | mise en place initiale du projet |

Six commits, un sujet par commit.

**Étape 3** · trois commits atomiques, un par nature de changement : la fonctionnalité, le refactor, le style.

**Étape 4**

| Hash | Type | Message | Traduction |
| --- | --- | --- | --- |
| `87ad631` | `wip` | reorganize file and handle fetch errors | réorganiser le fichier et gérer les erreurs |
| `b78f0d1` | `feat` | rename filter-button and listen to filter clicks | renommer filter-button et écouter le clic sur les filtres |

> `87ad631` est un `wip:` assumé · réorganisation et gestion d'erreur se croisent sur les mêmes lignes, `git add --patch` n'a pas permis de les séparer proprement. Justification dans `04-choix-techniques.md`.

---

## État Git

**Branche** `main`, à jour avec `origin/main`.

**Étape 4** · tout est commité et poussé.

> Cinq `console.log` de debug conservés volontairement dans le fichier commité, à retirer avant le commit de fin d'étape.

---

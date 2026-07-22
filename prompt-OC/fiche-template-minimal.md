# Fiche projet, template minimal

Les douze blocs d'une fiche projet. Un fichier par bloc dans `pXX/`. Le delta de fin de session se range sous ces titres.

Pour le format exact d'un bloc, tableaux et sous-sections, voir `fiche-template-complet.md`.

| Bloc | Contenu | Qui écrit |
| --- | --- | --- |
| `00-cadrage` | mission, specs, todo, pièges, ce qu'il faut maîtriser | Claude propose, Max valide |
| `01-journal` | 🧩 Pseudocode, 🗣️ Explication ligne par ligne | Max seul |
| `02-bugs` | `symptôme → cause → correction` | Claude seul |
| `03-connaissances` | 🧠 Nouvelles connaissances, 📚 Théorie non pratiquée | Claude seul |
| `04-choix-techniques` | `décision → pourquoi` | Claude propose, Max valide |
| `05-bilan` | 📐 Formule, 📊 Validation outils, 🔍 Vérification, 📋 Bilan mentor, ❓ Questions | Claude propose, Max valide |
| `06-git` | commits, état Git | Claude seul |
| `07-synthese` | ce que je maîtrise, erreurs récurrentes, découvertes | Claude propose, Max valide |
| `08-soutenance` | préparation, seulement si le projet est évalué en soutenance | Claude propose, Max valide |
| `09-memo` | 💡 Tips par concept, 📖 Lexique | Claude seul |
| `10-point-de-reprise` | où j'en suis, en détail | Claude seul |
| `11-a-verifier` | incohérences relevées, rempli au rangement, pas en session Chat | ne pas remplir en Chat |

## Trois blocs, trois rôles, sans recouvrement

`03-connaissances`, 📚 Théorie non pratiquée est le catalogue des notions non acquises. `05-bilan`, ➡️ À revoir par priorité est le plan d'action, l'ordre dans lequel les traiter. `07-synthese`, Ce qui reste à revoir est un renvoi, jamais une liste.

Même principe pour les tips : `03-connaissances` explique la notion, `09-memo` prescrit un réflexe et n'explique jamais.

## Format d'écriture

Mot-clé français, point médian, mot-clé anglais, les deux en `code`, puis une ou deux phrases en prose, puis un séparateur.

```
`portée des variables` · `scope`

Une variable déclarée dans un bloc n'existe pas en dehors.

> **Vu, pas acquis.** À reprendre sur exo dédié.

---
```

Ni tiret cadratin ni demi-cadratin. Point médian `·` pour séparer dans une ligne, flèche `→` pour une conséquence ou un renvoi.

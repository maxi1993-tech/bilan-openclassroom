## 🧭 Bilan technique (synthèse)

### Ce que je maîtrise

**API et asynchrone**

- `fetch` en GET et la chaîne `.then` / `.json()`, y compris le rôle du `Response` et du flux.

**Boucles**

- `forEach` pour parcourir un tableau d'objets, et pourquoi il ne renvoie rien.
- La différence avec `for...of`, interruption par `break`.

**Injection DOM**

- `createElement`, `setAttribute`, `textContent`, `appendChild`, `querySelector`.
- L'ordre des `appendChild` et pourquoi il est indifférent.
- Templates littéraux et interpolation avec `${}`.
- Les quatre positions de `insertAdjacentHTML`.

**Architecture**

- Le choix entre HTML statique et génération JS, et sa justification.
- Le principe de responsabilité unique appliqué à un découpage en fonctions.

**CSS**

- La portée d'un sélecteur et l'intérêt d'une classe dédiée.

**Chargement**

- `defer` et ce qui casserait sans lui.

**Git**

- `git rm --cached` et la logique suivi / ignoré.
- Commit conventionnel propre, historique lisible.

---

### Erreurs qui reviennent

| Erreur | Domaine |
| --- | --- |
| Passer une chaîne `"imageUrl"` au lieu de la valeur `work.imageUrl` | valeur contre littéral |
| Oublier les accolades quand la fonction fléchée a plusieurs lignes | syntaxe |
| Oublier les parenthèses d'appel d'une fonction | appel contre référence |
| Inverser le sens de `appendChild` | DOM |
| Placer les créations hors du `forEach` | portée |
| Placer une instruction hors du bloc où sa variable est déclarée | portée |
| Écrire dans la variable du callback au lieu d'une variable dédiée | portée |
| Modifier une règle CSS sans reporter sur tous les éléments concernés | cohérence |
| Répondre "je sais pas" avant d'avoir cherché ou observé | méthode |

> Trois des neuf erreurs relèvent de la portée des variables. C'est le point à travailler en priorité après l'asynchrone.

---

### Ce que j'ai découvert sur ce projet

- La chaîne `fetch` complète et le fonctionnement d'une promesse
- le `ReadableStream` du corps de réponse
- l'injection DOM from scratch
- l'attribut `defer`
- les templates littéraux et `insertAdjacentHTML`
- le principe de responsabilité unique
- le connecteur Figma et la duplication de maquette en lecture seule
- le diagnostic d'un port occupé sous PowerShell

---

### Ce qui reste à revoir

> Une seule source : `05-bilan.md`, bloc `➡️ À revoir, par priorité`.
> Le catalogue des notions elles-mêmes est dans `03-connaissances.md`, bloc `📚 Théorie non pratiquée`.

---

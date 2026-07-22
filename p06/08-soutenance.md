## 🎤 Préparation soutenance

> Projet évalué en soutenance. Bloc actif.
> Format : 15 min de présentation, 10 min de discussion, 5 min de débriefing. Timer conseillé, rappel du mentor en P3.

**Légende** · `[x]` sait l'expliquer · `[~]` base acquise, à consolider · `[ ]` pas encore

---

### Expliquer le fonctionnement

- [~] Les appels API et la récupération des données → base acquise : `fetch`, chaîne `.then`, `Response`, `.json()`, structure de `works` et `categories`
- [~] Le fonctionnement du filtre → l'affichage des boutons est maîtrisé et justifié, le filtrage au clic reste à faire (étape 4)
- [ ] La gestion de la connexion, différence connecté et non connecté
- [ ] L'envoi de nouvelles images à l'API

---

### Expliquer le timing du fetch

> Le point le plus probable en discussion, parce que c'est le sujet où j'ai le plus buté.

- [ ] Pourquoi les écouteurs ne peuvent pas être branchés en haut du fichier
- [ ] Pourquoi les trois appels ne peuvent pas être groupés en bas du fichier, chronologie à l'appui
- [ ] Pourquoi les trois fonctions ont bien trois appels, et pourquoi un seul ne peut pas être déplacé
- [ ] Pourquoi `fetchCategories()` est appelée à la main et `createButtons` non
- [ ] Pourquoi une absence d'erreur dans la console ne prouve pas l'absence de bug

---

### Justifier mes choix

- [~] `forEach` plutôt que `map` pour la génération DOM
- [ ] `insertAdjacentHTML` plutôt que `createElement`, et les quatre positions
- [ ] Le découpage en deux fonctions, responsabilité unique
- [ ] L'extraction de `listenFilterButtons`, même principe
- [ ] Vider et reconstruire la galerie plutôt que trier les figures affichées
- [ ] Garder volontairement deux méthodes de génération DOM

---

### Justifier la sémantique et l'accessibilité

- [ ] `ul` plutôt que `div`, et `button` plutôt qu'un lien
- [ ] L'avertissement W3C sur `#introduction` : `article` est un élément de sectionnement

---

### Justifier la méthode

- [~] L'usage de Git et des commits → historique propre, format conventionnel, un commit atomique par sujet

---

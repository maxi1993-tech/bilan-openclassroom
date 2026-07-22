## 💡 Tips

> **Ce bloc prescrit, il n'explique pas.** L'explication d'une notion vit dans `03-connaissances.md` et nulle part ailleurs.
> Ici, uniquement des réflexes : ce qu'il ne faut pas faire, ce qu'il faut faire. Deux lignes par concept.

---

### `fetch` et asynchrone

- **À éviter** · appeler une fonction qui dépend des données ailleurs que dans la chaîne `.then`. Elle s'exécute avant l'arrivée de la réponse, sans lever d'erreur.
- **À faire** · un `console.log` avant le `fetch`, un après, un dans le `.then`. L'ordre d'affichage prouve l'asynchrone.

---

### Génération d'éléments en JS

- **À éviter** · `innerHTML =` dans une boucle. Chaque tour écrase le précédent.
- **À faire** · traiter un élément généré en JS avec la même exigence qu'un élément écrit à la main : `alt`, sémantique, clavier, focus.

---

### Sélection dans le DOM

- **À éviter** · récupérer en haut du fichier un élément qui sera créé plus tard par JS.
- **À faire** · ce qui existe dans le HTML se récupère en haut du fichier, ce qui est créé par JS se récupère après sa création.

---

### Écouteurs d'événements

- **À éviter** · passer `maFonction(...)` à un `forEach`. Les parenthèses exécutent l'appel immédiatement.
- **À faire** · envisager un écouteur unique sur le conteneur avec `event.target`. Le conteneur existe dès le chargement.

---

### Portée des variables

- **À éviter** · réaffecter la variable du callback. Ça détruit la donnée du tour en cours.
- **À faire** · vérifier que l'instruction et la déclaration de sa variable vivent dans le même bloc. Trois des neuf erreurs récurrentes de ce projet viennent de là.

---

### Sémantique HTML

- **À éviter** · un `nav` pour des filtres. `nav` sert à aller ailleurs, un filtre agit sur place.
- **À faire** · une liste de commandes dans un `ul`, jamais un `div`. Le lecteur d'écran annonce le nombre d'éléments et la position.

---

### CSS

- **À éviter** · styler un sélecteur de type. Tous les futurs boutons hériteront du style.
- **À faire** · renommer une classe dans le JS et dans le CSS dans le même mouvement. L'oubli est arrivé deux fois sur ce projet.

---

### Git

- **À éviter** · commiter sans relire le diff quand l'éditeur formate à la sauvegarde.
- **À faire** · penser le `.gitignore` avant le premier `git add`, jamais après.

---

### Backend local

- **À éviter** · fermer le terminal à la croix, et `npm audit fix --force` sur un backend fourni.
- **À faire** · arrêter avec `Ctrl + C`. Port bloqué : `Get-NetTCPConnection -LocalPort 5678 -State Listen` donne le PID.

---

### Débogage

- **À éviter** · placer les `console.log` après la ligne suspecte. Une erreur non rattrapée interrompt le fichier.
- **À faire** · comparer un `console.log` immédiat et le même dans un `setTimeout`. Ça prouve un problème de timing au lieu de le supposer.

---

### Méthode de travail

- **À éviter** · coder la suite quand on ne sait pas expliquer ce qui est déjà écrit.
- **À faire** · pseudocode en français avant toute ligne de code, puis relire l'écart entre le pseudocode et le code final.

---

## 📖 Lexique

> Un terme, une définition d'une ligne. Les notions qui demandent une explication sont dans `03-connaissances.md`.

### API et asynchrone

| Terme | Définition |
| --- | --- |
| `Swagger` | interface de documentation d'une API, permet de tester ses routes en direct |
| `Promise` | objet renvoyé par `fetch`, représente une donnée à venir. États : `pending`, `fulfilled`, `rejected` |
| `Response` | enveloppe de la réponse HTTP, arrive avant que le corps soit téléchargé |
| `ReadableStream` | flux de données brutes, contenu de `Response.body` avant conversion |
| `token` | jeton d'authentification renvoyé après login, à renvoyer pour les actions protégées |
| `FormData` | objet JS pour construire des données de formulaire à envoyer, notamment avec fichier |

### JavaScript

| Terme | Définition |
| --- | --- |
| `callback` | fonction passée en argument à une autre, exécutée par elle. Exemple : la fonction dans `forEach` ou dans `.then` |
| `template literal` | chaîne délimitée par des backticks, acceptant `${}` et les retours à la ligne |
| `interpolation` | insertion d'une valeur dans une chaîne avec `${}` |
| `NodeList` | liste d'éléments renvoyée par `querySelectorAll`, parcourable avec `forEach` |
| `insertAdjacentHTML` | méthode qui interprète une chaîne comme du HTML et l'insère à une position donnée |
| `dataset` | accès JS aux attributs `data-*` d'un élément, via `element.dataset.nom` |
| `responsabilité unique` | principe selon lequel une fonction ne fait qu'un seul travail |

### Chargement

| Terme | Définition |
| --- | --- |
| `defer` | attribut de `<script>` qui exécute le script une fois tout le HTML chargé |

### Outils

| Terme | Définition |
| --- | --- |
| `git graph` | vue arborescente de l'historique Git, montre branches, merges et divergences. Extension VS Code, ou `git log --graph --oneline --all` |
| `jsbench` | outil en ligne de mesure de performance JavaScript, compare la vitesse de plusieurs écritures d'un même traitement |
| `PID` | identifiant numérique d'un processus en cours d'exécution |
| `axe DevTools` | extension navigateur d'audit d'accessibilité automatisé |
| `Lighthouse` | audit intégré à Chrome : performance, accessibilité, bonnes pratiques, SEO |
| `NVDA` | lecteur d'écran gratuit sous Windows, sert à tester le rendu vocal réel |

---

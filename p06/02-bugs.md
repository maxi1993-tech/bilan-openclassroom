## 🐛 Journal de bugs

> Lecture en trois temps. **Symptôme** ce que j'ai vu, **cause** ce qui le provoquait vraiment, **correction** ce que j'ai changé.

---

### Étape 2 et setup

**`undefined` affiché en trop** · `console.log(donnees.forEach(...))`

- **Cause** · `forEach` ne renvoie rien, le log extérieur affichait ce retour vide.
- **Correction** · retirer le `console.log` extérieur, garder celui dans le `forEach`.

---

**Erreur de syntaxe** · plusieurs lignes après `work =>`

- **Cause** · la flèche courte n'accepte qu'une seule expression.
- **Correction** · accolades `{ }` après la flèche pour un bloc multi-lignes.

---

**`setAttribute` sans effet** · rangé dans un `const`, un seul argument

- **Cause** · `setAttribute` ne renvoie rien et attend deux arguments (nom, valeur).
- **Correction** · retirer le `const`, ajouter la valeur `work.imageUrl`.

---

**Image cassée** · `src` rempli avec `"imageUrl"`

- **Cause** · les guillemets passent la chaîne littérale au lieu de la valeur.
- **Correction** · `work.imageUrl` sans guillemets.

---

**Rien ne s'accroche** · `project.appendChild(".gallery")`

- **Cause** · sens inversé, et une chaîne passée au lieu d'un élément.
- **Correction** · `gallery.appendChild(project)`, passer la variable, pas une string.

---

**Une seule figure générée** · créations placées hors du `forEach`

- **Cause** · `work` n'existe que dans le `forEach`, et le code ne se répétait pas.
- **Correction** · déplacer les créations dans le `forEach`.

---

**`git diff` vide** · sur `index.html` pourtant modifié

- **Cause** · le fichier était déjà stagé, `git add` avait été fait.
- **Correction** · `git diff --cached` pour voir le contenu stagé.

---

**`port: 5678 is already in use`** · au `npm start` suivant, après avoir fermé PowerShell à la croix

- **Cause** · fermer la fenêtre ne tue pas toujours le processus Node, qui continue d'occuper le port.
- **Correction** · `Get-NetTCPConnection -LocalPort 5678 -State Listen` pour trouver le PID, puis `Stop-Process -Id <PID>`.

> Prévention · arrêter le backend avec `Ctrl + C`, jamais à la croix.

---

**Deux backends en parallèle** · sans s'en rendre compte

- **Cause** · un terminal oublié en arrière-plan.
- **Correction** · vérifier avant de relancer. Un seul backend doit tourner.

---

### Étape 3

**Ordre des boutons inversé** · `insertAdjacentHTML("afterbegin", ...)` dans le `forEach`

- **Cause** · chaque nouveau bouton se posait en tête, `Tous` finissait en dernier.
- **Correction** · `beforeend` dans le `forEach`, `afterbegin` conservé pour `Tous` seul.

---

**Rien ne s'affiche** · `categorie = ...` dans le `forEach`

- **Cause** · la réaffectation écrasait la donnée du tour en cours, `${categorie.name}` ne pouvait plus fonctionner.
- **Correction** · ranger le HTML dans une variable dédiée (`buttonCategorie`), puis appeler `filters.insertAdjacentHTML`.

---

**Autant de boutons `Tous` que de catégories** · ligne placée dans le `forEach`

- **Cause** · elle s'exécutait une fois par tour de boucle.
- **Correction** · la sortir de la boucle, avant le `forEach`.

---

**Variables inaccessibles** · lignes `insertAdjacentHTML` écrites hors de la fonction

- **Cause** · `buttonAll` et `buttonCategorie` sont déclarés à l'intérieur.
- **Correction** · replacer chaque insertion dans le bloc où sa variable est déclarée.

---

**`.then` de trop** · écrit à l'intérieur de `createButtons`

- **Cause** · un `.then` s'accroche à une promesse, or `donnees` y est déjà le tableau.
- **Correction** · retirer le `.then`, garder le `forEach` seul.

---

**Fonction jamais appelée** · `.then(donnees => createButtons)`

- **Cause** · sans les parenthèses, la fonction est seulement nommée, pas appelée.
- **Correction** · `createButtons(donnees)`.

---

**Guillemets affichés à l'écran** · autour de `${categorie.name}` dans le template

- **Cause** · les guillemets font partie de la chaîne produite.
- **Correction** · guillemets retirés.

---

**Style qui déborde** · écrit sur le sélecteur `button`

- **Cause** · aurait touché tous les futurs boutons du projet (login, modale, ajout).
- **Correction** · classe dédiée sur les boutons de filtre, sélecteur CSS corrigé.

---

**Style partiellement appliqué** · sélecteur corrigé mais classe absente du bouton `Tous`

- **Cause** · seul le HTML des catégories avait été modifié.
- **Correction** · ajouter la classe sur les deux.

---

**`git diff` illisible** · `style.css` entièrement reformaté à la sauvegarde

- **Cause** · formatage automatique de l'éditeur, déjà rencontré en P4.
- **Correction** · fichier restauré à son formatage d'origine avant commit.

---

**Piège identifié, pas vécu** · repéré sur l'exemple du mentor

`innerHTML =` à l'intérieur d'une boucle écrase le contenu à chaque tour, seul le dernier élément reste affiché.

- **Deux solutions** · empiler dans une variable avec `+=` puis injecter une seule fois après la boucle, ou utiliser `insertAdjacentHTML` qui ajoute sans écraser.

---

### Étape 4

**`Cannot read properties of null (reading 'forEach')`**

- **Cause** · `querySelector` des boutons placé en haut du fichier, exécuté avant le retour du `fetch`, donc avant que les boutons existent.
- **Correction** · déplacer la récupération dans `createButtons`, après les `insertAdjacentHTML`.

> Preuve obtenue en console · un `console.log` au chargement affiche `null`, le même dans un `setTimeout` de 2 secondes affiche le bouton.

---

**`filterButton is not defined`**

- **Cause** · la variable est déclarée dans `createButtons`, la ligne qui l'utilise était restée en bas du fichier.
- **Correction** · déplacer l'instruction dans le même bloc que la déclaration. Même règle de portée que celle déjà notée depuis P5.

---

**`filterButton.forEach is not a function`**

- **Cause** · `querySelector` ne renvoie qu'un seul élément, pas une liste.
- **Correction** · `querySelectorAll`, qui renvoie une `NodeList` parcourable.

> Vérifié en console · un `button` d'un côté, `NodeList(4)` de l'autre.

---

**`addEventListener: 2 arguments required, but only 1 present`**

- **Cause** · appel écrit sans son deuxième argument, la fonction à exécuter.

---

**`undefined is not a function`** · sur `filterButton.forEach(filters.addEventListener("click", ...))`

- **Cause** · `addEventListener(...)` avec ses parenthèses est un appel, exécuté immédiatement, dont le résultat (`undefined`) était passé à `forEach`. Or `forEach` attend une fonction.
- **Correction** · passer une fonction à `forEach` (`button => { ... }`) et mettre l'appel `addEventListener` dans son corps.

> Symétrique du bug de l'étape 3, où `createButtons` sans parenthèses ne l'appelait pas.

---

**Un seul écouteur au lieu de quatre** · posé sur `filters` au lieu de `button`

- **Cause** · `filters` est le conteneur, alors que le `forEach` tend un bouton à chaque tour.
- **Correction** · poser l'écouteur sur `button`.

---

**Style disparu** · classe renommée `filter-button` dans le JS sans reporter dans le CSS

- **Cause** · répétition exacte du bug de l'étape 3, sélecteur corrigé mais pas la classe.
- **Correction** · report fait en session suivante.

---

**Boucle infinie** · `createButtons()` écrit à la fin de `createButtons`

- **Cause** · la fonction s'appelait elle-même. Bouton `Tous` reposé, puis plantage faute de données.
- **Correction** · écrire le nom de la fonction voulue, pas celui de la fonction courante.

---

**`undefined` dans la console** · `console.log(listenFilterButtons())`

- **Cause** · ce n'est pas une erreur. C'est ce que renvoie une fonction qui ne retourne rien, règle déjà notée à l'étape 2.
- **Correction** · retirer le `console.log` autour, garder l'appel seul.

---

**Console muette, aucune erreur** · `listenFilterButtons()` appelée en bas du fichier

- **Cause** · la ligne s'exécute avant le retour du `fetch`. `querySelectorAll` ne trouve rien, le `forEach` tourne zéro fois.
- **Correction** · replacer l'appel dans `createButtons`.

> **Absence d'erreur ne veut pas dire absence de bug.** Le bug le plus long de l'étape 4 n'a produit aucun message rouge.

---

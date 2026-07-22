## 🧩 Pseudocode

> Écrit en français avant chaque étape. Ce bloc ne contient que tes mots.

**Étape 2, galerie dynamique**

*Pseudocode :*

1. J'attrape la galerie avec querySelector.
2. Je récupère les données (les works) du backend.
3. Avec forEach, je parcours chaque travail, un par un.

Pour un travail :

- je crée une `figure` que j'accroche sur la classe `gallery`
- je crée une `img`, je l'accroche à `figure` et je lui passe l'`imageUrl` (dans `src`) puis lui passe `title` (dans `alt`)
- je crée une `figcaption`, je l'accroche à `figure` et je lui passe le `title`

*Écarts entre le pseudocode et le code final, et pourquoi :*

- Aucun écart de logique. Ajusté seulement l'ordre pour placer "attraper la galerie" et "récupérer les données" avant la boucle (une seule fois), et les créations dans le forEach (répétées à chaque travail).

**Étape 3, filtres par catégorie**

*Pseudocode, première version :*

```
1. recuperer class .filters (ul)
2. creer filter tous
3. demande fetch sur http://localhost:5678/api/categories
4. recuperer response avec .json
5. donnees.forEach
6. creer balise li
7. creer balise button type button
8. ajouter text au button
9. accrocher li a ul et button a li
```

*Pseudocode révisé, après la décision template littéral + `insertAdjacentHTML` :*

```
1. recuperer class .filters (ul)
2. creer filter tous
3. demande fetch sur http://localhost:5678/api/categories
4. recuperer response avec .json
5. donnees.forEach
6. construire html
7. injecter
```

*Écarts entre le pseudocode et le code final, et pourquoi :*

- Écouter les clics et filtrer l'affichage avaient été écrits au départ dans le pseudocode. Retirés : ils appartiennent à l'étape 4 du brief, pas à l'étape 3.
- Le code final répartit ces étapes dans deux fonctions (`fetchCategories` pour les lignes 3 et 4, `createButtons` pour les lignes 1, 2, 5 à 7). Découpage décidé après l'écriture du pseudocode, sur le principe de responsabilité unique.

**Étape 4, filtre fonctionnel** : à écrire avant de coder.

### Étape 4

**Étape 4, filtre fonctionnel**

*Pseudocode :*

```
1. recuperer la class filter-button-selected et filter-button
2. foreach pour écouter les click sur cette class filter-button
3. tous doit avoir tous les projets par défaut
4. je vide la galerie
5. je reconstruis la galerie avec les travaux dont la catégorie correspond à celle du bouton cliqué
6. je retire la class filter-button-selected du bouton qui l'avait, puis je la passe au bouton cliqué
```

*Avancement :* lignes 1, 2, 3 codées. Lignes 4, 5, 6 restantes.

*Écarts entre le pseudocode et le code final, et pourquoi :*

- Ligne 1 : le pseudocode parlait de récupérer les classes en une fois. Le code final range ces deux `querySelector` dans `listenFilterButtons`, appelée depuis `createButtons`, pour cause de timing du fetch.
- Suite à compléter une fois les lignes 4, 5, 6 codées.

---


## 🗣️ Explication ligne par ligne

> Ce bloc ne contient que tes mots, sans le code sous les yeux.

**Ce que fait mon script, en quelques phrases :**

On commence par cibler la classe `.gallery` (le conteneur div des figures) qu'on déclare dans une constante. On va chercher les projets avec `fetch`, qui prend la commande, me donne un ticket en retour (promise), puis me ramène les données. Une fois les données récupérées, grâce à `forEach` il parcourt chaque objet du tableau un par un et crée les balises, les place et les remplit, ainsi que les attributs.

**Comment fonctionne la chaîne fetch, dans l'ordre :**

1. `fetch("...")` part chercher les données à l'adresse donnée et renvoie une promesse (un ticket), pas les données. Comme quand on commande, on demande telle chose, le serveur va demander cette chose et nous donne un ticket pour récupérer cette commande.
2. `.then(reponse => reponse.json())` : le serveur me donne ma commande et sort les articles.
3. `.then(donnees => ...)` : je peux les utiliser, les manger.

**Ce qui se passe exactement pour un travail, dans l'ordre :**

On cible la classe `.gallery`, on lui accroche une `figure`. On accroche une `img` à la `figure` et on remplit le `src` avec `work.imageUrl` et l'`alt` avec `work.title`. On accroche une `figcaption` à la `figure` également et on la remplit avec `work.title` (la même valeur que l'alt).

**Ordre des `appendChild` :**

Non, une fois la boîte remplie on peut la déplacer complète.

**Ce que contient la réponse de fetch avant `.json()` :**

L'enveloppe avec les données.

**Ce que fait `.json()` :**

`json` lit les données brutes et les transforme en tableau d'objets.

**Pourquoi `forEach` ne renvoie rien :**

`forEach` parcourt chaque objet. Cela ne renvoie rien car pas défini.

**Pourquoi `.gitignore` ne suffit pas sur un fichier déjà suivi :**

`git rm --cached` car déjà commité.

**À quoi sert `defer` :**

`defer` pour que JS attende que le DOM soit chargé. Sans, et au-dessus, JS n'attend pas : si le DOM n'existe pas, le script non plus. Sinon juste le script en bas suffit.

**Ce que fait `insertAdjacentHTML` (tes mots, exo console) :**

Permet de placer les balises et de les interpréter en code HTML avec le contenu directement.
`beforebegin` permet de placer avant le début (balise ouvrante).
`afterbegin` permet de placer après le début (balise ouvrante).
`beforeend` permet de placer avant la fin (balise fermante).
`afterend` permet de placer après la fin (balise fermante).

**Différence entre concaténation et template littéral :**

*(à écrire avec tes mots. Tes réponses en session étaient trop courtes pour former une entrée : "la première concatène et la seconde template", "3 fois", "1 fois", "backtick permet le passage à la ligne". La notion est acquise, la formulation reste à faire.)*

**Différence `forEach` et `for...of` :**

*(à écrire avec tes mots. Réponse en session : "stopper", pour `break`. La notion est acquise, la formulation reste à faire.)*

**Étape 3, à alimenter à froid, sans le code sous les yeux :**

- le rôle de chacune des deux fonctions
- pourquoi `createButtons` reçoit `donnees` en paramètre
- pourquoi `fetchCategories()` est appelée à la main et pas `createButtons`
- ce qui se passe dans l'ordre entre le chargement de la page et l'affichage des boutons
- pourquoi `Tous` est inséré avec `afterbegin` et les catégories avec `beforeend`

### Étape 4, à alimenter à froid

Sans le code sous les yeux, à écrire avec mes mots :

- pourquoi les deux `querySelector` des boutons sont dans `createButtons` et pas en haut du fichier
- la différence entre `querySelector` et `querySelectorAll`, et laquelle permet un `forEach`
- ce que représente le mot placé avant la flèche dans un `forEach`
- pourquoi l'écouteur se pose sur `button` et pas sur `filters`
- pourquoi `listenFilterButtons()` est appelée depuis `createButtons` et pas en bas du fichier
- pourquoi les trois appels groupés en bas ne fonctionnent pas, alors que c'est plus lisible
- ce qui se passe entre le départ du fetch et son retour
- pourquoi `createButtons` ne peut pas être appelée en bas du fichier comme les deux autres
- pourquoi renommer le paramètre en `categories` n'a rien cassé

---

# Bilan final p06

*Fichier généré par concaténation des blocs. Ne pas l'éditer, éditer les blocs sources.*
*Généré le 2026-07-22.*

---

# P6 Sophie Bluel, architecte d'intérieur

---

## 🎯 Mission

| | |
| --- | --- |
| **Client** | Sophie Bluel, architecte d'intérieur, site portfolio |
| **Contexte** | renfort dev front-end chez l'agence ArchiWebos |
| **Trois missions** | présentation des travaux (HTML fourni), connexion admin (from scratch), modale d'upload (from scratch) |
| **Livrable** | repo GitHub du front-end, plus un TXT ou PDF contenant le lien |
| **Nommage** | ZIP `Titre_du_projet_nom_prénom`, interne `Nom_Prénom_1_repo_github_mmaaaa` |
| **Deadline** | à confirmer |
| **Évaluation** | soutenance |

**Format de la soutenance**

15 min de présentation (galerie et filtres, connexion, ajout de travaux), 10 min de discussion (l'évaluateur joue Charlotte), 5 min de débriefing.

> Tolérance 10 à 20 min. Hors de ces bornes, refus possible. Le bloc `08-soutenance.md` est donc actif sur ce projet.

---

## 🔧 Specs techniques

### Stack

| | |
| --- | --- |
| **Langage** | JavaScript vanilla, HTML fourni |
| **Communication** | API via `fetch` |
| **Backend** | Node.js fourni, non livrable, outil de test |
| **Interdits** | framework, librairie externe |

### Données

| | |
| --- | --- |
| **Ressources API** | `works` (travaux), `categories`, `users` |
| **Authentification** | token à stocker après login |

### Fichiers

| | |
| --- | --- |
| **Dossier de travail** | `FrontEnd/` |
| **Fourni** | `index.html` |
| **Créés from scratch** | `script.js` (galerie et filtres), à venir : login, modale |
| **Icônes** | `instagram.png` dans `FrontEnd/assets/icons` |

### Design

| | |
| --- | --- |
| **Polices** | Syne (titres), Work Sans (texte) |
| **Vert marque** | `#1D6154` |
| **Terracotta logo** | `#B1663C` |
| **Fond maquette** | `#FFFEF8`, crème. Le CSS fourni est sur blanc par défaut. |
| **Fiche dédiée** | `sophie-bluel-design-tokens.md`, dans le dépôt du projet P6, avec le code et les docs. Pas dans `bilan-oc`. |
| **Breakpoints** | à extraire de Figma. Desktop dispo, mobile pas encore. |
| **Animations** | à définir avec la maquette |

### Catégories du client

`Tous` · `Objets` · `Appartements` · `Hôtels & restaurants`

Récupérées de `/api/categories`, jamais écrites en dur.

### Validation

W3C aux étapes structurantes · Lighthouse sur URL de prod en navigation privée · axe DevTools · NVDA

### Choix de structure en cours

Galerie et filtres sont générés dynamiquement. Plus aucun travail ni bouton de filtre en dur dans le HTML, seul le conteneur `ul.filters` est statique.

> **Deux méthodes de génération DOM coexistent volontairement.**
> `createElement` / `appendChild` pour la galerie (étape 2), template littéral + `insertAdjacentHTML` pour les filtres (étape 3).
> Décision assumée : les garder toutes les deux pour comparer. À savoir défendre devant le jury.

---

## ✅ Todo

### Étape 4, filtre fonctionnel · en cours

- [x] Pseudocode écrit avant de coder, six lignes
- [x] Classe `filter-button-selected` posée sur `Tous` à la génération
- [x] Écouteur de clic branché sur chaque bouton, vérifié en console
- [x] Écouteurs extraits dans `listenFilterButtons`
- [x] Appel de `listenFilterButtons()` placé à la fin de `createButtons`
- [x] Fichier réordonné : constantes, trois fonctions, appel de lancement en bas
- [x] Paramètre de `createButtons` renommé `donnees` en `categories`
- [ ] Vider la galerie au clic → mot-clé donné : `innerHTML`
- [ ] Reconstruire la galerie avec les travaux filtrés
- [ ] Déplacer `filter-button-selected` sur le bouton cliqué

> Le filtre ne filtre rien pour l'instant. Le clic ne fait qu'un `console.log`.

### Étape 5, page de connexion · à venir

- [ ] Intégrer la page de login conforme à la maquette, non fonctionnelle

---

### Dettes et vérifications en attente

**Code**

- [ ] `filterButtonSelected` déclarée dans `listenFilterButtons`, jamais utilisée. Servira à la ligne 6 du pseudocode.
- [ ] Restructurer le repo pour GitHub Pages. `index.html` est dans `FrontEnd/`, Pages sert la racine.

**Accessibilité**

- [ ] Navigation clavier et focus visible sur les boutons de filtre
- [ ] Contraste du texte des boutons (`#1D6154` sur blanc)
- [ ] Contraste de l'état actif (texte blanc sur `#1D6154`)
- [ ] axe DevTools sur la page, une fois l'étape 4 terminée
- [ ] Navigation clavier de la modale, focus visible
- [ ] Éléments générés en JS aussi accessibles que du HTML écrit à la main

**Performance et responsive**

- [ ] Lighthouse sur l'URL de production, navigation privée
- [ ] Responsive mobile, en attente de la maquette (Kanban : en cours côté design)

**Avant de rendre**

- [ ] Rendu conforme à la maquette
- [ ] W3C, Lighthouse, DevTools
- [ ] ZIP livrable et fichier lien repo

---

### Étapes terminées

- **Étape 0, installation** · Node.js et npm installés, Kanban et code fourni parcourus, dépendances backend installées, backend lancé, Swagger découvert, route works testée, lien Figma récupéré.

- **Étape 1, versioning** · `git init`, premier commit, dépôt distant créé, remote ajouté. Ordre inversé (distant avant local), sans conséquence.

- **Étape 2, galerie dynamique** · Travaux récupérés via `fetch` et affichés dynamiquement, travaux statiques retirés du HTML, compréhension des étapes 0 à 2 contrôlée.

- **Étape 2 bis, refactor** · Exos console sur les templates littéraux et `insertAdjacentHTML`. Décision prise : méthode retenue et appliquée aux filtres, galerie laissée en `createElement`.

- **Étape 3, filtres affichés** · Filtres posés au-dessus de la galerie, boutons stylés selon la maquette, conteneur `ul.filters` en dur entre le `h2` et `.gallery`, découpage en `fetchCategories` et `createButtons`, W3C validé (0 erreur, 1 avertissement sur du code fourni OC).

- **Nettoyage Git** · `Backend/.env` sorti du suivi et ignoré, sort de `.vscode/settings.json` tranché (gardé suivi, question au mentor), `Backend/node_modules/` vérifié ignoré, `filters-button` renommé `filter-button` dans le JS et le CSS.

- **Accessibilité acquise** · `alt` pertinents sur les images générées, `alt` = `work.title`.

---

### Étapes à venir

6. login fonctionnel · POST des identifiants, redirection si OK, message d'erreur si KO, stockage du token

7. accueil en mode connecté · bandeau noir d'édition, login devient logout, déconnexion, filtres cachés, bouton Modifier

8. modale · deux zones (galerie de suppression, formulaire d'ajout), ouverture au clic sur Modifier, fermeture par la croix et par l'extérieur, une seule modale dans le DOM, navigation interne avec flèche retour

9. suppression · requête DELETE, retrait du DOM sans recharger

10. formulaire d'ajout · preview à la sélection, catégories depuis l'API, message d'erreur si incomplet, envoi via `FormData`

11. ajout dynamique · le projet apparaît dans les deux galeries sans recharger

12. validation finale · formulaires testés avec données erronées, conformité maquette, gestion de l'interface, projet prêt pour la soutenance

---

## 🧗 Ce qu'il va falloir maîtriser sur ce projet

### Jamais pratiqué avant ce projet

- [ ] `appels API` · `fetch` en GET, POST, DELETE → GET acquis aux étapes 2 et 3
- [x] `injection de données distantes` · `remote data into the DOM` → fait aux étapes 2 et 3
- [ ] `gestion d'événements` · `event handling at scale`
- [ ] `données de formulaire` · `FormData`
- [ ] `authentification` · `authentication`, envoi d'identifiants, réception et stockage d'un token
- [ ] `stockage navigateur` · `localStorage`, `sessionStorage`
- [ ] `fenêtre modale` · `modal`, from scratch, ouverture, fermeture, navigation interne
- [ ] `aperçu avant envoi` · `image preview before upload`
- [x] `gabarit de chaîne` · `template literal` → orienté par le mentor, vu en console, appliqué à l'étape 3
- [x] `insertion adjacente` · `insertAdjacentHTML` → les 4 positions vues en console, appliqué à l'étape 3

### Déjà vu mais fragile, à consolider ici

- [x] `création et sélection DOM` · `createElement`, `appendChild`, `querySelector` → consolidés à l'étape 2. `classList` et `addEventListener` restent à revoir.
- [x] `parcours de tableau` · `forEach` → fait à l'étape 2, refait à l'étape 3
- [ ] `portée des variables` · `scope`, bloc, callback, fonction → règle connue depuis P5, retrouvée à tâtons au découpage en fonctions de l'étape 3

### Pièges connus à surveiller

> **Git** · Ne pas cocher README ni .gitignore auto à la création du repo. Penser le `.gitignore` AVANT le premier `git add`. Un `.env` ne se committe jamais.

> **Backend** · Ne jamais fermer le terminal à la croix. Le processus Node survit et bloque le port 5678.

> **Éditeur** · Le formatage automatique peut reformater tout un fichier fourni et noyer le `git diff`. Rencontré en P4, revu à l'étape 3 sur `style.css`.

> **Accessibilité** · `alt` en français, pas en anglais (piège relevé en P5). L'`alt` de la galerie vaut `work.title`, qui vient de l'API en anglais. Question posée au mentor.

---

---

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

---

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

---

## 🧠 Nouvelles connaissances

> Chaque entrée commence par le mot-clé en français, puis en anglais pour chercher sur MDN.
> Une mention `vu, pas acquis` signale une notion donnée plutôt que trouvée, à reprendre sur exo dédié.

---

### JavaScript, bases

`fonction fléchée` · `arrow function`

Forme courte `x => ...` pour une seule expression. Plusieurs instructions demandent des accolades `{ }` après la flèche.

---

`renvoyer contre agir` · `return vs side effect`

`fetch` rend une valeur qu'on récupère. `forEach` et `setAttribute` font une action et ne renvoient rien.

---

`valeur absente` · `undefined`

Ce que renvoie une fonction qui ne retourne rien. Un `console.log` qui affiche `undefined` est une preuve, pas un bug.

---

`gabarit de chaîne` · `template literal`

Une seule paire de backticks, variables insérées avec `${}`, aucun `+` ni guillemet à rouvrir. La concaténation classique demandait trois paires de guillemets et des `+` pour la même phrase.

Le backtick autorise aussi le passage à la ligne. Les guillemets classiques lèvent `Uncaught SyntaxError: Invalid or unexpected token`.

---

`bloc collé en console` · `syntax error scope`

Une erreur de syntaxe empêche tout le bloc de s'exécuter, y compris les lignes valides avant l'erreur. Rejouer les instructions séparément pour isoler.

---

`interruption de boucle` · `break`, `for...of`, `forEach`

`for...of` s'interrompt avec `break`. `forEach` ne le peut pas, `break` y lève `Illegal break statement` et la boucle va toujours jusqu'au bout. Un `if` reste possible dans les deux.

---

`variable du callback` · `callback parameter`

Le mot placé avant la flèche (`categorie =>`, `button =>`) nomme l'élément que la boucle tend à chaque tour. Sans lui, aucun moyen de l'attraper.

Réaffecter cette variable (`categorie = ...`) détruit la donnée du tour en cours. Utiliser une variable dédiée.

> **Vu, pas acquis.** Notion donnée par Claude, pas trouvée. À reprendre sur exo dédié hors projet.

---

`appeler contre nommer` · `function call vs reference`

`createButtons` désigne la fonction, `createButtons(donnees)` l'exécute. Une fonction déclarée ne s'exécute que si quelque chose l'appelle.

Passer `maFonction(...)` à un `forEach` exécute l'appel tout de suite et transmet son résultat, pas la fonction. Il faut passer une fonction non appelée.

> **Vu, pas acquis.**

---

`emplacement d'un appel` · `where to call a function`

Sans paramètre (`fetchCategories()`, `listenFilterButtons()`), appelable de partout : la fonction ne demande rien. Avec paramètre (`createButtons(categories)`), appelable seulement là où la donnée existe.

Ce n'est pas l'asynchrone qui contraint l'emplacement, c'est la donnée : le tableau des catégories n'existe qu'à l'intérieur du `.then`.

---

`paramètre local` · `function parameter scope`

Un paramètre est un nom local. `createButtons(categories)` ne connaît pas la variable du `.then`, elle en reçoit la valeur sous son propre nom.

```javascript
function direBonjour(nom) { console.log("bonjour " + nom) }
const prenom = "Max"
direBonjour(prenom)
```

`prenom` n'existe qu'à l'extérieur, `nom` qu'à l'intérieur, et l'affichage fonctionne.

Deuxième preuve sur le projet : paramètre de `createButtons` renommé en `categories` sans toucher à `fetchCategories`, le code fonctionne toujours. Ce sont bien deux variables distinctes.

> **Vu et testé, à consolider.**

---

`portée des variables` · `scope`

Une variable déclarée dans un bloc (fonction, callback) n'existe pas en dehors. L'instruction qui l'utilise doit vivre dans le même bloc. Règle déjà posée en P5.

---

`appel récursif involontaire` · `infinite recursion`

Une fonction qui contient son propre appel se relance en boucle.

---

### JavaScript, asynchrone

`exécution non bloquante` · `asynchronous execution`

Un `fetch` n'attend pas. Le fichier continue de se lire immédiatement, pendant que la demande voyage.

```javascript
console.log("1 avant le fetch")
fetch("https://jsonplaceholder.typicode.com/todos/1")
    .then(reponse => reponse.json())
    .then(donnees => console.log("4 les donnees sont la", donnees))
console.log("2 juste apres le fetch")
console.log("3 fin du fichier")
```

Affichage réel : 1, 2, 3, puis 4 en dernier, alors que le 4 est écrit avant les autres dans le fichier.

---

`point de synchronisation` · `.then` as the sync point

La chaîne `.then` est le seul endroit qui sait que la réponse est arrivée. Tout code qui dépend des données doit y être branché, directement ou via une fonction appelée depuis elle.

> **Notion non acquise, priorité.** Exo dédié à froid avant de reprendre l'étape 4.

---

### JavaScript / DOM

`création d'élément` · `document.createElement`

`document.createElement("balise")` crée l'élément en mémoire. Invisible tant qu'il n'est pas accroché.

---

`contenu textuel` · `textContent`

`element.textContent = "..."` met du texte dans une balise.

---

`pose d'attribut` · `setAttribute`

`element.setAttribute("nom", valeur)` prend deux arguments, nom et valeur. Ne renvoie rien.

---

`accrochage` · `appendChild`

`parent.appendChild(enfant)` accroche l'élément dans la page. Le parent reçoit, l'enfant est accroché.

Les enfants suivent leur parent : accrocher un élément déplace tout ce qu'il contient. L'ordre des `appendChild` (parent d'abord ou enfants d'abord) ne change pas le rendu.

> Piège · un élément créé mais non accroché existe et ne s'affiche pas.

---

`sélection` · `querySelector`, `querySelectorAll`

`querySelector` renvoie un seul élément, `querySelectorAll` renvoie une `NodeList` (ici de 4 boutons). Seule la seconde se parcourt avec `forEach`.

`querySelector` qui ne trouve rien renvoie `null`. Toute méthode appelée dessus lève `Cannot read properties of null`.

---

`parcours de tableau` · `forEach`

Un tour par élément. À chaque tour, la variable contient l'élément entier (l'objet), pas son index. On lit une valeur avec le point : `work.imageUrl`, `work.title`.

---

`insertion adjacente` · `insertAdjacentHTML`

`element.insertAdjacentHTML(position, html)`. Le texte passé est interprété comme du HTML, pas posé comme du texte brut. Crée et pose en une seule instruction, là où `createElement` demandait de créer, remplir, puis accrocher.

Ajoute sans écraser, contrairement à `innerHTML =`. Pas besoin d'accumuler dans une variable avant d'injecter.

Les quatre positions sont relatives aux balises de l'élément cible, pas à son contenu :

| Position | Où |
| --- | --- |
| `beforebegin` | avant la balise ouvrante, à l'extérieur |
| `afterbegin` | après la balise ouvrante, à l'intérieur, en premier |
| `beforeend` | avant la balise fermante, à l'intérieur, en dernier |
| `afterend` | après la balise fermante, à l'extérieur |

---

`inspection en console` · `outerHTML`, `parentElement`

`element.outerHTML` montre l'élément avec ses balises. `element.parentElement.innerHTML` montre son voisinage.

---

`élément généré, timing` · `dynamically generated element`

Un élément généré après un `fetch` n'existe pas au chargement du fichier. Tout code qui en dépend doit s'exécuter après sa pose, donc dans la fonction qui le pose.

Il n'existe aucun événement natif signalant "mon fetch est revenu et mon DOM est construit". `load` ne dit rien du fetch.

---

`écoute d'événement` · `addEventListener`

Se pose sur un élément qui existe déjà à l'instant où la ligne s'exécute. Sur une liste vide, le `forEach` tourne zéro fois : aucun écouteur, aucune erreur, aucun message.

---

`donnée sur un élément` · `data-*`, `dataset`

Range une information sur un élément HTML sans qu'elle s'affiche, et indépendamment du texte affiché. Relue en JS avec `element.dataset.nom`.

> **Vu en console, non acquis.** À reprendre à froid sur exo dédié.

---

### API & fetch

`route des travaux` · `GET /api/works`

Renvoie un tableau d'objets. Chaque travail a `id`, `title`, `imageUrl` (URL complète, prête pour un `src`), `categoryId`, et `category { id, name }`.

---

`route des catégories` · `GET /api/categories`

Renvoie la liste des catégories, chacune avec `id` et `name`. C'est `name` qui alimente le texte des boutons de filtre.

> `categoryId` (numéro) sert à comparer, `category.name` (texte) sert à afficher.

---

`route de connexion` · `POST /api/users/login`

Attend `email` et `password`, renvoie `{ userId, token }` si OK, `404` sinon.

> À retester dans Swagger : une API distingue en général utilisateur inconnu et mot de passe incorrect par deux codes différents.

---

`test de route` · `Swagger`

`Try it out` puis `Execute` teste une route en vrai et montre la forme des données. Une route GET peut aussi être ouverte directement dans la barre d'adresse.

---

`promesse` · `Promise`

`fetch("url")` renvoie une promesse, pas les données. Trois états : `pending`, `fulfilled` (tenue), `rejected` (rompue, par exemple serveur éteint).

---

`enveloppe de réponse` · `Response`

La réponse de `fetch` est une enveloppe. Elle arrive dès les en-têtes reçus (`status`, `ok`), avant que le corps soit téléchargé.

C'est pour ça que `.json()` renvoie une deuxième promesse : la lecture du corps prend du temps.

`Response.body` est un `ReadableStream`, un flux brut. Les données ne sont lisibles nulle part dans le `Response` tel quel. C'est `reponse.json()` qui ouvre et convertit, le `.then` suivant ne fait que récupérer le résultat.

---

`chaîne type` · `promise chain`

`fetch(url).then(r => r.json()).then(donnees => ...)`. Appliquée en vrai à `GET /api/works` puis à `GET /api/categories`.

---

`gestion d'erreur` · `.catch`

Dans une chaîne `.then`, l'erreur se rattrape avec un maillon `.catch`, méthode `Promise.prototype.catch`.

> À reformuler après vérification : `try / catch` n'est pas réservé à `async / await`, il fonctionne sur tout code synchrone. Ce qui est vrai, c'est qu'il n'attrape pas le rejet d'une promesse dans une chaîne `.then`, le rejet arrivant après la sortie du bloc.

---

### Authentification

`jeton` · `token`

Vient de la réponse du login. À stocker pour les actions protégées, ajout et suppression.

---

### Débogage

`vérification pas à pas` · `console.log`

Vérifier chaque étape avant de continuer : galerie attrapée, données reçues, boucle qui passe sur chaque élément.

---

`preuve de timing` · `setTimeout`

Comparer un `console.log` immédiat et le même dans un `setTimeout` prouve un problème de timing plutôt que de le supposer.

---

`erreur qui change` · `error progression`

Un message d'erreur différent à chaque rechargement est un signe de progression : chaque nouveau message correspond à un nouveau problème, le précédent est réglé.

---

`arrêt d'exécution` · `uncaught error`

Une erreur non rattrapée interrompt le fichier : les `console.log` placés après ne s'affichent jamais. Les placer avant la ligne fautive, ou commenter cette ligne le temps du test.

---

`console muette` · `silent failure`

Une console sans aucune erreur peut signaler un bug tout aussi réel qu'un message rouge.

---

`observation directe` · `read the render`

Recharger la page et observer le rendu est parfois plus rapide qu'un raisonnement. L'ordre d'insertion des boutons a été tranché comme ça.

---

`diff invisible` · `git diff --cached`

`git diff` ne montre rien pour un fichier untracked (pas de version précédente) ni pour un fichier déjà stagé.

---

### HTML & Sémantique

`structure de galerie` · `figure`, `figcaption`

Un projet de galerie est une `figure` contenant une `img` et une `figcaption`. Même structure quand elle est générée en JS.

---

`enfants d'une liste` · `ul`, `li`

Un `button` inséré dans un `ul` doit être enveloppé dans un `li`.

> Formulation à préciser : la spec autorise aussi `script` et `template` comme enfants directs de `ul`. La règle pratique reste bonne.

---

`navigation contre commande` · `nav`, `button`

`nav` est réservé à de la navigation, aller ailleurs. Un filtre déclenche une action sur place : c'est un `button`, pas un lien, et son conteneur n'est pas un `nav`.

---

`type de bouton` · `type="submit"`, `type="button"`

Un `button` sans attribut `type` vaut `submit` par défaut. Dans un `form`, il envoie le formulaire. `type="button"` le neutralise.

---

`élément de sectionnement` · `sectioning content`

`article` crée sa propre section. Un `h2` placé dans un `article` titre cet `article`, pas la `section` qui l'englobe. D'où l'avertissement W3C sur `#introduction` du HTML fourni.

---

`statique contre dynamique` · règle du projet

Ce qui est stable va en dur dans le HTML, ce qui dépend des données va en JS.

---

### CSS

`portée d'un sélecteur` · `type selector`

Un sélecteur de type (`button`) touche tous les éléments de ce type dans tout le projet, y compris ceux à venir. Une classe dédiée limite la portée.

---

`alignement horizontal` · `display: flex`, `gap`

Sur un `ul`, sans `flex`, les `li` s'empilent en colonne, comportement bloc par défaut.

---

### Accessibilité

`texte alternatif dynamique` · `alt`

Posé sur l'`img` générée avec `work.title`. Même exigence que du HTML écrit à la main, socle intégrateur.

---

`liste annoncée` · `ul` contre `div`

Sur une liste de commandes, le lecteur d'écran annonce une liste, son nombre d'éléments et la position courante. Un `div` ne porte aucune de ces informations.

---

`bouton natif` · `button` contre lien

Le lecteur d'écran annonce un bouton, et l'élément est nativement atteignable au clavier, activable avec Entrée ou Espace.

---

`région sans nom` · `accessible name`

Une `section` sans nom accessible n'est pas exposée comme région, elle devient une simple boîte. La navigation par titres reste fonctionnelle, d'où un avertissement et non une erreur.

---

### Outils & process

`retrait du suivi` · `git rm --cached`

`git rm --cached fichier` retire un fichier du suivi sans le supprimer du disque. La variante sans `--cached` supprime aussi le fichier.

---

`fichier déjà suivi` · `.gitignore`

Un `.gitignore` ne lâche pas un fichier déjà suivi. Le retirer du suivi d'abord, puis l'ignorer pour l'avenir. Se pense avant le premier `git add`, jamais après.

---

`ajout depuis un sous-dossier` · `git add .`

Ajoute les changements de ce dossier et en dessous. Git retrouve la racine (`.git`) depuis n'importe où dans le repo.

---

`granularité d'un commit` · `atomic commit`

Un commit est une unité cohérente et utile. Pas de commit pour un fichier vide.

Un commit de refactor décrit ce qui a été fait, pas le fait que ce soit un refactor : le type `refactor:` porte déjà cette information.

---

`diff noyé` · `editor auto-format`

Le formatage automatique de l'éditeur peut reformater tout un fichier fourni et noyer le `git diff`. Vérifier le diff avant de commiter.

---

`terminal occupé` · `npm start`

Le backend Node laisse le terminal occupé. Prévoir un second terminal pour travailler en parallèle.

Arrêt : `Ctrl + C`, puis `O` si PowerShell demande. Libère le port 5678. Fermer la fenêtre à la croix ne suffit pas.

---

`port occupé` · `Get-NetTCPConnection`

`Get-NetTCPConnection -LocalPort <port> -State Listen | Select-Object -ExpandProperty OwningProcess` trouve le PID qui occupe un port. `Stop-Process -Id <PID>` arrête ce seul processus.

---

`mise à jour risquée` · `npm audit fix --force`

À éviter sur un backend fourni : applique des changements de version cassants.

---

`log du backend` · `SQL query`

Le log au démarrage montre la requête SQL exécutée à chaque appel de `/api/works`, avec la jointure sur `categories`. La forme des données y est lisible en clair.

---

`connecteur Figma` · `MCP`

Besoin d'un accès éditeur. Maquette OC en lecture seule, la dupliquer dans ses brouillons (`Duplicate to your drafts`), le connecteur lit ensuite la copie.

> Avertissement OC : le code du Dev Mode Figma est souvent de mauvaise qualité. Se servir de la maquette pour les specs, pas pour copier du code.

---

`chargement différé` · `defer`

`<script defer>` dans le `<head>` s'exécute après le chargement du HTML.

`defer` et `window.addEventListener("load", ...)` répondent au même besoin, attendre que le HTML soit là. Les cumuler ne casse rien mais fait doublon.

---

`langue du code` · convention

Contenu affiché à l'utilisateur en français, noms de variables et de fonctions en anglais.

En anglais, un nom qui en qualifie un autre reste au singulier : `filter buttons`, `filter script`. Même règle pour les noms de classes CSS.

---

## 📚 Théorie non pratiquée

> **Catalogue des notions non acquises.** Ce qui a été vu, ce qui manque encore.
> L'ordre dans lequel les traiter est dans `05-bilan.md`, bloc `➡️ À revoir, par priorité`.

### Priorité

`ordre d'exécution asynchrone` · `event loop`, `async execution order`

Compris ligne par ligne, pas dans son ensemble. Exo dédié avant de reprendre l'étape 4.

---

`délégation d'événement` · `event.target`

Un écouteur unique sur le conteneur `ul.filters` plutôt qu'un par bouton. Supprimerait le problème de timing, le conteneur étant en dur dans le HTML, et supprimerait `listenFilterButtons`. Exo décidé en session.

---

### À reprendre

`transformation de tableau` · `map`

Vu en console, `[1,2,3].map(n => n * 10)` renvoie `[10,20,30]`. Non assimilé.

> À traiter avant la soutenance : `map` est justifié dans les choix techniques, un jury interrogera dessus.

---

`donnée sur un élément` · `data-*`, `dataset`

Découvert en console : attribut invisible, indépendant du texte affiché, relu par `element.dataset.nom`. Non acquis.

---

`paramètre de callback` · `callback parameter`

Notion donnée, pas trouvée. À reconsolider sur exo hors projet.

---

`rattrapage d'erreur` · `.catch`

Mot-clé donné, pas encore lu ni pratiqué. Le code des filtres n'en a pas, celui de l'étape 2 non plus.

---

`syntaxe asynchrone moderne` · `async / await`

Croisé pendant la discussion sur `fetch`, pas pratiqué. On est resté sur `.then`.

---

`boucle interruptible` · `for...of`

Vue en console pour la comparer à `forEach`, non utilisée dans le projet.

---

`état pour lecteur d'écran` · `aria-pressed`

Attribut d'état sur un bouton actif. Croisé comme question, pas encore étudié.

---

### Sorti de cette liste

`gabarit de chaîne` · `template literal` et `insertion adjacente` · `insertAdjacentHTML` : vus en console et appliqués à l'étape 3.

---

> Le lexique et les tips sont dans `09-memo.md`.

---

---

## 🔍 Choix techniques

> Format `décision → pourquoi`. C'est ce sur quoi le jury interroge en premier.
> Une mention `[à valider]` signale une proposition non confirmée.

---

### Setup et Git

`.env` **retiré du suivi et ignoré**

Un secret ne se committe jamais. L'historique le garde encore, non critique ici puisque le backend est un exercice fourni.

> Réflexe pro pour un vrai secret fuité : rotation du secret, pas seulement le retrait du suivi.

---

`.vscode/settings.json` **laissé suivi**

Choix assumé, question posée au mentor.

---

**Un seul commit pour l'étape 2**, afficher et retirer le statique

Les deux forment un tout cohérent. Un commit intermédiaire gardant le statique afficherait les projets en double.

---

`script.js` **placé dans `FrontEnd/`**, à côté de `index.html`

Permet un `src="script.js"` simple, même dossier.

---

`[à valider]` **Un fichier JS par responsabilité** (galerie, login, modale) plutôt qu'un seul gros fichier

À trancher selon l'ampleur.

---

### API et structure du code

**Chaîne `.then` plutôt que `async / await`**

Notion déjà pratiquée en console. `async / await` pas encore vue.

---

**`forEach` plutôt qu'une boucle `for` avec `length - 1`**

Pas de compteur à gérer, pas de risque de dépasser l'index.

---

**`forEach` plutôt que `map`** pour la galerie

La génération DOM est une action, aucune valeur de retour n'est nécessaire. `map` servirait si on voulait récupérer un tableau de résultats.

> À maîtriser avant la soutenance : `map` est classé "non assimilé" dans la théorie non pratiquée. Un jury interrogera sur cette justification.

---

**`forEach` plutôt que `for...of`** pour les filtres

`for...of` sert quand on a besoin d'interrompre avec `break`. Ici il faut parcourir toutes les catégories jusqu'au bout.

---

**Découpage en `fetchCategories` et `createButtons`**

Responsabilité unique. Une fonction va chercher les données, l'autre fabrique les boutons. Celle qui fabrique n'a besoin que d'un tableau, peu importe d'où il vient.

---

**Écouteurs extraits dans `listenFilterButtons`**

Même principe. `createButtons` faisait deux choses, fabriquer et écouter.

---

**`<script src="script.js" defer>` dans le `<head>`**

`defer` exécute le script après le chargement du HTML, donc `querySelector` trouve bien la galerie.

---

**`defer` seul, sans `window.addEventListener("load", start)`**

Les deux répondent au même besoin, attendre le HTML. Version du mentor testée puis écartée. Question posée au mentor.

---

`[à valider]` **`localStorage` ou `sessionStorage`** pour le token

À trancher selon le comportement voulu à la fermeture de l'onglet.

---

### Timing et emplacement du code

**`querySelectorAll` des boutons placé dans `createButtons`**, après la boucle, et non en haut du fichier

Les boutons sont générés en JS après le retour du `fetch`. En haut du fichier, ils n'existent pas encore.

> **Règle dégagée** · ce qui existe dans le HTML se récupère en haut du fichier, ce qui est créé par JS se récupère après sa création.

---

**Appel de `listenFilterButtons()` à la fin de `createButtons`**, et non en bas du fichier

Contrainte du `fetch`, pas un choix de style. En bas, la ligne s'exécute avant le retour de la réponse, `querySelectorAll` renvoie une liste vide, aucun écouteur posé.

> Vérifié en direct · console muette au clic.

---

**Ordre du fichier** · constantes, trois déclarations de fonctions, appel de lancement seul en bas

On ne lit jamais un appel avant d'avoir vu la fonction.

---

### Génération du DOM

**Template littéral et `insertAdjacentHTML` plutôt que `createElement` / `appendChild`** pour les filtres

Une seule instruction fabrique et pose l'élément, là où `createElement` en demandait quatre. Décision prise après les deux exos console.

---

**`beforeend` pour les catégories, `afterbegin` pour `Tous`**

`Tous` reste en tête, les catégories s'ajoutent à la suite dans l'ordre de l'API.

---

**Conteneur `ul.filters` en dur, boutons générés en JS**

Le conteneur est toujours là quoi qu'il arrive, les boutons dépendent des données de l'API.

> **Règle générale** · ce qui est stable va en dur, ce qui dépend des données va en JS.

---

**Vider puis reconstruire la galerie plutôt que trier les figures affichées**

Une `figure` générée ne porte aucune trace de sa catégorie. Inscrire cette information sur chaque figure serait du travail en plus, alors que la génération depuis un tableau est déjà écrite.

---

### Nommage

**Paramètre renommé `categories` plutôt que `donnees`**

Le nom décrit la donnée reçue. Renommage dans `createButtons` seulement, `fetchCategories` inchangée, le code fonctionne toujours.

---

**Classe `filter-button-selected` posée dans le template du bouton `Tous`**

L'état par défaut est connu à la génération, pas besoin de le poser après coup.

Le nom applique la règle déjà notée en fiche, un nom qui en qualifie un autre reste au singulier, et un seul séparateur, le tiret.

---

**Classe dédiée plutôt qu'un sélecteur CSS `button`**

Le projet aura d'autres boutons (login, modale, ajout de photo) qui ne doivent pas hériter du style des filtres.

---

**Texte du bouton `Tous` en français**

C'est du contenu affiché à l'utilisateur. L'anglais reste réservé aux noms de variables et de fonctions.

---

### Sémantique et accessibilité

**`alt` de l'image générée = `work.title`**

Image fonctionnelle, le titre décrit le projet. Socle accessibilité.

---

**`ul` plutôt que `div`** pour le conteneur des filtres

Le lecteur d'écran annonce une liste, avec le nombre d'éléments et la position dans la liste. Un `div` n'apporte rien de tout ça.

---

**Pas de `nav` pour les filtres**

Un clic sur un filtre ne mène nulle part, on reste au même endroit. Ce n'est pas de la navigation mais une commande d'affichage. Donc `button`, pas un lien.

---

`[à valider]` **`type="button"` explicite** sur chaque bouton de filtre

Un `button` sans `type` vaut `submit` par défaut. Sans conséquence hors formulaire, mais l'écrire évite un envoi involontaire si le bouton se retrouve un jour dans un `form`.

À confirmer comme choix assumé et non comme réflexe.

---

### CSS

**Design tokens extraits du `style.css` fourni plutôt que de Figma**

Le CSS est le code réellement appliqué, la source qui fait foi.

> Écart relevé · le CSS ne met aucun fond (blanc), la maquette est sur crème `#FFFEF8`.

---

---

## 📐 Formule et méthode de calcul

> Toute formule mathématique, tout calcul, toute méthode reproductible utilisée sur le projet.
> Format : nom de la formule, le calcul en bloc code, puis à quoi elle sert.

Aucune formule sur ce projet pour l'instant.

**Exemple du format, repris de P4 OhMyFood**

`interpolation linéaire` · `linear interpolation`, pour `clamp()`

```
pente = (valeur_max - valeur_min) / (largeur_max - largeur_min)
ordonnée = valeur_min - pente × largeur_min
→ clamp(valeur_min, calc(ordonnée_rem + pente_vw), valeur_max)
```

Sert à faire varier une taille en continu entre deux largeurs d'écran, sans media query.

> **Le terme exact compte à l'oral** · interpolation, deux points et une droite exacte. Ce n'est pas une régression, qui est une approximation sur un nuage de points.

---

## 📊 Validation outils

> Ce que les outils mesurent, par opposition au bloc Vérification qui liste ce que je teste à la main.
> Une ligne par passage. On garde l'historique, on n'écrase pas.

### W3C

| Date | Fichier | Erreurs | Avertissements | Détail |
| --- | --- | --- | --- | --- |
| étape 4 | `index.html` | 0 | 1 | `#introduction` : un `h2` dans un `article` titre l'`article`, pas la `section`. Code fourni OC, non corrigé, justifiable. |
| étape 4 | `style.css` | 0 | 0 | |

### Lighthouse

À passer sur l'URL de production, en navigation privée, jamais sur Live Server.

| Date | Perf | Accessibilité | Bonnes pratiques | SEO | Note |
| --- | --- | --- | --- | --- | --- |
| | | | | | pas encore passé, GitHub Pages non configuré |

### Accessibilité

| Date | Outil | Résultat | Détail |
| --- | --- | --- | --- |
| | axe DevTools | non passé | à faire une fois l'étape 4 terminée |
| | WAVE | non passé | |
| | NVDA | non passé | |
| | Navigation clavier | non passé | focus visible sur les boutons générés |
| | Contraste | non passé | texte `#1D6154` sur blanc, et état actif blanc sur `#1D6154` |

---

## 🔍 Vérification

### Validé

- [x] La galerie affiche les travaux de l'API, sans doublon
- [x] Plus aucun travail en dur dans le HTML
- [x] Compréhension des étapes 0 à 2 contrôlée (`appendChild`, `json`, `forEach`, git, `defer`)
- [x] Les filtres affichent les bonnes catégories
- [x] Le bouton `Tous` apparaît en première position, les catégories suivent dans l'ordre de l'API
- [x] Aucun bouton de filtre en dur, seul le `ul` conteneur est statique
- [x] Le refactor en deux fonctions n'a pas changé le rendu
- [x] Le style des boutons ne déborde pas sur les autres boutons du projet
- [x] `style.css` restauré à son formatage d'origine avant commit, diff lisible
- [x] `index.html` validé au W3C après ajout du `ul.filters`
- [x] Chaque bouton renvoie bien le sien au clic, `console.log(button)`, jamais le voisin
- [x] Le clic log toujours le bon bouton après l'extraction dans `listenFilterButtons`
- [x] Les boutons s'affichent toujours après le renommage du paramètre en `categories`

### Preuve obtenue par l'échec

- [x] Vérifié que les trois appels groupés en bas du fichier ne fonctionnent pas. Testé, console muette, aucune erreur.

### En attente

- [ ] Le clic sur un filtre affiche les bons travaux
- [ ] Un seul bouton porte `filter-button-selected` à tout moment
- [ ] Boutons de filtre atteignables au clavier, focus visible
- [ ] Le login redirige si OK, affiche une erreur si KO
- [ ] Le token est bien stocké
- [ ] Le mode connecté change l'affichage attendu
- [ ] La modale ne se duplique pas après plusieurs ouvertures
- [ ] La suppression retire le travail sans recharger
- [ ] L'ajout affiche le travail sans recharger, dans les deux galeries

---

## 📋 Bilan, préparation session mentor

> Tout ce bloc est `[à valider]`, proposé et à confirmer.

### 🟢 Ce que j'ai fait seul

**Diagnostic de mon propre code**

- Constat posé seul en ouverture de la seconde session : "mon code est emmêlé et n'est pas de moi". C'est ce constat qui a déclenché le refactor.
- Diagnostic autonome que `createButtons` fait deux choses, donc écart à la responsabilité unique. Non soufflé.
- Frontière entre les deux responsabilités localisée seule, ligne exacte désignée.
- Auto-appel de `createButtons` repéré et conséquence anticipée.

**Décisions justifiées**

- Choix HTML contre JS pour les boutons, justifié seul par analogie avec l'étape 2.
- `nav` écarté et `button` retenu sur un raisonnement d'usage, pas par habitude.
- `ul` justifié sur un argument d'accessibilité concret.
- Choix de vider plutôt que trier, justifié sur l'absence d'information de catégorie dans le DOM généré.
- Nom `filter-button-selected` tranché en appliquant une règle de nommage que j'avais notée moi-même.
- Portée du sélecteur CSS anticipée seul, classe dédiée plutôt que sélecteur `button`.
- Version `window load` du mentor testée sur mon propre code, puis écartée avec une raison.

**Méthode**

- Pseudocode de l'étape 4 écrit en entier avant toute ligne de code, six lignes cohérentes.
- Pseudocode de l'étape 3 nettoyé de ce qui appartenait à l'étape 4.
- Piège des doublons dans la galerie anticipé seul, avant de coder.
- Ordre retirer puis ajouter la classe active, corrigé après avoir vu le piège.
- État `filter-selected` repéré sur la maquette et volontairement reporté à l'étape 4.
- Test des trois appels groupés en bas mené jusqu'au bout, résultat observé, preuve obtenue.
- Différence entre un `fetch` au niveau du fichier et un `fetch` enfermé dans une fonction, trouvée seule après observation. Formulée avec mes mots : "la mettre dans une fonction implique qu'elle s'exécute à l'appel".

**Rigueur**

- Setup Git propre et autonome : root-commit, message conventionnel, remote, push.
- Trois commits atomiques sur l'étape 3, un par sujet : feature, refactor, style.
- Reformatage automatique de `style.css` repéré et annulé avant commit.
- Diagnostic du port occupé mené jusqu'au bout, cause comprise et prévention identifiée.
- Erreur de position d'insertion (`afterbegin` contre `beforeend`) diagnostiquée et corrigée seul, en observant le rendu.
- W3C passé, avertissement compris et justifiable devant le jury.
- Accessibilité posée dès la génération, `alt` sur image dynamique.
- **Refus de commiter un code que je ne sais pas expliquer**, alors que le commit était proposé.

**Restitution**

- Étapes 0 à 2 réexpliquées sans le code sous les yeux.
- Bloc des écouteurs réexpliqué avec mes mots, sans le code sous les yeux.
- Deux notions pointées par le mentor découvertes en console et reformulées avec mes mots.
- Refactor en deux fonctions mené jusqu'au bout sans casser le rendu.

---

### 🔴 Difficultés rencontrées

**Sur le fond, à aborder avec Florian**

- Étape 4 très difficile sur deux sessions. Blocage prolongé, perte du fil, forte frustration, découragement exprimé plusieurs fois.
- Sentiment de ne pas m'approprier le code produit sur la partie écouteurs de clic. Notion donnée par l'IA plutôt que trouvée, donc à réapprendre.
- **Claude a donné le nom et la structure de la fonction à créer**, ce que le prompt interdit sur du code OC évalué. Le cadre n'a pas tenu.
- `data-*` introduit au mauvais moment, pseudocode déjà complet, notion non nécessaire à cet instant. A cassé la progression.
- Reprise du réflexe "je sais pas" avant d'avoir observé.
- Doute sur mes capacités exprimé plusieurs fois.
- Fatigue de fin de session : plusieurs blocages tenaient à ça plus qu'à la notion elle-même.

**Notions**

- Blocage sur l'asynchrone : chaque ligne du fichier est comprise isolément, l'assemblage ne l'est pas.
- Plusieurs angles tentés sur le timing du `fetch` (chronologie, analogie, exos console) sans que la notion passe.
- `map` non assimilé après plusieurs angles. Notion mise de côté volontairement plutôt que forcée en fin de session.
- Difficulté persistante à distinguer une valeur (`name`, texte) d'un identifiant (`id`, `categoryId`) dans une comparaison.
- Portée des variables retrouvée à tâtons lors du découpage en fonctions. `buttonAll` et `buttonCategorie` déplacés plusieurs fois avant d'atterrir au bon endroit.

**Syntaxe et mécanique**

- Syntaxe des fonctions fléchées multi-lignes, besoin des accolades.
- `setAttribute`, deux arguments, pas de `const` devant.
- Sens de `appendChild`, le parent reçoit, et placement du code dans le `forEach`.
- Assembler deux morceaux déjà écrits (l'appel `insertAdjacentHTML` et le HTML de la catégorie) : blocage long alors que les deux pièces existaient.
- Réflexe de repartir sur `createElement` après avoir tranché le passage aux templates littéraux.
- Blocage complet, sur une session entière, sur l'affichage des données de l'API en console. Sortie trouvée seulement à la session suivante.

**Périphérique**

- Mise en ligne GitHub Pages, structure `FrontEnd/` en sous-dossier contre racine servie par Pages.
- Formulation des messages de commit en anglais, accords et ordre des mots, plusieurs allers-retours.

---

### ➡️ À revoir, par priorité

> **C'est le plan d'action, la seule liste ordonnée.** Le détail de chaque notion est dans `03-connaissances.md`, bloc `📚 Théorie non pratiquée`.

**Priorité 1, bloquant pour l'étape 4**

- Ordre d'exécution asynchrone, sur exo dédié hors projet, à froid.
- `event.target` et l'écouteur unique sur conteneur, sur exo dédié.

**Priorité 2, notions à consolider**

- Le paramètre de callback dans un `forEach`, sur exo hors projet.
- `querySelector` contre `querySelectorAll`, réflexe à ancrer.
- Passage d'une valeur en paramètre.
- Portée des variables lors d'un découpage en fonctions.
- `data-*` et `dataset`, à froid.
- `map`, à froid, sur exo dédié.
- `.catch` dans une chaîne de promesses.
- `async / await`, croisé, pas encore pratiqué.

**Priorité 3, méthode**

- Traduire un pseudocode en code sans aide, morceau par morceau.
- Déclencher les réflexes du socle intégrateur sans rappel : W3C aux étapes structurantes, clavier, contraste.
- **Dépendance à l'aide de l'IA** : à aborder directement avec Florian, pas seulement à corriger par le prompt.

**Priorité 4, à trancher**

- Aligner ou non la galerie de l'étape 2 sur les templates littéraux.
- Restructuration du repo pour la mise en ligne.

---

## ❓ Questions pour le mentor

> Toutes `[à valider]`, propositions.

### Sur ma progression

11. J'ai l'impression de ne pas m'approprier ce que je produis quand l'aide arrive trop vite. Comment le mesurer honnêtement, et que faire concrètement pour y remédier ?

13. Pourquoi mon code est-il si difficile à comprendre dans son ensemble ? Je comprends à peu près chaque ligne isolément, mais le tout assemblé me paraît impossible à suivre. Est-ce normal à ce stade, un problème de structure, ou un problème de notion ?

12. Peux-tu m'aider à revoir mon prompt Claude, voire m'en proposer ta version ? Le cadre actuel n'a pas tenu en session, l'aide arrive encore trop vite.

### Sur l'architecture du code

10. Brancher les écouteurs de clic depuis `createButtons` est imposé par le timing du `fetch`. Est-ce la pratique attendue, ou existe-t-il une organisation plus propre en agence ?

14. `defer` et `window.addEventListener("load", ...)` : tu utilises le second dans ton exemple, j'ai le premier. Lequel attends-tu, et pourquoi ?

5. Le refactor de la galerie en template littéral et `insertAdjacentHTML` est-il attendu pour la soutenance, ou `createElement` reste-t-il acceptable s'il est maîtrisé ?

6. Deux méthodes de génération DOM dans le même fichier : acceptable si les deux sont justifiées, ou incohérence à corriger ?

15. Les garder volontairement pour comparer : acceptable comme démarche d'apprentissage, ou à éviter sur un livrable ?

1. `localStorage` ou `sessionStorage` pour le token, quelle pratique attendue ?

### Sur la sémantique et l'accessibilité

3. L'`alt` de la galerie vaut `work.title`, qui vient de l'API en anglais. Acceptable pour l'accessibilité, ou faut-il autre chose ?

8. `type="button"` systématique sur les boutons hors formulaire : pratique attendue en agence, ou bruit inutile ?

9. Un bouton de filtre actif doit-il porter une information d'état pour un lecteur d'écran, ou la classe CSS suffit-elle à ce niveau de projet ?

7. L'état visuel du filtre actif (`filter-selected` de la maquette) : plutôt une classe posée en JS, ou une autre approche attendue ?

### Sur le livrable

2. Le backend fourni doit-il rester dans mon repo, ou seul le front-end est attendu comme livrable ?

4. GitHub Pages : `index.html` est dans `FrontEnd/`. Quelle structure recommandée, remonter à la racine ou dossier `docs/` ?

---

---

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

---

## État Git

**Branche** `main`, à jour avec `origin/main`.

**Étape 4** · rien de commité. Modifications en attente dans `script.js` et `style.css`.

> **Commit reporté volontairement** · je ne commite pas un code que je ne sais pas encore expliquer en entier.
> À surveiller : plus l'attente dure, plus le commit sera gros et difficile à découper en sujets uniques.

---

---

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

> Une seule source, plus haut dans ce fichier : `➡️ À revoir, par priorité`.
> Le catalogue des notions elles-mêmes est dans `03-connaissances.md`, bloc `📚 Théorie non pratiquée`.

---

---

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

---

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

---

## 📝 Point de reprise

> Où j'en suis, en détail. La version courte est dans `ETAT.md` à la racine.

---

### Où j'en suis exactement

**Étape 4, filtre fonctionnel. Non terminée.**

- **Fait** · lignes 1, 2, 3 du pseudocode. Récupérer les boutons, écouter les clics, classe active par défaut sur `Tous`.

- **Restant** · lignes 4, 5, 6. Vider la galerie, la reconstruire filtrée, déplacer la classe active.

> **Le filtre ne filtre rien.** Le clic ne fait qu'un `console.log`.

---

### Décision de session, à respecter

> **Ne rien coder tant que l'ordre d'exécution asynchrone n'est pas compris.**

Chaque ligne du fichier est comprise isolément, l'assemblage ne l'est pas. Coder la suite dans cet état produirait du code que je ne saurais pas défendre.

---

### Prochaine action, dans cet ordre

1. Refaire seul le visuel de la chronologie ci-dessous, en le construisant, pas en le relisant.

2. Exo dédié hors projet sur l'asynchrone, à froid.

3. Puis exo `event.target` sur un conteneur.

4. Puis exos hors projet à froid : paramètre de callback dans `forEach`, `data-*` et `dataset`.

5. Seulement ensuite, lignes 4, 5, 6 du pseudocode. Mot-clé déjà donné pour la ligne 4 : `innerHTML`.

6. Commit une fois le code compris et explicable.

7. Point à aborder avec Florian : le sentiment de ne pas m'approprier le code, et la dépendance à l'aide.

---

### Avant de coder

Relancer le backend · `cd Backend`, puis `npm start`. Sinon `fetch` échoue.

> Arrêt propre avec `Ctrl + C`, jamais à la croix. Sinon le processus survit et bloque le port 5678.

---

### Visuel à reconstruire de mémoire

**Version actuelle, qui marche**

```
t = 0 ms      fetchCategories()        le fetch part
t = 0 ms      fin du fichier           aucun bouton dans la page
              ... attente reseau ...
t = 200 ms    la reponse arrive        .then appelle createButtons()
t = 200 ms    boutons poses            insertAdjacentHTML
t = 200 ms    listenFilterButtons()    appelee depuis createButtons
                                       les boutons existent, ecouteurs poses
```

**Les trois appels groupés en bas, qui ne marche pas**

```
t = 0 ms      fetchCategories()        le fetch part
t = 0 ms      listenFilterButtons()    s'execute tout de suite
                                       querySelectorAll renvoie une liste vide
                                       forEach tourne 0 fois, aucun ecouteur
              ... attente reseau ...
t = 200 ms    boutons poses            trop tard, plus personne ne vient
```

> **Point unique à retenir** · entre le départ du fetch et son retour, il s'écoule un temps réel pendant lequel le fichier a déjà fini de se lire.

---

### État Git

Branche `main`, à jour avec `origin/main`.

Étape 4 · rien de commité. Modifications en attente dans `script.js` et `style.css`.

> **Commit reporté volontairement** · je ne commite pas un code que je ne sais pas encore expliquer en entier.

---

### Vérifications non faites, à rattraper

- Navigation clavier et focus visible sur les boutons générés
- Contraste de l'état actif
- axe DevTools
- `git diff` non relu avant le commit du CSS, proposé et écarté sur le moment

---

### Notions restant à découvrir

**Priorité** · ordre d'exécution asynchrone · `event.target`

**Pour l'étape 4** · `innerHTML` pour vider un conteneur · filtrage d'un tableau

**Plus tard** · `map` · `.catch` · `async / await` · `dataset`, vu mais non acquis

---

### En attente : mise en ligne GitHub Pages

**Problème identifié** · `index.html` est dans `FrontEnd/`, mais Pages est réglé sur la branche `main` et le dossier `/ (root)`. Pages cherche à la racine, ne trouve pas `index.html`, n'affiche rien.

**Deux pistes, à m'expliquer avant d'agir**

1. Faire remonter le contenu de `FrontEnd/` à la racine du repo. Le plus propre, mais manip Git à comprendre, `git mv`, sans toucher à `Backend/`.
2. Ou renommer `FrontEnd/` en `docs/`, que Pages sait servir. Moins propre.

> **À retenir** · même en ligne, la galerie restera vide. Le JS appelle `http://localhost:5678`, un backend local que GitHub ne peut pas faire tourner. La mise en ligne sert surtout à passer Lighthouse en fin de projet, rien d'urgent.

---

### Historique du projet

- **Cadrage** · Swagger compris, arrêt backend connu, connecteur Figma opérationnel via copie de la maquette. Fiche de design tokens produite (`sophie-bluel-design-tokens.md`, dans le dépôt du projet P6, pas ici).

- **Notions découvertes en console, hors projet** · `fetch`, `forEach`, injection DOM, templates littéraux, `insertAdjacentHTML`, `for...of` contre `forEach`, ordre d'exécution du fetch, passage de valeur en paramètre.

- **Étape 2** · codée de bout en bout par moi, commitée et poussée (`2fd429c`). Contrôle de compréhension des étapes 0 à 2 validé.

- **RDV mentor** · orientation vers les templates littéraux et `insertAdjacentHTML`, et consigne de réduire la délégation à l'IA : plus de `console.log`, d'exos, de mots-clés, indices très courts. Prompt v7 produit en conséquence, barème d'indice à 5 niveaux, règle "notion qui ne passe pas", prompt réduit d'environ 40 %.

- **Étape 3** · conteneur `ul.filters` en dur, boutons générés depuis `/api/categories`, refactor en `fetchCategories` et `createButtons`, style sur classe dédiée, trois commits poussés.

- **Étape 4, ce qui est fait** · W3C sur `index.html` (0 erreur, 1 avertissement sur `#introduction`, code fourni OC), CSS validé 0 erreur, hashes de l'étape 3 relevés, pseudocode écrit, classe renommée `filter-button` dans le JS puis le CSS, `filter-button-selected` posée sur `Tous`, écouteurs branchés et vérifiés en console, lignes de debug retirées, écouteurs extraits dans `listenFilterButtons`, fichier réordonné, paramètre renommé `categories`, version `window load` du mentor testée puis écartée.

- **Incidents résolus** · port 5678 occupé, diagnostiqué et résolu.

---

### Vérifications déjà faites

Galerie affiche les works de l'API, une seule fois, sans doublon · plus aucun travail en dur dans le HTML · `alt` présent sur chaque image générée · étapes 0 à 2 réexpliquées avec mes mots sans le code sous les yeux · boutons de filtre affichés dans le bon ordre, `Tous` en tête · rendu inchangé après le refactor · style limité aux boutons de filtre · `style.css` restauré à son formatage d'origine avant commit

---

---

## 🔎 À vérifier

Relevé par Claude pendant le rangement de l'inbox. Faits observés uniquement, rien d'inventé.
Une ligne résolue est barrée, pas supprimée.

Format : `[date] type : constat → où` 

Types : `contradiction`, `savoir douteux`, `annoncé jamais fait`, `doublon`, `écart pratique pro`

---

### Relevé du 2026-07-21 (découpage de la fiche d'origine)

- `[2026-07-21] savoir douteux` : "maillon `.catch`, pas `try / catch` (qui va avec `async / await`)". `try / catch` n'est pas réservé à `async / await`, il fonctionne sur tout code synchrone. Ce qui est vrai : `try / catch` n'attrape pas le rejet d'une promesse dans une chaîne `.then`, parce que le rejet arrive après la sortie du bloc. Reformuler avec mes mots après vérification → `03-connaissances.md`, API & fetch

- `[2026-07-21] savoir douteux` : "`POST /api/users/login` renvoie `{ userId, token }` si OK, `404` sinon". Une API distingue en général utilisateur inconnu et mot de passe incorrect par deux codes différents. À retester dans Swagger avant de coder l'étape login, la checklist prévoit "affiche une erreur si KO" → `03-connaissances.md`, API & fetch

- `[2026-07-21] savoir douteux` : "Un `ul` n'accepte que des `li` comme enfants directs". La spec HTML autorise aussi `script` et `template`. La règle pratique reste bonne, la formulation absolue est fausse → `03-connaissances.md`, HTML & Sémantique

- `[2026-07-21] contradiction` : `map` est justifié finement dans les choix techniques ("`map` servirait si on voulait récupérer un tableau de résultats") mais classé "non assimilé, à reprendre à froid" dans la théorie non pratiquée. Les deux peuvent coexister, mais un jury qui lit le choix technique interrogera sur `map`. À traiter avant la soutenance → `05-bilan.md` et `03-connaissances.md`

- `[2026-07-21] annoncé jamais fait` : "Trancher le sort de la galerie de l'étape 2" est reporté sans décision depuis le point de reprise. Aucune trace de ce qui bloque → `10-point-de-reprise.md`

- `[2026-07-21] annoncé jamais fait` : `git diff` proposé avant le commit du CSS, écarté sur le moment, alors que le formatage automatique de l'éditeur avait déjà noyé un diff en P4. Le réflexe est écrit dans les connaissances mais n'a pas été appliqué → `02-bugs.md` et `03-connaissances.md`

- `[2026-07-21] doublon` : les justifications `forEach` contre `map` et `for...of` figurent en double, en tant que savoir dans les connaissances et en tant que décision dans les choix techniques. Acceptable si assumé, à ne pas laisser diverger : corriger les deux ou aucun → `03-connaissances.md` et `05-bilan.md`

- `[2026-07-21] écart pratique pro` : `.vscode/settings.json` laissé suivi par Git, marqué "choix assumé, question posée au mentor". La réponse du mentor n'est consignée nulle part → `05-bilan.md`, Setup et Git

### Relevé du 2026-07-21 (comparaison version 01 contre version 02)

- `[2026-07-21] perte de trace` : la version 01 gardait l'URL complète `GET http://localhost:5678/api/works` dans la chaîne `.then` type. La version 02 l'a raccourcie en `GET /api/works`. Le port 5678 reste documenté ailleurs (journal de bugs), donc rien d'utile n'est perdu, mais la fiche ne dit plus explicitement sur quelle machine tourne l'API → `03-connaissances.md`, API & fetch

- ~~`[2026-07-21] annoncé jamais fait` : la version 01 listait "Bouton `Tous` actif par défaut au chargement" comme tâche de l'étape 3. La version 02 déclare l'étape 3 terminée, et cette case reste non cochée.~~ **Résolu au delta étape 4** : classe `filter-button-selected` posée sur `Tous` à la génération.

- ~~`[2026-07-21] dette assumée` : la version 01 posait "Décider si la galerie est refactorée ou laissée en `createElement`". La question est reportée depuis deux versions sans décision.~~ **Tranché au delta étape 4** : les deux méthodes sont conservées volontairement, pour comparer. Décision assumée, à savoir défendre devant le jury.

### Relevé du 2026-07-21 (delta étape 4)

- `[2026-07-21] écart cadre pédagogique` : "Claude a donné le nom et la structure de la fonction à créer, ce que le prompt interdit sur du code OC évalué. Le cadre n'a pas tenu." Fait rapporté par Max lui-même. `listenFilterButtons` est donc dans le code sans avoir été trouvée. À réapprendre sur exo dédié avant la soutenance, sous peine de ne pas savoir défendre une fonction du livrable → `05-bilan.md`, Difficultés

- `[2026-07-21] formulation trompeuse` : dans les vérifications, la ligne "Les trois appels groupés en bas du fichier ne fonctionnent pas (testé, console muette)" est cochée `[x]`. Dans une checklist, `[x]` se lit "conforme". Un lecteur externe comprendra que le code ne fonctionne pas. Reformuler en "vérifié que les trois appels groupés en bas ne fonctionnent pas, preuve obtenue" → `05-bilan.md`, Vérification

- `[2026-07-21] doublon` : plusieurs notions figurent à la fois dans `🧠 Nouvelles connaissances` avec la mention "Vu, pas acquis" et dans `📚 Théorie non pratiquée` (paramètre de callback dans `forEach`, `dataset`, ordre asynchrone). Cohérent sur le fond, mais deux endroits à corriger le jour où la notion est acquise. Ne pas les laisser diverger → `03-connaissances.md`

- `[2026-07-21] à surveiller` : "je ne commite pas un code que je ne sais pas encore expliquer" est une bonne décision, mais l'étape 4 accumule des modifications non commitées dans `script.js` et `style.css`. Plus l'attente dure, plus le commit sera gros et difficile à découper en sujets uniques → `10-point-de-reprise.md`, État Git

### Relevé du 2026-07-21 (contrôle version 01 contre bilan final)

- ~~`[2026-07-21] perte de trace` : la version 01 nommait les quatre catégories réelles de l'API. Le bilan final ne les citait plus nulle part.~~ **Résolu au reformatage du 22-07** : section "Catégories du client" ajoutée dans `00-cadrage.md`, Specs techniques.

### Relevé du 2026-07-22 (mise en dépôt Git du dossier de notes)

- ~~`[2026-07-22] doublon` : `fiche-p6-sophie-bluel.md` est resté à la racine du dépôt alors que son contenu existe déjà en deux endroits.~~ **Résolu le 22-07** : supprimé après vérification ligne à ligne, contenu intégralement retrouvé dans les blocs de `p06/`.

- ~~`[2026-07-22] doublon` : `_template/04-bilan.md` ne contient plus qu'une note "fichier remplacé".~~ **Résolu le 22-07** : supprimé.

- ~~`[2026-07-22] doublon` : douze fichiers `.sauv*` hors convention dans `p06/_deltas/`.~~ **Résolu le 22-07** : supprimés après vérification ligne à ligne.

> **Leçon de la session du 22-07.** Ces douze `.sauv*` étaient couverts par `.gitignore`, donc jamais suivis par Git. Claude les a présentés comme récupérables depuis l'historique : c'était faux. Avant d'annoncer qu'une suppression est réversible, vérifier que le fichier est réellement suivi, avec `git ls-files`.

---

### Relevé du 2026-07-22 (audit général du dépôt)

- ~~`[2026-07-22] renvoi cassé` : `sophie-bluel-design-tokens.md` est cité comme fiche existante dans `00-cadrage.md` et dans `10-point-de-reprise.md`, sans exister dans ce dépôt.~~ **Résolu le 22-07** : la fiche vit dans le dépôt du projet P6, avec le code. Les deux renvois précisent maintenant où elle est.

- `[2026-07-22] séparateurs` : `fusionne-sous-sections.py` supprimait les `---` entre entrées, alors que le format de référence de `CLAUDE.md` les exige. **Résolu le 22-07**, commit `080fe72`. Les séparateurs manquants de `p06/` seront ajoutés au prochain passage du script.

- `[2026-07-22] contenu perdu à la génération` : `build-lisible.py` n'exportait aucune ligne de `02-bugs.md`, 95 lignes absentes, et annonçait 58 bugs au lieu de 30. **Résolu le 22-07**, commit `c925252`.


---


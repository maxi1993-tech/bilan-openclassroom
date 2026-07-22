# Fiche P6, version 02

*Archive brute, état après l'étape 3 (filtres affichés). Source du découpage en blocs.*
*Date de session inconnue, à compléter par Max.*

---

# Sophie Bluel architecte d'intérieur

> Fiche fusionnée : version précédente + session étape 3. 18 blocs, aucun supprimé, aucun contenu écrasé.

---

## 🎯 Mission

Client : Sophie Bluel, architecte d'intérieur (site portfolio).

Contexte : renfort dev front-end chez l'agence ArchiWebos. Trois missions : la page de présentation des travaux (à partir du HTML fourni), la page de connexion admin (from scratch), la modale d'upload de médias (from scratch).

Livrable : repo GitHub du code front-end. Fichier TXT ou PDF contenant le lien du repo. ZIP nommé `Titre_du_projet_nom_prénom`, livrable interne nommé `Nom_Prénom_1_repo_github_mmaaaa`.

Deadline : à confirmer.

Format évaluation : soutenance. 15 min de présentation (galerie/filtres, connexion, ajout de travaux), 10 min de discussion (l'évaluateur joue Charlotte), 5 min de débriefing. Tolérance 10 à 20 min, hors bornes = refus possible.

*Le bloc Préparation soutenance est donc présent sur ce projet.*

---

## 🔧 Specs techniques

Langage / stack : JavaScript vanilla, HTML fourni, communication avec une API via fetch. Backend Node.js fourni (non livrable, outil de test). Structure de données : données récupérées de l'API. Ressources works (travaux), categories, users. Token d'authentification à stocker après login. Fichiers touchés : dossier FrontEnd. index.html fourni. Créés from scratch : `script.js` (galerie + filtres), à venir page login et fichiers JS modale. Approche : manipulation du DOM, gestion des événements, appels API. Galerie et filtres générés dynamiquement, plus aucun travail ni bouton de filtre en dur dans le HTML (seul le conteneur `ul.filters` est statique). Icônes : instagram.png présent dans FrontEnd/assets/icons. Breakpoints : à extraire de la maquette Figma (desktop dispo, mobile pas encore). Mise en page : à extraire de la maquette Figma (desktop dispo). Design tokens extraits (fiche dédiée `sophie-bluel-design-tokens.md`) : polices Syne (titres) + Work Sans (texte), vert marque `#1D6154`, terracotta logo `#B1663C`, fond maquette crème `#FFFEF8` (le CSS fourni est sur blanc par défaut). Pas de : framework, librairie externe. JS natif. Animations : à définir avec la maquette. Valide : W3C aux étapes structurantes, Lighthouse sur URL de prod en navigation privée, axe DevTools, NVDA.

Deux méthodes de génération DOM coexistent volontairement pour l'instant : `createElement` / `appendChild` pour la galerie (étape 2), template littéral + `insertAdjacentHTML` pour les filtres (étape 3). Alignement à trancher.

---

## ✅ Todo

**Étape 0, installation et prise de connaissance**

- [x]  Installer Node.js et npm
- [x]  Prendre connaissance du Kanban et du code fourni
- [x]  Installer les dépendances du Backend (suivre son ReadMe)
- [x]  Lancer le back-end
- [x]  Découvrir la doc Swagger de l'API
- [x]  Tester la route de récupération des travaux (Swagger ou Postman)
- [x]  Récupérer le lien Figma de la maquette

---

**Étape 1, versioning**

- [x]  Initialiser le versioning local (git init)
- [x]  Premier commit
- [x]  Créer le dépôt distant sur GitHub
- [x]  Ajouter la référence du dépôt distant (remote)

*Fait en début de session. Ordre inversé (repo distant créé avant le local), sans conséquence.*

---

**Étape 2, galerie dynamique** : terminée

- [x]  Récupérer les travaux via fetch
- [x]  Les afficher dynamiquement dans la galerie
- [x]  Supprimer du HTML les travaux statiques (ne garder que le dynamique)
- [x]  Compréhension des étapes 0 à 2 contrôlée avant de passer à l'étape 3

---

**Étape 2 bis, refactor éventuel (piste mentor)** : tranchée

- [x]  Exo console sur les templates littéraux (hors projet)
- [x]  Exo console sur `insertAdjacentHTML` (hors projet)
- [x]  Décider si la galerie est refactorée ou laissée en `createElement` / `appendChild` → décision : la méthode template littéral + `insertAdjacentHTML` est retenue et appliquée aux filtres. La galerie de l'étape 2 reste en `createElement`, à aligner ou à justifier.

---

**Étape 3, filtres par catégorie (affichage)** : terminée

- [x]  Afficher les filtres au-dessus de la galerie (bouton Tous + catégories de l'API)
- [x]  Styler les boutons de filtre selon la maquette
- [x]  Conteneur `ul.filters` posé en dur dans `index.html`, entre le `h2` et `.gallery`
- [x]  Découpage en deux fonctions, `fetchCategories` et `createButtons`
- [ ]  **Validation W3C non faite** alors que `index.html` a été modifié (ajout du `ul.filters`). Étape structurante, à faire avant d'aller plus loin.
- [→]  Bouton Tous actif par défaut au chargement → déplacé à l'étape 4 (c'est de la gestion d'état, pas de l'affichage)

---

**Étape 4, filtre fonctionnel**

- [ ]  Filtrer les travaux au clic sur une catégorie
- [ ]  Bouton Tous actif par défaut au chargement (état visuel `filter-selected` de la maquette, repéré à l'étape 3)
- [ ]  Gérer le retrait de l'état actif sur le bouton précédent

---

**Étape 5, page de connexion (intégration)**

- [ ]  Intégrer la page de login conforme à la maquette, non fonctionnelle

---

**Étape 6, login fonctionnel**

- [ ]  Requête POST avec les identifiants
- [ ]  Redirection vers l'accueil si connexion OK
- [ ]  Message d'erreur si identifiants incorrects
- [ ]  Stocker le token d'authentification

---

**Étape 7, page d'accueil mode connecté**

- [ ]  Bandeau noir mode édition en haut
- [ ]  login devient logout dans la nav
- [ ]  Déconnexion fonctionnelle
- [ ]  Filtres cachés
- [ ]  Bouton Modifier affiché

---

**Étape 8, modale**

- [ ]  Deux zones (galerie suppression + formulaire ajout)
- [ ]  Ouverture au clic sur Modifier
- [ ]  Fermeture au clic sur la croix et en dehors de la modale
- [ ]  Une seule modale dans le DOM quel que soit le nombre d'ouvertures
- [ ]  Clic Ajouter une photo affiche le formulaire
- [ ]  Flèche retour ramène à la galerie

---

**Étape 9, suppression d'un travail**

- [ ]  Requête DELETE vers l'API
- [ ]  Retrait du DOM après confirmation, sans recharger

---

**Étape 10, formulaire d'ajout**

- [ ]  Preview à la sélection d'image
- [ ]  Catégories récupérées dynamiquement de l'API
- [ ]  Message d'erreur si formulaire incomplet
- [ ]  Envoi via FormData au bon format attendu par l'API

---

**Étape 11, ajout dynamique au DOM**

- [ ]  Ajout du projet dans la galerie principale après envoi, sans recharger
- [ ]  Ajout du projet dans la galerie de la modale

---

**Étape 12, test et validation finale**

- [ ]  Tester les formulaires avec des données erronées
- [ ]  Vérifier la conformité visuelle à la maquette
- [ ]  Vérifier la gestion de l'interface à l'ajout et à la suppression
- [ ]  Projet prêt pour la soutenance

---

**Refactor / Nettoyage**

- [x]  Sortir `Backend/.env` du suivi Git et l'ignorer
- [x]  Décider du sort de `.vscode/settings.json` (gardé suivi, question posée au mentor)
- [x]  Vérifier que `Backend/node_modules/` est ignoré avant le prochain add
- [ ]  Restructurer le repo pour GitHub Pages (index.html est dans FrontEnd/, Pages sert la racine, voir Point de reprise)
- [ ]  Aligner la galerie de l'étape 2 sur la méthode template littéral + `insertAdjacentHTML`, ou justifier de la laisser en `createElement`
- [ ]  Renommer la classe `filters-button` en `filter-button` (cohérence avec la règle appliquée aux messages de commit : un nom qui en qualifie un autre reste au singulier)

---

**Performance**

- [ ]  Lighthouse sur l'URL de production, navigation privée

---

**Contenu & Accessibilité**

- [x]  `alt` pertinents sur les images générées dynamiquement (galerie : `alt` = `work.title`)
- [ ]  Navigation clavier de la modale, focus visible
- [ ]  Contrastes conformes
- [ ]  Éléments générés en JS aussi accessibles que du HTML écrit à la main (galerie OK, filtres à vérifier, modale à venir)
- [ ]  Boutons de filtre : navigation clavier et focus visible à vérifier
- [ ]  Contraste du texte des boutons (`#1D6154` sur blanc) à vérifier, et surtout l'état actif de la maquette (texte blanc sur `#1D6154`)
- [ ]  Passer axe DevTools sur la page une fois l'étape 4 terminée

---

**Responsive**

- [ ]  En attente maquette mobile (Kanban : version mobile en cours côté design)

---

**Avant de rendre**

- [ ]  Rendu conforme à la maquette
- [ ]  W3C, Lighthouse, DevTools
- [ ]  Préparer le ZIP livrable et le fichier lien repo

---

## 🧗 Ce qu'il va falloir maîtriser sur ce projet

**Notions jamais pratiquées avant ce projet**

- [ ]  Appels API avec fetch (GET, POST, DELETE) → GET acquis à l'étape 2, réutilisé à l'étape 3
- [x]  Récupérer et injecter des données distantes dans le DOM → fait à l'étape 2 (galerie) et à l'étape 3 (filtres)
- [ ]  Gestion d'événements utilisateurs à plus grande échelle
- [ ]  Objet FormData pour l'envoi de formulaire
- [ ]  Authentification : envoi d'identifiants, réception et stockage d'un token
- [ ]  Stockage navigateur (localStorage ou sessionStorage) pour le token
- [ ]  Fenêtre modale from scratch (ouverture, fermeture, navigation interne)
- [ ]  Preview d'image avant upload
- [x]  Templates littéraux (backticks) → orienté par le mentor, vus en console et appliqués à l'étape 3
- [x]  `insertAdjacentHTML` comme alternative à `createElement` / `appendChild` → orienté par le mentor, vu en console (4 positions) et appliqué à l'étape 3

**Notions déjà vues mais fragiles, à consolider ici**

- [x]  createElement, appendChild, querySelector → réutilisés et consolidés à l'étape 2 (classList et addEventListener restent à revoir)
- [x]  Parcours d'un tableau de données pour générer du DOM → fait avec forEach à l'étape 2, refait à l'étape 3
- [ ]  Portée des variables (bloc, callback, fonction) → règle connue depuis P5, retrouvée à tâtons lors du découpage en fonctions de l'étape 3

**Pièges déjà connus à surveiller**

- Ne pas cocher README ni .gitignore auto à la création du repo GitHub (fait sur ce repo, à surveiller sur les suivants)
- `.gitignore` à penser AVANT le premier `git add`, jamais après
- Un `.env` ne se committe jamais
- `alt` en français, pas en anglais (piège relevé en P5). Note étape 2 : l'`alt` de la galerie vaut `work.title`, qui vient de l'API en anglais. Question posée au mentor (voir Questions).
- Ne jamais fermer le terminal du backend à la croix : le processus Node peut survivre et bloquer le port 5678.
- Le formatage automatique de l'éditeur peut reformater tout un fichier fourni et noyer le `git diff`. Piège déjà rencontré en P4, revu à l'étape 3 sur `style.css`.

---

## 🔍 Choix techniques

> Format : `décision → pourquoi`.

**Setup et Git**

- `.env` retiré du suivi et ignoré → un secret ne se committe jamais. L'historique le garde encore, non critique ici (backend d'exercice fourni). Réflexe pro pour un vrai secret fuité : rotation du secret, pas seulement le retrait du suivi.
- `.vscode/settings.json` laissé suivi → choix assumé, question posée au mentor.
- Un seul commit pour l'étape 2 (afficher + retirer le statique) → les deux forment un tout cohérent ; un commit intermédiaire gardant le statique afficherait les projets en double.
- `script.js` placé dans `FrontEnd/` à côté de `index.html` → `src="script.js"` simple, même dossier.
- `[à valider]` Un fichier JS par responsabilité (galerie, login, modale) plutôt qu'un seul gros fichier, à trancher selon l'ampleur.

**API et structure du code**

- Approche `.then` chaînée plutôt que `async / await` → notion déjà pratiquée en console, async/await pas encore vue.
- `forEach` plutôt qu'une boucle `for` avec `length - 1` → pas de compteur à gérer, pas de risque de dépasser l'index.
- `forEach` plutôt que `map` pour la galerie → la génération DOM est une action, aucune valeur de retour n'est nécessaire. `map` servirait si on voulait récupérer un tableau de résultats.
- `forEach` plutôt que `for...of` pour les filtres → `for...of` sert quand on a besoin d'interrompre la boucle avec `break`. Ici il faut parcourir toutes les catégories jusqu'au bout, donc `forEach` suffit, comme à l'étape 2.
- Découpage en deux fonctions, `fetchCategories` et `createButtons` → responsabilité unique. Une fonction va chercher les données, l'autre fabrique les boutons. Celle qui fabrique n'a besoin que d'un tableau, peu importe d'où il vient.
- `<script src="script.js" defer>` dans le `<head>` → defer exécute le script après le chargement du HTML, donc querySelector trouve bien la galerie.
- `[à valider]` localStorage vs sessionStorage pour le token, à trancher selon le comportement voulu à la fermeture de l'onglet.

**Génération du DOM**

- Template littéral + `insertAdjacentHTML` plutôt que `createElement` / `appendChild` pour les filtres → une seule instruction fabrique et pose l'élément, là où `createElement` en demandait quatre. Décision prise après les deux exos console. Remplace la ligne `[en suspens]` de la version précédente.
- `beforeend` pour les boutons de catégorie, `afterbegin` pour le bouton `Tous` → `Tous` reste en tête, les catégories s'ajoutent à la suite dans l'ordre de l'API.
- Conteneur `ul.filters` en dur dans le HTML, boutons générés en JS → le conteneur est toujours là quoi qu'il arrive, les boutons dépendent des données de l'API. Règle générale : ce qui est stable va en dur, ce qui dépend des données va en JS.

**Sémantique et accessibilité**

- `alt` de l'image générée = `work.title` → image fonctionnelle, le titre décrit le projet (socle accessibilité).
- `ul` plutôt que `div` pour le conteneur des filtres → le lecteur d'écran annonce une liste, avec le nombre d'éléments et la position dans la liste. Un `div` n'apporte rien de tout ça.
- Pas de `nav` pour les filtres → un clic sur un filtre ne mène nulle part, on reste au même endroit. Ce n'est pas de la navigation mais une commande d'affichage. Donc `button`, pas un lien.
- `[à valider]` `type="button"` explicite sur chaque bouton de filtre → un `button` sans `type` vaut `submit` par défaut. Sans conséquence hors formulaire, mais l'écrire évite un envoi involontaire si le bouton se retrouve un jour dans un `form`. À confirmer comme choix assumé et non comme réflexe.

**CSS et contenu**

- Design tokens extraits du `style.css` fourni plutôt que de Figma → le CSS est le code réellement appliqué (source qui fait foi). Écart relevé : le CSS ne met aucun fond (blanc), la maquette est sur crème `#FFFEF8`.
- Classe `filters-button` sur les boutons plutôt qu'un sélecteur CSS `button` → le projet aura d'autres boutons (login, modale, ajout de photo) qui ne doivent pas hériter du style des filtres. Nom à corriger en `filter-button` (voir Refactor).
- Texte du bouton `Tous` en français → c'est du contenu affiché à l'utilisateur. L'anglais reste réservé aux noms de variables et de fonctions.

---

## 📐 Formule / méthode de calcul

*Non applicable pour l'instant.*

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

---

## 🔍 Vérification

- [x]  La galerie affiche bien les travaux de l'API
- [x]  Plus aucun travail en dur dans le HTML
- [x]  Compréhension des étapes 0 à 2 contrôlée (appendChild, json, forEach, git, defer)
- [x]  Les filtres affichent les bonnes catégories
- [x]  Le bouton `Tous` apparaît en première position, les catégories suivent dans l'ordre de l'API
- [x]  Aucun bouton de filtre en dur dans le HTML, seul le `ul` conteneur est statique
- [x]  Le refactor en deux fonctions n'a pas changé le rendu à l'écran
- [x]  Le style des boutons ne déborde pas sur les autres boutons du projet (classe dédiée)
- [x]  `style.css` restauré à son formatage d'origine avant commit (diff lisible)
- [ ]  `index.html` validé au W3C après ajout du `ul.filters`
- [ ]  Boutons de filtre atteignables au clavier, focus visible
- [ ]  Le clic sur un filtre affiche les bons travaux
- [ ]  Le login redirige si OK, affiche une erreur si KO
- [ ]  Le token est bien stocké
- [ ]  Le mode connecté change l'affichage attendu
- [ ]  La modale ne se duplique pas après plusieurs ouvertures
- [ ]  La suppression retire le travail sans recharger
- [ ]  L'ajout affiche le travail sans recharger, dans les deux galeries

---

## 🐛 Journal de bugs

> `bug observé → cause réelle → correction`.

**Étape 2 et setup**

- `console.log(donnees.forEach(...))` affiche `undefined` en plus → `forEach` ne renvoie rien, le log extérieur affiche ce retour vide → retirer le console.log extérieur, garder celui dans le forEach
- Erreur de syntaxe en mettant plusieurs lignes après `work =>` → la flèche courte n'accepte qu'une seule expression → ajouter des accolades `{ }` après la flèche pour un bloc multi-lignes
- `setAttribute` rangé dans un `const`, avec un seul argument → setAttribute ne renvoie rien et attend deux arguments (nom, valeur) → retirer le const, ajouter la valeur `work.imageUrl`
- `src` rempli avec `"imageUrl"` (texte) → les guillemets passent la chaîne littérale au lieu de la valeur → `work.imageUrl` sans guillemets
- `project.appendChild(".gallery")` → sens inversé et chaîne au lieu d'un élément → `gallery.appendChild(project)`, passer la variable, pas une string
- Créations placées hors du forEach → `work` n'existe que dans le forEach et le code ne se répéterait pas → déplacer les créations dans le forEach
- `git diff` vide sur `index.html` pourtant modifié → fichier déjà stagé (git add déjà fait) → `git diff --cached` pour voir le stagé
- Fenêtre PowerShell du backend fermée à la croix, puis `npm start` répond `port: 5678 is already in use` → fermer la fenêtre ne tue pas toujours le processus Node, qui continue d'occuper le port → trouver le PID avec `Get-NetTCPConnection -LocalPort 5678 -State Listen`, puis `Stop-Process -Id <PID>`. Prévention : arrêter le backend avec `Ctrl + C`.
- Deux backends lancés en parallèle sans s'en rendre compte → un terminal oublié en arrière-plan → vérifier avant de relancer, un seul backend doit tourner.

**Étape 3**

- `insertAdjacentHTML("afterbegin", ...)` dans le `forEach` → chaque nouveau bouton se posait en tête, donc l'ordre s'inversait et `Tous` finissait en dernier → `beforeend` dans le `forEach`, `afterbegin` conservé pour `Tous` seul
- `categorie = ...` dans le `forEach` pour construire le HTML → écrasait la donnée du tour en cours, `${categorie.name}` ne pouvait plus fonctionner, et rien n'était posé dans la page → ranger le HTML dans une variable dédiée (`buttonCategorie`) puis appeler `filters.insertAdjacentHTML`
- Ligne `insertAdjacentHTML` du bouton `Tous` placée dans le `forEach` → elle se serait exécutée une fois par catégorie, donc autant de boutons `Tous` que de catégories → la sortir de la boucle, avant le `forEach`
- Lignes `insertAdjacentHTML` écrites en dehors de la fonction et du `forEach` → `buttonAll` et `buttonCategorie` sont déclarés à l'intérieur, donc inaccessibles depuis l'extérieur → replacer chaque insertion dans le bloc où sa variable est déclarée
- `.then` écrit à l'intérieur de `createButtons` → un `.then` s'accroche à une promesse, or `donnees` y est déjà le tableau → retirer le `.then`, garder le `forEach` seul
- `.then(donnees => createButtons)` → sans les parenthèses, la fonction est seulement nommée, pas appelée → `createButtons(donnees)`
- Guillemets autour de `${categorie.name}` dans le template → le nom se serait affiché entre guillemets à l'écran → guillemets retirés
- Style écrit sur le sélecteur `button` → aurait touché tous les futurs boutons du projet (login, modale, ajout) → classe dédiée sur les boutons de filtre, sélecteur CSS corrigé
- Sélecteur CSS corrigé mais classe absente du bouton `Tous` → seul le HTML des catégories avait été modifié → ajouter la classe sur les deux
- Fichier `style.css` entièrement reformaté à la sauvegarde (sélecteurs éclatés ligne par ligne) → formatage automatique de l'éditeur, déjà rencontré en P4 → fichier restauré à son formatage d'origine avant commit
- **Piège identifié, pas vécu** (repéré sur l'exemple du mentor) : `innerHTML = ` à l'intérieur d'une boucle écrase le contenu à chaque tour, seul le dernier élément reste affiché. Solutions : empiler dans une variable avec `+=` puis injecter une seule fois après la boucle, ou utiliser `insertAdjacentHTML` qui ajoute sans écraser.

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

---

## 📋 Bilan, préparation session mentor

> `[à valider]` Proposé, à confirmer.

### 🔴 Difficultés rencontrées

- `[à valider]` Syntaxe des fonctions fléchées multi-lignes (besoin des accolades)
- `[à valider]` `setAttribute` : deux arguments, pas de `const` devant
- `[à valider]` Sens de `appendChild` (le parent reçoit) et placement du code dans le `forEach`
- `[à valider]` Mise en ligne GitHub Pages : structure `FrontEnd/` sous-dossier contre racine servie par Pages
- `[à valider]` `map` non assimilé après plusieurs angles. Notion mise de côté volontairement plutôt que forcée en fin de session.
- `[à valider]` Réflexe "je sais pas" avant d'avoir cherché, signalé plusieurs fois en session.
- `[à valider]` Blocage complet, sur une session entière, sur l'affichage des données de l'API en console. Sortie trouvée seulement à la session suivante.
- `[à valider]` Assembler deux morceaux déjà écrits (l'appel `insertAdjacentHTML` et le HTML de la catégorie) : blocage long alors que les deux pièces existaient
- `[à valider]` Portée des variables retrouvée à tâtons lors du découpage en fonctions (`buttonAll` et `buttonCategorie` déplacés plusieurs fois avant d'atterrir au bon endroit)
- `[à valider]` Réflexe de repartir sur `createElement` après avoir tranché le passage aux templates littéraux
- `[à valider]` Formulation des messages de commit en anglais (accords, ordre des mots), plusieurs allers-retours
- `[à valider]` Fatigue de fin de session : plusieurs blocages tenaient à ça plus qu'à la notion elle-même

### 🟢 Points forts

- `[à valider]` Setup Git propre et autonome (root-commit, message conventionnel, remote, push)
- `[à valider]` fetch, forEach et injection DOM compris et réexpliqués avec mes mots
- `[à valider]` Accessibilité posée dès la génération (`alt` sur image dynamique)
- `[à valider]` Commit conventionnel propre pour l'étape 2
- `[à valider]` Étapes 0 à 2 réexpliquées sans le code sous les yeux
- `[à valider]` Diagnostic du port occupé mené jusqu'au bout, cause comprise et prévention identifiée
- `[à valider]` Choix HTML contre JS pour les boutons justifié seul, par analogie avec l'étape 2
- `[à valider]` `nav` écarté et `button` retenu sur un raisonnement d'usage, pas par habitude
- `[à valider]` `ul` justifié sur un argument d'accessibilité concret
- `[à valider]` Pseudocode écrit, puis nettoyé de ce qui appartenait à l'étape 4
- `[à valider]` Erreur de position d'insertion (`afterbegin` contre `beforeend`) diagnostiquée et corrigée seul, en observant le rendu
- `[à valider]` Deux notions pointées par le mentor découvertes en console et reformulées avec mes mots
- `[à valider]` Refactor en deux fonctions mené jusqu'au bout sans casser le rendu
- `[à valider]` Portée du sélecteur CSS anticipée seul (classe dédiée plutôt que sélecteur `button`)
- `[à valider]` État `filter-selected` repéré sur la maquette et volontairement reporté à l'étape 4
- `[à valider]` Reformatage automatique de `style.css` repéré et annulé avant commit
- `[à valider]` Trois commits atomiques sur l'étape 3, un par sujet (feature, refactor, style)

### ➡️ À revoir / approfondir

- `[à valider]` `async / await` (croisé, pas encore pratiqué)
- `[à valider]` Restructuration du repo pour la mise en ligne
- `[à valider]` `map`, à froid, sur exo dédié
- `[à valider]` `.catch` dans une chaîne de promesses
- `[à valider]` Réduire la dépendance à l'IA : plus de `console.log`, plus de recherche MDN autonome, indices plus courts (consigne mentor, intégrée au prompt v7)
- `[à valider]` Portée des variables (quel bloc, quelle boucle, quelle fonction) : à consolider sur un exo dédié
- `[à valider]` Traduire un pseudocode en code sans aide, morceau par morceau
- `[à valider]` Aligner ou non la galerie de l'étape 2 sur les templates littéraux
- `[à valider]` Réflexes du socle intégrateur (W3C aux étapes structurantes) : à déclencher sans qu'on me le rappelle

---

## ❓ Questions pour le mentor

> `[à valider]` Propositions.

1. `[à valider]` localStorage ou sessionStorage pour le token, quelle pratique attendue ?
2. `[à valider]` Le backend fourni doit-il rester dans mon repo, ou seul le front-end est attendu comme livrable ?
3. `[à valider]` L'`alt` de la galerie vaut `work.title`, qui vient de l'API en anglais. Acceptable pour l'accessibilité, ou faut-il autre chose ?
4. `[à valider]` GitHub Pages : `index.html` est dans `FrontEnd/`. Quelle structure recommandée pour la mise en ligne (remonter à la racine, dossier `docs/`) ?
5. `[à valider]` Le refactor de la galerie en template littéral + `insertAdjacentHTML` est-il attendu pour la soutenance, ou `createElement` reste-t-il acceptable s'il est maîtrisé ?
6. `[à valider]` Deux méthodes de génération DOM dans le même fichier (galerie en `createElement`, filtres en template littéral) : acceptable si les deux sont justifiées, ou incohérence à corriger ?
7. `[à valider]` L'état visuel du filtre actif (`filter-selected` de la maquette) : plutôt une classe posée en JS, ou une autre approche attendue ?
8. `[à valider]` `type="button"` systématique sur les boutons hors formulaire : pratique attendue en agence, ou bruit inutile ?
9. `[à valider]` Un bouton de filtre actif doit-il porter une information d'état pour un lecteur d'écran, ou la classe CSS suffit-elle à ce niveau de projet ?

---

## Commit

```powershell
git log --oneline
```

- `feat: add style to filter buttons` (FR : ajouter le style des boutons de filtre)
- `refactor: split filter script into two functions` (FR : séparer le script des filtres en deux fonctions)
- `feat: add filter buttons from API` (FR : ajouter les boutons de filtre depuis l'API)
- `2fd429c` feat: display works from API (FR : afficher les travaux depuis l'API)
- `85f4ea2` chore: untrack .env
- `0d5d46d` chore: initial project setup

*Hashes des trois commits de l'étape 3 à relever avec `git log --oneline` et à reporter ici.*

---

## 🎤 Préparation soutenance

> Projet évalué en soutenance. Bloc actif.

Format : 15 min présentation, 10 min discussion, 5 min débriefing. Timer conseillé (rappel mentor P3).

**Sujets à maîtriser**

- [~] Expliquer les appels API et la récupération des données → base acquise (fetch, chaîne `.then`, `Response`, `.json()`, structure works et categories)
- [ ]  Expliquer la gestion de la connexion, différence connecté / non connecté
- [~] Expliquer le fonctionnement du filtre → l'affichage des boutons est maîtrisé et justifié. Le filtrage au clic reste à faire (étape 4).
- [ ]  Expliquer l'envoi de nouvelles images à l'API
- [~] Justifier l'usage de Git et des commits → historique propre, format conventionnel, commit atomique par étape
- [~] Justifier le choix `forEach` plutôt que `map` pour la génération DOM
- [ ]  Justifier le choix `insertAdjacentHTML` plutôt que `createElement`, et les quatre positions
- [ ]  Justifier le découpage en deux fonctions (responsabilité unique)
- [ ]  Justifier `ul` plutôt que `div`, et `button` plutôt que lien
- [ ]  Expliquer pourquoi `fetchCategories()` est appelée à la main et `createButtons` non

---

## 🧠 Nouvelles connaissances

> Sous-blocs adaptés au projet : SVG et Animations CSS retirés, JavaScript / DOM, API & fetch, Authentification ajoutés.

### JavaScript, bases

- Fonction fléchée courte `x => ...` : une seule expression. Plusieurs instructions : accolades `{ }` après la flèche.
- Différence **renvoyer** (rendre une valeur qu'on récupère, ex fetch) et **faire une action** (forEach, setAttribute ne renvoient rien, `undefined`).
- `undefined` est ce que renvoie une fonction qui ne retourne rien. Un `console.log` qui affiche `undefined` est une preuve, pas un bug.
- Template littéral (backticks) : une seule paire de délimiteurs, les variables insérées avec `${}`, aucun `+` et aucun guillemet à rouvrir. La concaténation classique demandait trois paires de guillemets et des `+` pour la même phrase.
- Le backtick autorise le passage à la ligne dans une chaîne. Les guillemets classiques lèvent `Uncaught SyntaxError: Invalid or unexpected token`.
- Une erreur de syntaxe dans un bloc collé en console empêche tout le bloc de s'exécuter, y compris les lignes valides avant l'erreur. Rejouer les instructions séparément pour isoler.
- `for...of` peut être interrompue en cours de route avec `break`. `forEach` ne le peut pas : `break` y lève `Illegal break statement`, la boucle va toujours jusqu'au bout. Un `if` reste possible dans les deux.
- Réaffecter la variable du callback (`categorie = ...`) détruit la donnée du tour en cours. Utiliser une variable dédiée.
- Nommer une fonction sans parenthèses ne l'appelle pas. `createButtons` désigne la fonction, `createButtons(donnees)` l'exécute.
- Une fonction déclarée n'est exécutée que si quelque chose l'appelle. `fetchCategories()` est appelée à la main en bas du fichier, `createButtons` est appelée par le `.then` quand les données arrivent.
- Une variable déclarée dans un bloc (fonction, callback) n'existe pas en dehors. L'instruction qui l'utilise doit vivre dans le même bloc. Règle déjà posée en P5.

### JavaScript / DOM, notions avancées

- `document.createElement("balise")` : crée l'élément en mémoire, invisible tant qu'il n'est pas accroché.
- `element.textContent = "..."` : met du texte dans une balise.
- `element.setAttribute("nom", valeur)` : pose un attribut. Deux arguments. Ne renvoie rien.
- `parent.appendChild(enfant)` : accroche l'élément dans la page. Le parent reçoit, l'enfant est accroché.
- Les enfants suivent leur parent : accrocher un élément déplace tout ce qu'il contient. L'ordre des `appendChild` (parent d'abord ou enfants d'abord) ne change pas le rendu.
- `querySelector` qui ne trouve rien renvoie `null`. Toute méthode appelée ensuite dessus lève `Cannot read properties of null`.
- `forEach` : un tour par élément du tableau. À chaque tour, la variable contient l'élément entier (l'objet), pas son index. On lit une valeur avec le point : `work.imageUrl`, `work.title`.
- Piège : un élément créé mais non accroché existe mais ne s'affiche pas.
- `element.insertAdjacentHTML(position, html)` : le texte passé est interprété comme du HTML, pas posé comme du texte brut. Crée et pose en une seule instruction, là où `createElement` demandait de créer, remplir, puis accrocher.
- Les quatre positions, relatives aux balises de l'élément cible, pas à son contenu :
  - `beforebegin` : avant la balise ouvrante, donc à l'extérieur
  - `afterbegin` : après la balise ouvrante, donc à l'intérieur, en premier
  - `beforeend` : avant la balise fermante, donc à l'intérieur, en dernier
  - `afterend` : après la balise fermante, donc à l'extérieur
- `insertAdjacentHTML` ajoute sans écraser, contrairement à `innerHTML = `. Pas besoin d'accumuler dans une variable avant d'injecter.
- Vérification en console : `element.outerHTML` montre l'élément avec ses balises, `element.parentElement.innerHTML` montre son voisinage.

### API & fetch

- Route `GET /api/works` : renvoie un tableau d'objets. Chaque travail a `id`, `title`, `imageUrl` (URL complète, prête pour un `src`), `categoryId`, et `category { id, name }`.
- Route `GET /api/categories` : renvoie la liste des catégories, chacune avec `id` et `name`. C'est `name` qui alimente le texte des boutons de filtre.
- `categoryId` (numéro) sert à comparer, `category.name` (texte) sert à afficher.
- Route `POST /api/users/login` : attend `email` et `password`, renvoie `{ userId, token }` si OK, `404` sinon.
- Swagger (`Try it out` / `Execute`) permet de tester une route en vrai et de voir la forme des données.
- Une route d'API en GET peut aussi être ouverte directement dans la barre d'adresse du navigateur : les données s'affichent telles quelles.
- `fetch("url")` renvoie une promesse, pas les données. La promesse est d'abord `pending`.
- Trois états d'une promesse : `pending`, `fulfilled` (tenue), `rejected` (rompue, ex serveur éteint).
- La réponse de fetch est un objet `Response`, une enveloppe. `reponse.json()` l'ouvre et extrait les données.
- Le `Response` arrive dès les en-têtes reçus (`status`, `ok`), avant que le corps soit téléchargé. C'est pour ça que `.json()` renvoie une deuxième promesse : la lecture du corps prend du temps.
- `Response.body` est un `ReadableStream`, un flux de données brutes. Les données ne sont lisibles nulle part dans le `Response` tel quel.
- C'est `.json()` qui ouvre et convertit. Le `.then` suivant ne fait que récupérer le résultat une fois prêt.
- Gestion d'erreur dans une chaîne `.then` : maillon `.catch`, pas `try / catch` (qui va avec `async / await`).
- Chaîne type : `fetch(url).then(r => r.json()).then(donnees => ...)`. Appliquée en vrai à `GET /api/works` puis à `GET /api/categories`.

### Authentification

- Le token d'authentification vient de la réponse du login, à stocker pour les actions protégées (ajout, suppression).

### Débogage

- Réflexe : vérifier chaque étape avec un `console.log` avant de continuer (galerie attrapée, données reçues, boucle qui passe sur chaque élément).
- `git diff` ne montre rien pour un fichier untracked (pas de version précédente) ni pour un fichier déjà stagé (utiliser `git diff --cached`).
- Recharger la page et observer le rendu est parfois plus rapide qu'un raisonnement : l'ordre d'insertion des boutons a été tranché comme ça.

### HTML & Sémantique

- Un projet de galerie = une `figure` contenant une `img` et une `figcaption`. Même structure quand elle est générée en JS.
- Un `ul` n'accepte que des `li` comme enfants directs. Un `button` inséré dans un `ul` doit être enveloppé dans un `li`.
- `nav` est réservé à de la navigation (aller ailleurs). Un filtre déclenche une action sur place : c'est un `button`, pas un lien, et son conteneur n'est pas un `nav`.
- Un `button` sans attribut `type` vaut `submit` par défaut. Dans un `form`, il envoie le formulaire. `type="button"` le neutralise.
- Règle générale posée sur ce projet : ce qui est stable va en dur dans le HTML, ce qui dépend des données va en JS.

### CSS

- Un sélecteur de type (`button`) touche tous les éléments de ce type dans tout le projet, y compris ceux à venir. Une classe dédiée limite la portée.
- `ul` en `display: flex` avec `gap` pour aligner les filtres horizontalement : sans ça, les `li` s'empilent en colonne (comportement bloc par défaut).

### Accessibilité

- `alt` posé sur l'`img` générée dynamiquement, avec `work.title`. Même exigence d'accessibilité que du HTML écrit à la main (socle intégrateur).
- `ul` plutôt que `div` sur une liste de commandes : le lecteur d'écran annonce une liste, son nombre d'éléments et la position courante. Un `div` ne porte aucune de ces informations.
- `button` plutôt qu'un lien pour une action sur place : le lecteur d'écran annonce un bouton, et l'élément est nativement atteignable au clavier et activable avec Entrée ou Espace.

### Outils & process

- `git rm --cached fichier` retire un fichier du suivi Git sans le supprimer du disque. La variante sans `--cached` supprime aussi le fichier.
- Un `.gitignore` ne lâche pas un fichier déjà suivi. Il faut d'abord le retirer du suivi, puis l'ignorer pour l'avenir.
- Un `.gitignore` se pense avant le premier `git add`, jamais après.
- Backend Node lancé avec `npm start`, laisse le terminal occupé : prévoir un second terminal pour travailler en parallèle.
- `npm audit fix --force` sur un backend fourni est à éviter : il applique des changements de version cassants.
- Arrêter le backend : `Ctrl + C`, puis `O` si PowerShell demande. Libère le port 5678. Fermer la fenêtre à la croix ne suffit pas.
- `Get-NetTCPConnection -LocalPort <port> -State Listen | Select-Object -ExpandProperty OwningProcess` : trouve le PID qui occupe un port. `Stop-Process -Id <PID>` arrête ce seul processus.
- Le log du backend au démarrage montre la requête SQL exécutée à chaque appel de `/api/works`, avec la jointure sur `categories`. La forme des données y est lisible en clair.
- Connecteur Figma (MCP) : besoin d'un accès éditeur. Maquette OC en lecture seule, la dupliquer dans ses brouillons (`Duplicate to your drafts`), le connecteur lit ensuite la copie.
- Avertissement OC dans la maquette : le code du Dev Mode Figma est souvent de mauvaise qualité. Se servir de la maquette pour les specs, pas pour copier du code.
- `<script defer>` dans le `<head>` : le script s'exécute après le chargement du HTML.
- `git add .` depuis un sous-dossier ajoute les changements de ce dossier et en dessous. Git retrouve la racine (`.git`) depuis n'importe où dans le repo.
- Un commit = une unité cohérente et utile. Pas de commit pour un fichier vide.
- Contenu affiché à l'utilisateur en français, noms de variables et de fonctions en anglais.
- En anglais, un nom qui en qualifie un autre reste au singulier : `filter buttons`, `filter script`. Même règle à appliquer aux noms de classes CSS.
- Le formatage automatique de l'éditeur peut reformater tout un fichier fourni et noyer le `git diff`. Vérifier le diff avant de commiter.
- Un commit de refactor décrit ce qui a été fait, pas le fait que ce soit un refactor : le type `refactor:` porte déjà cette information.

---

## 📚 Théorie non pratiquée

**Notions non abordées sur ce projet** :

- `async / await` : croisé pendant la discussion sur fetch, pas pratiqué (on est resté sur `.then`).
- `map` : vu en console (`[1,2,3].map(n => n * 10)` renvoie `[10,20,30]`), non assimilé. À reprendre à froid sur un exo dédié.
- `Promise.prototype.catch` : mot-clé donné, pas encore lu ni pratiqué. Le code des filtres n'en a pas, comme celui de l'étape 2.
- `for...of` : vue en console pour la comparer à `forEach`, non utilisée dans le projet.
- Templates littéraux et `insertAdjacentHTML` : **retirés de cette liste**, vus en console et appliqués à l'étape 3.

**Accessibilité / archi** :

- Attributs d'état pour lecteur d'écran sur un bouton actif (`aria-pressed` ou équivalent) : croisé comme question, pas encore étudié.

**Lexique** :

- Swagger : interface de documentation d'une API, permet de tester ses routes
- FormData : objet JS pour construire des données de formulaire à envoyer, notamment avec fichier
- Token : jeton d'authentification renvoyé par l'API après login, à renvoyer pour les actions protégées
- Promise : promesse, objet renvoyé par fetch qui représente une donnée à venir (états : pending, fulfilled, rejected)
- defer : attribut de `<script>` qui exécute le script une fois tout le HTML chargé
- ReadableStream : flux de données brutes, contenu de `Response.body` avant conversion
- PID : identifiant numérique d'un processus en cours d'exécution
- Template littéral : chaîne délimitée par des backticks, acceptant `${}` et les retours à la ligne
- Interpolation : insertion d'une valeur dans une chaîne avec `${}`
- `insertAdjacentHTML` : méthode qui interprète une chaîne comme du HTML et l'insère à une position donnée par rapport à un élément
- Responsabilité unique : principe selon lequel une fonction ne fait qu'un seul travail
- Callback : fonction passée en argument à une autre, exécutée par elle (ex : la fonction dans `forEach`, dans `.then`)

---

## 🧭 Bilan technique (synthèse)

### Erreurs fréquentes

- Passer une chaîne `"imageUrl"` au lieu de la valeur `work.imageUrl`
- Oublier les accolades quand la fonction fléchée a plusieurs lignes
- Inverser le sens de `appendChild`
- Placer les créations hors du `forEach`
- Répondre "je sais pas" avant d'avoir cherché ou observé
- Écrire dans la variable du callback au lieu d'une variable dédiée
- Placer une instruction hors de la boucle ou hors de la fonction où sa variable est déclarée
- Oublier les parenthèses d'appel d'une fonction
- Modifier une règle CSS sans reporter le changement sur tous les éléments concernés

### Ce que je maîtrise

- fetch (GET) et la chaîne `.then` / `.json()`, y compris le rôle du `Response` et du flux
- forEach pour parcourir un tableau d'objets, et pourquoi il ne renvoie rien
- Injection DOM : createElement, setAttribute, textContent, appendChild, querySelector
- L'ordre des `appendChild` et pourquoi il est indifférent
- `defer` et ce qui casserait sans lui
- `git rm --cached` et la logique suivi / ignoré
- Commit conventionnel propre, historique lisible
- Templates littéraux et interpolation avec `${}`
- Les quatre positions de `insertAdjacentHTML`
- La différence `forEach` contre `for...of` (interruption avec `break`)
- Le choix entre HTML statique et génération JS, et sa justification
- La portée d'un sélecteur CSS et l'intérêt d'une classe dédiée

### À revoir

- `async / await`
- `map`
- `.catch` dans une chaîne de promesses
- Restructuration du repo pour la mise en ligne GitHub Pages
- Portée des variables lors d'un découpage en fonctions
- Passage du pseudocode au code, en autonomie
- Déclencher les vérifications du socle intégrateur sans rappel (W3C, clavier, contraste)

### Ce que j'ai découvert

- La chaîne fetch complète et le fonctionnement d'une promesse
- Le `ReadableStream` du corps de réponse
- L'injection DOM from scratch
- L'attribut `defer`
- Le connecteur Figma et la duplication de maquette en lecture seule
- Le diagnostic d'un port occupé sous PowerShell
- Les templates littéraux et `insertAdjacentHTML`
- Le principe de responsabilité unique appliqué à un découpage en fonctions

---

## 📝 Point de reprise

### Fait

- Cadrage bouclé : Swagger compris, arrêt backend connu, connecteur Figma opérationnel via copie de la maquette.
- Fiche de design tokens produite pour Claude Design (`sophie-bluel-design-tokens.md`).
- Notions découvertes en console, hors projet : fetch, forEach, injection DOM, templates littéraux, `insertAdjacentHTML`, `for...of` contre `forEach`.
- Étape 2 codée de bout en bout par moi, commitée et poussée (`2fd429c`).
- RDV mentor : orientation vers les templates littéraux et `insertAdjacentHTML`, et consigne de réduire la délégation à l'IA (plus de `console.log`, d'exos, de mots-clés, indices très courts).
- Contrôle de compréhension des étapes 0 à 2 : validé.
- Incident port 5678 occupé, diagnostiqué et résolu.
- Prompt v7 produit (barème d'indice à 5 niveaux, règle "notion qui ne passe pas", prompt réduit d'environ 40 %).
- Étape 3 terminée : conteneur `ul.filters` en dur dans `index.html`, bouton `Tous` et boutons de catégories générés en JS depuis `/api/categories`.
- Refactor en deux fonctions, `fetchCategories` et `createButtons`.
- Style des boutons de filtre appliqué, sur une classe dédiée `filters-button`.
- Trois commits poussés sur l'étape 3.

### État Git

- Branche `main`, à jour avec `origin/main`. Working tree propre après le dernier push.

### Vérifications faites

- Galerie affiche les works de l'API, une seule fois, sans doublon.
- Plus aucun travail en dur dans le HTML.
- `alt` présent sur chaque image générée.
- Étapes 0 à 2 réexpliquées avec mes mots, sans le code sous les yeux.
- Boutons de filtre affichés dans le bon ordre, `Tous` en tête.
- Rendu inchangé après le refactor en deux fonctions.
- Style limité aux boutons de filtre.
- `style.css` restauré à son formatage d'origine avant commit.

### Vérifications NON faites, à rattraper

- W3C sur `index.html` après ajout du `ul.filters`.
- Navigation clavier et focus visible sur les boutons générés.
- Contraste des boutons, notamment l'état actif de la maquette.
- `git diff` non relu avant le commit du CSS (proposé, écarté sur le moment).

### À relancer avant de coder

- Le backend : `cd Backend`, puis `npm start`. Sinon fetch échoue. Arrêt propre avec `Ctrl + C`, jamais à la croix.

### Prochaine action

1. W3C sur `index.html`, avant d'ajouter du code à l'étape 4.
2. Relever les hashes des trois commits de l'étape 3 et les reporter dans le bloc Commit.
3. Étape 4, filtre fonctionnel. Pseudocode français avant toute ligne de code.
4. Prévoir dans ce pseudocode l'état visuel du bouton actif, et le retrait de cet état sur le bouton précédemment actif.
5. Renommer `filters-button` en `filter-button` (commit `refactor:` séparé).
6. Trancher le sort de la galerie de l'étape 2.

### À m'expliquer et vérifier : mise en ligne GitHub Pages

- Problème identifié : mon `index.html` est dans `FrontEnd/`, mais Pages est réglé sur la branche `main` + dossier `/ (root)`. Pages cherche à la racine, ne trouve pas `index.html`, n'affiche rien.
- Pistes à m'expliquer proprement avant d'agir :
    1. Faire remonter le contenu de `FrontEnd/` à la racine du repo (le plus propre ; manip Git à comprendre, `git mv`, sans toucher à `Backend/`).
    2. Ou renommer `FrontEnd/` en `docs/` (Pages sait servir `/docs`), moins propre.
- À retenir : même une fois en ligne, la galerie restera vide, car le JS appelle `http://localhost:5678` (le backend local, que GitHub ne peut pas faire tourner). La mise en ligne sert surtout à passer Lighthouse en fin de projet, rien d'urgent.

### Notions restant à découvrir

- `map`, `.catch`, `async / await`
- Gestion du clic sur un bouton généré en JS (`addEventListener`, `classList`)
- Filtrage d'un tableau
- `dataset` pour associer une donnée (l'`id` de catégorie) à un élément HTML

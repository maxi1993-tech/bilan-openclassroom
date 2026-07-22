# Fiche P6, version 01

*Archive brute, état avant l'étape 3 (filtres). Déposée telle quelle, non modifiée.*
*Date de session inconnue, à compléter par Max.*

---

# **Sophie Bluel architecte d'intérieur**

## **🎯 Mission**

Client : Sophie Bluel, architecte d'intérieur (site portfolio).

Contexte : renfort dev front-end chez l'agence ArchiWebos. Trois missions : la page de présentation des travaux (à partir du HTML fourni), la page de connexion admin (from scratch), la modale d'upload de médias (from scratch).

Livrable : repo GitHub du code front-end. Fichier TXT ou PDF contenant le lien du repo. ZIP nommé `Titre_du_projet_nom_prénom`, livrable interne nommé `Nom_Prénom_1_repo_github_mmaaaa`.

Deadline : à confirmer.

Format évaluation : soutenance. 15 min de présentation (galerie/filtres, connexion, ajout de travaux), 10 min de discussion (l'évaluateur joue Charlotte), 5 min de débriefing. Tolérance 10 à 20 min, hors bornes = refus possible.

*Le bloc Préparation soutenance est donc présent sur ce projet.*

---

## **🔧 Specs techniques**

Langage / stack : JavaScript vanilla, HTML fourni, communication avec une API via fetch. Backend Node.js fourni (non livrable, outil de test). Structure de données : données récupérées de l'API. Ressources works (travaux), categories, users. Token d'authentification à stocker après login. Fichiers touchés : dossier FrontEnd. index.html fourni. Créés from scratch : `script.js` (galerie), à venir page login et fichiers JS modale. Approche : manipulation du DOM, gestion des événements, appels API. Galerie et filtres générés dynamiquement, plus aucun travail en dur dans le HTML. Icônes : instagram.png présent dans FrontEnd/assets/icons. Breakpoints : à extraire de la maquette Figma (desktop dispo, mobile pas encore). Mise en page : à extraire de la maquette Figma (desktop dispo). Design tokens extraits (fiche dédiée `sophie-bluel-design-tokens.md`) : polices Syne (titres) + Work Sans (texte), vert marque `#1D6154`, terracotta logo `#B1663C`, fond maquette crème `#FFFEF8` (le CSS fourni est sur blanc par défaut). Pas de : framework, librairie externe. JS natif. Animations : à définir avec la maquette. Valide : W3C aux étapes structurantes, Lighthouse sur URL de prod en navigation privée, axe DevTools, NVDA.

---

## **✅ Todo**

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

**Étape 2 bis, refactor éventuel (piste mentor)**

- [ ]  Exo console sur les templates littéraux (hors projet)
- [ ]  Exo console sur `insertAdjacentHTML` (hors projet)
- [ ]  Décider si la galerie est refactorée ou laissée en `createElement` / `appendChild`

---

**Étape 3, filtres par catégorie (affichage)**

- [ ]  Afficher les filtres au-dessus de la galerie (bouton Tous + catégories de l'API)
- [ ]  Bouton Tous actif par défaut au chargement
- [ ]  Styler les boutons de filtre selon la maquette

---

**Étape 4, filtre fonctionnel**

- [ ]  Filtrer les travaux au clic sur une catégorie

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

---

**Performance**

- [ ]  Lighthouse sur l'URL de production, navigation privée

---

**Contenu & Accessibilité**

- [x]  `alt` pertinents sur les images générées dynamiquement (galerie : `alt` = `work.title`)
- [ ]  Navigation clavier de la modale, focus visible
- [ ]  Contrastes conformes
- [ ]  Éléments générés en JS aussi accessibles que du HTML écrit à la main (galerie OK, modale à venir)

---

**Responsive**

- [ ]  En attente maquette mobile (Kanban : version mobile en cours côté design)

---

**Avant de rendre**

- [ ]  Rendu conforme à la maquette
- [ ]  W3C, Lighthouse, DevTools
- [ ]  Préparer le ZIP livrable et le fichier lien repo

---

## **🧗 Ce qu'il va falloir maîtriser sur ce projet**

**Notions jamais pratiquées avant ce projet**

- [ ]  Appels API avec fetch (GET, POST, DELETE) → GET acquis à l'étape 2
- [x]  Récupérer et injecter des données distantes dans le DOM → fait à l'étape 2 (galerie)
- [ ]  Gestion d'événements utilisateurs à plus grande échelle
- [ ]  Objet FormData pour l'envoi de formulaire
- [ ]  Authentification : envoi d'identifiants, réception et stockage d'un token
- [ ]  Stockage navigateur (localStorage ou sessionStorage) pour le token
- [ ]  Fenêtre modale from scratch (ouverture, fermeture, navigation interne)
- [ ]  Preview d'image avant upload
- [ ]  Templates littéraux (backticks) → orienté par le mentor
- [ ]  `insertAdjacentHTML` comme alternative à `createElement` / `appendChild` → orienté par le mentor

**Notions déjà vues mais fragiles, à consolider ici**

- [x]  createElement, appendChild, querySelector → réutilisés et consolidés à l'étape 2 (classList et addEventListener restent à revoir)
- [x]  Parcours d'un tableau de données pour générer du DOM → fait avec forEach à l'étape 2

**Pièges déjà connus à surveiller**

- Ne pas cocher README ni .gitignore auto à la création du repo GitHub (fait sur ce repo, à surveiller sur les suivants)
- `.gitignore` à penser AVANT le premier `git add`, jamais après
- Un `.env` ne se committe jamais
- `alt` en français, pas en anglais (piège relevé en P5). Note étape 2 : l'`alt` de la galerie vaut `work.title`, qui vient de l'API en anglais. Question posée au mentor (voir Questions).
- Ne jamais fermer le terminal du backend à la croix : le processus Node peut survivre et bloquer le port 5678.

---

## **🔍 Choix techniques**

> Format : `décision → pourquoi`.

- `.env` retiré du suivi et ignoré → un secret ne se committe jamais. L'historique le garde encore, non critique ici (backend d'exercice fourni). Réflexe pro pour un vrai secret fuité : rotation du secret, pas seulement le retrait du suivi.
- `.vscode/settings.json` laissé suivi → choix assumé, question posée au mentor.
- `[à valider]` Un fichier JS par responsabilité (galerie, login, modale) plutôt qu'un seul gros fichier, à trancher selon l'ampleur.
- `[à valider]` localStorage vs sessionStorage pour le token, à trancher selon le comportement voulu à la fermeture de l'onglet.
- Approche `.then` chaînée plutôt que `async / await` → notion déjà pratiquée en console, async/await pas encore vue.
- `forEach` plutôt qu'une boucle `for` avec `length - 1` → pas de compteur à gérer, pas de risque de dépasser l'index.
- `forEach` plutôt que `map` pour la galerie → la génération DOM est une action, aucune valeur de retour n'est nécessaire. `map` servirait si on voulait récupérer un tableau de résultats.
- `<script src="script.js" defer>` dans le `<head>` → defer exécute le script après le chargement du HTML, donc querySelector trouve bien la galerie.
- Un seul commit pour l'étape 2 (afficher + retirer le statique) → les deux forment un tout cohérent ; un commit intermédiaire gardant le statique afficherait les projets en double.
- `alt` de l'image générée = `work.title` → image fonctionnelle, le titre décrit le projet (socle accessibilité).
- `script.js` placé dans `FrontEnd/` à côté de `index.html` → `src="script.js"` simple, même dossier.
- Design tokens extraits du `style.css` fourni plutôt que de Figma → le CSS est le code réellement appliqué (source qui fait foi). Écart relevé : le CSS ne met aucun fond (blanc), la maquette est sur crème `#FFFEF8`.
- `[en suspens]` Génération de la galerie : `createElement` / `appendChild` (actuel) contre template littéral + `insertAdjacentHTML` (piste mentor). À trancher après exo dédié, pas avant.

---

## **📐 Formule / méthode de calcul**

*Non applicable pour l'instant.*

---

## **🧩 Pseudocode**

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

**Étape 3, filtres par catégorie** : à écrire avant de coder.

---

## **🔍 Vérification**

- [x]  La galerie affiche bien les travaux de l'API
- [x]  Plus aucun travail en dur dans le HTML
- [x]  Compréhension des étapes 0 à 2 contrôlée (appendChild, json, forEach, git, defer)
- [ ]  Les filtres affichent les bonnes catégories
- [ ]  Le clic sur un filtre affiche les bons travaux
- [ ]  Le login redirige si OK, affiche une erreur si KO
- [ ]  Le token est bien stocké
- [ ]  Le mode connecté change l'affichage attendu
- [ ]  La modale ne se duplique pas après plusieurs ouvertures
- [ ]  La suppression retire le travail sans recharger
- [ ]  L'ajout affiche le travail sans recharger, dans les deux galeries

---

## **🐛 Journal de bugs**

> `bug observé → cause réelle → correction`.

- `console.log(donnees.forEach(...))` affiche `undefined` en plus → `forEach` ne renvoie rien, le log extérieur affiche ce retour vide → retirer le console.log extérieur, garder celui dans le forEach
- Erreur de syntaxe en mettant plusieurs lignes après `work =>` → la flèche courte n'accepte qu'une seule expression → ajouter des accolades `{ }` après la flèche pour un bloc multi-lignes
- `setAttribute` rangé dans un `const`, avec un seul argument → setAttribute ne renvoie rien et attend deux arguments (nom, valeur) → retirer le const, ajouter la valeur `work.imageUrl`
- `src` rempli avec `"imageUrl"` (texte) → les guillemets passent la chaîne littérale au lieu de la valeur → `work.imageUrl` sans guillemets
- `project.appendChild(".gallery")` → sens inversé et chaîne au lieu d'un élément → `gallery.appendChild(project)`, passer la variable, pas une string
- Créations placées hors du forEach → `work` n'existe que dans le forEach et le code ne se répéterait pas → déplacer les créations dans le forEach
- `git diff` vide sur `index.html` pourtant modifié → fichier déjà stagé (git add déjà fait) → `git diff --cached` pour voir le stagé
- Fenêtre PowerShell du backend fermée à la croix, puis `npm start` répond `port: 5678 is already in use` → fermer la fenêtre ne tue pas toujours le processus Node, qui continue d'occuper le port → trouver le PID avec `Get-NetTCPConnection -LocalPort 5678 -State Listen`, puis `Stop-Process -Id <PID>`. Prévention : arrêter le backend avec `Ctrl + C`.
- Deux backends lancés en parallèle sans s'en rendre compte → un terminal oublié en arrière-plan → vérifier avant de relancer, un seul backend doit tourner.

---

## **🗣️ Explication ligne par ligne**

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

---

## **📋 Bilan, préparation session mentor**

> `[à valider]` Proposé, à confirmer.

### **🔴 Difficultés rencontrées**

- `[à valider]` Syntaxe des fonctions fléchées multi-lignes (besoin des accolades)
- `[à valider]` `setAttribute` : deux arguments, pas de `const` devant
- `[à valider]` Sens de `appendChild` (le parent reçoit) et placement du code dans le `forEach`
- `[à valider]` Mise en ligne GitHub Pages : structure `FrontEnd/` sous-dossier contre racine servie par Pages
- `[à valider]` `map` non assimilé après plusieurs angles. Notion mise de côté volontairement plutôt que forcée en fin de session.
- `[à valider]` Réflexe "je sais pas" avant d'avoir cherché, signalé plusieurs fois en session.

### **🟢 Points forts**

- `[à valider]` Setup Git propre et autonome (root-commit, message conventionnel, remote, push)
- `[à valider]` fetch, forEach et injection DOM compris et réexpliqués avec mes mots
- `[à valider]` Accessibilité posée dès la génération (`alt` sur image dynamique)
- `[à valider]` Commit conventionnel propre pour l'étape 2
- `[à valider]` Étapes 0 à 2 réexpliquées sans le code sous les yeux
- `[à valider]` Diagnostic du port occupé mené jusqu'au bout, cause comprise et prévention identifiée

### **➡️ À revoir / approfondir**

- `[à valider]` `async / await` (croisé, pas encore pratiqué)
- `[à valider]` Restructuration du repo pour la mise en ligne
- `[à valider]` `map`, à froid, sur exo dédié
- `[à valider]` `.catch` dans une chaîne de promesses
- `[à valider]` Templates littéraux et `insertAdjacentHTML`
- `[à valider]` Réduire la dépendance à l'IA : plus de `console.log`, plus de recherche MDN autonome, indices plus courts (consigne mentor, intégrée au prompt v7)

---

## **❓ Questions pour le mentor**

> `[à valider]` Propositions.

1. `[à valider]` localStorage ou sessionStorage pour le token, quelle pratique attendue ?
2. `[à valider]` Le backend fourni doit-il rester dans mon repo, ou seul le front-end est attendu comme livrable ?
3. `[à valider]` L'`alt` de la galerie vaut `work.title`, qui vient de l'API en anglais. Acceptable pour l'accessibilité, ou faut-il autre chose ?
4. `[à valider]` GitHub Pages : `index.html` est dans `FrontEnd/`. Quelle structure recommandée pour la mise en ligne (remonter à la racine, dossier `docs/`) ?
5. `[à valider]` Le refactor de la galerie en template littéral + `insertAdjacentHTML` est-il attendu pour la soutenance, ou `createElement` reste-t-il acceptable s'il est maîtrisé ?

---

## **Commit**

```powershell
git log --oneline
```

- `2fd429c` feat: display works from API (FR : afficher les travaux depuis l'API)
- `85f4ea2` chore: untrack .env
- `0d5d46d` chore: initial project setup

---

## **🎤 Préparation soutenance**

> Projet évalué en soutenance. Bloc actif.

Format : 15 min présentation, 10 min discussion, 5 min débriefing. Timer conseillé (rappel mentor P3).

**Sujets à maîtriser**

- [~] Expliquer les appels API et la récupération des données → base acquise (fetch, chaîne `.then`, `Response`, `.json()`, structure works)
- [ ]  Expliquer la gestion de la connexion, différence connecté / non connecté
- [ ]  Expliquer le fonctionnement du filtre
- [ ]  Expliquer l'envoi de nouvelles images à l'API
- [~] Justifier l'usage de Git et des commits → historique propre, format conventionnel, commit atomique par étape
- [~] Justifier le choix `forEach` plutôt que `map` pour la génération DOM

---

## **🧠 Nouvelles connaissances**

> Sous-blocs adaptés au projet : SVG et Animations CSS retirés, JavaScript / DOM, API & fetch, Authentification ajoutés.

### **JavaScript, bases**

- Fonction fléchée courte `x => ...` : une seule expression. Plusieurs instructions : accolades `{ }` après la flèche.
- Différence **renvoyer** (rendre une valeur qu'on récupère, ex fetch) et **faire une action** (forEach, setAttribute ne renvoient rien, `undefined`).
- `undefined` est ce que renvoie une fonction qui ne retourne rien. Un `console.log` qui affiche `undefined` est une preuve, pas un bug.

### **JavaScript / DOM, notions avancées**

- `document.createElement("balise")` : crée l'élément en mémoire, invisible tant qu'il n'est pas accroché.
- `element.textContent = "..."` : met du texte dans une balise.
- `element.setAttribute("nom", valeur)` : pose un attribut. Deux arguments. Ne renvoie rien.
- `parent.appendChild(enfant)` : accroche l'élément dans la page. Le parent reçoit, l'enfant est accroché.
- Les enfants suivent leur parent : accrocher un élément déplace tout ce qu'il contient. L'ordre des `appendChild` (parent d'abord ou enfants d'abord) ne change pas le rendu.
- `querySelector` qui ne trouve rien renvoie `null`. Toute méthode appelée ensuite dessus lève `Cannot read properties of null`.
- `forEach` : un tour par élément du tableau. À chaque tour, la variable contient l'élément entier (l'objet), pas son index. On lit une valeur avec le point : `work.imageUrl`, `work.title`.
- Piège : un élément créé mais non accroché existe mais ne s'affiche pas.

### **API & fetch**

- Route `GET /api/works` : renvoie un tableau d'objets. Chaque travail a `id`, `title`, `imageUrl` (URL complète, prête pour un `src`), `categoryId`, et `category { id, name }`.
- `categoryId` (numéro) sert à comparer, `category.name` (texte) sert à afficher.
- Route `POST /api/users/login` : attend `email` et `password`, renvoie `{ userId, token }` si OK, `404` sinon.
- Swagger (`Try it out` / `Execute`) permet de tester une route en vrai et de voir la forme des données.
- `fetch("url")` renvoie une promesse, pas les données. La promesse est d'abord `pending`.
- Trois états d'une promesse : `pending`, `fulfilled` (tenue), `rejected` (rompue, ex serveur éteint).
- La réponse de fetch est un objet `Response`, une enveloppe. `reponse.json()` l'ouvre et extrait les données.
- Le `Response` arrive dès les en-têtes reçus (`status`, `ok`), avant que le corps soit téléchargé. C'est pour ça que `.json()` renvoie une deuxième promesse : la lecture du corps prend du temps.
- `Response.body` est un `ReadableStream`, un flux de données brutes. Les données ne sont lisibles nulle part dans le `Response` tel quel.
- C'est `.json()` qui ouvre et convertit. Le `.then` suivant ne fait que récupérer le résultat une fois prêt.
- Gestion d'erreur dans une chaîne `.then` : maillon `.catch`, pas `try / catch` (qui va avec `async / await`).
- Chaîne type : `fetch(url).then(r => r.json()).then(donnees => ...)`. Appliquée en vrai à `GET http://localhost:5678/api/works`.

### **Authentification**

- Le token d'authentification vient de la réponse du login, à stocker pour les actions protégées (ajout, suppression).

### **Débogage**

- Réflexe : vérifier chaque étape avec un `console.log` avant de continuer (galerie attrapée, données reçues, boucle qui passe sur chaque élément).
- `git diff` ne montre rien pour un fichier untracked (pas de version précédente) ni pour un fichier déjà stagé (utiliser `git diff --cached`).

### **HTML & Sémantique**

- Un projet de galerie = une `figure` contenant une `img` et une `figcaption`. Même structure quand elle est générée en JS.

### **CSS**

- (rien de neuf, styles fournis par OC pour la partie existante)

### **Accessibilité**

- `alt` posé sur l'`img` générée dynamiquement, avec `work.title`. Même exigence d'accessibilité que du HTML écrit à la main (socle intégrateur).

### **Outils & process**

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

---

## **📚 Théorie non pratiquée**

**Notions non abordées sur ce projet** :

- `async / await` : croisé pendant la discussion sur fetch, pas pratiqué (on est resté sur `.then`).
- `map` : vu en console (`[1,2,3].map(n => n * 10)` renvoie `[10,20,30]`), non assimilé. À reprendre à froid sur un exo dédié.
- `Promise.prototype.catch` : mot-clé donné, pas encore lu ni pratiqué.
- Templates littéraux et `insertAdjacentHTML` : signalés par le mentor, pas encore abordés.

**Accessibilité / archi** :

**Lexique** :

- Swagger : interface de documentation d'une API, permet de tester ses routes
- FormData : objet JS pour construire des données de formulaire à envoyer, notamment avec fichier
- Token : jeton d'authentification renvoyé par l'API après login, à renvoyer pour les actions protégées
- Promise : promesse, objet renvoyé par fetch qui représente une donnée à venir (états : pending, fulfilled, rejected)
- defer : attribut de `<script>` qui exécute le script une fois tout le HTML chargé
- ReadableStream : flux de données brutes, contenu de `Response.body` avant conversion
- PID : identifiant numérique d'un processus en cours d'exécution

---

## **🧭 Bilan technique (synthèse)**

### **Erreurs fréquentes**

- Passer une chaîne `"imageUrl"` au lieu de la valeur `work.imageUrl`
- Oublier les accolades quand la fonction fléchée a plusieurs lignes
- Inverser le sens de `appendChild`
- Placer les créations hors du `forEach`
- Répondre "je sais pas" avant d'avoir cherché ou observé

### **Ce que je maîtrise**

- fetch (GET) et la chaîne `.then` / `.json()`, y compris le rôle du `Response` et du flux
- forEach pour parcourir un tableau d'objets, et pourquoi il ne renvoie rien
- Injection DOM : createElement, setAttribute, textContent, appendChild, querySelector
- L'ordre des `appendChild` et pourquoi il est indifférent
- `defer` et ce qui casserait sans lui
- `git rm --cached` et la logique suivi / ignoré
- Commit conventionnel propre, historique lisible

### **À revoir**

- `async / await`
- `map`
- `.catch` dans une chaîne de promesses
- Templates littéraux et `insertAdjacentHTML`
- Restructuration du repo pour la mise en ligne GitHub Pages

### **Ce que j'ai découvert**

- La chaîne fetch complète et le fonctionnement d'une promesse
- Le `ReadableStream` du corps de réponse
- L'injection DOM from scratch
- L'attribut `defer`
- Le connecteur Figma et la duplication de maquette en lecture seule
- Le diagnostic d'un port occupé sous PowerShell

---

## **📝 Point de reprise**

### **Fait**

- Cadrage bouclé : Swagger compris, arrêt backend connu, connecteur Figma opérationnel via copie de la maquette.
- Fiche de design tokens produite pour Claude Design (`sophie-bluel-design-tokens.md`).
- Notions découvertes en console, hors projet : fetch, forEach, injection DOM.
- Étape 2 codée de bout en bout par moi, commitée et poussée (`2fd429c`).
- RDV mentor : orientation vers les templates littéraux et `insertAdjacentHTML`, et consigne de réduire la délégation à l'IA (plus de `console.log`, d'exos, de mots-clés, indices très courts).
- Contrôle de compréhension des étapes 0 à 2 : validé.
- Incident port 5678 occupé, diagnostiqué et résolu.
- Prompt v7 produit (barème d'indice à 5 niveaux, règle "notion qui ne passe pas", prompt réduit d'environ 40 %).

### **État Git**

- Branche `main`, à jour avec `origin/main`. Working tree propre. Aucun commit sur la session de contrôle (pas de code produit).

### **Vérifications faites**

- Galerie affiche les works de l'API, une seule fois, sans doublon.
- Plus aucun travail en dur dans le HTML.
- `alt` présent sur chaque image générée.
- Étapes 0 à 2 réexpliquées avec mes mots, sans le code sous les yeux.

### **À relancer avant de coder**

- Le backend : `cd Backend`, puis `npm start`. Sinon fetch échoue. Arrêt propre avec `Ctrl + C`, jamais à la croix.

### **Prochaine action**

1. Exo console sur les templates littéraux, puis sur `insertAdjacentHTML` (hors projet, noms bidons).
2. Décider si la galerie de l'étape 2 est refactorée ou laissée en l'état.
3. Étape 3 : afficher les boutons de filtre (Tous, Objets, Appartements, Hôtels & restaurants) au-dessus de la galerie. Pseudocode français avant toute ligne de code.

### **À m'expliquer et vérifier : mise en ligne GitHub Pages**

- Problème identifié : mon `index.html` est dans `FrontEnd/`, mais Pages est réglé sur la branche `main` + dossier `/ (root)`. Pages cherche à la racine, ne trouve pas `index.html`, n'affiche rien.
- Pistes à m'expliquer proprement avant d'agir :
    1. Faire remonter le contenu de `FrontEnd/` à la racine du repo (le plus propre ; manip Git à comprendre, `git mv`, sans toucher à `Backend/`).
    2. Ou renommer `FrontEnd/` en `docs/` (Pages sait servir `/docs`), moins propre.
- À retenir : même une fois en ligne, la galerie restera vide, car le JS appelle `http://localhost:5678` (le backend local, que GitHub ne peut pas faire tourner). La mise en ligne sert surtout à passer Lighthouse en fin de projet, rien d'urgent.

### **Notions restant à découvrir**

- Templates littéraux, `insertAdjacentHTML`, `map`, `.catch`, étape 3 (boutons de filtre, catégories de l'API, gestion du clic).
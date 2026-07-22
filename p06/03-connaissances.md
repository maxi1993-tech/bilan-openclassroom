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

`repère de fin de fichier` · `end-of-file marker`

Un `console.log` placé tout en bas du fichier coupe la sortie console en deux : ce qui s'exécute pendant la lecture du fichier, et ce qui s'exécute au retour du réseau.

> Preuve obtenue sur le projet, ordre réel · `bonjour`, `bonjour un`, **fin du fichier**, `bonjour deux`, `bonjour trois`.

---

`report d'exécution` · `setTimeout`

`setTimeout` met une instruction de côté et la fait exécuter plus tard, pendant que le reste du fichier continue. Même mécanisme de report que le `fetch`, sans le réseau.

> Preuve en console · `console.log("A"); setTimeout(() => console.log("B"), 1000); console.log("C")` affiche A, C, puis B.

---

`portée temporelle d'un try / catch` · `synchronous error handling`

Un `try / catch` ne peut attraper qu'une erreur survenant pendant qu'il est actif. Toute erreur reportée dans le temps (`setTimeout`, `fetch`) arrive après sa fermeture. Prouvé sur les deux, hors projet puis sur le projet.

---

`attraper l'erreur d'une promesse` · `.catch()`

`.catch()` est un maillon de la chaîne, au même titre que `.then()`. Il s'accroche sous les `.then`, commence par un point, et reçoit l'erreur comme paramètre.

---

`erreur non attrapée` · `Uncaught (in promise)`

Cette mention dans la console signale une erreur non attrapée. Sa disparition prouve que le `.catch` a fait son travail. Deux erreurs comparées côte à côte, une avec la mention, une sans.

---

### JavaScript, paramètres

`paramètre` · `parameter`

Un paramètre est le nom que la fonction donne, chez elle, à la valeur qu'elle reçoit. Analogie du colis : l'expéditeur écrit une étiquette, le destinataire en écrit une autre, c'est le même colis. Sur le projet, `donnees` est l'étiquette de l'expéditeur dans `fetchCategories`, `categories` celle du destinataire dans `createButtons`.

> Preuve en console · après `direBonjour(prenom)`, taper `prenom` renvoie `'Max'`, taper `nom` renvoie `ReferenceError: nom is not defined`.
>
> Deuxième preuve · `function test(x) { x = 99; console.log(x) }` puis `test(5)` affiche `99`, et `x` seul renvoie `ReferenceError`.

---

### JavaScript, dépendance aux données

`dépendance au nombre` · `data-driven count`

Le nombre d'éléments à générer dépend des données au même titre que leur contenu. Créer des éléments vides à l'avance ne dispense pas d'attendre : à t = 0 on ne sait pas combien en créer.

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

`pile d'appels` · `console.trace()`

Affiche la liste des fonctions qui ont mené jusqu'à cette ligne. Répond à "qui a appelé cette fonction, et depuis où". Même information que les lignes `viewGallery @ script.js:6` visibles sous une erreur.

> **Non pratiqué en session.** À tester en console.

---

`repère textuel de diagnostic` · `log marker`

Un repère placé en fin de fichier (`fin du fichier`) est un outil de diagnostic à part entière : il transforme une question de chronologie en observation.

---

`emplacement d'un log de debug` · `debug log placement`

Un `console.log` de debug se place en première instruction du corps de la fonction, pas autour de son appel.

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

`stager par morceaux` · `git add --patch`

Propose les modifications bloc par bloc et permet de n'en stager qu'une partie. Touche `?` pour la liste des commandes, `s` pour découper un bloc en blocs plus petits, `e` pour l'éditer à la main, `q` pour quitter.

---

`vider la zone de préparation` · `git reset`

`q` quitte `--patch` sans annuler les blocs déjà stagés. `git reset` vide la zone de préparation sans jamais toucher aux fichiers du disque.

---

`sujets qui se croisent` · `entangled changes`

Deux sujets qui se croisent sur les mêmes lignes ne se séparent pas proprement en deux commits. Dans ce cas, un `wip:` assumé et justifié vaut mieux qu'un historique forcé.

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

`syntaxe asynchrone moderne` · `async / await`

Permet d'écrire l'attente dans l'ordre de lecture, sans supprimer l'attente elle-même. Demandé plusieurs fois en session, volontairement reporté.

> **Priorité 1 pour un exo dédié hors projet.**

---

`paramètre contre variable` · `parameter vs variable`

La différence de vocabulaire n'est pas passée malgré deux preuves console. Exo dédié à froid, hors projet.

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

`pile d'appels` · `console.trace()`

À tester en console sur une chaîne d'appels bidon.

---

`édition manuelle d'un bloc` · `git add --patch`, touche `e`

À pratiquer sur un dépôt bac à sable, jamais sur un livrable.

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

`ordre d'exécution asynchrone` · `event loop` : résolu en session le 22-07, prouvé par observation avec un repère de fin de fichier. Reste à consolider à froid.

---

`rattrapage d'erreur` · `.catch` : lu, posé sur les deux fetch de l'étape 4, vérifié back-end coupé.

---

> Le lexique et les tips sont dans `09-memo.md`.

---

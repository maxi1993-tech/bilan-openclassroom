# Delta 03, étape 4

*Archive brute du delta déposé en inbox, non modifié.*
*Date de session inconnue, à compléter par Max.*

---

# Delta de fiche, étape 4 (début + suite, fusionné)

> Fusion des deux deltas de l'étape 4. Rien supprimé, rien écrasé. À fusionner dans la fiche existante.

---

## ✅ Todo, mises à jour

**Étape 3**

- [x]  Validation W3C de `index.html` après ajout du `ul.filters` → faite, 0 erreur, 1 avertissement (code fourni OC)

**Étape 4, filtre fonctionnel**

- [x]  Pseudocode écrit avant de coder
- [x]  Classe `filter-button-selected` posée sur le bouton `Tous` à la génération (état par défaut)
- [x]  Écouteur de clic branché sur chaque bouton de filtre, vérifié en console
- [x]  Écouteurs extraits de `createButtons` dans une fonction dédiée `listenFilterButtons`
- [x]  Appel de `listenFilterButtons()` placé à la fin de `createButtons`, après la pose des boutons
- [x]  Fichier réordonné : constantes, puis les trois fonctions, puis l'appel de lancement en bas
- [x]  Paramètre de `createButtons` renommé `donnees` en `categories`
- [ ]  Vider la galerie au clic (mot-clé déjà donné : `innerHTML`)
- [ ]  Reconstruire la galerie avec les travaux filtrés
- [ ]  Déplacer la classe `filter-button-selected` sur le bouton cliqué

**Refactor / Nettoyage**

- [x]  Renommer `filters-button` en `filter-button` dans le JS (`script.js`)
- [x]  Renommer `filters-button` en `filter-button` dans `style.css` → fait en session suivante, le style s'applique de nouveau
- [x]  `createButtons` faisait deux choses (fabriquer les boutons + brancher les écouteurs), écart au principe de responsabilité unique → résolu par l'extraction de `listenFilterButtons`
- [ ]  `filterButtonSelected` déclarée dans `listenFilterButtons` mais jamais utilisée. Servira à la ligne 6 du pseudocode.
- [ ]  Deux méthodes de génération DOM conservées volontairement (galerie en `createElement`, filtres en template littéral) → **décision de session : on garde les deux pour comparer et tester plusieurs façons de faire.** Remplace l'entrée précédente qui parlait d'aligner.

---

## 🔍 Choix techniques, ajouts

**Timing et emplacement du code**

- `querySelectorAll` des boutons placé **dans** `createButtons`, après la boucle, et non en haut du fichier → les boutons sont générés en JS après le retour du fetch. En haut du fichier, ils n'existent pas encore. Règle dégagée : ce qui existe dans le HTML se récupère en haut du fichier, ce qui est créé par JS se récupère après sa création.
- Appel de `listenFilterButtons()` à la fin de `createButtons` et non en bas du fichier → contrainte du fetch, pas un choix de style. En bas, la ligne s'exécute avant le retour de la réponse, `querySelectorAll` renvoie une liste vide, aucun écouteur posé. Vérifié en direct : console muette au clic.
- Ordre du fichier : constantes, trois déclarations de fonctions, appel de lancement seul en bas → on ne lit jamais un appel avant d'avoir vu la fonction.

**Structure et nommage**

- Écouteurs extraits dans `listenFilterButtons` plutôt que laissés dans `createButtons` → responsabilité unique. Une fonction fabrique, l'autre écoute.
- Paramètre renommé `categories` plutôt que `donnees` → le nom décrit la donnée reçue. Renommage dans `createButtons` seulement, `fetchCategories` inchangée, le code fonctionne toujours.
- Classe `filter-button-selected` posée directement dans le template du bouton `Tous` → l'état par défaut est connu à la génération, pas besoin de le poser après coup.
- Nom de classe `filter-button-selected` → application de la règle déjà notée en fiche (un nom qui en qualifie un autre reste au singulier) et un seul séparateur, le tiret.

**Logique de filtrage**

- Vider puis reconstruire la galerie plutôt que trier les figures déjà affichées → une `figure` générée ne porte aucune trace de sa catégorie. Inscrire cette information sur chaque figure serait du travail en plus, alors que la génération depuis un tableau est déjà écrite.

**Chargement**

- `defer` seul conservé, sans `window.addEventListener("load", start)` → les deux répondent au même besoin (attendre le HTML). Version du mentor testée puis écartée. Question posée au mentor.

---

## 🧩 Pseudocode

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

## 🔍 Vérification, ajouts

- [x]  `index.html` validé au W3C après ajout du `ul.filters`
- [x]  Chaque bouton de filtre renvoie bien le sien au clic (vérifié par `console.log(button)`, jamais le voisin)
- [x]  Le clic sur un bouton log toujours le bouton cliqué après l'extraction dans `listenFilterButtons`
- [x]  Les boutons s'affichent toujours après le renommage du paramètre en `categories`
- [x]  Les trois appels groupés en bas du fichier ne fonctionnent pas (testé, console muette)
- [ ]  Le clic sur un filtre affiche les bons travaux
- [ ]  Un seul bouton porte `filter-button-selected` à tout moment

---

## 🐛 Journal de bugs

**Étape 4, début**

- `Cannot read properties of null (reading 'forEach')` → `querySelector` des boutons placé en haut du fichier, exécuté avant le retour du fetch, donc avant que les boutons existent → déplacer la récupération dans `createButtons`, après les `insertAdjacentHTML`. Preuve obtenue en console : `console.log` au chargement affiche `null`, le même dans un `setTimeout` de 2 secondes affiche le bouton.
- `filterButton is not defined` → la variable est déclarée dans `createButtons`, la ligne qui l'utilise était restée en bas du fichier → déplacer l'instruction dans le même bloc que la déclaration. Même règle de portée que celle déjà notée depuis P5.
- `filterButton.forEach is not a function` → `querySelector` ne renvoie qu'un seul élément, pas une liste → `querySelectorAll`, qui renvoie une `NodeList` parcourable. Vérifié en console : un `button` d'un côté, `NodeList(4)` de l'autre.
- `addEventListener: 2 arguments required, but only 1 present` → appel écrit sans son deuxième argument (la fonction à exécuter).
- `undefined is not a function` sur `filterButton.forEach(filters.addEventListener("click", ...))` → `addEventListener(...)` avec ses parenthèses est un appel, exécuté immédiatement, dont le résultat (`undefined`) était passé à `forEach`. Or `forEach` attend une fonction → passer une fonction à `forEach` (`button => { ... }`) et mettre l'appel `addEventListener` dans son corps. Symétrique du bug de l'étape 3 (`createButtons` sans parenthèses ne l'appelait pas).
- Écouteur posé sur `filters` au lieu de `button` → `filters` est le conteneur, un seul écouteur pour tout, alors que le `forEach` tend un bouton à chaque tour → poser l'écouteur sur `button`.
- Classe renommée en `filter-button` dans le JS sans reporter dans le CSS → le style ne s'applique plus. Répétition exacte du bug de l'étape 3 (sélecteur corrigé, classe absente du bouton `Tous`) → corrigé en session suivante.

**Étape 4, suite**

- `createButtons()` écrit à la fin de `createButtons` → la fonction s'appelait elle-même, bouton `Tous` reposé puis plantage faute de données → écrire le nom de la fonction voulue, pas celui de la fonction courante.
- `console.log(listenFilterButtons())` affiche `undefined` → ce n'est pas une erreur, c'est ce que renvoie une fonction qui ne retourne rien (règle déjà notée à l'étape 2) → retirer le `console.log` autour, garder l'appel seul.
- `listenFilterButtons()` appelée en bas du fichier → console muette au clic, **aucun message d'erreur**. La ligne s'exécute avant le retour du fetch, `querySelectorAll` ne trouve rien, le `forEach` tourne zéro fois → replacer l'appel dans `createButtons`. **Absence d'erreur ne veut pas dire absence de bug.**

---

## 🗣️ Explication ligne par ligne, à alimenter à froid

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

## 🧠 Nouvelles connaissances

### JavaScript, bases

- `querySelector` renvoie **un seul** élément, `querySelectorAll` renvoie une `NodeList` (ici de 4 boutons). Seule la seconde se parcourt avec `forEach`.
- Le mot placé avant la flèche dans un `forEach` (`categorie =>`, `button =>`) est le nom donné à l'élément que la boucle tend à chaque tour. Sans lui, aucun moyen de l'attraper. **Vu, pas acquis : donné par Claude, à réapprendre sur exo dédié hors projet.**
- Passer `maFonction(...)` à un `forEach` exécute l'appel tout de suite et transmet son résultat, pas la fonction. Il faut passer une fonction non appelée. **Vu, pas acquis.**
- Une fonction sans paramètre (`fetchCategories()`, `listenFilterButtons()`) peut être appelée depuis n'importe où : elle ne demande rien. Une fonction avec paramètre (`createButtons(categories)`) ne peut être appelée que là où la valeur qu'elle attend existe. Ce n'est pas l'asynchrone qui contraint son emplacement, c'est la donnée : le tableau des catégories n'existe qu'à l'intérieur du `.then`, nulle part ailleurs dans le fichier.
- Un paramètre de fonction est un nom local. `createButtons(categories)` ne connaît pas la variable du `.then`, elle en reçoit la valeur sous son propre nom. Preuve faite en console :

```javascript
function direBonjour(nom) { console.log("bonjour " + nom) }
const prenom = "Max"
direBonjour(prenom)
```

`prenom` n'existe qu'à l'extérieur, `nom` qu'à l'intérieur, et l'affichage fonctionne. **Vu et testé, à consolider.**

- Deuxième preuve, sur le projet : paramètre de `createButtons` renommé en `categories` sans toucher à `fetchCategories`, le code fonctionne toujours. Ce sont bien deux variables distinctes.
- Une fonction qui contient son propre appel se relance en boucle.

### JavaScript, asynchrone

- Un `fetch` n'attend pas. Le fichier continue de se lire immédiatement, pendant que la demande voyage. Preuve obtenue en console, hors projet :

```javascript
console.log("1 avant le fetch")
fetch("https://jsonplaceholder.typicode.com/todos/1")
    .then(reponse => reponse.json())
    .then(donnees => console.log("4 les donnees sont la", donnees))
console.log("2 juste apres le fetch")
console.log("3 fin du fichier")
```

Affichage réel : 1, 2, 3, puis 4 en dernier, alors que le 4 est écrit avant les autres dans le fichier.

- La chaîne `.then` est le seul endroit qui sait que la réponse est arrivée. Tout code qui dépend des données doit y être branché, directement ou via une fonction appelée depuis elle. **Notion non acquise, rangée pour un exo dédié à froid.**

### JavaScript / DOM

- Un élément généré en JS après un `fetch` n'existe pas au moment où le fichier se charge. Tout code qui en dépend doit s'exécuter après sa pose, donc dans la fonction qui le pose.
- Il n'existe pas d'événement natif signalant "mon fetch est revenu et mon DOM est construit". `load` ne dit rien du fetch. Ce point de synchronisation, c'est la chaîne `.then` qui le fournit.
- `addEventListener` se pose sur un élément qui existe déjà dans la page à l'instant où la ligne s'exécute. Sur une liste vide, le `forEach` tourne zéro fois : aucun écouteur, aucune erreur, aucun message.
- Un attribut `data-*` range une information sur un élément HTML sans qu'elle s'affiche, et indépendamment du texte affiché. Relu en JS avec `element.dataset.nom`. **Vu en console, non acquis. À reprendre à froid sur exo dédié.**

### HTML & Sémantique

- `article` est un élément de sectionnement : il crée sa propre section. Un `h2` placé dans un `article` titre cet `article`, pas la `section` qui l'englobe. D'où l'avertissement W3C sur `#introduction` du HTML fourni.

### Accessibilité

- Une `section` sans nom accessible n'est pas exposée comme région par les lecteurs d'écran, elle devient une simple boîte. La navigation par titres reste fonctionnelle, d'où un avertissement et non une erreur.

### Débogage

- Comparer un `console.log` immédiat et le même dans un `setTimeout` permet de prouver un problème de timing plutôt que de le supposer.
- Un message d'erreur qui change à chaque rechargement est un signe de progression : chaque nouveau message correspond à un nouveau problème, le précédent est réglé.
- Une erreur non rattrapée interrompt l'exécution du fichier : les `console.log` placés après ne s'affichent jamais. Les placer avant la ligne fautive, ou commenter cette ligne le temps du test.
- Une console muette, sans aucune erreur, peut signaler un bug tout aussi réel qu'un message rouge.

### Outils & process

- `defer` sur le `<script>` et `window.addEventListener("load", ...)` répondent au même besoin : attendre que le HTML soit là. Les cumuler ne casse rien mais fait doublon.

---

## 📚 Théorie non pratiquée, mise à jour

- **Ordre d'exécution asynchrone** : compris ligne par ligne, pas encore compris dans son ensemble. **Priorité.** Exo dédié à faire à froid avant de reprendre l'étape 4.
- **Écouteur unique sur le conteneur** (`ul.filters`) plutôt qu'un écouteur par bouton : supprimerait le problème de timing (le conteneur est en dur dans le HTML) et supprimerait `listenFilterButtons`. Mot-clé MDN : `event.target`. **Exo dédié à faire hors projet, décidé en session.**
- `data-*` et `dataset` : découverts en console (attribut invisible, indépendant du texte affiché, relu par `element.dataset.nom`). **Non acquis.** À reprendre à froid sur un exo dédié, hors situation de blocage.
- Le paramètre de callback dans un `forEach` : notion donnée, pas trouvée. À reconsolider sur exo hors projet.

---

## 📋 Bilan, préparation session mentor

### 🔴 Difficultés rencontrées, ajouts

- `[à valider]` Étape 4 très difficile sur deux sessions. Blocage prolongé, perte du fil, forte frustration, découragement exprimé plusieurs fois.
- `[à valider]` Sentiment de ne pas m'approprier le code produit sur la partie écouteurs de clic. Notion donnée par l'IA plutôt que trouvée, donc à réapprendre.
- `[à valider]` Claude a donné le nom et la structure de la fonction à créer, ce que le prompt interdit sur du code OC évalué. Le cadre n'a pas tenu.
- `[à valider]` `data-*` introduit au mauvais moment (pseudocode déjà complet, notion non nécessaire à cet instant), ce qui a cassé la progression.
- `[à valider]` Blocage sur l'asynchrone : chaque ligne du fichier est comprise isolément, l'assemblage ne l'est pas.
- `[à valider]` Plusieurs angles tentés sur le timing du fetch (chronologie, analogie, exos console) sans que la notion passe.
- `[à valider]` Difficulté persistante à distinguer une valeur (`name`, texte) d'un identifiant (`id`, `categoryId`) dans une comparaison.
- `[à valider]` Reprise du réflexe "je sais pas" avant d'avoir observé.
- `[à valider]` Doute sur mes capacités exprimé plusieurs fois.

### 🟢 Points forts, ajouts

- `[à valider]` W3C passé, avertissement compris et justifiable devant le jury (code fourni, non corrigé, expliqué)
- `[à valider]` Pseudocode de l'étape 4 écrit en entier avant toute ligne de code, six lignes cohérentes
- `[à valider]` Piège des doublons dans la galerie anticipé seul, avant de coder
- `[à valider]` Choix de vider plutôt que trier, justifié sur l'absence d'information de catégorie dans le DOM généré
- `[à valider]` Ordre retirer puis ajouter la classe active, corrigé après avoir vu le piège
- `[à valider]` Nom `filter-button-selected` tranché en appliquant une règle de nommage notée par moi-même
- `[à valider]` Diagnostic autonome que `createButtons` fait deux choses, donc écart à la responsabilité unique. Regard critique sur mon propre code, non soufflé.
- `[à valider]` Constantes replacées au bon endroit dans `createButtons`, après la boucle, une fois le problème de timing compris
- `[à valider]` Constat posé seul en ouverture de la seconde session : "mon code est emmêlé et n'est pas de moi". C'est ce constat qui a déclenché le refactor.
- `[à valider]` Frontière entre les deux responsabilités de `createButtons` localisée seule, ligne exacte désignée
- `[à valider]` Bloc des écouteurs réexpliqué avec mes mots, sans le code sous les yeux
- `[à valider]` Différence entre un fetch écrit au niveau du fichier et un fetch enfermé dans une fonction, trouvée seule après observation. Règle formulée avec mes mots : "la mettre dans une fonction implique qu'elle s'exécute à l'appel".
- `[à valider]` Auto-appel de `createButtons` repéré et conséquence anticipée
- `[à valider]` Test des trois appels groupés en bas mené jusqu'au bout, résultat observé, preuve obtenue
- `[à valider]` Version `window load` du mentor testée sur mon propre code, puis écartée avec une raison
- `[à valider]` Refus de commiter un code que je ne sais pas expliquer, alors que le commit était proposé

### ➡️ À revoir / approfondir, ajouts

- `[à valider]` Ordre d'exécution asynchrone, en priorité, sur exo dédié hors projet
- `[à valider]` `event.target` et l'écouteur unique sur conteneur, sur exo dédié
- `[à valider]` `data-*` et `dataset`, sur exo dédié à froid
- `[à valider]` Le paramètre de callback dans un `forEach`, sur exo hors projet
- `[à valider]` `querySelector` contre `querySelectorAll`, réflexe à ancrer
- `[à valider]` Passage d'une valeur en paramètre, à consolider
- `[à valider]` Dépendance à l'aide de l'IA : point à aborder directement avec Florian, pas seulement à corriger par le prompt

---

## ❓ Questions pour le mentor, ajouts

10. `[à valider]` Brancher les écouteurs de clic depuis `createButtons` est imposé par le timing du fetch. Est-ce la pratique attendue, ou existe-t-il une organisation plus propre attendue en agence ?
11. `[à valider]` Sur le fond : j'ai l'impression de ne pas m'approprier ce que je produis quand l'aide arrive trop vite. Comment le mesurer honnêtement, et que faire concrètement pour y remédier ?
12. `[à valider]` Peux-tu m'aider à revoir mon prompt Claude, voire m'en proposer ta version ? Le cadre actuel n'a pas tenu en session, l'aide arrive encore trop vite.
13. `[à valider]` Pourquoi mon code est-il si difficile à comprendre dans son ensemble ? Je comprends à peu près chaque ligne isolément, mais le tout assemblé me paraît impossible à suivre. Est-ce normal à ce stade, un problème de structure, ou un problème de notion ?
14. `[à valider]` `defer` et `window.addEventListener("load", ...)` : tu utilises le second dans ton exemple, j'ai le premier. Lequel attends-tu, et pourquoi ?
15. `[à valider]` Garder volontairement deux méthodes de génération DOM dans le même fichier pour comparer : acceptable comme démarche d'apprentissage, ou à éviter sur un livrable ?

---

## Commit, hashes relevés

- `87ea86d` feat: add style to filter buttons (FR : ajouter le style des boutons de filtre)
- `3e1f4e5` refactor: split filter script into two functions (FR : séparer le script des filtres en deux fonctions)
- `4c23113` feat: add filter buttons from API (FR : ajouter les boutons de filtre depuis l'API)
- `2fd429c` feat: display works from API (FR : afficher les travaux depuis l'API)
- `85f4ea2` chore: untrack .env
- `0d5d46d` chore: initial project setup

---

## 🎤 Préparation soutenance, ajouts

- [ ]  Expliquer pourquoi les écouteurs ne peuvent pas être branchés en haut du fichier (timing du fetch)
- [ ]  Expliquer pourquoi les trois appels ne peuvent pas être groupés en bas du fichier, chronologie à l'appui
- [ ]  Expliquer pourquoi les trois fonctions ont bien trois appels, et pourquoi un seul d'entre eux ne peut pas être déplacé
- [ ]  Justifier l'extraction de `listenFilterButtons` (responsabilité unique)
- [ ]  Expliquer pourquoi une absence d'erreur dans la console ne prouve pas l'absence de bug
- [ ]  Expliquer l'avertissement W3C sur `#introduction` (`article` est un élément de sectionnement)
- [ ]  Justifier le choix de vider et reconstruire la galerie plutôt que de trier les figures affichées

---

## 📝 Point de reprise

### Fait sur l'étape 4 (les deux sessions)

- W3C sur `index.html` : 0 erreur, 1 avertissement sur `#introduction`, code fourni OC, non corrigé
- CSS validé, 0 erreur
- Hashes des trois commits de l'étape 3 relevés
- Pseudocode de l'étape 4 écrit, six lignes
- Classe renommée `filter-button` dans le JS puis dans `style.css`, `filter-button-selected` posée sur `Tous`
- Écouteurs de clic branchés sur chaque bouton, vérifiés en console
- Lignes de debug retirées du fichier
- Écouteurs extraits de `createButtons` dans `listenFilterButtons`, appel placé à la fin de `createButtons`, testé et fonctionnel
- Fichier réordonné : constantes, trois fonctions, appel de lancement en bas
- Paramètre de `createButtons` renommé en `categories`
- Version `window load` du mentor testée puis écartée
- Deux exos console hors projet : ordre d'exécution du fetch, passage de valeur en paramètre

### État Git

- Rien de commité sur l'étape 4. Modifications non commitées dans `script.js` et `style.css`.
- **Commit volontairement reporté** : je ne commite pas un code que je ne sais pas encore expliquer en entier.

### Étape 4, état réel

**Fait :** lignes 1, 2, 3 du pseudocode (récupérer les boutons, écouter les clics, classe active par défaut sur `Tous`).

**Restant :** lignes 4, 5, 6. Vider la galerie, la reconstruire filtrée, déplacer la classe active.

**L'étape 4 n'est pas terminée** : le filtre ne filtre rien, le clic ne fait qu'un `console.log`.

### Vérifications NON faites

- Navigation clavier et focus visible sur les boutons générés
- Contraste de l'état actif
- axe DevTools

### Prochaine action

1. **Ne rien coder tant que l'ordre d'exécution asynchrone n'est pas compris.** Décision prise en session.
2. **Refaire le visuel de la chronologie** (ci-dessous), en le construisant moi-même plutôt qu'en le lisant.
3. Exo dédié hors projet sur l'asynchrone, à froid.
4. Puis exo `event.target` sur un conteneur.
5. Exos hors projet à froid : paramètre de callback dans `forEach`, `data-*` / `dataset`.
6. Seulement ensuite : lignes 4, 5, 6 du pseudocode. Mot-clé déjà donné pour la ligne 4, `innerHTML`.
7. Commit une fois le code compris et explicable.
8. Point à aborder avec Florian : le sentiment de ne pas m'approprier le code, et la dépendance à l'aide.

### Visuel à refaire à la prochaine session

Chronologie à reconstruire de mémoire, les deux versions côte à côte.

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

Point unique à retenir : entre le départ du fetch et son retour, il s'écoule un temps réel pendant lequel le fichier a déjà fini de se lire.

### Notions restant à découvrir

- Ordre d'exécution asynchrone (priorité)
- `event.target`
- `innerHTML` pour vider un conteneur
- Filtrage d'un tableau
- `map`, `.catch`, `async / await`
- `dataset` (vu, non acquis)

# Delta de fiche, P6 étape 4, session ordre d'exécution et gestion d'erreur

> Additif. Rien d'existant n'est écrasé ni réorganisé. À coller dans `p06/_inbox.md`.

---

## ✅ Todo, mises à jour

**Étape 4, filtre fonctionnel**

- [x] Fichier restructuré en trois blocs : constantes, déclarations, appels de lancement
- [x] `fetch` des works enveloppé dans une fonction `viewGallery`
- [x] `.catch` ajouté sur les deux fetch
- [ ] Retirer les cinq `console.log` de debug avant le commit de fin d'étape
- [ ] Vider la galerie au clic (mot-clé déjà donné : `innerHTML`)
- [ ] Reconstruire la galerie avec les travaux filtrés
- [ ] Déplacer la classe `filter-button-selected` sur le bouton cliqué

**Nommage**

- [ ] `viewGallery` ne suit pas le moule des trois autres fonctions (verbe + objet, cohérence avec `gallery` déclarée en ligne 1). À trancher avant le commit de fin d'étape.

---

## 🔍 Choix techniques, ajouts

**Structure du fichier**

- Fichier réordonné en trois blocs : constantes, puis les quatre déclarations de fonctions, puis les deux appels de lancement en bas → on lit le fichier dans l'ordre de la chronologie d'exécution, sans jamais remonter. Les déclarations du bloc du milieu n'exécutent rien.
- `createButtons` et `listenFilterButtons` n'apparaissent pas dans le bloc des appels → elles sont déjà appelées par le chaînage, au moment où leurs données existent. Seuls les points de départ figurent en bas.
- `fetch` des works enveloppé dans `viewGallery` → aligne le fichier sur la même forme que les trois autres traitements. Ce n'est pas un simple déplacement de lignes : enveloppé, le fetch ne part plus à la lecture du fichier mais à l'appel.

**Gestion d'erreur**

- `try / catch` autour des appels de lancement testé puis écarté → il finit son travail avant que l'erreur du fetch n'existe. Prouvé en console : `try`, `bonjour`, `bonjour un`, `fin du fichier`, puis seulement les erreurs réseau. Le `console.error` du `catch` ne s'affiche jamais.
- `.catch()` accroché à la chaîne des `.then` → c'est le seul endroit encore actif au retour du fetch. Preuve : la mention `Uncaught (in promise)` disparaît de l'erreur une fois le `.catch` posé.

**Dépendance au fetch, questionnée puis assumée**

- Créer les boutons avant le retour du fetch, puis les remplir → écarté. Le nombre de boutons dépend des données autant que leur nom : à t = 0 on ne sait pas combien de catégories l'API va renvoyer. Deux étapes au lieu d'une, sans rien gagner.
- Écrire les catégories en dur → écarté, non conforme au brief, qui demande « les catégories présentes dans l'API ».
- `async / await` pour supprimer la dépendance → écarté à ce stade. Ça change l'écriture de l'attente, pas son existence. Réécrire dans une syntaxe non maîtrisée ferait perdre la compréhension acquise sur `.then`.

**Git**

- `git add --patch` tenté pour séparer réorganisation et gestion d'erreur en deux commits, puis abandonné → les deux sujets se croisent physiquement sur les mêmes lignes. Séparer proprement aurait demandé l'édition manuelle d'un bloc (`e`), manipulation risquée en fin de session. Commit unique `wip:` assumé, avec sa justification.

---

## 🗣️ Explication ligne par ligne

**Pourquoi `listenFilterButtons()` est appelée depuis `createButtons` et pas en bas du fichier**

`viewGallery` s'affiche avant « fin du fichier », `listenFilterButtons` s'affiche après. Entre les deux, les données du fetch sont arrivées. Cela crée les boutons quand les données sont reçues, et ensuite écoute. `listenFilterButtons` fonctionne quand les boutons sont créés, ce qui n'arrive pas avant que les données soient arrivées et déclenchent `createButtons`.

**La chaîne des appels**

`fetchCategories()` en bas du fichier appelle la fonction `fetchCategories`, qui appelle `createButtons`, qui appelle `listenFilterButtons`.

**Pourquoi le `try / catch` n'attrape rien**

L'erreur n'a pas le temps d'arriver que le script a terminé.

---

## 🐛 Journal de bugs

**Étape 4, session ordre d'exécution**

**`console.log` écrit autour de l'appel au lieu d'être dans la fonction** · `console.log(viewGallery())`

- **Cause** · confusion entre observer une fonction et afficher ce qu'elle retourne.
- **Correction** · placer le `console.log` en première instruction du corps, entre les accolades.

> Preuve obtenue en console · une fonction sans `return` affiche `undefined`, règle déjà notée à l'étape 2.

---

**Appel d'une fonction écrit à l'intérieur d'elle-même** · `function viewGallery() { console.log(viewGallery()) ... }`

- **Cause** · répétition du bug déjà rencontré sur `createButtons`.
- **Correction** · mettre une chaîne de texte dans le `console.log`, pas un appel.

---

**`try / catch` autour des appels de lancement, `console.error` jamais affiché** · aucun message d'erreur, aucun `attrapé`

- **Cause** · le bloc `try / catch` s'exécute et se referme à t = 0. Les erreurs du fetch arrivent à t = 200 ms, quand plus rien n'écoute.
- **Correction** · `.catch()` accroché à la chaîne des `.then`.

> Preuve obtenue en console, hors projet · `try { console.log("dans le try"); alerteInexistante() } catch (e) { console.log("attrapé") }` affiche `attrapé`. La même chose avec l'erreur enfermée dans un `setTimeout` de 1 seconde ne l'affiche pas.

---

**Appels de lancement déplacés dans `createButtons`** · plus rien ne démarre

- **Cause** · déplacement de bloc au jugé, sans repartir de la chronologie.
- **Correction** · retour au fichier précédent. Réflexe à prendre : ne pas déplacer de code tant que la question posée n'est pas résolue.

---

**`try / catch` refermé autour d'une déclaration de fonction** · sortie console identique aux essais précédents

- **Cause** · un bloc de déclarations n'exécute rien, donc rien à attraper.
- **Correction** · sujet clos, `.catch` retenu.

---

**`git add --patch` puis `q`, blocs déjà stagés conservés**

- **Cause** · `q` quitte l'outil mais ne dé-stage pas ce qui a été validé avec `y`. Information donnée à tort en session comme étant l'inverse.
- **Correction** · `git reset` vide la zone de préparation sans toucher aux fichiers.

---

## 🧠 Nouvelles connaissances

### JavaScript, asynchrone

- Un repère `console.log` placé tout en bas du fichier coupe la sortie console en deux : ce qui s'exécute pendant la lecture du fichier, et ce qui s'exécute au retour du réseau. Preuve obtenue sur le projet, ordre réel : `bonjour`, `bonjour un`, **fin du fichier**, `bonjour deux`, `bonjour trois`.
- `setTimeout` met une instruction de côté et la fait exécuter plus tard, pendant que le reste du fichier continue. Même mécanisme de report que le `fetch`, sans le réseau. Preuve en console : `console.log("A"); setTimeout(() => console.log("B"), 1000); console.log("C")` affiche A, C, puis B.
- Un `try / catch` ne peut attraper qu'une erreur survenant pendant qu'il est actif. Toute erreur reportée dans le temps (`setTimeout`, `fetch`) arrive après sa fermeture. Prouvé sur les deux, hors projet puis sur le projet.
- `.catch()` est un maillon de la chaîne, au même titre que `.then()`. Il s'accroche sous les `.then`, commence par un point, et reçoit l'erreur comme paramètre.
- La mention `Uncaught (in promise)` dans la console signale une erreur **non attrapée**. Sa disparition prouve que le `.catch` a fait son travail. Deux erreurs comparées côte à côte, une avec la mention, une sans.

### JavaScript, paramètres

- Un paramètre est le nom que la fonction donne, chez elle, à la valeur qu'elle reçoit. Analogie du colis : l'expéditeur écrit une étiquette, le destinataire en écrit une autre, c'est le même colis. Sur le projet : `donnees` est l'étiquette de l'expéditeur dans `fetchCategories`, `categories` celle du destinataire dans `createButtons`.
- Preuve en console : après `direBonjour(prenom)`, taper `prenom` renvoie `'Max'`, taper `nom` renvoie `ReferenceError: nom is not defined`.
- Deuxième preuve : `function test(x) { x = 99; console.log(x) }` puis `test(5)` affiche `99`, et `x` seul renvoie `ReferenceError`.

### JavaScript, dépendance aux données

- Le nombre d'éléments à générer dépend des données au même titre que leur contenu. Créer des éléments vides à l'avance ne dispense pas d'attendre : à t = 0 on ne sait pas combien en créer.

### Débogage

- `console.trace()` affiche la pile d'appels au point où il est écrit, c'est-à-dire la liste des fonctions qui ont mené jusqu'à cette ligne. Utile pour répondre à « qui a appelé cette fonction, et depuis où ». C'est la même information que les lignes `viewGallery @ script.js:6` visibles sous une erreur. **Non pratiqué en session, à tester en console.**
- Un repère textuel placé en fin de fichier (`fin du fichier`) est un outil de diagnostic à part entière : il transforme une question de chronologie en observation.
- Un `console.log` de debug se place en première instruction du corps de la fonction, pas autour de son appel.

### Git

- `git add --patch` propose les modifications bloc par bloc et permet de n'en stager qu'une partie. Touche `?` pour la liste des commandes, `s` pour découper un bloc en blocs plus petits, `e` pour l'éditer à la main, `q` pour quitter.
- `q` quitte `--patch` sans annuler les blocs déjà stagés. `git reset` vide la zone de préparation sans jamais toucher aux fichiers du disque.
- Deux sujets qui se croisent sur les mêmes lignes ne se séparent pas proprement en deux commits. Dans ce cas `wip:` assumé et justifié vaut mieux qu'un historique forcé.

---

## 📚 Théorie non pratiquée, mise à jour

- **Ordre d'exécution asynchrone** → **résolu en session**, prouvé par observation. Passe en connaissances acquises. Reste à consolider à froid.
- `async / await` : permet d'écrire l'attente dans l'ordre de lecture, sans supprimer l'attente elle-même. **Priorité 1 pour un exo dédié hors projet.** Demandé plusieurs fois en session, volontairement reporté.
- **Paramètre contre variable** : la différence de vocabulaire n'est pas passée malgré deux preuves console. Exo dédié à froid, hors projet.
- `console.trace()` : à tester en console sur une chaîne d'appels bidon.
- `git add --patch`, touche `e` : édition manuelle d'un bloc. À pratiquer sur un dépôt bac à sable, jamais sur un livrable.
- `event.target` et écouteur unique sur conteneur : toujours en attente.
- `data-*` et `dataset` : toujours en attente.
- Le paramètre de callback dans un `forEach` : toujours en attente.

---

## 🔍 Vérification, ajouts

- [x] Ordre réel d'exécution du fichier prouvé en console avec un repère de fin de fichier
- [x] `try / catch` inopérant sur une erreur asynchrone, prouvé hors projet puis sur le projet
- [x] Les deux `.catch` attrapent bien leurs erreurs, back-end coupé, plus aucun `Uncaught`
- [x] Galerie et boutons toujours affichés après la réorganisation en trois blocs
- [ ] Le clic sur un filtre affiche les bons travaux
- [ ] Un seul bouton porte `filter-button-selected` à tout moment
- [ ] Navigation clavier et focus visible sur les boutons générés
- [ ] Contraste de l'état actif
- [ ] axe DevTools

---

## 📋 Bilan, préparation session mentor

### 🟢 Ce que j'ai fait seul, ajouts

- `[à valider]` Structure cible du fichier en trois blocs proposée par moi, avec sa justification : lire le fichier dans l'ordre de la chronologie
- `[à valider]` Identification seul que `createButtons` et `listenFilterButtons` n'ont pas leur place dans le bloc des appels
- `[à valider]` Ordre d'exécution prouvé par l'observation, pas admis : repère de fin de fichier, lecture de la sortie, conclusion formulée avec mes mots
- `[à valider]` Chaîne complète des trois appels reconstituée seul
- `[à valider]` `setTimeout` compris par comparaison A, C, B, sans explication préalable
- `[à valider]` Lien fait seul entre le `setTimeout` de l'exercice et le `fetch` du projet
- `[à valider]` Place du `.catch` dans la chaîne trouvée seul, à partir de la forme des `.then`
- `[à valider]` Second `.catch` posé seul sur `viewGallery`, sans indication
- `[à valider]` Touche `s` de `git add --patch` trouvée seul en lisant l'aide
- `[à valider]` Refus de créer les boutons en dur après relecture du brief
- `[à valider]` Question posée seul sur la légitimité de la dépendance entre fonctions, au lieu de subir la structure

### 🔴 Difficultés rencontrées, ajouts

- `[à valider]` Distinction entre paramètre et variable non acquise malgré deux preuves console
- `[à valider]` Réflexe de déplacer des blocs de code au jugé quand une question reste sans réponse, au lieu de s'arrêter
- `[à valider]` `console.log` placé autour de l'appel plutôt que dans la fonction, puis appel de la fonction dans elle-même : deux bugs déjà rencontrés, non reconnus
- `[à valider]` Réflexe « je sais pas » encore présent, y compris sur des points déjà notés en fiche
- `[à valider]` `git add --patch` abandonné en cours de route, séquence vécue comme confuse
- `[à valider]` Difficulté persistante à accepter une chronologie qui ne suit pas l'ordre de lecture du fichier

### ➡️ À revoir, par priorité, ajouts

- `[à valider]` **Priorité 1** · `async / await`, sur exo dédié hors projet
- `[à valider]` **Priorité 2** · paramètre contre variable, vocabulaire
- `[à valider]` **Priorité 3** · `git add --patch`, touche `e`, sur dépôt bac à sable

---

## ❓ Questions pour le mentor, ajouts

16. `[à valider]` L'ordre de lecture d'un fichier ne correspond pas à son ordre d'exécution dès qu'il y a un fetch. Est-ce que ça reste difficile avec l'expérience, ou est-ce qu'on finit par lire un fichier asynchrone naturellement ?
17. `[à valider]` `async / await` est présenté comme permettant d'écrire l'attente dans l'ordre. En agence, qu'est-ce qui est attendu sur ce type de projet : `.then` ou `async / await` ?
18. `[à valider]` Gestion d'erreur : un `.catch` avec un simple `console.log` suffit-il pour ce livrable, ou attends-tu un message affiché à l'utilisateur ?
19. `[à valider]` Quand deux sujets se croisent sur les mêmes lignes, comment tu fais concrètement pour garder un historique de commits propre ?
20. `[à valider]` Les `console.log` de debug : tu les acceptes dans des commits intermédiaires, ou tu attends un historique sans aucune trace de debug ?

---

## Commit, hashes relevés

- `87ad631` wip: reorganize file and handle fetch errors (FR : réorganiser le fichier et gérer les erreurs)
- `b78f0d1` feat: rename filter-button and listen to filter clicks (FR : renommer filter-button et écouter le clic sur les filtres)

---

## 🎤 Préparation soutenance, ajouts

- [ ] Expliquer l'ordre réel d'exécution du fichier, avec le repère de fin de fichier comme preuve
- [ ] Expliquer pourquoi un `try / catch` ne peut pas attraper une erreur de fetch
- [ ] Expliquer ce que signifie `Uncaught (in promise)` et comment le faire disparaître
- [ ] Justifier la structure du fichier en trois blocs
- [ ] Justifier le fait de ne pas créer les boutons avant le retour du fetch
- [ ] Expliquer le rôle du paramètre `categories` et d'où vient sa valeur
- [ ] Justifier le commit `wip:` plutôt que deux commits séparés

---

## 📝 Point de reprise

### Fait cette session

- Fichier restructuré en trois blocs, `fetch` des works enveloppé dans `viewGallery`
- Ordre d'exécution prouvé en console, blocage de deux sessions levé
- `try / catch` testé, compris comme inopérant sur l'asynchrone, retiré
- `.catch` posé sur les deux fetch, vérifié back-end coupé
- Deux commits poussés : `b78f0d1`, `87ad631`

### État Git

- Tout est commité et poussé. Branche `main` à jour avec `origin/main`.
- Cinq `console.log` de debug conservés volontairement dans le fichier commité.

### Étape 4, état réel

**Fait :** lignes 1, 2, 3 du pseudocode, plus la restructuration et la gestion d'erreur.

**Restant :** lignes 4, 5, 6. Vider la galerie, la reconstruire filtrée, déplacer la classe active.

**L'étape 4 n'est pas terminée** : le filtre ne filtre rien, le clic ne fait qu'un `console.log`.

### Prochaine action, dans cet ordre

1. Trancher le nom de `viewGallery` pour l'aligner sur les trois autres fonctions
2. Retirer les cinq `console.log` de debug
3. Lignes 4, 5, 6 du pseudocode. Mot-clé déjà donné pour la ligne 4 : `innerHTML`
4. Exos hors projet à froid : `async / await` en priorité, puis `console.trace()`, `event.target`, `dataset`, paramètre de callback dans `forEach`

### Étapes restantes du projet

- **Étape 5** · intégrer la page de connexion, conforme à la maquette, non fonctionnelle
- **Étape 6** · connexion fonctionnelle : envoi du formulaire, redirection, message d'erreur, stockage du token
- **Étape 7** · mode édition : bandeau noir, `login` devenu `logout`, déconnexion, filtres masqués, bouton modifier
- **Étape 8** · fenêtre modale, deux zones, ouverture et fermeture, une seule modale dans le DOM
- **Étape 9** · suppression d'un travail, requête API et mise à jour du DOM sans rechargement
- **Étape 10** · formulaire d'ajout, aperçu image, catégories depuis l'API, validation, envoi
- **Étape 11** · ajout dynamique dans le portfolio **et** dans la galerie de la modale
- **Étape 12** · tests, W3C, clavier, focus, contrastes, axe DevTools, Lighthouse
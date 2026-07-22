## 📐 Formule et méthode de calcul

> Toute formule mathématique, tout calcul, toute méthode reproductible utilisée sur le projet.
> Format : nom de la formule, le calcul en bloc code, puis à quoi elle sert.

Non applicable. Le format d'une entrée est dans `templates/fiche-template-complet.md`.

---

## 📊 Validation outils

> Ce que les outils mesurent, par opposition au bloc Vérification qui liste ce que je teste à la main.
> Une ligne par passage. On garde l'historique, on n'écrase pas.

### W3C

| Date | Fichier | Erreurs | Avertissements | Détail |
| --- | --- | --- | --- | --- |
| étape 4 | `index.html` | 0 | 1 | `#introduction` : un `h2` dans un `article` titre l'`article`, pas la `section`. Code fourni OC, non corrigé, justifiable. |
| étape 4 | `style.css` | 0 | 0 | |

---

### Lighthouse

À passer sur l'URL de production, en navigation privée, jamais sur Live Server.

| Date | Perf | Accessibilité | Bonnes pratiques | SEO | Note |
| --- | --- | --- | --- | --- | --- |
| | | | | | pas encore passé, GitHub Pages non configuré |

---

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
- [x] Compréhension des étapes 0 à 2 contrôlée (`appendChild`, `json`, `forEach`, git, `defer`), réexpliquées avec mes mots sans le code sous les yeux
- [x] `alt` présent sur chaque image générée
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
- [x] Ordre réel d'exécution du fichier prouvé en console avec un repère de fin de fichier
- [x] Les deux `.catch` attrapent bien leurs erreurs, back-end coupé, plus aucun `Uncaught`
- [x] Galerie et boutons toujours affichés après la réorganisation en trois blocs

---

### Preuve obtenue par l'échec

- [x] Vérifié que les trois appels groupés en bas du fichier ne fonctionnent pas. Testé, console muette, aucune erreur.
- [x] `try / catch` inopérant sur une erreur asynchrone, prouvé hors projet puis sur le projet

---

### En attente

- [ ] Le clic sur un filtre affiche les bons travaux
- [ ] Un seul bouton porte `filter-button-selected` à tout moment
- [ ] Boutons de filtre atteignables au clavier, focus visible
- [ ] Contraste de l'état actif
- [ ] axe DevTools
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
- Structure cible du fichier en trois blocs proposée par moi, avec sa justification : lire le fichier dans l'ordre de la chronologie.
- Identification seul que `createButtons` et `listenFilterButtons` n'ont pas leur place dans le bloc des appels.
- Ordre d'exécution prouvé par l'observation, pas admis : repère de fin de fichier, lecture de la sortie, conclusion formulée avec mes mots.
- Chaîne complète des trois appels reconstituée seul.
- `setTimeout` compris par comparaison A, C, B, sans explication préalable.
- Lien fait seul entre le `setTimeout` de l'exercice et le `fetch` du projet.
- Place du `.catch` dans la chaîne trouvée seul, à partir de la forme des `.then`.
- Second `.catch` posé seul sur `viewGallery`, sans indication.
- Touche `s` de `git add --patch` trouvée seul en lisant l'aide.
- Refus de créer les boutons en dur après relecture du brief.
- Question posée seul sur la légitimité de la dépendance entre fonctions, au lieu de subir la structure.

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

**Étape 4, session ordre d'exécution**

- Distinction entre paramètre et variable non acquise malgré deux preuves console.
- Réflexe de déplacer des blocs de code au jugé quand une question reste sans réponse, au lieu de s'arrêter.
- `console.log` placé autour de l'appel plutôt que dans la fonction, puis appel de la fonction dans elle-même : deux bugs déjà rencontrés, non reconnus.
- Réflexe "je sais pas" encore présent, y compris sur des points déjà notés en fiche.
- `git add --patch` abandonné en cours de route, séquence vécue comme confuse.
- Difficulté persistante à accepter une chronologie qui ne suit pas l'ordre de lecture du fichier.

---

### ➡️ À revoir, par priorité

> **C'est le plan d'action, la seule liste ordonnée.** Le détail de chaque notion est dans `03-connaissances.md`, bloc `📚 Théorie non pratiquée`.

**Priorité 1, à traiter en premier à froid**

> Plus rien ne bloque l'étape 4 depuis le 22-07 : l'ordre d'exécution asynchrone est acquis, prouvé par observation. Reste à le consolider.

- ~~Ordre d'exécution asynchrone~~ **résolu le 22-07**, prouvé par observation. Reste à consolider à froid.
- `async / await`, sur exo dédié hors projet. Demandé plusieurs fois en session, volontairement reporté.
- `event.target` et l'écouteur unique sur conteneur, sur exo dédié.

**Priorité 2, notions à consolider**

- Paramètre contre variable, le vocabulaire, sur exo dédié à froid.
- `git add --patch`, touche `e`, sur dépôt bac à sable.
- Le paramètre de callback dans un `forEach`, sur exo hors projet.
- `querySelector` contre `querySelectorAll`, réflexe à ancrer.
- Passage d'une valeur en paramètre.
- Portée des variables lors d'un découpage en fonctions.
- `data-*` et `dataset`, à froid.
- `map`, à froid, sur exo dédié.
- `.catch` dans une chaîne de promesses.

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

1. J'ai l'impression de ne pas m'approprier ce que je produis quand l'aide arrive trop vite. Comment le mesurer honnêtement, et que faire concrètement pour y remédier ?

2. Pourquoi mon code est-il si difficile à comprendre dans son ensemble ? Je comprends à peu près chaque ligne isolément, mais le tout assemblé me paraît impossible à suivre. Est-ce normal à ce stade, un problème de structure, ou un problème de notion ?

3. Peux-tu m'aider à revoir mon prompt Claude, voire m'en proposer ta version ? Le cadre actuel n'a pas tenu en session, l'aide arrive encore trop vite.

---

### Sur l'architecture du code

4. Brancher les écouteurs de clic depuis `createButtons` est imposé par le timing du `fetch`. Est-ce la pratique attendue, ou existe-t-il une organisation plus propre en agence ?

5. `defer` et `window.addEventListener("load", ...)` : tu utilises le second dans ton exemple, j'ai le premier. Lequel attends-tu, et pourquoi ?

6. Le refactor de la galerie en template littéral et `insertAdjacentHTML` est-il attendu pour la soutenance, ou `createElement` reste-t-il acceptable s'il est maîtrisé ?

7. Deux méthodes de génération DOM dans le même fichier : acceptable si les deux sont justifiées, ou incohérence à corriger ?

8. Les garder volontairement pour comparer : acceptable comme démarche d'apprentissage, ou à éviter sur un livrable ?

9. `localStorage` ou `sessionStorage` pour le token, quelle pratique attendue ?

---

### Sur la sémantique et l'accessibilité

10. L'`alt` de la galerie vaut `work.title`, qui vient de l'API en anglais. Acceptable pour l'accessibilité, ou faut-il autre chose ?

11. `type="button"` systématique sur les boutons hors formulaire : pratique attendue en agence, ou bruit inutile ?

12. Un bouton de filtre actif doit-il porter une information d'état pour un lecteur d'écran, ou la classe CSS suffit-elle à ce niveau de projet ?

13. L'état visuel du filtre actif (`filter-selected` de la maquette) : plutôt une classe posée en JS, ou une autre approche attendue ?

---

### Sur le livrable

14. Le backend fourni doit-il rester dans mon repo, ou seul le front-end est attendu comme livrable ?

15. GitHub Pages : `index.html` est dans `FrontEnd/`. Quelle structure recommandée, remonter à la racine ou dossier `docs/` ?

---

### Sur l'asynchrone et la gestion d'erreur

16. L'ordre de lecture d'un fichier ne correspond pas à son ordre d'exécution dès qu'il y a un fetch. Est-ce que ça reste difficile avec l'expérience, ou est-ce qu'on finit par lire un fichier asynchrone naturellement ?

17. `async / await` est présenté comme permettant d'écrire l'attente dans l'ordre. En agence, qu'est-ce qui est attendu sur ce type de projet : `.then` ou `async / await` ?

18. Gestion d'erreur : un `.catch` avec un simple `console.log` suffit-il pour ce livrable, ou attends-tu un message affiché à l'utilisateur ?

---

### Sur Git

19. Quand deux sujets se croisent sur les mêmes lignes, comment tu fais concrètement pour garder un historique de commits propre ?

20. Les `console.log` de debug : tu les acceptes dans des commits intermédiaires, ou tu attends un historique sans aucune trace de debug ?

---

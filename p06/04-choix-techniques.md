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

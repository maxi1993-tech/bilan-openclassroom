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

---

### Données

| | |
| --- | --- |
| **Ressources API** | `works` (travaux), `categories`, `users` |
| **Authentification** | token à stocker après login |

---

### Fichiers

| | |
| --- | --- |
| **Dossier de travail** | `FrontEnd/` |
| **Fourni** | `index.html` |
| **Créés from scratch** | `script.js` (galerie et filtres), à venir : login, modale |
| **Icônes** | `instagram.png` dans `FrontEnd/assets/icons` |

---

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

---

### Catégories du client

`Tous` · `Objets` · `Appartements` · `Hôtels & restaurants`

Récupérées de `/api/categories`, jamais écrites en dur.

---

### Validation

W3C aux étapes structurantes · Lighthouse sur URL de prod en navigation privée · axe DevTools · NVDA

---

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
- [x] Fichier restructuré en trois blocs : constantes, déclarations, appels de lancement
- [x] `fetch` des works enveloppé dans une fonction `viewGallery`
- [x] `.catch` ajouté sur les deux fetch
- [ ] Retirer les cinq `console.log` de debug avant le commit de fin d'étape
- [ ] Vider la galerie au clic → mot-clé donné : `innerHTML`
- [ ] Reconstruire la galerie avec les travaux filtrés
- [ ] Déplacer `filter-button-selected` sur le bouton cliqué
- [ ] Trancher le nom de `viewGallery`, qui ne suit pas le moule des trois autres fonctions (verbe + objet, cohérence avec `gallery` déclarée en ligne 1), avant le commit de fin d'étape

> Le filtre ne filtre rien pour l'instant. Le clic ne fait qu'un `console.log`.

---

### Étape 5, page de connexion · à venir

- [ ] Intégrer la page de login conforme à la maquette, non fonctionnelle

---

### Dettes et vérifications en attente

**Code**

- [ ] `filterButtonSelected` déclarée dans `listenFilterButtons`, jamais utilisée. Servira à la ligne 6 du pseudocode.
- [ ] Restructurer le repo pour GitHub Pages. `index.html` est dans `FrontEnd/`, Pages est réglé sur `main` et `/ (root)`, ne trouve pas `index.html`, n'affiche rien. Deux pistes, à m'expliquer avant d'agir : faire remonter le contenu de `FrontEnd/` à la racine avec `git mv`, sans toucher à `Backend/`, le plus propre · ou renommer `FrontEnd/` en `docs/`, que Pages sait servir, moins propre.

> **Sans urgence** · même en ligne, la galerie restera vide, le JS appelle `http://localhost:5678` que GitHub ne peut pas faire tourner. La mise en ligne sert à passer Lighthouse en fin de projet.

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

> Étapes 6 à 12, du login fonctionnel à la validation finale · le détail est dans le brief OC et le Kanban, il n'est pas recopié ici. La todo se remplit étape par étape, à l'ouverture de chacune.

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

---

### Déjà vu mais fragile, à consolider ici

- [x] `création et sélection DOM` · `createElement`, `appendChild`, `querySelector` → consolidés à l'étape 2. `classList` et `addEventListener` restent à revoir.
- [x] `parcours de tableau` · `forEach` → fait à l'étape 2, refait à l'étape 3
- [ ] `portée des variables` · `scope`, bloc, callback, fonction → règle connue depuis P5, retrouvée à tâtons au découpage en fonctions de l'étape 3

---

### Pièges connus à surveiller

> **Git** · Ne pas cocher README ni .gitignore auto à la création du repo. Penser le `.gitignore` AVANT le premier `git add`. Un `.env` ne se committe jamais.

> **Backend** · Ne jamais fermer le terminal à la croix. Le processus Node survit et bloque le port 5678.

> **Éditeur** · Le formatage automatique peut reformater tout un fichier fourni et noyer le `git diff`. Rencontré en P4, revu à l'étape 3 sur `style.css`.

> **Accessibilité** · `alt` en français, pas en anglais (piège relevé en P5). L'`alt` de la galerie vaut `work.title`, qui vient de l'API en anglais. Question posée au mentor.

---

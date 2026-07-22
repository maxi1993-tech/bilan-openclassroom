# Ohmyfood

## 🎯 Mission

Client : **OhMyFood**, start-up restauration, déjà implantée à New York, ouverture du marché parisien

Contexte : Développeur junior, positionnement haut de gamme sur un marché de niche (restaurants gastronomiques). Budget 20 000€, livraison V1 sous 1 mois.

Livrable : 1 page index + 4 pages restaurant, HTML/CSS/SASS

Deadline soutenance :

Format évaluation : **Soutenance orale** (présentation 15 min + discussion 10 min + débriefing 5 min), l'évaluateur joue Paul, le CTO

Développer un site mobile-first qui répertorie les menus de restaurants gastronomiques. Phase 1 : affichage des menus de 4 restaurants, sans réservation ni composition de menu (prévu en phase 2). Animations en CSS pur, aucun JavaScript.

---

## 🔧 Specs techniques

Icônes : SVG inline, export Figma direct
Breakpoints : fixes, `$md: 768px` / `$lg: 1024px` / `$xl: 1440px`
Approche : Mobile-first
Mise en page : Flexbox / Grid
SASS : obligatoire, architecture 7-1, multi-fichiers
Pas de : framework CSS, JS
Animations : CSS uniquement
Valide : W3C HTML + CSS

---

## ✅ Todo

**Avant de coder**

- [x]  Extraire couleurs, typo, espacements du Figma
- [x]  Découper les maquettes (index + restaurant)
- [x]  Créer arborescence SASS
- [x]  GitHub Pages

---

**HTML/CSS index + restaurant**

- [x]  Header, localisation, hero, fonctionnement, cards, footer (index)
- [x]  Header + retour, bannière, menu, bouton Commander, footer (restaurant)
- [x]  CSS mobile stylé, hors animations

---

**Refactor**

- [x]  SVG : icônes Figma migrées, plus de Font Awesome ; SVG footer corrigé et reporté sur les 4 pages restaurant (était appliqué à une seule)
- [x]  Mixins : `flex-center` étoffée, `flex-column` créée
- [x]  Nettoyage Sass : variables, sélecteurs morts, couplage BEM

---

**rem + clamp**

- [x]  `$fs-*` et espacements convertis en rem
- [x]  `clamp()` sur h1, logo, `main__img`, `.menu`, `menu__content-title`

---

**Performance images**

- [x]  4 images redimensionnées (Squoosh, 1440px, WebP), `.jpg` parasites supprimés
- [x]  `srcset`/`sizes` sur `card__img` et `main__img`
- [x]  `fetchpriority`/`loading` corrects sur toutes les images

---

**Contenu & accessibilité**

- [x]  Alt manquants remplis, `sr-only` posé où nécessaire
- [x]  Focus, hover boutons/cards/cœur/coche
- [x]  Ellipses nom/description plat trop long

---

**Responsive**

- [x]  Cards restaurant en grid, 2 colonnes à 768px
- [x]  `respond-to` écrite, ajustements `$lg`/`$xl`
- [x]  Pages restaurant : tablette + desktop

---

**Animations**

- [x]  Apparition décalée des plats
- [x]  Coche dish animée
- [x]  Cœur qui se remplit
- [x]  Loader page d'accueil
- [x]  `prefers-reduced-motion` sur les 4

---

**Avant de rendre**

- [x]  Passe classes HTML inutiles (méthode + commande universelle créée)
- [x]  W3C HTML toutes les pages (bug ids dupliqués corrigé)
- [x]  W3C CSS toutes les pages (3 avertissements `webkit-` attendus, pas de vraie erreur)
- [x]  Lighthouse — 5 pages testées mobile/desktop (sous-points détaillés ci-dessous)
- [x]  Test mobile/tablette/desktop DevTools
- [x]  Test Chrome + Firefox
- [x]  Nettoyer branches obsolètes

---

**Points Lighthouse détaillés (issus de l'audit)**

- [x]  `font-display: fallback` tranché
- [x]  CLS `how-it-works` couvert par cette décision
- [x]  `pointer-events` animé dans `loader-finish` → utilisé z-index
- [x]  Re-tester en production GitHub Pages (pas en local)

---

**Dernière passe (reportée)**

- [x]  Passe finale projet / Figma / brief

---

## 🔍 Choix techniques

> Format : `décision → pourquoi`
> 
- Logo en `<span>`, sans `<a>` ni `<h1>` → texte stylé Shrikhand, pas une image. Un seul `<h1>` par page, déjà pris par le titre principal.

---

- `<h1>` = "Réservez le menu qui vous convient" sur l'index, nom du restaurant sur les pages restaurant → c'est le sujet de chaque page.

---

- `<article>` pour les cards restaurant → unité de contenu autonome. `<ol>`/`<li>` pour les étapes du fonctionnement → suite d'étapes dans un ordre logique.

---

- BEM sur tout le projet → lisibilité et maintenabilité en équipe.

---

- `<hgroup>` plutôt qu'une div pour le titre du hero → regroupe sémantiquement `<h1>` et sous-titre.

---

- Localisation en `<p>` dans le hero, pas en `<form>` → pas de bouton de validation pour l'instant, vrai champ prévu plus tard. Placée dans la section hero plutôt qu'en navigation séparée → fait partie du message principal de la page.

---

- `id="restaurant"` sur la section restaurants → ancre au bouton hero, lien intra-page sans JS.

---

- `<span>` + `white-space: nowrap` sur les 2 derniers mots du h1, plutôt qu'un `<br>` → empêche seulement ce groupe de mots de se séparer entre deux lignes, sans casser le HTML sémantique.

---

- SASS multi-fichiers, architecture 7-1, `@use ... as *` dans chaque partial → un fichier par responsabilité, accès direct aux variables sans namespace à répéter.

---

- `counter` + `::before` pour les numéros des étapes → pas de spans inutiles dans le HTML.

---

- `flex-center` étoffée avec `$direction`/`$align`/`$gap` (défauts `null`), `flex-column($gap)` créée à part → les variations avaient déjà été vues sur des call sites réels, pas anticipées ; les deux mixins reflètent des intentions différentes (centrer vs empiler).

---

- `::before`/`::after` sur `&__section-title` → une seule occurrence confirmée, pas de mixin créé. `$shadow-card` et `$shadow-dish` gardées séparées → pas de fusion forcée entre composants distincts malgré des valeurs proches.

---

- Aucun dossier `animation/` dans le 7-1 → chaque animation vit dans le partial de son composant hôte. Le loader a son propre fichier `_loader.scss` car son contenu est trop différent de `_home.scss`.

---

- Toutes les icônes en SVG inline, exports Figma directs, plus de Font Awesome → zéro requête réseau, contrôle de couleur via `fill`.

---

- `aria-hidden="true"` sur toutes les icônes décoratives → l'information est déjà portée par le texte adjacent. Sans ça, un lecteur d'écran annoncerait l'icône en plus du texte, redondance inutile.

---

- `fill: currentColor` global dans le reset → fallback de couleur pour toutes les icônes sans toucher au HTML. L'icône cœur reste en outline par défaut (`fill: none` posé dans le fichier), mais un attribut de présentation HTML est structurellement sous n'importe quelle règle CSS : le reset gagne toujours tant qu'aucune règle CSS plus spécifique ne vient l'annuler.

---

- **Coche dish** : `background-image` simple, pas `mask-image` → le SVG check a un trou natif créé par `fill-rule` (deux sous-tracés dessinés en sens opposés), le fond teal traverse déjà sans avoir besoin d'un masque CSS.

---

- `.dish::before` (icône, glisse + tourne) et `.dish::after` (rectangle teal, s'élargit) séparés, chacun avec sa propre `transition` → une transition ne s'applique jamais aux pseudo-éléments ou enfants d'un autre bloc, chacun doit déclarer la sienne.

---

- `min-width: 0` à deux niveaux de flex imbriqués (`__subtitle` dans `__details`, `__content` dans `.dish`) → sinon l'ellipsis ne fonctionne pas et la coche n'a pas sa place au survol.

---

- `overflow-x: hidden` sur `html` et `body` → le `::before` de la coche déborde volontairement en `right: -20px` au repos (pour glisser vers l'intérieur au survol). Un enfant en `position: absolute` hors de la boîte de son parent participe quand même au `scrollWidth` de la page, même invisible.

---

- **Apparition décalée des plats** : boucle `@for $i from 1 through 10` sur `.menu__item:nth-child(#{$i}) .dish`, pas `.dish:nth-child()` directement → chaque `.dish` est seul dans son propre `<li class="menu__item">`, donc toujours enfant unique de son parent. `:nth-child()` compte parmi les frères directs ; il faut compter sur `.menu__item` (frères entre eux) puis descendre. La boucle est écrite à la racine du fichier, pas imbriquée dans `.dish{}`, sinon Sass préfixerait le sélecteur du parent et produirait un sélecteur qui ne matche jamais rien. `animation: dish 1s backwards` : `backwards` maintient l'état invisible pendant le délai, sinon le plat resterait visible puis sauterait brutalement à son état caché au démarrage. Délai réel dans le code : `0.1s` par plat.

---

- **Cœur** : un `<path>` (contour) + un `<use href="#path">` cloné par-dessus (`.heart__fill`, animé). Un seul `<linearGradient id="heart-gradient">` déclaré dans `<defs>`, partagé par les 4 cœurs de `index.html` → un id référencé (`url(#id)`) peut être unique et pointé depuis toute la page ; un id matérialisé plusieurs fois dans le DOM (chaque `<path>`) doit être différent par instance, d'où 4 ids de path distincts.

---

- `fill` SVG n'accepte pas `linear-gradient()` CSS → seulement une couleur unie ou `url(#id)` vers un gradient natif. Les coordonnées `x1/y1/x2/y2` sont la conversion de l'angle CSS (`193.33deg`) en deux points symétriques autour du centre `(0.5, 0.5)` d'un repère normalisé 0→1.

---

- Remplissage via `transform: scale(0→1)` + `transform-origin: center`, pas `clip-path` → `scale` garde toujours la forme exacte du cœur ; `center` fait grossir le remplissage depuis le milieu, pour qu'il reste superposé au contour à chaque instant de l'animation.

---

- `stroke: url(#heart-gradient)` ajouté sur `.heart__fill:hover` → `fill` ne peint que l'intérieur, pas l'épaisseur du trait, donc sans ce `stroke` un liseré sombre resterait visible autour du cœur rempli. Le `<use>`, écrit après le `<path>` dans le markup, se peint par-dessus (ordre de peinture SVG). Évite d'avoir besoin d'un `scale > 1` combiné à `overflow: visible`, qui se heurterait au clipping du viewBox `0 0 22 21`.

---

- `.heart:hover .heart__fill`, pas `.heart__fill:hover` directement → au repos `.heart__fill` est à `scale(0)`, sa zone de rendu est nulle et ne peut jamais recevoir `:hover`. `.heart` (le `<svg>` entier) a une taille constante, c'est lui qu'on survole pour changer l'état de son enfant caché.

---

- **Loader** : deux animations séparées. `loader-finish` sur `.loader` (overlay plein écran, disparaît en 3s, `animation-fill-mode: forwards` pour rester invisible après). `loader` sur chaque `.loader__letter` (ondulation, un seul cycle, pas infini). `pointer-events: none` ajouté à la fin de `loader-finish` → `opacity: 0` seul ne désactive pas les clics d'un overlay `fixed` plein écran. Lighthouse signale la propriété comme "non composée" (question mentor 13, non résolu).

---

- Texte en dégradé via `background-clip: text` + `color: transparent` (préfixes `-webkit-` inclus). `padding: 0 30px` + `margin: 0 -30px` sur chaque lettre → agrandit la boîte de clip pour couvrir les glyphes débordants (f/d en Shrikhand), sans réintroduire d'espacement visuel entre les lettres.

---

- Boucle `@for $i from 1 through 8` posée directement sur `.loader__letter:nth-child(#{$i})` → contrairement aux plats, ça marche en direct car les 8 lettres sont toutes enfants directs (frères) du même `.loader`. Point de vigilance : la borne colle exactement au nombre de lettres de "ohmyfood", zéro marge — un changement de nom casserait la cascade sans retoucher le SCSS.

---

- `prefers-reduced-motion` : annulation complète (pas d'atténuation), media query dans chaque fichier concerné plutôt que centralisée → cohérent avec la règle "l'animation vit dans son composant hôte". Sur le loader, seule l'ondulation des lettres est coupée ; la disparition de l'overlay reste, car elle est fonctionnelle, pas juste esthétique.

---

- Resize physique (Squoosh, cible 1440px) avant export WebP → le format optimise la compression à dimensions données, le resize réduit les pixels eux-mêmes ; les deux sont complémentaires, l'un ne remplace pas l'autre. Gains : 703→212 Ko, 1948→260 Ko, 730→501 Ko, 430→126 Ko. `$gradient-primary: linear-gradient(193.33deg, ...)` : angles pris directement du Figma, fidélité maximale.

---

- `fetchpriority="high"` sur `main__img` uniquement, pas sur `card__img` → cible spécifiquement l'image LCP (Largest Contentful Paint) de la page, pas toute image visible au chargement. `loading="lazy"` retiré sur `main__img` (LCP), conservé sur `card__img` (hors premier écran mobile potentiel).

---

- `font-display: fallback` retenu partout, malgré un score Lighthouse inférieur à `optional` → trois valeurs testées sur l'accueil desktop : `optional` (99 perf / CLS 0), `fallback` (95 / CLS 0,023), `swap` (96 / CLS 0,116). Sur mobile réseau lent, `fallback` remonte à CLS 0,12, mais le CLS ne concerne que l'accueil : confirmé à 0 sur une page restaurant testée dans les mêmes conditions. `fallback` choisi pour la cohérence d'un seul réglage sur tout le site plutôt qu'un score marginalement meilleur par page.

---

- `:focus` plutôt que `:focus-visible` → choix délibéré : contour visible au clic souris ET au clavier, cohérence du signal plutôt que discrétion au clic. Le brief impose Chrome/Firefox desktop, pas de navigation clavier exclusive.

---

- `outline` plutôt que `border` pour le focus → hors box model, pas de reflow. `display: block` sur `.restaurant__link` pour deux raisons : l'outline suit le border-radius seulement si la boîte de l'`<a>` s'aligne sur le visuel, et un `<a>` inline n'offre pas de base fiable pour un `width: 100%` enfant. `a:focus, button:focus` déclarés séparément pour éviter que le `border-radius` de l'un ne fuie sur l'autre.

---

- `filter: brightness(1.15)` plutôt que `opacity` sur le hover des boutons → le fond est un gradient, `opacity` rendrait le texte translucide aussi. Nouvelle variable `$shadow-button-hover`, distincte de l'ombre de repos, pour un effet "plus visible" réel. `transition` posée sur l'état de repos, jamais sur `:hover`, pour couvrir entrée et sortie.

---

- Cards restaurant : `scale(1.03)` sur `.restaurant__link:hover`, pas `.restaurant__list` (qui ferait grossir toute la grille). `border-radius` ajouté dans le `:hover` (coins droits au repos sinon), et `box-shadow: $shadow-button-hover` réutilisée depuis les boutons → deux écarts assumés aux règles habituelles, sans creuser plus loin.

---

- `list-style: none` conservé sans `role` sur les listes → testé Chrome/Firefox avec NVDA et Narrator, aucune perte de sémantique de liste constatée. `sr-only` sur "Localisation :" → donne le contexte au lecteur d'écran, sinon un nom de ville isolé n'a pas de sens.

---

- `max-width` + `margin: 0 auto` déplacés de `.card` vers `.restaurant__list` → centralise la contrainte de largeur à un seul endroit. `margin: 0 auto` plutôt que `justify-self` → le parent `.restaurant` n'est ni flex ni grid, `justify-self` n'aurait aucun effet.

---

- `position: relative` + `z-index: 1` sur `.header` → fait passer son ombre au-dessus de l'élément suivant. Même traitement sur `.menu`, combiné à un `margin-bottom` négatif sur `.main__img` → masque le chevauchement entre bannière et carte menu.

---

- `dish__details` en wrapper flex pur, `.button--order` porte sa propre largeur (186px) en modifier → évite le couplage `.menu .button--order`, contraire à l'autonomie des composants BEM.

---

- Cards restaurant en CSS Grid (`1fr` en mobile) → transition plus naturelle vers 2 colonnes qu'avec `flex-wrap`.

---

- Badge "Nouveau" affiché sur 2 des 4 cartes seulement, `card__img--center` sur une carte → recadrage justifié au cas par cas selon le visuel de chaque photo, pas une règle uniforme.

---

- `respond-to($breakpoint)` : un seul paramètre, pas de `max-width` → mobile-first pur, rien à annuler en descendant. `clamp()` du h1 et du logo calculés par **interpolation linéaire** (2 points connus, exact), pas choisis à l'œil — voir formule ci-dessous.

---

- Containers (`restaurant__container`, `how-it-works__container`) : `max-width` fixe plutôt que `clamp()` → le brief impose des breakpoints fixes, la courbe clamp ne tombe pas exactement sur la valeur voulue à ces points. `min-height` retiré sur `.hero__container`, remplacé par du padding → hauteur dictée par le contenu, plus robuste qu'une valeur fixe entre breakpoints.

---

- `.menu`/`.menu__section` : pattern `max-width: clamp(...) + width: 100%` sans media query → le navigateur prend toujours la plus petite valeur, transition mathématiquement continue. Léger rétrécissement accepté vers 425px (croisement de courbe), jugé non gênant.

---

- `main__img` : hauteur en `clamp()` (275px à 375px de viewport → 383px à 1440px), `menu__content-title` : `max-width` fixe avec `margin: 0 auto` seulement à partir de `$md`, `object-position: center 60%` via `respond-to($lg)` sans répétition à `$xl` (la règle reste active de `$lg` à l'infini). Marges négatives sur `how-it-works__title`/`__list` à `$xl` : ajustement pixel-perfect contre la maquette, valeurs arbitraires côté design.

---

## 📐 Formule clamp() (interpolation linéaire)

```powershell
pente = (valeur_max - valeur_min) / (largeur_max - largeur_min)
ordonnée = valeur_min - pente × largeur_min
→ clamp(valeur_min, calc(ordonnée_rem + pente_vw), valeur_max)
```

**Interpolation** (2 points, droite exacte) ≠ **régression** (approximation). Le terme exact compte à l'oral.

## 🔍 Vérification

!image.png

Untitled

## 📋 Bilan, préparation session mentor

### 🔴 Difficultés rencontrées

- `list-style: none` confondu avec suppression de compteur, deux mécanismes différents
- Focus faussé en DevTools (le clic fait perdre le focus) → résolu avec "Force element state"
- Outline invisible sur les cards → `overflow: hidden` sur `.card` le rognait
- Largeur incohérente entre cards identiques → `display: block` manquant sur `.restaurant__link`
- Faux conflit git sur le CSS compilé → watch Sass qui recompile pendant un checkout
- `git push origin --delete` échoue à tort → contourné avec `refs/heads/<branche>`
- Erreur d'arrondi px→rem (23.93 au lieu de 23.9375)
- Risque de sur-paramétrer `flex-column` avec `$direction` → corrigé, paramètre retiré, aucun call site ne l'utilisait
- Premier essai de `box-shadow` plus visible raté : le flou avait été réduit au lieu d'être augmenté
- SVG en data URI raté (guillemets) → abandonné pour un fichier `.svg` séparé
- Chemin `url()` mal résolu → résolution depuis le CSS compilé, pas la racine ni le `.scss` source
- `::before`/`::after` posés directement sur un `<svg>` peu fiables → piste `<use>` retenue
- Piège `:nth-child()` rencontré deux fois : plats isolés dans leur `<li>`, boucle imbriquée par erreur dans `.dish{}`
- `background-clip: text` coupait les lettres f/d → glyphe débordant de sa boîte typographique, corrigé par padding + margin négative
- Overlay loader cliquable malgré `opacity: 0` → `pointer-events: none` nécessaire en plus
- Bug PowerShell `notmatch` sur un tableau (filtre au lieu de renvoyer un booléen) → fusion en chaîne avant comparaison
- Recherche de classes mortes dans le Sass source échoue (nesting BEM jamais écrit en toutes lettres) → chercher dans le CSS compilé
- 4 cœurs invisibles après renommage d'ids → `<use>` référençait un ancien id disparu, gradient CSS pointait vers un id qui n'existait plus nulle part
- Deux écarts trouvés entre le bilan écrit et le code réellement commité (délai `dish`, ondulation/padding du loader) → le bilan avait dérivé sans revérification contre le fichier source

### 🟢 Points forts

- Réflexe de test empirique (NVDA, Narrator, Chrome, Firefox) avant de conclure
- Retour au brief pour trancher un doute de scope plutôt que chercher une solution technique hors sujet
- A anticipé plusieurs effets de bord avant qu'ils n'arrivent (fuite de border-radius, dilution de mixin)
- A challengé plusieurs généralisations et messages de commit imprécis plutôt que de les accepter
- A diagnostiqué seul plusieurs causes réelles à partir de l'observation (boucle des plats, croisement de courbe clamp, double cause Lighthouse)
- A construit une méthode généralisable (détection de classes mortes) et demandé sa documentation
- A signalé lui-même un manquement à la règle de guidage socratique en cours de session
- A retrouvé seul le piège `nth-child` sur le loader par transfert direct depuis l'exemple des plats
- A repéré que le calcul trigonométrique du gradient était disproportionné et a demandé un support visuel plutôt que d'abandonner

### ➡️ À revoir / approfondir

- Spécificité de sélecteur CSS vs priorité des attributs de présentation HTML — deux mécanismes différents, confondus plusieurs fois pendant le quiz
- `fill` (intérieur) vs `stroke` (contour) sur SVG
- Critère réel de `fetchpriority`/`loading="lazy"` : statut LCP, pas "visible au chargement"
- Justifier `:focus` vs `:focus-visible` à l'oral sous forme de phrase prête
- "La dernière déclaration gagne" ne s'applique qu'à spécificité égale, pas à invoquer sinon
- `transition`, `filter: brightness()`, `outline` vs `display: block`, `role`
- Commandes git du merge à expliquer mot par mot
- Flex vs grid sur `justify-self`/`align-self`/`align-items`
- Breakpoint exact `how-it-works` en row (1026px vs `$lg: 1024px`)
- `vh` vs `dvh`
- Pattern `max-width: clamp() + width: 100%`, point de croisement
- Syntaxe `url()` et chemins relatifs, encore fragile
- Éléments remplacés (`<svg>`, `<img>`) vs éléments normaux pour les pseudo-éléments
- Calcul trigonométrique de conversion d'angle CSS → coordonnées SVG dans le détail (la logique de synthèse est acquise, non bloquant pour l'oral)

---

## ❓ Questions pour le mentor

1. `counter` CSS ou spans acceptés pour les numéros d'étapes ?
2. Font Awesome vs export SVG Figma, préférence agence ?
3. Nommage BEM `card`/`restaurant__card`, validation ?
4. Focus sur les étapes de fonctionnement, attendu ?
5. `mask-image` pour la coche : approche pertinente en agence pour éviter la duplication SVG ? *(ici le SVG avait un trou natif, `background-image` a suffi ; question valable pour le cas général)*
6. Classes BEM sans règle CSS dédiée : garder ou toujours nettoyer ?
7. Alignement SVG/texte `how-it-works`, tenté sans succès : qu'est-ce qui bloque ?
8. Tablette : maquette dispo ou jugement personnel jusqu'à 1440px ?
9. Ellipse plat trop long : attendu dès l'intégration de base ou phase animations ?
10. `clamp() + width: 100%` : léger saut accepté sur `.menu` mais pas sur les containers — cohérent ou à uniformiser ?
11. `git push origin --delete` échoue malgré `git ls-remote` positif : bug connu ou config locale ?
12. Classes BEM sans règle CSS (`restaurant__item`, `restaurant__card`, `footer__item`) sans justification apparente : garder ou nettoyer ?
13. `pointer-events` animé, signalé "non composé" par Lighthouse : pratique pro standard pour désactiver les clics d'un overlay sans passer par le `@keyframes` ?

---

## Commit

```powershell
PS C:\Users\jah19\dev\openclassroom\Projet-4\ohmyfood> git log --oneline
b6f9833 (HEAD -> main, origin/main, origin/HEAD) feat: fill heart on click with checkbox
4a6daf1 refactor: move heart out of card and rename to restaurant__icon
9ef036d docs: write readme with setup and context
226003a fix: use z-index instead of pointer-events for loader
c59e6bd fix: fix duplicate heart ids on homepage
e20a7a0 feat: add hover scale on cards
3ecb002 feat: add prefers-reduced-motion support
16a0ea4 feat: add animated loader on homepage
aaa3774 feat: animate dish entrance with per-item delay
4ee1a60 feat: add animated heart and adjust checkmark offset
7b08e4e fix: prevent horizontal scroll on mobile
35627dd fix: unify font-display to fallback everywhere
053a134 fix: truncate dish title with ellipsis at 320px
9202949 feat: add animated checkmark with rotation and dish wrapper
d886dd6 fix: remove duplicate dish
b7cddf9 fix: use font-display optional to fix CLS
5b77b35 fix: correct sizes attribute on restaurant card images
a5f220d refactor: adjust image object-position on tablet
d786ad4 feat: add tablet and desktop responsive to restaurant pages
5fd4f1a fix: apply updated footer svg to all restaurant pages
6f7c5fb fix: adjust card image position on desktop
17b4ebb fix: finalize how-it-works desktop spacing
6bdd20a feat: add desktop responsive layout and container centering
36b3a27 feat: add desktop layout adjustments at lg breakpoint
0a5580a feat: add tablet responsive layout with respond-to mixin
b44a4bf style: adjust width/padding/left/top and fix line break on h1
de87f95 fix: correct steps sizing and switch cards to grid
ca054f6 feat: add fluid clamp() sizing to h1 title
1f74cd5 fix: adjust padding on how-it-works and restaurant sections
03d54b5 refactor: extract repeated flex patterns into mixins
c67ecfd refactor: migrate remaining icons to figma svg exports
96854dc feat: add a11y, focus and hover states
aeaf9e1 fix: add missing alt text to restaurant images
fc62aff refactor: convert spacing values to rem
d537135 refactor: fix redundant header and hero rules
6ddb17b refactor: remove dead Sass code
7b42aa6 feat: add srcset and sizes on card and main images
0a940b2 fix: prioritize loading of restaurant banner images
a66921f fix: resize new badge to match design
6cd8ec8 fix: resize restaurant images to reduce file weight
a127b09 fix: remove lazy loading from above-the-fold images
1e3ef3d refactor: convert font sizes from px to rem
0e2009c refactor: clean up sass variables
705f6f4 refactor: remove dead css declarations
acbadd3 refactor: reorder main.scss imports
085f983 refactor: use figma svg for header back icon
fe6466e fix: use fill instead of color on header icon
94ca434 refactor: move header icon styles to header partial
84c34b1 fix: move order button width to its own modifier
461acd4 feat: add mobile styles for restaurant page
3f457c8 feat: add dish component with title, subtitle and price
2c6dc22 wip: add dish component, variables and restaurant page layout
11f3f8a fix: update badge text color for wcag aa compliance
85c1a76 fix: replace deprecated clip with clip-path in sr-only
89fac1b fix: replace filled heart with outline heart on index cards
01ac2df feat: add html for all four restaurant pages
351cf2e refactor: move how-it-works and restaurant styles to dedicated partials
8d2d392 refactor: replace fa footer icons with inline svg
5e30bae refactor: replace fa heart icons with inline svg
6e84dfb refactor: replace fa how-it-works icons with inline svg
dbb43c6 refactor: replace fa location-dot with inline svg
0783ef6 feat: add footer styles
fb9b8ad feat: add card component styles
6644101 feat: add restaurant section styles
df89a00 wip: add how-it-works styles and step counter
a31c2e6 feat: add box-shadow to button and z-index to header
5789817 chore: add shadow variables for header and location
602a28b fix: remove list-style reset from ol to preserve screen reader semantics
3afc80f refactor: extract location out of hero and simplify hero structure
5d8e7aa feat: add hero section styles
a4277b7 refactor: use flex-center mixin in header and button
9219d81 chore: add flex-center mixin
41792d5 refactor: rename bg-footer and bg-step to bg-dark and bg-grey
f078ceb refactor: replace div with hgroup in hero section
8757e98 feat: add header layout with min-height 63px
3d64325 feat: add line-height base and white color to footer logo
a5d450f chore: add white color variable
69d69c9 fix: add variables import and update logo font selectors
e6d0d38 chore: add Shrikhand font and merge google fonts imports
b08e8c1 chore: add main.scss with all partial imports
dacf90b chore: add sr-only utility class and fix reset order
d8b1ae1 refactor: use span for logo and rename footer__logo class
3003707 chore: add typography base styles
96e6964 chore: add css reset
d1c6bf3 chore: add sass variables
ba05875 feat: replace jpg images with compressed webp versions
9e9f3a3 chore: setup sass folder structure and update watch script
c85ee27 feat: add restaurant ids and anchor links
e133fc9 feat: add footer with logo, nav links and contact
96ef512 feat: add lazy loading to restaurant images
2f8f980 feat: add class to header and logo
ebd94d3 feat: add restaurant cards section
82673f2 fix: remove redundant number spans from how-it-works
8cbc9eb feat: add how-it-works section
beadf81 feat: update hero section
f5627fb feat: update header and h1 structure
a12d481 feat: add location bar and hero section
50a316e feat: add header with logo
96eb9dd chore: add html boilerplate to all pages
323af1e chore: rename images folder and update readme
088d2b9 chore: setup sass with npm and watch script
e7a849a chore: initial project setup
PS C:\Users\jah19\dev\openclassroom\Projet-4\ohmyfood>
```

## 🎤 Préparation soutenance

Format : 15 min présentation + 10 min discussion + 5 min débriefing

**Sujets à maîtriser**

- [x]  Chaque choix technique, format `décision → pourquoi`
- [x]  `color` vs `fill` sur SVG, pourquoi `currentColor`
- [x]  `srcset`/`sizes`, principe du 2x Retina
- [x]  Un commit = un sujet, git log comme preuve de méthode
- [x]  `:focus` vs `:focus-visible`, choix délibéré
- [x]  `filter: brightness()` vs `opacity` sur un gradient
- [x]  Mixin vs paramètre anticipé (`flex-column`)
- [x]  `clamp()` par interpolation linéaire, pas régression
- [x]  Centrage flex/grid/bloc normal selon le `display` du parent
- [x]  `clamp()` vs media query selon le composant
- [x]  Pattern `max-width: clamp() + width: 100%`
- [x]  Les 4 mécaniques d'animation (voir Choix techniques)
- [x]  Piège `:nth-child` : frères directs (loader) vs isolés (plats)
- [x]  Cascade : attribut HTML vs règle CSS vs spécificité entre deux règles CSS — encore fragile
- [x]  `fetchpriority`/`loading` : critère LCP — encore fragile
- [x]  `fill` vs `stroke` — encore fragile

---

## 🧠 Nouvelles connaissances

### HTML & Sémantique

- `list-style: none` ne casse pas forcément la sémantique de liste pour les lecteurs d'écran modernes, à vérifier empiriquement
- `role="list"` à ajouter seulement si une régression réelle est observée
- `loading="lazy"` jamais sur l'image LCP, `fetchpriority="high"` réservé à l'image LCP

### CSS — cascade et priorité

- Un attribut de présentation HTML est structurellement sous n'importe quelle règle CSS, catégorie de priorité à part, pas une bataille de spécificité
- Entre deux règles CSS, spécificité classique (classe > type), indépendante de l'ordre d'écriture sauf à spécificité strictement égale

### CSS — transitions et animations

- Une `transition` ne s'applique qu'aux propriétés de l'élément qui la porte, jamais à ses pseudo-éléments ou enfants
- `animation-fill-mode: backwards` maintient l'état `0%` pendant le délai, `forwards` maintient l'état `100%` après la fin
- `:nth-child()` compte parmi les frères directs, pas parmi tous les éléments de même classe sur la page
- Une boucle `@for` imbriquée dans un bloc Sass se fait préfixer par le sélecteur du parent, peut produire un sélecteur qui ne matche rien
- `pointer-events: none` nécessaire en plus d'`opacity: 0` pour qu'un élément invisible cesse d'intercepter les clics
- Un enfant `position: absolute` hors de la boîte de son parent participe quand même au `scrollWidth` de la page
- `@use` vs `@import` : `@use` ne rend plus les variables globales automatiquement, `as *` supprime le namespace
- `@content` dans les mixins : permet d'injecter un bloc de styles personnalisé au moment de l'appel
- `calc()` exige un opérateur mathématique entre deux valeurs, jamais une virgule ; `clamp()` accepte des virgules entre ses 3 arguments, deux syntaxes différentes
- Code mort en CSS : une déclaration peut être syntaxiquement valide sans aucun effet réel (ex. `font-size` sur un SVG), vérifier l'effet, pas juste la validité syntaxique
- `align-items` en `flex-direction: column` agit sur l'axe horizontal, pas vertical
- Un bloc `respond-to($xl)` imbriqué dans `respond-to($lg)` donne le même résultat final (min-width cumulatif), mais casse la cohérence de lecture du fichier
- `min-height: 100dvh` vs `100vh` : `dvh` tient compte de la barre d'adresse mobile
- Ordre 7-1 canonique : abstracts → base → layout → components → pages. L'ordre des dossiers et l'ordre des `@use` dans `main.scss` sont deux choses distinctes à vérifier séparément
- Nommage des variables : décrire le rôle, pas le contexte d'origine (préfixe cohérent par catégorie, ex. `fs-` pour toutes les tailles de police)
- Une `transition`/`animation` déclarée deux fois pour la même propriété dans le même bloc : la dernière écrase silencieusement la première, sans erreur.
- Combiner plusieurs fonctions `transform` sur une ligne : séparées par un espace, jamais une virgule.

Architecture Sass 7-1 :

```powershell
sass/
  abstracts/     (_variables.scss, _mixins.scss)
  base/          (_reset.scss, _typography.scss)
  layout/        (_header.scss, _footer.scss)
  components/    (_button.scss, _card.scss, _dish.scss, _heart.scss)
  pages/         (_home.scss, _how-it-works.scss, _restaurants.scss, _restaurant-page.scss, _loader.scss)
  main.scss
```

### SVG et couleur

- `color` n'affecte jamais un SVG, `fill` colore l'intérieur, `stroke` colore le contour
- `<use href="#id">` clone le rendu d'un élément sans dupliquer le markup
- Un id référencé (`url(#id)`) peut être unique et pointé depuis toute la page, un id matérialisé plusieurs fois doit être différent à chaque instance
- `transform: scale()` garde toujours la forme exacte, `transform-origin` définit le point fixe de l'agrandissement
- Ordre de peinture SVG : un élément plus tard dans le markup se peint par-dessus
- Le viewBox clippe par défaut tout débordement au-delà de sa fenêtre
- `:hover` ne se déclenche jamais sur une zone de rendu nulle (`scale(0)`)
- `background-clip: text`, technique de pochoir pour texte en dégradé, glyphes débordants corrigibles par padding + margin négative
- Un `fill-rule` avec sous-tracés en sens opposés peut créer un trou natif transparent dans un SVG
- `::before`/`::after` ne peuvent jamais contenir un vrai SVG enfant, seulement `content` (texte) ou `background-image`/`mask-image`

### Accessibilité

- `aria-hidden="true"` pour une icône décorative dont l'info est déjà dans un texte adjacent
- `prefers-reduced-motion: reduce`, réglage système testable en DevTools sans changer l'OS
- "Force element state" en DevTools pour tester focus/hover sans dépendre du focus réel
- Un élément purement décoratif sans vraie fonction (le cœur "j'aime" sans sauvegarde réelle en V1) ne doit pas recevoir d'`aria-label` suggérant une action qui n'existe pas encore ; `aria-hidden="true"` reste le bon choix tant que la fonctionnalité n'est pas implémentée
- NVDA : lecture continue via Insert + flèche bas, différent du parcours au Tab. Windows Narrator : mode lecture via Caps Lock + Espace, distinct également
- Onglet Styles (cascade, sélecteurs, priorité) vs onglet Computed (liste alphabétique des propriétés finales) : deux usages pour diagnostiquer un style écrasé

### Performance

- WebP et redimensionnement physique sont deux leviers complémentaires, l'un ne remplace pas l'autre
- Lighthouse distingue Time to First Byte et délai d'affichage dans la répartition du LCP
- Auditer en navigation privée et en production, jamais en local avec extensions actives

### Responsive

- iPad portrait : certains modèles (iPad Mini, iPad 9e gen et antérieurs) font exactement 768px CSS, mais pas tous — un breakpoint à 768px concerne un vrai appareil répandu, pas qu'un test DevTools théorique

### Outils & process

- `git ls-remote origin <branche>` avant de conclure qu'une branche distante n'existe plus
- `refs/heads/<branche>` si `git push origin --delete` échoue à tort
- `notmatch` en PowerShell sur un tableau filtre les éléments au lieu de renvoyer un booléen
- Chercher des classes mortes dans le CSS compilé, jamais le Sass source
- Un déplacement de code sans changement visuel est `refactor:`, jamais `fix:`
- `git add -p` : stager hunk par hunk pour séparer deux sujets mélangés dans les mêmes fichiers
- Piège `git add .*` en PowerShell : ne matche rien à la racine du repo, utiliser `git add .`
- Toujours vérifier la portée du brief (navigateurs/lecteurs d'écran supportés) avant de chercher une solution à un comportement hors scope
- Un faux conflit de merge git peut venir d'un outil de build (watch Sass) qui recompile pendant un checkout, vérifier le `git diff` avant de croire à un vrai changement
- Relire le git log peut révéler une décision déjà tranchée puis défaite sans s'en rendre compte
- Ne jamais commiter le CSS compilé séparément de sa source Sass : compromis imposé par GitHub Pages ici, en agence c'est le CI/CD qui compile au push
- Squoosh : resize + export, toujours vérifier le format de sortie sélectionné avant de télécharger
- System.Drawing (PowerShell/.NET) ne sait pas lire le WebP, utiliser l'explorateur Windows (colonne Dimensions) ou Shell.Application en COM
- VS Code "le contenu du fichier est plus récent" pendant un merge : ne jamais cliquer "remplacer par mes changements" sans vérifier d'où vient la divergence
- Un commit `wip:` est une solution honnête et acceptée quand plusieurs sujets non terminés se mélangent en fin de session, pas un anti-pattern systématique

**Commande de détection de classes HTML sans règle CSS :**

powershell

```powershell
$htmlClasses = Get-ChildItem -Recurse -Include *.html | Select-String -Pattern 'class="([^"]*)"' -AllMatches | ForEach-Object {
    $_.Matches | ForEach-Object { $_.Groups[1].Value -split '\s+' }
} | Where-Object { $_ -ne '' } | Sort-Object -Unique

$cssContent = Get-Content .\assets\css\style.css -Raw

$htmlClasses | ForEach-Object {
    $pattern = "\." + [regex]::Escape($_) + "(?![\w-])"
    if ($cssContent -notmatch $pattern) { $_ }
}
```

Filtre manuel après coup : certains résultats sont des faux positifs légitimes.

**Commandes git du refactor par branche :**

powershell

```powershell
git checkout -b refactor/svg-icons
git checkout main
git merge refactor/svg-icons
```

**Recherche de répétitions avant de créer une mixin :**

powershell

```powershell
Select-String -Path .\sass\**\*.scss -Pattern "border-bottom"
Select-String -Path .\sass\**\*.scss -Pattern "::after"
Select-String -Path .\sass\**\*.scss -Pattern "display: flex" -Context 0,3
Select-String -Path .\sass\**\*.scss -Pattern "padding-right|padding-left"
(Select-String -Path .\sass\**\*.scss -Pattern "display: flex").Count
Select-String -Path .\**\*.html -Pattern "loading=\"lazy\""
```

`.\sass\**\*.scss` ne descend dans les sous-dossiers que si le globbing récursif est actif. Sinon, `Get-ChildItem -Recurse` est le filet de sécurité.

---

## 📚 Théorie non pratiquée

**Images** : AVIF (meilleur que WebP, `<picture>`) · `srcset` = inventaire de fichiers, `sizes` = contrainte de mise en page

**Responsive avancé** : Container queries (`@container`, `cqw`) · `min()`/`max()` · `max-width: 65ch` · `padding-inline: max(1.5rem, 5vw)` · `box-sizing: inherit`

**Layout** : Flexbox = 1D, Grid = 2D · stacking context implicite · `overflow: hidden` casse `box-shadow` et `position: sticky` des enfants · scroll horizontal sans barre visible

**Performance** : Reflow vs Repaint · `transform`/`opacity` traités GPU · INP < 200ms · PageSpeed Insights, WebPageTest, Yellow Lab Tools

**Accessibilité/archi** : `alt=""` pour décoratif · règle d'or ARIA · `%placeholder`+`@extend` déconseillé en Sass moderne · `@function` vs `@mixin`

**Lexique** : Fallback, Width Descriptor, Fluid Typography

**`pointer-events` "non composé"** selon Lighthouse : alternative à explorer, séparer la désactivation des clics du `@keyframes`

---

## 🧭 Bilan technique (synthèse)

### Erreurs fréquentes

Tailles fixes là où une taille responsive suffirait · confusion flex vs grid sur `justify-self`/`align-self`/`align-items` · arrondi px→rem trop agressif · confondre "le saut visuel existe" avec "`clamp()` en est la cause" · laisser le bilan diverger du code réellement commité sans revérification · mélanger spécificité CSS et priorité des attributs de présentation

### Ce que je maîtrise

BEM · Flexbox · Sass (7-1, mixins, `@for`, `@content`) · SVG inline (`<use>`, `currentColor`) · `srcset`/`sizes` · Git (branches, merge, diagnostic de faux conflit) · centrage selon le parent · diagnostic DevTools · lecture Lighthouse jusqu'aux causes réelles · animation Sass à délai échelonné · mécanique complète du cœur SVG

### À revoir

`transition`/`filter`/`outline` vs `display: block`/`role` · commandes git du merge mot par mot · flex/grid sur self/items · pattern `clamp() + width: 100%` · spécificité CSS vs attributs de présentation · `fill` vs `stroke` · critère LCP · calcul trigo (détail)

### Ce que j'ai découvert

`currentColor` · `fetchpriority`/`loading`/`sizes` · `clamp()` et interpolation linéaire · mixins/`%placeholder` · cascade CSS > attributs HTML · Force element state · id référencé vs matérialisé · conversion angle→coordonnées SVG · pièges `background-clip: text` et `:nth-child()` · `pointer-events` comme verrou indépendant de l'opacité · `-notmatch` PowerShell sur tableau · `animation-fill-mode`

---

!image.png
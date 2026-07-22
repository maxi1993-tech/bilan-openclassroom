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

- **Cadrage** · Swagger compris, arrêt backend connu, connecteur Figma opérationnel via copie de la maquette. Fiche de design tokens produite (`sophie-bluel-design-tokens.md`).

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

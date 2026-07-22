## 📝 Point de reprise

> Où j'en suis, en détail. La version courte est dans `ETAT.md` à la racine.

---

### Où j'en suis exactement

**Étape 4, filtre fonctionnel. Non terminée.**

- **Fait** · lignes 1, 2, 3 du pseudocode. Récupérer les boutons, écouter les clics, classe active par défaut sur `Tous`. Plus la restructuration du fichier en trois blocs et la gestion d'erreur.

- **Restant** · lignes 4, 5, 6 du pseudocode. Le détail cochable est dans la todo de `00-cadrage.md`, étape 4.

> **Le filtre ne filtre rien.** Le clic ne fait qu'un `console.log`.

---

### Prochaine action, dans cet ordre

1. Trancher le nom de `viewGallery` pour l'aligner sur les trois autres fonctions.

2. Retirer les cinq `console.log` de debug.

3. Lignes 4, 5, 6 du pseudocode. Mot-clé déjà donné pour la ligne 4 : `innerHTML`.

4. Exos hors projet à froid, dans cet ordre : `async / await` en priorité, puis `console.trace()`, `event.target`, `dataset`, paramètre de callback dans `forEach`.

5. Point à aborder avec Florian : le sentiment de ne pas m'approprier le code, et la dépendance à l'aide.

---

### Avant de coder

Relancer le backend · `cd Backend`, puis `npm start`. Sinon `fetch` échoue.

> Arrêt propre avec `Ctrl + C`, jamais à la croix. Sinon le processus survit et bloque le port 5678.

---

### État Git

> Dans `06-git.md`. Ne pas recopier ici.

---

### Historique du projet

- **Cadrage** · Swagger compris, arrêt backend connu, connecteur Figma opérationnel via copie de la maquette. Fiche de design tokens produite (`sophie-bluel-design-tokens.md`, dans le dépôt du projet P6, pas ici).

- **Notions découvertes en console, hors projet** · `fetch`, `forEach`, injection DOM, templates littéraux, `insertAdjacentHTML`, `for...of` contre `forEach`, ordre d'exécution du fetch, passage de valeur en paramètre.

- **Étape 2** · codée de bout en bout par moi, commitée et poussée (`2fd429c`). Contrôle de compréhension des étapes 0 à 2 validé.

- **RDV mentor** · orientation vers les templates littéraux et `insertAdjacentHTML`, et consigne de réduire la délégation à l'IA : plus de `console.log`, d'exos, de mots-clés, indices très courts. Prompt v7 produit en conséquence, barème d'indice à 5 niveaux, règle "notion qui ne passe pas", prompt réduit d'environ 40 %.

- **Étape 3** · conteneur `ul.filters` en dur, boutons générés depuis `/api/categories`, refactor en `fetchCategories` et `createButtons`, style sur classe dédiée, trois commits poussés.

- **Étape 4, ce qui est fait** · W3C sur `index.html` (0 erreur, 1 avertissement sur `#introduction`, code fourni OC), CSS validé 0 erreur, hashes de l'étape 3 relevés, pseudocode écrit, classe renommée `filter-button` dans le JS puis le CSS, `filter-button-selected` posée sur `Tous`, écouteurs branchés et vérifiés en console, lignes de debug retirées, écouteurs extraits dans `listenFilterButtons`, fichier réordonné, paramètre renommé `categories`, version `window load` du mentor testée puis écartée.

- **Étape 4, session du 22-07** · fichier restructuré en trois blocs, `fetch` des works enveloppé dans `viewGallery`, `try / catch` testé puis écarté, `.catch` posé sur les deux fetch, deux commits poussés. Blocage de deux sessions levé : l'ordre d'exécution asynchrone a été prouvé par observation, avec un repère de fin de fichier. À consolider à froid, sans bloquer l'étape.

- **Incidents résolus** · port 5678 occupé, diagnostiqué et résolu.

---

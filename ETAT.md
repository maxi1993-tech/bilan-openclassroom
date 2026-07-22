# État

*Régénéré par Claude en fin de session. À coller en Chat quand la question dépend du contexte.*

**Projet actif** : P6 Sophie Bluel, étape 4 (filtre fonctionnel), **non terminée**. Évaluation en soutenance.
**Validés** : P1 à P5.
**Git** : rien de commité sur l'étape 4. Modifications en attente dans `script.js` et `style.css`. Commit reporté volontairement, tant que le code n'est pas explicable.

**Fait sur l'étape 4** : W3C passé (0 erreur, 1 avertissement sur du code fourni OC), pseudocode écrit en 6 lignes, lignes 1 à 3 codées (boutons récupérés, clics écoutés, classe active par défaut sur `Tous`), écouteurs extraits dans `listenFilterButtons`, fichier réordonné, paramètre renommé `categories`.

**Restant** : lignes 4, 5, 6 du pseudocode. Vider la galerie, la reconstruire filtrée, déplacer la classe active. Le filtre ne filtre rien pour l'instant, le clic ne fait qu'un `console.log`.

**Blocage principal** : l'ordre d'exécution asynchrone. Chaque ligne est comprise isolément, l'assemblage ne l'est pas.

**Prochaine action, décidée en session**

1. Ne rien coder tant que l'asynchrone n'est pas compris.
2. Refaire seul le visuel de la chronologie (les deux versions côte à côte), en le construisant, pas en le lisant.
3. Exos dédiés hors projet, à froid : asynchrone, puis `event.target`, puis paramètre de callback dans `forEach`, puis `data-*` / `dataset`.
4. Seulement ensuite, lignes 4, 5, 6. Mot-clé déjà donné pour la ligne 4 : `innerHTML`.

**Dettes**

- `filterButtonSelected` déclarée dans `listenFilterButtons`, jamais utilisée (servira à la ligne 6).
- Vérifs non faites : navigation clavier, focus visible, contraste de l'état actif, axe DevTools.
- GitHub Pages KO : `index.html` est dans `FrontEnd/`, Pages pointe sur la racine.
- À aborder avec Florian : le sentiment de ne pas m'approprier le code, et la dépendance à l'aide.

**Avant de coder** : relancer le backend (`cd Backend`, `npm start`), sinon fetch échoue.

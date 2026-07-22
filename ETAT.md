# État

*Régénéré par Claude en fin de session. À coller en Chat quand la question dépend du contexte.*

**Projet actif** : P6 Sophie Bluel, étape 4 (filtre fonctionnel), **non terminée**. Évaluation en soutenance.
**Validés** : P1 à P5.
**Git** : tout commité et poussé. Derniers commits : `87ad631` (`wip:` réorganisation et gestion d'erreur), `b78f0d1` (renommage `filter-button`, écoute des clics).

**Fait sur l'étape 4** : lignes 1 à 3 du pseudocode, écouteurs extraits dans `listenFilterButtons`, fichier restructuré en trois blocs (constantes, déclarations, appels de lancement), `fetch` des works enveloppé dans `viewGallery`, `.catch` posé sur les deux fetch et vérifié back-end coupé.

**Restant** : lignes 4, 5, 6 du pseudocode. Vider la galerie, la reconstruire filtrée, déplacer la classe active. Le filtre ne filtre rien, le clic ne fait qu'un `console.log`.

**Blocage levé le 22-07** : l'ordre d'exécution asynchrone, prouvé par observation avec un repère de fin de fichier. Reste à consolider à froid, sans bloquer l'étape.

**Prochaine action**

1. Trancher le nom de `viewGallery`, qui ne suit pas le moule des trois autres fonctions.
2. Retirer les cinq `console.log` de debug.
3. Lignes 4, 5, 6 du pseudocode. Mot-clé déjà donné pour la ligne 4 : `innerHTML`.
4. Exos hors projet à froid : `async / await` en priorité 1, puis `console.trace()`, `event.target`, `dataset`, paramètre de callback dans `forEach`.

**Dettes**

- `filterButtonSelected` déclarée dans `listenFilterButtons`, jamais utilisée (servira à la ligne 6).
- Cinq `console.log` de debug dans le code commité, à retirer avant le commit de fin d'étape.
- Vérifs non faites : navigation clavier, focus visible, contraste de l'état actif, axe DevTools.
- GitHub Pages KO : `index.html` est dans `FrontEnd/`, Pages pointe sur la racine.
- À aborder avec Florian : le sentiment de ne pas m'approprier le code, et la dépendance à l'aide.

**Avant de coder** : relancer le backend (`cd Backend`, `npm start`), sinon fetch échoue. Arrêt avec `Ctrl + C`, jamais à la croix.

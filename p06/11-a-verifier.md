## 🔎 À vérifier

Relevé par Claude pendant le rangement de l'inbox. Faits observés uniquement, rien d'inventé.
Une ligne résolue est barrée, pas supprimée.

Format : `[date] type : constat → où` 

Types : `contradiction`, `savoir douteux`, `annoncé jamais fait`, `doublon`, `écart pratique pro`

---

### Relevé du 2026-07-21 (découpage de la fiche d'origine)

- `[2026-07-21] savoir douteux` : "maillon `.catch`, pas `try / catch` (qui va avec `async / await`)". `try / catch` n'est pas réservé à `async / await`, il fonctionne sur tout code synchrone. Ce qui est vrai : `try / catch` n'attrape pas le rejet d'une promesse dans une chaîne `.then`, parce que le rejet arrive après la sortie du bloc. Reformuler avec mes mots après vérification → `03-connaissances.md`, API & fetch

- `[2026-07-21] savoir douteux` : "`POST /api/users/login` renvoie `{ userId, token }` si OK, `404` sinon". Une API distingue en général utilisateur inconnu et mot de passe incorrect par deux codes différents. À retester dans Swagger avant de coder l'étape login, la checklist prévoit "affiche une erreur si KO" → `03-connaissances.md`, API & fetch

- `[2026-07-21] savoir douteux` : "Un `ul` n'accepte que des `li` comme enfants directs". La spec HTML autorise aussi `script` et `template`. La règle pratique reste bonne, la formulation absolue est fausse → `03-connaissances.md`, HTML & Sémantique

- `[2026-07-21] contradiction` : `map` est justifié finement dans les choix techniques ("`map` servirait si on voulait récupérer un tableau de résultats") mais classé "non assimilé, à reprendre à froid" dans la théorie non pratiquée. Les deux peuvent coexister, mais un jury qui lit le choix technique interrogera sur `map`. À traiter avant la soutenance → `05-bilan.md` et `03-connaissances.md`

- `[2026-07-21] annoncé jamais fait` : "Trancher le sort de la galerie de l'étape 2" est reporté sans décision depuis le point de reprise. Aucune trace de ce qui bloque → `10-point-de-reprise.md`

- `[2026-07-21] annoncé jamais fait` : `git diff` proposé avant le commit du CSS, écarté sur le moment, alors que le formatage automatique de l'éditeur avait déjà noyé un diff en P4. Le réflexe est écrit dans les connaissances mais n'a pas été appliqué → `02-bugs.md` et `03-connaissances.md`

- `[2026-07-21] doublon` : les justifications `forEach` contre `map` et `for...of` figurent en double, en tant que savoir dans les connaissances et en tant que décision dans les choix techniques. Acceptable si assumé, à ne pas laisser diverger : corriger les deux ou aucun → `03-connaissances.md` et `05-bilan.md`

- `[2026-07-21] écart pratique pro` : `.vscode/settings.json` laissé suivi par Git, marqué "choix assumé, question posée au mentor". La réponse du mentor n'est consignée nulle part → `05-bilan.md`, Setup et Git

### Relevé du 2026-07-21 (comparaison version 01 contre version 02)

- `[2026-07-21] perte de trace` : la version 01 gardait l'URL complète `GET http://localhost:5678/api/works` dans la chaîne `.then` type. La version 02 l'a raccourcie en `GET /api/works`. Le port 5678 reste documenté ailleurs (journal de bugs), donc rien d'utile n'est perdu, mais la fiche ne dit plus explicitement sur quelle machine tourne l'API → `03-connaissances.md`, API & fetch

- ~~`[2026-07-21] annoncé jamais fait` : la version 01 listait "Bouton `Tous` actif par défaut au chargement" comme tâche de l'étape 3. La version 02 déclare l'étape 3 terminée, et cette case reste non cochée.~~ **Résolu au delta étape 4** : classe `filter-button-selected` posée sur `Tous` à la génération.

- ~~`[2026-07-21] dette assumée` : la version 01 posait "Décider si la galerie est refactorée ou laissée en `createElement`". La question est reportée depuis deux versions sans décision.~~ **Tranché au delta étape 4** : les deux méthodes sont conservées volontairement, pour comparer. Décision assumée, à savoir défendre devant le jury.

### Relevé du 2026-07-21 (delta étape 4)

- `[2026-07-21] écart cadre pédagogique` : "Claude a donné le nom et la structure de la fonction à créer, ce que le prompt interdit sur du code OC évalué. Le cadre n'a pas tenu." Fait rapporté par Max lui-même. `listenFilterButtons` est donc dans le code sans avoir été trouvée. À réapprendre sur exo dédié avant la soutenance, sous peine de ne pas savoir défendre une fonction du livrable → `05-bilan.md`, Difficultés

- `[2026-07-21] formulation trompeuse` : dans les vérifications, la ligne "Les trois appels groupés en bas du fichier ne fonctionnent pas (testé, console muette)" est cochée `[x]`. Dans une checklist, `[x]` se lit "conforme". Un lecteur externe comprendra que le code ne fonctionne pas. Reformuler en "vérifié que les trois appels groupés en bas ne fonctionnent pas, preuve obtenue" → `05-bilan.md`, Vérification

- `[2026-07-21] doublon` : plusieurs notions figurent à la fois dans `🧠 Nouvelles connaissances` avec la mention "Vu, pas acquis" et dans `📚 Théorie non pratiquée` (paramètre de callback dans `forEach`, `dataset`, ordre asynchrone). Cohérent sur le fond, mais deux endroits à corriger le jour où la notion est acquise. Ne pas les laisser diverger → `03-connaissances.md`

- `[2026-07-21] à surveiller` : "je ne commite pas un code que je ne sais pas encore expliquer" est une bonne décision, mais l'étape 4 accumule des modifications non commitées dans `script.js` et `style.css`. Plus l'attente dure, plus le commit sera gros et difficile à découper en sujets uniques → `10-point-de-reprise.md`, État Git

### Relevé du 2026-07-21 (contrôle version 01 contre bilan final)

- ~~`[2026-07-21] perte de trace` : la version 01 nommait les quatre catégories réelles de l'API. Le bilan final ne les citait plus nulle part.~~ **Résolu au reformatage du 22-07** : section "Catégories du client" ajoutée dans `00-cadrage.md`, Specs techniques.


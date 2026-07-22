# Message pour la prochaine session Cowork

À coller tel quel en début de session.

---

```
Audit complet du dossier bilan-oc. Dans cet ordre, et sans rien sauter.

1. VÉRIFIER
Contrôle l'ensemble du dossier : CLAUDE.md, README.md, .gitignore, .gitattributes,
_scripts/, _template/, prompt-OC/, p01 à p12.
Cherche les erreurs et les incohérences : renvoi vers un fichier qui n'existe pas,
information écrite à deux endroits qui pourraient diverger, règle contredite ailleurs,
bloc déclaré quelque part et absent d'un autre, script qui perd du contenu.

Mesure, n'affirme pas. Lance les scripts, compare les sorties aux sources ligne à ligne,
compte. Une conclusion sans commande derrière ne vaut rien.

2. NOTER
Si l'organisation tient la route, note-la, puis note prompt-OC/prompt-oc-v8.md.

Avant de noter, cherche sur le web. Commence par vérifier la date du jour, ta date de
coupure de connaissances est antérieure et les recommandations ont pu changer depuis.
Cherche les bonnes pratiques Anthropic de prompt engineering en vigueur en 2026, sur
docs.claude.com et anthropic.com, y compris les pages propres au modèle en cours.
Ne note jamais de mémoire, et dis explicitement sur quelles pages tu t'appuies.

Donne une note chiffrée, ce qui la justifie, et ce qui manque pour la note maximale.
La dernière note attribuée était 8 sur 10, le 22 juillet 2026. Les deux points manquants
portaient sur le manque de diversité des exemples et sur des critères qui mesurent tous
la retenue, aucun la progression. Vérifie si c'est toujours vrai, ne le reprends pas
sans contrôle.

3. TA MISSION
Liste ta mission complète, en points courts et concis, un par ligne.

4. AXES D'AMÉLIORATION
Liste-les à titre indicatif, sans rien modifier. Classe-les par gravité.
Ne corrige rien à cette étape.

5. CE QUE JE DOIS FAIRE
Liste mes actions, dans l'ordre d'exécution, en séparant ce qui bloque
de ce qui peut attendre.

CONTRAINTES
- Réponses visuelles : tableaux et schémas plutôt que paragraphes.
- Jamais de tiret cadratin ni demi-cadratin.
- Avant d'annoncer qu'une suppression est réversible, vérifie avec git ls-files que le
  fichier est réellement suivi. Une erreur de ce type a déjà été commise le 22-07-2026.
- Les commandes git lancées depuis le sandbox laissent un .git/index.lock que je dois
  supprimer à la main. Limite-les, ou fais-les moi lancer dans PowerShell.
- Ne modifie rien sans me demander.
```

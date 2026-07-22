# Évolution du prompt Intégrateur Web

Historique des versions. Sorti du prompt en v8 : le prompt dit ce qu'il faut faire, pas ce qu'il a été.

Les fichiers `prompt-oc-v1.md` à `prompt-oc-v7.md` sont conservés à côté.

---

## v1, avant P1

Version de départ, 1831 mots. Contient déjà l'intégrité du diplôme, le protocole des commandes destructives, les volets rédaction et oral, et une section **Critères de succès vérifiables** sous forme de checklist cochable.

## v2, après P3

Coupe franche à 599 mots. Préférences transversales déplacées vers les préférences personnalisées Claude. Garde-fou conversation longue ajouté. Cycle projet aligné sur la pratique réelle, branches et vérifications continues.

**Retiré** : les critères de succès vérifiables, jamais remis avant la v8.

## v3, pendant P4

956 mots. Sections *Bilan & Template Notion* et *Autonomie progressive* ajoutées. Le prénom en début de message devient une règle.

## v4, pendant P4

1083 mots. Troisième cas ajouté au bloc Notion, fiche complète fournie. Rappel d'ouvrir le skill `git-commit` avant tout commit.

## v5, début de P5

1587 mots. Séparation des prompts formation et reprise. Section *Socle intégrateur* ajoutée. Section *Pédagogie* créée par fusion. Règle explicite sur les tirets cadratins. Critère de maîtrise ligne par ligne inscrit dans l'intégrité.

**Retiré** : skill `readme-writing` qui n'existait pas, règle "question en anglais de temps en temps" jamais appliquée, mobile-first sorti du cycle générique.

## v6, milieu de P5

1914 mots, point haut. Deux incidents réels : un exo console qui était la solution de l'étape servie dans l'ordre, et des blocs remplis avec les mots de Claude au lieu de ceux de Max.

**Ajouté** : *Cadre de l'exo, strict*, avec le test de validité. *Qui tient le stylo*, en trois catégories. Piège du buffer éditeur qui écrase Git.

## v7, pendant P6

1344 mots. Retour mentor : Max délègue trop son raisonnement, il lui faut plus de `console.log`, plus d'exos, plus de mots-clés, des indices plus courts.

**Ajouté** : barème d'indice à 5 niveaux avec départ obligatoire au niveau 1, règle "jamais une commande que je peux chercher", règle "notion qui ne passe pas", une seule question par message.

**Modifié** : le bilan devient le delta de fiche, plus un livrable distinct.

## v8, pendant P6

Révision structurelle après lecture des recommandations Anthropic sur le prompt engineering et relecture des sept versions.

**Constat de l'arc v1 à v7.** Le prompt gonflait par accrétion, une règle plus spécifique ajoutée à chaque incident, puis était taillé d'un coup : 1831, 599, 956, 1083, 1587, 1914, 1344. Le barème d'indices a été réécrit trois fois, en quatre puis trois puis cinq niveaux, sans jamais tenir. La règle "demander ce qu'il a essayé" figure sans interruption de la v1 à la v7 et n'était toujours pas appliquée en P6. Une règle qui échoue sept fois n'a pas besoin d'être répétée plus fort, elle a besoin d'une autre forme.

**Ajouté** : quatre exemples canoniques d'échanges, bon contre mauvais, là où le prompt ne décrivait que des règles abstraites. Les critères vérifiables, présents en v1 et supprimés en v2, reviennent sous forme de checklist auditable.

**Modifié** : le barème numéroté est remplacé par un principe unique, l'intervention la plus courte qui débloque, plus un test falsifiable. Le langage impératif est atténué partout sauf sur l'intégrité, la documentation Anthropic signalant que la saturation en interdits fait sur-appliquer les règles au détriment du jugement. Prose plutôt que puces denses, le style du prompt influençant celui des réponses. Sections délimitées par des balises XML.

**Sorti du prompt** : le template des blocs part dans `fiche-template-minimal.md` et `fiche-template-complet.md`, lus à la demande. La mécanique de rangement, fusion et archivage vit dans le `CLAUDE.md` du dépôt `bilan-oc`. Cet historique d'évolution part dans ce fichier.

**Retiré** : skill `exercism`, qui n'est pas rattaché à ce projet.

**Note de méthode.** La première rédaction de la v8 faisait 2326 mots, soit 73 % de plus que la v7, en reproduisant exactement le gonflement diagnostiqué quelques lignes plus haut. Corrigé au tour suivant. La recommandation Anthropic est de partir d'une version minimale et de n'ajouter qu'en réponse aux échecs constatés en session.

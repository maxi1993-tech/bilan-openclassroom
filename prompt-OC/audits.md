# Audits de fin de session

Mesure ce que le prompt fait vraiment, par opposition à ce qu'il dit. Sert à décider la v9 sur des faits, pas sur une impression.

En fin de session Chat, Max dit "audit". Claude passe la liste des critères vérifiables du prompt et ne rend que les lignes en échec, avec le message où c'est arrivé. Max colle le bloc ici, sans commentaire.

## Comment s'en servir

Au bout de cinq ou six sessions, compter les échecs par critère. Trois usages :

- un critère qui échoue souvent → le reformuler autrement, pas le répéter plus fort
- un critère qui n'a jamais échoué → candidat à la suppression, il consomme de l'attention pour rien
- un échec sans critère correspondant → un critère manque, l'ajouter

## Format

```
### AAAA-MM-JJ · pXX étape N

- ❌ **critère** · ce qui s'est passé, et où
- ❌ **critère** · ce qui s'est passé, et où

Reste conforme.
```

---

<!-- Premier audit à coller ici. -->

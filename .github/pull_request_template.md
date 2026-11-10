# <type>(<scope>) : <résumé court de la PR>

> Gabarit de pull request du dépôt, fourni par le skill `git-workflow`.

## Contexte

<Pourquoi cette PR ? Le problème, l'issue liée (Closes #123), le besoin.>

## Changements

- <Changement 1>
- <Changement 2>

## Comment tester

1. <Étapes pour reproduire / vérifier.>
2. <Commande de tests : ex. `make test`.>

## Points d'attention

- <Décision de conception, dette technique assumée, zone sensible.>

## Checklist

- [ ] La branche est à jour par rapport à `main` (rebase ou merge).
- [ ] Les commits suivent `type(scope): message` et sont atomiques.
- [ ] Les tests passent en local.
- [ ] Aucun secret, debug ou fichier généré n'est inclus.
- [ ] La documentation (README / référence) est à jour si nécessaire.
- [ ] L'issue liée est référencée (`Closes #…`).

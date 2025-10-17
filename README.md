# Répertoire pédagogique — usage d'UV et respect des standards PSR

## Objectif
- Ce dépôt sert uniquement à apprendre à utiliser UV et à appliquer les conventions PSR.
- Il n'est pas destiné à la production.

## Règles de branches et workflow
- Branches protégées : `main` et `dev` (aucun push direct).
- Nouveau travail : créer des branches de fonctionnalité nommées selon le format :
    - `feat/<slug>` (ex. : `feat/ajout-authentification`)
- Flux attendu :
    1. Développer sur `feat/<slug>`.
    2. Ouvrir une pull request (PR) vers `dev`.
    3. Effectuer revue et tests.
    4. Fusionner selon la politique de protection des branches.

## Conventions de code
- Respecter les recommandations PSR applicables (autoloading, style, namespaces, etc.).
- Ajouter commentaires/documentation et tests unitaires pour toute contribution.
- Suivre les bonnes pratiques de nommage et structuration des fichiers pour faciliter l'autoloading.
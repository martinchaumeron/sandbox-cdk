# Session 1 — CDK, première stack (17/09/2026)

## Objectif
Sortir du dev en console AWS : passer à une infra décrite en code,
versionnée, déployable en une commande.

## Fait
- Compte AWS perso (187478112166, eu-west-3), user IAM martin-dev, budget zero-spend
- Node installé sans droits admin (zip portable + PATH utilisateur)
- Stack CDK : Lambda (Python 3.12) + S3 + API Gateway
- Testée de bout en bout : HTTP → Lambda → écriture S3 → réponse
- Code poussé sur GitHub

## Ce qui a cassé, et pourquoi
1. **node introuvable** — pas d'admin sur le poste. Fix : zip portable dans
   ~/tools/node + ajout au PATH utilisateur (SetEnvironmentVariable "User").
   Le PATH n'est relu qu'au redémarrage complet de VS Code, pas du terminal.

2. **npm.ps1 non signé** — le zip téléchargé est marqué "venant d'internet".
   Fix : `Get-ChildItem -Recurse | Unblock-File`. Débloquer le .zip AVANT
   décompression évite le problème.

3. **aws configure a avalé mes commandes** — j'ai collé un bloc entier pendant
   qu'une commande interactive attendait des réponses ligne par ligne.
   Fix : `aws configure set <clé> <valeur> --profile sandbox`, non interactif.
   Règle : ne rien coller tant que le prompt PS n'est pas revenu.

4. **Bootstrap manquant** — `cdk bootstrap` est requis une fois par compte+région.

5. **Stack vide déployée sans erreur** — le plus important. J'avais édité app.py
   mais pas sandbox_cdk_stack.py, resté au squelette de `cdk init`. Le deploy a
   réussi et créé zéro ressource : une stack vide est un état valide, le CDK ne
   signale rien.
   → `cdk diff` AVANT chaque `cdk deploy`, systématiquement.

## Ce que je retiens
- Stack = unité de vie/mort. CloudFormation tient le registre de ce qu'elle a créé ;
  ce qui est créé à la main dans la console lui est invisible.
- `bucket.grant_put(fn)` génère la policy IAM minimale — gros gain vs console.
- `RemovalPolicy.DESTROY` + `auto_delete_objects` = bac à sable uniquement,
  jamais sur un bucket de prod.
- L'infra devient jetable parce qu'elle est reproductible.

## Bug d'ergonomie noté
Une clé AWS a été exposée en clair pendant la config → supprimée et recréée.
Réflexe : une secret key ne sort jamais de la machine.

## Prochaine session
Bundling Docker des dépendances Lambda (le vieux sujet lxml / PyPDF2).
Puis : deux environnements (dev/prod) dans la même stack, et tests
avec `assertions.Template.from_stack()`.

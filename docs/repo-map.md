# Carte du dépôt — Kindle Sustainability Project

> Générée par le skill `repo-cartography`. À lire en premier sur une nouvelle
> tâche, à mettre à jour (pas à reconstruire) quand le dépôt change.
> Dernière mise à jour : 2026-11-10

## Objectif

Guide et outillage pour « ressusciter » une liseuse **Kindle Basic 3 (KT4, 10ᵉ
génération)** sous firmware `5.18.1.1.1` : jailbreak (SpringBreak), déploiement
de KUAL + KOReader en mode *No-Framework*, et transfert de livres sans fil —
afin de réduire le gaspillage électronique en prolongeant la durée de vie de
l'appareil.

## Arborescence

- `README.md` — guide principal (payoff, procédure complète, dépannage).
- `guide.md` — manuel d'automatisation destiné à un agent CLI (spécifications, étapes shell).
- `kindle_drop/` — application web « Kindle Drop » (Flask) d'upload de livres vers la Kindle.
- `kindle_drop/templates/` — gabarit HTML (`index.html`) de l'interface Kindle Drop.
- `docs/` — documentation du dépôt (cette carte).

## Points d'entrée

- Lancer Kindle Drop : `./kindle_drop/run.sh` (ouvre `http://localhost:5050` ; crée `app_env/` et installe les deps).
- Lancer les tests : aucun test automatisé pour l'instant.
- Lint / format : non configuré.

## Conventions

- Style / formatage : Markdown pour la doc, Python 3 (PEP 8 implicite) pour l'app.
- Nommage : dossiers et fichiers en `snake_case` ; branche `<type>/<slug>` (kebab-case).
- Commits / branches : Conventional Commits `type(scope): message`, impératif, sans point final ; jamais de modification directe sur `main` (voir skill `git-workflow`).

## Dépendances clés

- `flask` — serveur web de l'interface Kindle Drop.
- `paramiko` — client SSH/SFTP vers le serveur Dropbear de KOReader.
- `qrcode[pil]` + `pillow` — génération du QR code pour l'upload depuis téléphone.

## Zones à éviter

- `app_env/` — environnement virtuel généré (voir `.gitignore`).
- `kindle_drop/config.json` — configuration locale (IP de la Kindle), ignorée par Git.
- `staged_packages/`, `kindle_payload/`, `*.bin`, `*.zip`, `*.tar.xz` — payloads binaires ignorés.

# om-editor

Application Python permettant de générer facilement des ordres de mission administratifs à partir de modèles Word.

Pensée initialement pour les élèves de l’ENSAI, l’application vise à simplifier la création et le remplissage des formulaires d’ordre de mission pour différents types de déplacements : stages, formations, conférences, représentation de l’école, missions professionnelles, etc.

Le projet repose sur une architecture simple et extensible basée sur Python, Streamlit et des modèles `.docx`.

---

# Fonctionnalités

- Génération automatique d’ordres de mission `.docx`
- Profils missionnaires sauvegardés
- Types de mission préconfigurés
- Préremplissage des informations récurrentes
- Interface Streamlit légère et simple d’utilisation

---

# Technologies utilisées

- Python
- Streamlit
- docxtpl
- python-docx
- PyYAML
- uv

---

# Installation

## 1. Cloner le dépôt

```bash
git clone https://github.com/<votre-utilisateur>/om-editor.git
cd om-editor
```

## 2. Installer les dépendances

Le projet utilise `uv` pour la gestion des dépendances.

```bash
uv sync
```

---

# Lancement

```bash
uv run streamlit run app.py
```

---

# Structure du projet

```text
om-editor/
├── app.py
├── pyproject.toml
├── templates/
├── generated/
├── data/
├── src/
└── tests/
```

---

# Configuration des profils

Le dossier `data/` est ignoré par Git afin de permettre à chaque utilisateur de conserver ses propres profils locaux.

Créer un fichier :

```text
data/profils.yaml
```

Exemple :

```yaml
default:
  nom: DUPONT
  prenom: Jean
  date_naissance: "2000-01-01"
  mail: jean.dupont@example.com
  telephone: ""
  adresse: ""
  code_postal: "00000"
  ville: Paris
  nationalite: Française
  profession: Étudiant
```

Ces profils permettent de préremplir automatiquement les informations du missionnaire.

---

# Configuration des types de mission

Créer un fichier :

```text
data/mission_types.yaml
```

Exemple :

```yaml
aucun:
  label: Aucun préremplissage
  motif: ""

stage:
  label: Stage
  motif: "Stage à préciser"

formation:
  label: Formation
  motif: "Participation à une formation"
```

---

# Génération des documents

Les documents générés sont enregistrés dans :

```text
generated/
```

Le dossier est ignoré par Git afin d’éviter de versionner des documents générés automatiquement.

---

# Roadmap

Fonctionnalités prévues :

- Export PDF
- Ajout dynamique d’étapes de trajet
- Validation automatique des champs
- Historique des missions
- Déploiement web léger

---

# Licence

Projet distribué sous licence GNU GPL v3.

Toute version modifiée ou redistribuée du projet doit également rester open source sous la même licence.
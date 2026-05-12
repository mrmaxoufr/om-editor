# om-editor

Application Python permettant de générer facilement des ordres de mission administratifs à partir de modèles Word.

Pensée initialement pour les élèves de l’ENSAI, l’application vise à simplifier la création et le remplissage des formulaires d’ordre de mission pour différents types de déplacements : stages, formations, conférences, représentation de l’école, missions professionnelles, etc.

Le projet repose sur une architecture simple et extensible basée sur Python, Streamlit et des modèles `.docx`, avec pour objectif de proposer :

- une génération rapide des documents ;
- un préremplissage intelligent des informations récurrentes ;
- une interface simple d’utilisation ;
- une automatisation des tâches administratives répétitives.

L’architecture du projet est conçue pour pouvoir être étendue à terme aux besoins du GENES, de l’INSEE ou plus largement de la fonction publique.

---

## Fonctionnalités prévues

- Génération automatique d’ordres de mission `.docx`
- Gestion de plusieurs types de missions
- Profils utilisateurs préremplis
- Export PDF
- Historique des missions
- Préremplissage intelligent des trajets et informations administratives
- Déploiement local ou serveur léger

---

## Technologies utilisées

- Python
- Streamlit
- docxtpl
- python-docx
- YAML / JSON

---

## Objectif du projet

Réduire le temps perdu à remplir manuellement des documents administratifs répétitifs et proposer un outil simple, moderne et open source.
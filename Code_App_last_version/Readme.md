# Projet de Géolocalisation et Visualisation sur Carte

Ce projet utilise des bibliothèques Python pour charger des données, géocoder des adresses et afficher des marqueurs sur une carte interactive.

## Prérequis

- Python 3.12 installé
- `conda` (optionnel mais recommandé) ou `venv` pour la gestion des environnements virtuels

## Installation

1. **Création d'un environnement virtuel avec Python 3.12 :**

   Avec Conda (recommandé) :
   ```bash
   conda create -n geo_env python=3.12 -y
   conda activate geo_env
   ```
   
    Avec Venv
    ```bash
    python3.12 -m venv geo_env
    source geo_env/bin/activate  # les systèmes hors windows
    .\geo_env\Scripts\activate # Sous Windows
    ```

2. **Installations des dépendances**
   ```bash
       pip install -r requirements.txt
    ```
## Lancement du projet
```bash
    python interface.py
   ```

## Description des fichiers
- **interface.py** : Classe principale pour lancer l’interface utilisateur.
- **requirements.txt** : Fichier contenant les dépendances Python nécessaires.
- **paths.py** : Définit le chemin d’accès aux données utilisées dans le projet.
- **app.py** : le système de recommandation(backend)
- **data** : Données recueillies sur **google Maps**
- **preprocessed_data** : Données nettoyées (*Ceux qui sont utilisées pour le système*)

## Notes
- Les fichiers de données doivent être placés dans les chemins spécifiés dans paths.py.
- lisez un identifiant d’utilisateur différent si vous rencontrez des erreurs liées à Nominatim.
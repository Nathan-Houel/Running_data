# 🏃‍♂️ Running Data Visualizer

Ce projet est un outil d'analyse de données de course à pied écrit en Python. Il permet de visualiser l'évolution de différentes métriques (Zones Cardiaques, Zones Aérobies, Cadence) à travers le temps via des graphiques interactifs générés avec `matplotlib`.

## 📋 Fonctionnalités

* [cite_start]**Analyse Cardio :** Visualisation des minutes passées en zones Aérobie, Seuil et Maximum[cite: 10].
* [cite_start]**Analyse Aérobie :** Suivi des zones Basse Aérobie, Haute Aérobie et Anaérobie[cite: 3].
* [cite_start]**Analyse Cadence :** Graphique coloré (heatmap) de la cadence (pas par minute/spm) au fil du temps[cite: 1].
* **Filtrage temporel :** Possibilité de voir les données depuis le début, par année (2023, 2024) ou par mois spécifique.
* **Gestion des données manquantes :** Le script remplit automatiquement les jours sans course pour garder une échelle de temps cohérente.

## 🛠️ Prérequis

* Python 3.x
* Librairie `matplotlib`

## 🚀 Installation

1.  **Cloner ou télécharger ce dossier** sur votre machine.

2.  **Configurer l'environnement virtuel** (recommandé) :
    Ouvrez un terminal dans le dossier du projet et exécutez :

    ```powershell
    # Création du venv
    python -m venv venv

    # Activation (Windows PowerShell)
    .\venv\Scripts\Activate
    ```

3.  **Installer les dépendances :**
    ```powershell
    pip install matplotlib
    ```

## 📂 Structure des données

Le programme attend trois fichiers `.txt` spécifiques dans le même répertoire que le script. **Les données doivent être séparées par des espaces.**

### 1. `Cardio_data.txt`
Contient les données de zones cardiaques.
**Format :** `Date Aerobic Threshold Maximum`
```text
Date Aerobic Threshold Maximum
23/09/23 32 18 0
24/09/23 6 8 2
...
# Sudoku Solver - Projet de Résolution de Sudoku avec Backtracking

Ce projet implémente un résolveur de Sudoku utilisant l'algorithme du backtracking et inclut une interface graphique avec Tkinter. Il permet de résoudre un Sudoku donné ou de générer des grilles de Sudoku partiellement résolues et à résoudre.

## Fonctionnalités

Résolution d'un Sudoku à l'aide de l'algorithme de backtracking.

Génération de Sudoku avec des cases vides pour les résoudre.

Interface graphique permettant de saisir manuellement des valeurs pour un Sudoku et de visualiser la grille.

Détection des carrés résolus et non résolus avec des bordures colorées.

## Prérequis

Avant de commencer, assurez-vous d'avoir les prérequis suivants installés sur votre machine :

Python 3.x (recommandé : 3.7+)

Tkinter (généralement installé par défaut avec Python)

Les bibliothèques suivantes (vous pouvez les installer avec pip si elles ne sont pas déjà installées) :

pip install random

### Installation

Clonez le dépôt sur votre machine locale :

git clone https://github.com/votre-utilisateur/votre-projet.git
cd votre-projet


Installez les dépendances si nécessaire (Python 3 devrait déjà avoir Tkinter installé par défaut, mais vous pouvez vérifier ou installer les dépendances via pip) :

pip install -r requirements.txt

## Structure du projet

Voici la structure du projet :

projet-sudoku/
│
├── src/
│   ├── sudokuGUI.py       # Interface graphique avec Tkinter
│   ├── Sudoku.py          # Logique du Sudoku (résolution et génération)
│   ├── Backtracking.py    # Implémentation de l'algorithme de backtracking
│   ├── Grille.py          # Gestion de la grille du Sudoku
│   ├── Game.py            # Logique du jeu et vérification des coups
│   └── CarreLatin.py      # Logique de génération des carrés latins
│
├── requirements.txt       # Liste des dépendances à installer
└── README.md              # Ce fichier

## Dépendances

Tkinter : utilisé pour l'interface graphique.

random : utilisé pour la génération aléatoire des Sudokus et des perturbations dans l'algorithme de recuit simulé.

Comment exécuter le projet

Lancer l'interface graphique :

Assurez-vous que vous êtes dans le répertoire src et que toutes les dépendances sont installées.

Exécutez le fichier sudokuGUI.py :

python sudokuGUI.py


Cela ouvrira une fenêtre Tkinter où vous pourrez :

Résoudre un Sudoku.

Générer un Sudoku partiellement résolu.

Visualiser les carrés résolus ou non résolus avec des bordures colorées.

Utilisation du Sudoku Solver

Saisie manuelle d'un Sudoku :

Vous pouvez entrer un Sudoku dans l'interface graphique, case par case.

Cliquez sur "Résoudre" pour résoudre le Sudoku avec l'algorithme de backtracking.

## Génération d'un Sudoku :

Cliquez sur "Générer" pour générer un Sudoku aléatoire avec des cases vides.

Le Sudoku généré peut être résolu en cliquant sur "Résoudre".

## Couleurs des carrés :

Les carrés résolus seront colorés en vert.

Les carrés non résolus auront une bordure rouge.

## Tests automatiques

Il existe une méthode de vérification automatique dans la classe Sudoku pour s'assurer que la grille est valide après la résolution :

sudoku.verifier_grille()  # Vérifie si la grille résolue est valide.

Cela garantit que les règles du Sudoku sont respectées après la résolution.




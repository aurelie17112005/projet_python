import random
import math
from CarreLatin import CarreLatin


class Sudoku:
    def __init__(self, n=9):
        self.n = n
        self.grille = [[0] * n for _ in range(n)]  # Initialiser une grille de n x n

    def solve(self):
        """Résout le Sudoku en utilisant le backtracking."""
        case_vide = self.recherche_premiere_case_vide()
        if not case_vide:
            return True  # Si plus de cases vides, le Sudoku est résolu
        row, col = case_vide

        for num in range(1, 10):  # Tester les chiffres de 1 à 9
            if self.isValidCoup(row, col, num):
                self.grille[row][col] = num
                if self.solve():
                    return True
                self.grille[row][col] = 0  # Annuler le coup et essayer le suivant

        return False  # Aucun coup valide trouvé, donc on échoue

    def isValidCoup(self, row, col, num):
        """Vérifie si le coup est valide (pas de doublon dans la ligne, la colonne et le sous-carré)."""
        for i in range(self.n):
            if self.grille[row][i] == num or self.grille[i][col] == num:
                return False

        start_row, start_col = (row // 3) * 3, (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.grille[start_row + i][start_col + j] == num:
                    return False
        return True

    def recherche_premiere_case_vide(self):
        """Retourne la première case vide dans la grille (si elle existe)."""
        for i in range(self.n):
            for j in range(self.n):
                if self.grille[i][j] == 0:
                    return i, j
        return None  # Si aucune case vide, retourne None

    def generate(self):
        """Génère un Sudoku valide avec des cases vides."""
        # Étape 1 : Résoudre le Sudoku (obtenir une grille complète valide)
        self.solve()

        # Étape 2 : Supprimer des cases pour rendre le Sudoku partiellement résolu
        holes = 40  # Nombre de cases à vider
        while holes > 0:
            row = random.randint(0, self.n - 1)
            col = random.randint(0, self.n - 1)

            # Ne pas effacer une case déjà vide
            if self.grille[row][col] != 0:
                backup = self.grille[row][col]
                self.grille[row][col] = 0  # Effacer la case

                # Vérifier si le Sudoku a toujours une solution unique
                grid_copy = [row[:] for row in self.grille]
                temp_sudoku = Sudoku(self.n)
                temp_sudoku.grille = grid_copy
                if temp_sudoku.solve():  # Vérifier qu'il existe une solution
                    holes -= 1
                else:
                    self.grille[row][col] = backup  # Restaurer la case si pas de solution unique

    def print_grille(self):
        for i in range(9):
            row = ""
            for j in range(9):
                if self.grille[i][j] == 0:
                    row += ". "
                else:
                    row += str(self.grille[i][j]) + " "
            print(row)

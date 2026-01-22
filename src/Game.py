from Grille import Grille
import random
import copy
class Game:
    def __init__(self, grille):
        self.grille = grille
        self.turn = 0
        self.score = 0
        self.finished = False

# faire une fonction append() pour ajouter le coup dans la grille (utilise la fonction isValidCoup)
    def append(self, valeur, x, y):
        if self.isValidCoup(valeur):
            self.grille[x][y] = valeur



# Vérifie si le coup est valide
    def isValidCoup(self, row, col, num):
        if num in self.grille.grid[row]:
            return False
        for i in range(9):
            if self.grille.grid[i][col] == num:
                return False
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.grille.grid[start_row + i][start_col + j] == num:
                    return False
        return True


        # Vérifie si la grille a une solution unique
    def count_solutions(self):
        def solve_count(grille):
            for i in range(9):
                for j in range(9):
                    if grille[i][j] == 0:
                        count = 0
                        for num in range(1, 10):
                            if self.isValidCoup_grille(grille, i, j, num):
                                grille[i][j] = num
                                count += solve_count(grille)
                                grille[i][j] = 0
                                if count > 1:
                                    return count
                        return count
            return 1  # grille complète = 1 solution

        grille_copy = copy.deepcopy(self.grille)
        return solve_count(grille_copy)

        # Version isValid pour une grille donné
    def isValidCoup_grille(self, grille, row, col, num):
        if num in grille[row]:
            return False
        for i in range(9):
            if grille[i][col] == num:
                return False
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if grille[start_row + i][start_col + j] == num:
                    return False
        return True

        # Supprimer des cases pour générer un Sudoku à résoudre
    def make_puzzle(self, holes=40):
        # holes = nombre de cases vides souhaitées
        attempts = holes
        while attempts > 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if self.grille[row][col] != 0:
                backup = self.grille[row][col]
                self.grille[row][col] = 0
                if self.count_solutions() != 1:
                    # remettre le chiffre si la solution n'est plus unique
                    self.grille[row][col] = backup
                else:
                    attempts -= 1

        # Affichage de la grille

    def print_grille(self):
        for i in range(9):
            row = ""
            for j in range(9):
                if self.grille[i][j] == 0:
                    row += ". "
                else:
                    row += str(self.grille[i][j]) + " "
            print(row)





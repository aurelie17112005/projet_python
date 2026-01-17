from Grille import Grille
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





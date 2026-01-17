from Game import Game
class Backtracking:
    def __init__(self, grille):
        self.grille = grille

    def recherche_premiere_case_vide(self):
        for row in range(9):
            for col in range(9):
                if self.grille.grid[row][col] == 0:
                    return row, col
        return None

    def backtracking(self):
        case = self.recherche_premiere_case_vide()
        if case is None:
            return True
        row, col = case
        for chiffre in range(1, 10):
            if Game.isValidCoup(row, col, chiffre):
                self.grille.grid[row][col] = chiffre
                if self.backtracking():
                    return True
                self.grille.grid[row][col] = 0
        return False


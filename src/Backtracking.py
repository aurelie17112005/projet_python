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

    def get_possibilities(self, row, col):
        if self.grille[row][col] != 0:
            return []
        possibles = []
        for num in range(1, 10):
            if Game.isValidCoup(row, col, num):
                possibles.append(num)
        return possibles

    def find_best_empty_cell(self):
        best_cell = None
        best_possibilities = None
        for row in range(9):
            for col in range(9):
                if self.grille[row][col] == 0:
                    possibilities = self.get_possibilities(row, col)
                    if len(possibilities) == 0:
                        return None, None
                    if best_possibilities is None or len(possibilities) < len(best_possibilities):
                        best_cell = (row, col)
                        best_possibilities = possibilities
        return best_cell, best_possibilities

    def solve_with_constraints(self):
        cell, possibilities = self.find_best_empty_cell()
        if cell is None:
            return True
        row, col = cell
        for num in possibilities:
            self.grille[row][col] = num
            if self.solve_with_constraints():
                return True
            self.grille[row][col] = 0
        return False





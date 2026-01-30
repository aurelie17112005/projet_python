from Game import Game  # Assurez-vous que Game est bien importé

class Backtracking:
    def __init__(self, sudoku):
        self.grille = sudoku.grille  # Utilisation de self.grille (la grille du Sudoku)

    def recherche_premiere_case_vide(self):
        for row in range(9):
            for col in range(9):
                if self.grille[row][col] == 0:
                    return row, col
        return None

    def backtracking(self):
        case = self.recherche_premiere_case_vide()
        if case is None:
            return True
        row, col = case
        for chiffre in range(1, 10):
            # Créer une instance de Game pour valider le coup avec la grille actuelle
            game = Game(self.grille)
            if game.isValidCoup(row, col, chiffre):  # Vérifier si le coup est valide
                self.grille[row][col] = chiffre
                if self.backtracking():
                    return True
                self.grille[row][col] = 0  # Annuler si pas de solution trouvée
        return False

    def isValidCoup(self, row, col, num):
        # Vérifier si le coup est valide pour une case donnée (pas de doublons dans la ligne, la colonne et le sous-carré)
        for i in range(9):
            if self.grille[row][i] == num or self.grille[i][col] == num:
                return False

        start_row, start_col = (row // 3) * 3, (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.grille[start_row + i][start_col + j] == num:
                    return False
        return True

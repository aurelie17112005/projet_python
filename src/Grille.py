import random
from Game import Game


class Grille:

    def __init__(self, taille = 9):
        self.board = []
        for i in range(taille):
            self.board.append([])
            for j in range(taille):
                self.board[i].append(0)

    def fill_grid(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    chiffres = list(range(1, 10))
                    random.shuffle(chiffres)
                    for num in chiffres:
                        game = Game(self.board)
                        if game.isValidCoup(i, j, num):
                            self.board[i][j] = num
                            if self.fill_grid():
                                return True
                            self.board[i][j] = 0  # backtrack
                    return False
        return True

    def to_string(self):
        display = ""

        for i in range(len(self.board)):
            display += str(self.board[i])
            if self.board[i] % 9 == 0:
                display += "\n"

        return display
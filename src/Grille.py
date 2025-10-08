import random


class Grille:

    def __init__(self, taille = 9):
        self.board = []
        for i in range(taille):
            self.board.append([])
            for j in range(taille):
                self.board[i].append()

    def populate(self, taille):
        nbInsert = 0
        nbCarre = 1
        for i in range(3 * nbCarre):
            if nbCarre == taille/3+1:
                break
            else:
                for j in range(3 * nbCarre):
                    if nbInsert == 9:
                        break
                    else:
                        nbInsert = nbInsert + 1
                        self.board[i] = random.randint(1, 9)

    def toString(self):
        display = ""

        for i in range(len(self.board)):
            display += str(self.board[i])
            if (self.board[i] % 9 == 0):
                display += "\n"

        return display
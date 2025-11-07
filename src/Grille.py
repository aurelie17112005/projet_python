import random


class Grille:

    def __init__(self, taille = 9):
        self.board = []
        for i in range(taille):
            self.board.append([])
            for j in range(taille):
                self.board[i].append(0)

    def populate_grille(self, taille):
        nb_insert = 0
        nb_carre = 1
        for i in range(3 * nb_carre):
            if nb_carre == taille/3+1:
                break
            else:
                for j in range(3 * nb_carre):
                    if nb_insert == 9:
                        break
                    else:
                        nb_insert = nb_insert + 1
                        self.board[i] = random.randint(1, 9)


    def to_string(self):
        display = ""

        for i in range(len(self.board)):
            display += str(self.board[i])
            if self.board[i] % 9 == 0:
                display += "\n"

        return display
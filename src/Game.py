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

# faire une fonction pour récupérer les coordonnées (x,y) du coup
    def getXCoup(self, coup):
        for i in range(1, self.grille.len()):
            if self.grille[i] == coup:
                    return i

    def getYCoup(self, coup):
        for i in range(1, self.grille.len()):
            for j in range(1, self.grille[i].len()):
                if self.grille[i][j] == coup:
                    return j

# faire une fonction pour récupérer le chiffre à une coordonnée donnée (peut être pas utile)

# Vérifie si le coup est valide
    def isValidCoup(self, coup):
        for i in range(9):
            if coup in self.grille[i]:
                return False
            for j in range(9):
                if coup in self.grille[self.getXCoup(coup)][j]:
                    return False
        blocs = []
        for bi in range(0, 9, 3):
            for bj in range(0, 9, 3):
                bloc = [self.grille[i][bj:bj + 3] for i in range(bi, bi + 3)]
                blocs.append(bloc)
        # pour vérifier pour le carré -> prendre les coordonnées du coup puis ajouté 3 au x et 3 au y pour vérifier les nombre autour de lui
        return True




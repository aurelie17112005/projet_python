class Game:
    def __init__(self, grille):
        self.grille = grille
        self.turn = 0
        self.score = 0
        self.finished = False

# faire une fonction append() pour ajouter le coup dans la grille (utilise la fonction isValidCoup)

# faire une fonction pour récupérer les coordonnées (x,y) du coup

# faire une fonction pour récupérer le chiffre à une coordonnée donnée (peut être pas utile)

    def isValidCoup(self, coup):
        for i in range(9):
            if coup in self.grille[i]:
                return False
            for j in range(9):
                if coup in self.grille[0][j]: # remplacer le 0 par la coordonnée du coup
                    return False
        # pour vérifier pour le carré -> prendre les coordonnées du coup puis ajouté 3 au x et 3 au y pour vérifier les nombre autour de lui
        return True




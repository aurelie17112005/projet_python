import random
from CarreLatin import CarreLatin

class Sudoku :
    def __init__(self):
        self.grille = []

    def sous_carre_est_complet(self, ligne, col):
        nombres = set()

        for i in range(ligne, ligne + 3):
            for j in range(col, col + 3):
                nombres.add(self.grille[i][j])

        return nombres == set(range(1, 10))


    def sont_compatibles(self, carres=None):
        if carres is None:
            carres = []
            candidats = CarreLatin.generer_carres_latins_backtracking(3)
            for _ in range(3):
                carres.append(random.choice(candidats))

        c1, c2, c3 = carres

        # On vérifie pour chaque ligne locale i, les 3 lignes contiennent 9 valeurs distinctes
        for i in range(3):
            ligne = c1[i] + c2[i] + c3[i]
            if len(set(ligne)) != 9:
                break
        else:
            return True

        # On vérifie pour chaque colonne locale j la colonne globale contient 9 valeurs distinctes
        for j in range(3):
            colonne = [
                c1[0][j], c1[1][j], c1[2][j],
                c2[0][j], c2[1][j], c2[2][j],
                c3[0][j], c3[1][j], c3[2][j]
            ]
            if len(set(colonne)) != 9:
                break
        else:
            return True

        return False

    def est_sudoku_valide(self, grille):
        attendu = set(range(1, 10))

        # Vérif des lignes
        for i in range(9):
            if set(grille[i]) != attendu:
                return False

        # Vérif des colonnes
        for j in range(9):
            colonne = {grille[i][j] for i in range(9)}
            if colonne != attendu:
                return False

        # Vérif des blocs
        blocs = []
        for bi in range(0, 9, 3):
            for bj in range(0, 9, 3):
                bloc = [grille[i][bj:bj + 3] for i in range(bi, bi + 3)]
                blocs.append(bloc)

        return True

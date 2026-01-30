class CarreMagic:


    # Ceci est la methode Siam, si il y a le temps, implémenter : méthode LUX, progression arithmétiques,
    # permutation et transformation, combinatoires et géométriques
    def __init__(self, p):
        """p est le paramètre pour calculer la taille de la matrice"""
        self.p = p
        taille = p*2+1
        self.grille = []
        coef = 0
        for i in range(taille):
            self.grille.append([])
            for j in range(taille):
                self.grille[i].append(coef)
        nb_cases = taille**2
        i = 0
        j = (p*2+1)//2
        for coef in range(1, nb_cases + 1):
            self.grille[i][j] = coef

            next_i = (i - 1) % taille
            next_j = (j + 1) % taille

            if self.grille[next_i][next_j] != 0:
                i = (i + 1) % taille
            else:
                i = next_i
                j = next_j

    def est_magic(self):
        taille = self.p * 2 + 1
        somme_magique = taille * (taille ** 2 + 1) // 2  # entier

        # Lignes
        for ligne in self.grille:
            if sum(ligne) != somme_magique:
                return False

        # Colonnes
        for j in range(taille):
            if sum(self.grille[i][j] for i in range(taille)) != somme_magique:
                return False

        # Diagonale (0,0) (1,1) (2,2) etc
        if sum(self.grille[i][i] for i in range(taille)) != somme_magique:
            return False

        # Diagonale (0,n) (1,n-1) (2,n-2) etc
        if sum(self.grille[i][taille - 1 - i] for i in range(taille)) != somme_magique:
            return False

        return True

    def to_string(self):
        result = []
        for ligne in self.grille:
            result.append(" ".join(f"{val:^2}" for val in ligne))
        return "\n".join(result)

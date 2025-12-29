from itertools import product

class CarreLatin:
    def __init__(self, n):
        """Construit un carré latin canonique de taille n."""
        self.n = n
        self.grille = []

        ligne0 = list(range(1, n + 1))

        # Chaque ligne est une rotation de la précédente
        for i in range(n):
            ligne = ligne0[i:] + ligne0[:i]
            self.grille.append(ligne)

    def est_latin(self):
        nombres = set(range(1, self.n + 1)) # set de 1 à la taille n

        # Vérifier les lignes si un nombre apparait plusieurs fois en comparant les sets
        for ligne in self.grille:
            if set(ligne) != nombres:
                return False

        # Vérifier les colonnes
        for j in range(self.n):
            colonne = {self.grille[i][j] for i in range(self.n)}
            if colonne != nombres:
                return False
        return True

    @staticmethod
    def est_latin_matrice(matrice):
        """Teste si une matrice est un carré latin."""
        n = len(matrice)
        symboles = set(range(1, n + 1))

        # Vérification des lignes
        for ligne in matrice:
            if set(ligne) != symboles:
                return False

        # Vérification des colonnes
        for j in range(n):
            colonne = {matrice[i][j] for i in range(n)}
            if colonne != symboles:
                return False

        return True

    @staticmethod
    def generer_matrices_candidates(n):
        """
        Génère tous les carrés latins d'ordre n. Pour n=4, 4^16=4 294 967 296 candidates...
        """
        valeurs = list(range(1, n + 1))
        matrices = []

        # Produit cartésien de n^2 positions
        for comb in product(valeurs, repeat=n * n):
            # Transformer la liste en matrice n×n
            m = [
                list(comb[i * n:(i + 1) * n])
                for i in range(n)
            ]
            matrices.append(m)

        return matrices

    @staticmethod
    def filtrer_latins(matrices):
        latins = []

        for m in matrices:
            if  CarreLatin.est_latin_matrice(m):
                latins.append(m)
        return latins

    @staticmethod
    def to_string_matrice(m):
        for ligne in m:
            print(" ".join(f"{val:^2}" for val in ligne))

    @staticmethod
    def generer_carres_latins_backtracking(n):
        # Grille vide n×n initialisée à 0
        # Chaque case sera remplie progressivement par le backtracking
        grille = [[0] * n for _ in range(n)]

        # Liste où seront stockés tous les carrés latins trouvés
        resultats = []

        def est_valide(i, j, val):
            """
            Vérifie si la valeur 'val' peut être placée en position (i, j)
            sans violer les règles d'un carré latin :
            - pas de répétition dans la ligne i
            - pas de répétition dans la colonne j
            """
            # Vérification de la ligne i
            if val in grille[i]:
                return False

            # Vérification de la colonne j
            for k in range(n):
                if grille[k][j] == val:
                    return False

            return True

        def backtrack(i, j):
            """
            Remplit la grille case par case.
            - i : index de ligne
            - j : index de colonne
            Quand la grille est entièrement remplie, on ajoute une copie au résultat.
            """

            # Si on a rempli toutes les lignes, la grille est complète
            if i == n:
                # On ajoute une copie profonde pour éviter les effets de bord
                copie = [ligne[:] for ligne in grille]
                resultats.append(copie)
                return

            # Calcul de la prochaine case (ni, nj)
            # On avance colonne par colonne, puis on passe à la ligne suivante
            ni = i + (j + 1) // n
            nj = (j + 1) % n

            # Essai de toutes les valeurs possibles de 1 à n
            for val in range(1, n + 1):
                if est_valide(i, j, val):
                    # On place la valeur
                    grille[i][j] = val

                    # On continue le remplissage
                    backtrack(ni, nj)

                    # On retire la valeur (backtracking)
                    grille[i][j] = 0

        # Lancement du backtracking à partir de la case (0, 0)
        backtrack(0, 0)

        return resultats

    def to_string(self):
        for ligne in self.grille:
            print(" ".join(f"{val:^2}" for val in ligne))
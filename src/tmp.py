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

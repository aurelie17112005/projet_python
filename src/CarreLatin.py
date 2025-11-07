class CarreLatin:
    def __init__(self):
        self.grille = []

    def permutations_recursives(self, liste):
        if len(liste) <= 1:
            return [liste]

        permutations = []

        for i in range(len(liste)):
            #[1, 2, 3] -> slicer 1 -> reste = [2, 3], permuter [2, 3] en [3, 2] -> Liste[i] (qui est 1 ) + reste qui a été permuté.
            #donne [1, 2 ,3]. Puis i = 1 donc on slice 2, permute 1 et 3, ce qui donne [3, 1] et qu'on ajoute à 2 ce qui donne [2, 1, 3]
            # et ainsi de suite...
            reste = liste[:i] + liste[i + 1:] #pour i = 0, liste[:0] est vide
            for p in self.permutations_recursives(reste):
                permutations.append([liste[i]] + p)

        return permutations

    def permutations_iteratives(self, iterable, r = None):
        #permutations('ABCD', 2) → AB AC AD BA BC BD CA CB CD DA DB DC
        #permutations(range(3)) → 012 021 102 120 201 210
        #Exemple dans itertools.
        return None

from CarreMagic import CarreMagic
from CarreLatin import CarreLatin


"""
c = CarreMagic(4)
c.afficher()
print("taille :")
print((2*2+1)**2)
print(c.verifier_magic())"""

matrices = CarreLatin.generer_matrices_candidates(4)
print("Nombre de matrices générées :" + str(len(matrices)))

latins = CarreLatin.filtrer_latins(matrices)
print("Nombre de carrés latins (méthode brute force) : " + str(len(latins)))

for l in latins:
    CarreLatin.to_string_matrice(l)
    print("-------")

latins = CarreLatin.generer_carres_latins_backtracking(4)
print("Nombre de carrés latins (méthode par backtracking) : " + str(len(latins)))

for l in latins:
    CarreLatin.to_string_matrice(l)
    print("-------")
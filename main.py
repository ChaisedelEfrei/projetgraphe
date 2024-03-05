from creation_matrice import creation_matrice
from verification_matrice import verification_matrice
from affichage_matrice import afficher_matrice

# Appel de la fonction lecture_fichier avec le nom du fichier
nom_fichier = "contraintes1.txt"
matrice_resultat = creation_matrice(nom_fichier)
print("\nLe tableau de contraintes est en mémoire\n")

# Affichage du tableau résultat
for ligne in matrice_resultat:
    print(ligne)

# Vérification de la matrice
print("\n"+verification_matrice(matrice_resultat)+"\n")

# Affichage de la matrice des valeurs
afficher_matrice(matrice_resultat)

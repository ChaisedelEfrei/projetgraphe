from creation_matrice import creation_matrice

# Appel de la fonction lecture_fichier avec le nom du fichier
nom_fichier = "contraintes1.txt"
tableau_resultat = creation_matrice(nom_fichier)

# Affichage du tableau résultat
for ligne in tableau_resultat:
    print(ligne)

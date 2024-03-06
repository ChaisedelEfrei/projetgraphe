def afficher_matrice(graphe):
    # Déterminer le nombre de sommets dans le graphe
    nb_sommets = len(graphe)-1

    # Initialiser la matrice avec des valeurs '*' pour représenter les arcs manquants
    matrice = [['*' for _ in range(nb_sommets + 1)] for _ in range(nb_sommets + 1)]

    # Remplir la matrice avec les valeurs des arcs
    for ligne in graphe:
        sommet = ligne[0]
        predecesseurs = ligne[2:]

        for pred in predecesseurs:
            valeurs_arcs = graphe[pred][1]
            matrice[pred][sommet] = valeurs_arcs

    # Afficher la matrice des valeurs
    print("Matrice des valeurs")
    print("    ", end="")
    for i in range(nb_sommets + 1):
        print(f"{str(i).center(3)}", end="")
    print()
    for i in range(nb_sommets + 1):
        print(f"{str(i).center(3)} ", end="")
        for j in range(nb_sommets + 1):
            print(f"{str(matrice[i][j]).center(3)}", end="")
        print()

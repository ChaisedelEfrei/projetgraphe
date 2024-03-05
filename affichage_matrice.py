def afficher_matrice(graphe):
    # Déterminer le nombre de sommets dans le graphe
    nb_sommets = len(graphe)

    # Initialiser la matrice avec des valeurs '*' pour représenter les arcs manquants
    matrice = [['*' for _ in range(nb_sommets + 1)] for _ in range(nb_sommets + 1)]

    # Remplir la matrice avec les valeurs des arcs
    for ligne in graphe:
        sommet = ligne[0]
        valeurs_arcs = ligne[1]
        predecesseurs = ligne[2:]

        for pred in predecesseurs:
            matrice[pred][sommet] = pred

    # Afficher la matrice des valeurs
    print("Matrice des valeurs")
    print(" ", end="")
    for i in range(nb_sommets + 1):
        print(f"{i:3}", end="")
    print()
    for i in range(nb_sommets):
        print(f"{i:2} ", end="")
        for j in range(nb_sommets + 1):
            print(f"{matrice[i][j]:3}", end="")
        print()

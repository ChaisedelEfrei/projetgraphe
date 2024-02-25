def creation_matrice(file_name):
    tableau = []
    with open(file_name, 'r') as file:
        for line in file:
            # Séparation des valeurs sur chaque ligne
            values = line.strip().split()
            # Conversion des valeurs en entiers
            values = [int(val) for val in values]
            # Extraction de la première et deuxième valeur
            premiere_valeur = values[0]
            deuxieme_valeur = values[1]
            # Extraction des valeurs suivantes
            suivantes_valeurs = values[2:]
            # Ajout des valeurs dans le tableau
            tableau.append([premiere_valeur, deuxieme_valeur, suivantes_valeurs])

    # Calcul des successeurs d'alpha donc trouver les premiere_valeur de ceux qui n'ont pas de suivantes_valeurs
    successeurs_a = []
    for ligne in tableau:
        if len(ligne[2]) == 0:  # Vérifier si la liste de successeurs est vide
            ligne[2] = 0
            successeurs_a.append(ligne[0])

    # Ajouter la ligne alpha avant la première ligne du tableau
    tableau.insert(0, [0, 0, successeurs_a])

    # Calcul des prédécesseurs d'oméga
    # donc trouver les premiere_valeur qui n'apparaissent jamais dans les suivantes_valeurs

    premiere_valeur_set = set()
    suivantes_valeurs_set = set()

    # Remplir la liste de toutes les premiere_valeur
    for i in range(len(tableau)):
        premiere_valeur_set.add(i)
    # Remplir la liste de toutes les suivantes_valeurs
    for ligne in tableau:
        if type(ligne[2]) is list:  # Vérifie s'il y a des suivantes_valeurs dans la ligne
            suivantes_valeurs_set.update(ligne[2])  # Ajoute les suivantes_valeurs à l'ensemble
            # (cas où ligne[2] est une liste)
        else:
            suivantes_valeurs_set.add(ligne[2])  # Ajoute la suivantes_valeurs à l'ensemble
            # (cas où ligne[2] est un int)

    # Retirer les premiere_valeur qui apparaissent dans les suivantes_valeurs
    predecesseurs_o = premiere_valeur_set - suivantes_valeurs_set
    predecesseurs_o = list(predecesseurs_o)

    # Ajouter la ligne omega après la dernière ligne du tableau
    tableau.append([len(tableau), 0, predecesseurs_o])

    return tableau

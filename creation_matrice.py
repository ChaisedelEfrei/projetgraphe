def creation_matrice(file_name):
    tableau = []
    with open(file_name, 'r') as file:
        for line in file:
            # Séparation des valeurs sur chaque ligne
            values = line.strip().split()
            # Conversion des valeurs en entiers
            values = [int(val) for val in values]
            # Extraction des valeurs :
            tableau.append(values)

# Calcul des successeurs d'alpha donc trouver les premiere_valeur de ceux qui n'ont pas de suivantes_valeurs
    for ligne in tableau:
        if len(ligne) == 2:  # Vérifier si la liste de successeurs est vide
            ligne.append(0)

    # Ajouter la ligne alpha avant la première ligne du tableau
    tableau.insert(0, [0, 0])

    # Calcul des prédécesseurs d'oméga
    # donc trouver les premiere_valeur qui n'apparaissent jamais dans les suivantes_valeurs

    premiere_valeur_set = set()
    suivantes_valeurs_set = set()

    # Remplir la liste de toutes les premiere_valeur
    for j in range(len(tableau)):
        premiere_valeur_set.add(j)
    # Remplir la liste de toutes les suivantes_valeurs
    for ligne in tableau:
        for valeur in ligne[2:]:
            suivantes_valeurs_set.add(valeur)

    # Retirer les premiere_valeur qui apparaissent dans les suivantes_valeurs
    predecesseurs_o = premiere_valeur_set - suivantes_valeurs_set

    # Ajouter la ligne omega après la dernière ligne du tableau
    tableau.append([len(tableau), 0])
    for k in predecesseurs_o:
        tableau[len(tableau)-1].append(k)

    return tableau

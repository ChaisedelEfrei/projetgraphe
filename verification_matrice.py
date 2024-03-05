def verification_matrice(matrice):
    if circuit(matrice) is False and arc_valeur_neg(matrice) is False:
        return "Le graphe respecte les conditions"
    elif circuit(matrice) is True and arc_valeur_neg(matrice) is False:
        return "Le graphe contient au moins un circuit"
    elif circuit(matrice) is False and arc_valeur_neg(matrice) is True:
        return "Le graphe contient au moins un arc à valeur négative"
    else:
        return ("Le graphe ne respecte aucune des deux conditions, il contient au moins un circuit "
                "et au moins un arc à valeur négative")


def circuit(graphe):
    def dfs(sommet_dfs, visite_dfs):
        visite_dfs[sommet_dfs] = True
        for successeur in graphe[sommet_dfs][2:]:
            if visite_dfs[successeur]:
                return True
            if dfs(successeur, visite_dfs):
                return True
        visite_dfs[sommet_dfs] = False
        return False

    for sommet in range(len(graphe)):
        visite = [False] * len(graphe)
        if dfs(sommet, visite):
            return True
    return False


# Fonction vérifiant si la valeur de l'arc est négative ou non
def arc_valeur_neg(tableau):
    for ligne in tableau:
        if ligne[1] < 0:
            # alors, il y a au moins un arc à valeur négative
            return True
    # alors, il n'y a pas d'arc à valeur négative
    return False

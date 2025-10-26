import heapq

graphe = {
    "A": [("B", 4), ("C", 2)],
    "B": [("C", 5), ("D", 10)],
    "C": [("E", 3)],
    "D": [("F", 11)],
    "E": [("D", 4)],
    "F": []
}

def dijkstra(graphe, depart, arrivee):
    # Initialisation des distances
    distances = {}
    for ville in graphe:
        distances[ville] = 1000000000  # très grand nombre pour infini
    distances[depart] = 0

    # Pour reconstruire le chemin
    predecesseurs = {}
    for ville in graphe:
        predecesseurs[ville] = None

    # Tas pour gérer les villes à explorer
    tas = []
    heapq.heappush(tas, (0, depart))  # on ajoute la ville de départ vec distance de 0

    # Boucle principale
    while len(tas) > 0:
        distance_actuelle, ville = heapq.heappop(tas)

        # qaund one arrie on stop
        if ville == arrivee:
            break

        # Parcourir les voisins
        voisins = graphe[ville]
        for voisin, poids in voisins:
            nouvelle_distance = distance_actuelle + poids
            if nouvelle_distance < distances[voisin]:
                distances[voisin] = nouvelle_distance
                predecesseurs[voisin] = ville
                heapq.heappush(tas, (nouvelle_distance, voisin))

    # Reconstruction du chemin (après la boucle)
    chemin = []
    ville = arrivee
    while ville != None:
        chemin.append(ville)
        ville = predecesseurs[ville]
    chemin.reverse()

    # Vérifier si le chemin existe
    if len(chemin) == 0 or chemin[0] != depart:
        return "Pas de chemin", []

    return distances[arrivee], chemin


distance, chemin = dijkstra(graphe, "A", "F")
print("Distance la plus courte de A à F :", distance)
print("Chemin :", chemin)

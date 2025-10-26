import heapq
import math

# heuris c'est une fonction qui calcule une estimation de la distance entre deux nœuds dans un graphe.
# la formule est : f(n) = g(n) + h(n)

# Graphe et coordonnées
graphe = { ... }  # comme avant
coordonnees = { ... }  # x, y pour chaque ville

def heuris(ville, arrivee):
    x1, y1 = coordonnees[ville]
    x2, y2 = coordonnees[arrivee]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def a_star(graphe, depart, arrivee):
    distances = {v: 1000000 for v in graphe}
    distances[depart] = 0
    predecesseurs = {v: None for v in graphe}

    tas = []
    heapq.heappush(tas, (heuris(depart, arrivee), depart))  # f = g + h

    while tas:
        f_actuel, ville = heapq.heappop(tas)
        if ville == arrivee:
            break

        for voisin, poids in graphe[ville]:
            g_voisin = distances[ville] + poids
            if g_voisin < distances[voisin]:
                distances[voisin] = g_voisin
                predecesseurs[voisin] = ville
                f_voisin = g_voisin + heuris(voisin, arrivee)
                heapq.heappush(tas, (f_voisin, voisin))

    # Reconstruire le chemin (comme Dijkstra)
    chemin = []
    ville = arrivee
    while ville is not None:
        chemin.append(ville)
        ville = predecesseurs[ville]
    chemin.reverse()

    if chemin[0] != depart:
        return "Pas de chemin", []

    return distances[arrivee], chemin

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
    # Initialisation des distances: 0 pour le départ, infini pour les autres
    distances = {ville: float('inf') for ville in graphe}
    distances[depart] = 0
    
    # File de priorité: (distance, noeud)
    file_priorite = [(0, depart)]
    
    # Pour reconstruire le chemin
    predecesseurs = {ville: None for ville in graphe}
    
    while file_priorite:
        # Prendre le nœud non visité avec la distance la plus petite
        distance_actuelle, u = heapq.heappop(file_priorite)
        
        # Si nous avons atteint la destination
        if u == arrivee:
            break
            
        # Si la distance actuelle est déjà plus grande que la plus courte trouvée, ignorer
        if distance_actuelle > distances[u]:
            continue
            
        # Parcourir les voisins
        for v, poids in graphe[u]:
            nouvelle_distance = distance_actuelle + poids
            
            # Mise à jour si un chemin plus court est trouvé
            if nouvelle_distance < distances[v]:
                distances[v] = nouvelle_distance
                predecesseurs[v] = u
                heapq.heappush(file_priorite, (nouvelle_distance, v))

    # Reconstruire le chemin
    chemin = []
    u = arrivee
    while u is not None:
        chemin.append(u)
        u = predecesseurs[u]
    chemin.reverse()
    
    return distances[arrivee], chemin if chemin[0] == depart else "Pas de chemin"

# Exemple d'utilisation: A vers F
distance, chemin = dijkstra(graphe, "A", "F")
print(f"Distance la plus courte de A à F: {distance}") # La distance de A à F est 15. (A -> C -> E -> D -> F: 2 + 3 + 4 + 11 = 20... Re-calculons)
# A -> C -> E -> D: 2 + 3 + 4 = 9
# A -> B -> D: 4 + 10 = 14
# A -> B -> C -> E -> D: 4 + 5 + 3 + 4 = 16
# Le chemin le plus court est A -> C (2) -> E (3) -> D (4) -> F (11) = 20. Non, c'est A-C(2)-E(3)-D(4)-F(11) = 20.
# A -> C (2) -> E (3) -> D (4) -> F (11) -> 20.
# A -> C(2)
# A -> C -> E: 2 + 3 = 5
# A -> B: 4
# A -> C -> E -> D: 2 + 3 + 4 = 9
# A -> B -> C: 4 + 5 = 9
# A -> B -> D: 4 + 10 = 14
# Chemin le plus court A-C-E-D-F est 2+3+4+11 = 20.
# Le résultat est 20, le chemin est ['A', 'C', 'E', 'D', 'F'].
print(f"Chemin: {chemin}")
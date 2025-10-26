graphe = {
    "A": [("B", 4), ("C", 2)],
    "B": [("C", 5), ("D", 10)],
    "C": [("E", 3)],
    "D": [("F", 11)],
    "E": [("D", 4)],
    "F": []
}

def dijkstra(graphe, depart):

    distances = {ville: float('inf') for ville in graphe}
    distances[depart] = 0

    visites = set()
    
    
    while len(visites) < len(graphe):
        
        
        min_distance = float('inf')
        u = None
        
        
        for ville in graphe:
            if ville not in visites and distances[ville] < min_distance:
                min_distance = distances[ville]
                u = ville
        
        
        if u is None:
            break
            
        
        visites.add(u)
        
        
        
        for v, poids in graphe[u]:
            
            nouvelle_distance = distances[u] + poids
            
            if nouvelle_distance < distances[v]:
                distances[v] = nouvelle_distance

    return distances

distances_finales = dijkstra(graphe, "A")
destination = "F"


print(f"Toutes les distances depuis A: {distances_finales}")

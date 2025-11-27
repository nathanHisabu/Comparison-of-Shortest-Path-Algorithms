def Bellman_Ford(M, s0):
    n = len(M)
    dist = [float('inf')] * n           # Distance minimale depuis s0
    pred = [None] * n                   # Prédécesseurs pour reconstruire les chemins
    dist[s0] = 0
    pred[s0] = s0

    F = [(i, j) for i in range(n) for j in range(n) if M[i][j] != 0]  # Liste des arêtes

    # Mettre a jour les arêtes n - 1 fois
    for _ in range(n - 1):
        for u, v in F:
            if dist[u] != float('inf') and dist[u] + M[u][v] < dist[v]:
                dist[v] = dist[u] + M[u][v]
                pred[v] = u

    # Détection des cycles de poids négatif
    cycle_negatif = [False] * n
    for u, v in F:
        if dist[u] != float('inf') and dist[u] + M[u][v] < dist[v]:
            cycle_negatif[v] = True

    # Propagation des effets des cycles négatifs
    changed = True
    while changed:
        changed = False
        for u, v in F:
            if cycle_negatif[u] and not cycle_negatif[v]:
                cycle_negatif[v] = True
                changed = True

    # Affichage des résultats
    for s in range(n):
        if s == s0:
            continue

        if dist[s] == float('inf'):
            print(f"Sommet {s} non joignable à {s0} par un chemin dans le graphe G")
        elif cycle_negatif[s]:
            print(f"Sommet {s} joignable depuis {s0} mais pas de plus court chemin (cycle négatif)")
        else:
            path = []
            current = s
            etapes = 0
            while current != s0 and etapes < n:  # Reconstruction du chemin
                path.append(current)
                current = pred[current]
                etapes += 1
            path.append(s0)
            path.reverse()
            print(f"Chemin de {s0} à {s} : longueur = {dist[s]}, itinéraire = {path}")

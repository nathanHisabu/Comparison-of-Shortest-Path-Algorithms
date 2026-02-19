def Bellman_Ford(M, s0):
    n = len(M)
    dist = [float('inf')] * n           # Minimum distance from s0
    pred = [None] * n                   # Predecessors to reconstruct paths
    dist[s0] = 0
    pred[s0] = s0

    F = [(i, j) for i in range(n) for j in range(n) if M[i][j] != 0]  # List of edges

    # Update edges n - 1 times
    for _ in range(n - 1):
        for u, v in F:
            if dist[u] != float('inf') and dist[u] + M[u][v] < dist[v]:
                dist[v] = dist[u] + M[u][v]
                pred[v] = u

    # Detect negative weight cycles
    cycle_negatif = [False] * n
    for u, v in F:
        if dist[u] != float('inf') and dist[u] + M[u][v] < dist[v]:
            cycle_negatif[v] = True

    # Propagate effects of negative cycles
    changed = True
    while changed:
        changed = False
        for u, v in F:
            if cycle_negatif[u] and not cycle_negatif[v]:
                cycle_negatif[v] = True
                changed = True

    # Display results
    for s in range(n):
        if s == s0:
            continue

        if dist[s] == float('inf'):
            print(f"Node {s} unreachable from {s0} via any path in graph G")
        elif cycle_negatif[s]:
            print(f"Node {s} reachable from {s0} but no shortest path exists (negative cycle)")
        else:
            path = []
            current = s
            etapes = 0
            while current != s0 and etapes < n:  # Reconstruct path
                path.append(current)
                current = pred[current]
                etapes += 1
            path.append(s0)
            path.reverse()
            print(f"Path from {s0} to {s}: length = {dist[s]}, route = {path}")

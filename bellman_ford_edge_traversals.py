import random

def parcours_aleatoire_fleche(M):
    """Returns the list of all edges (u,v) of the graph in a random order."""
    edges = []
    n = len(M)
    for u in range(n):
        for v in range(n):
            if M[u][v] != 0:
                edges.append((u,v))
    random.shuffle(edges)
    return edges

# Breadth-first traversal (BFS)
def pl(M,s):
    n = len(M)
    couleur = {i:'blanc' for i in range(n)}  # All nodes are white (unvisited)
    couleur[s] = 'vert'                       # Starting node is green (visited)
    file = [s]
    Parcours = [s]
    while file:
        i = file[0]  # Look at the first node in the queue
        for j in range(n):
            if M[i][j] != 0 and couleur[j] == 'blanc':
                file.append(j)
                couleur[j] = 'vert'  # Mark as visited
                Parcours.append(j)
        file.pop(0)  # Remove the processed node
    return Parcours

# Depth-first traversal (DFS)
def pp(M,s):
    n = len(M)
    couleur = {i:'blanc' for i in range(n)}  # All nodes unvisited (white)
    couleur[s] = 'vert'                       # Starting node marked as visited (green)
    pile = [s]                               # Initialize stack with s
    Resultat = [s]                           # List of visited nodes

    while pile:                             # While the stack is not empty
        i = pile[-1]                       # Node at the top of the stack
        # List of unvisited successors of i
        Succ_blanc = [j for j in range(n) if M[i][j] != 0 and couleur[j] == 'blanc']

        if Succ_blanc:
            pile.append(Succ_blanc[0])      # Push first unvisited successor
            couleur[Succ_blanc[0]] = 'vert' # Mark as visited
            Resultat.append(Succ_blanc[0])  # Add to visited list
        else:
            pile.pop()                      # No unvisited successor, pop i

    return Resultat


def transforme_parcours_en_fleche(M, parcours):
    """Transforms a list of nodes into a list of edges (arcs) of the graph."""
    fleche = []
    for i in parcours:
        for k in range(len(M)):
            if M[i][k] != 0:
                fleche.append((i,k))
    return fleche

def Bellman_Ford(M, s0, fleche_list, label=""):
    """Bellman-Ford algorithm to compute shortest paths from s0.

    M : adjacency matrix with weights
    s0 : source node
    fleche_list : list of edges to traverse (given order)
    label : string to identify the execution
    """
    n = len(M)
    dist = [float('inf')] * n
    pred = [None] * n
    dist[s0] = 0
    pred[s0] = s0

    tours = 0
    for _ in range(n-1):
        modification = False
        for u,v in fleche_list:
            if dist[u] + M[u][v] < dist[v]:
                dist[v] = dist[u] + M[u][v]
                pred[v] = u
                modification = True
        tours += 1
        if not modification:
            break
    print(f"[{label}] Number of iterations performed: {tours}")

    # Detect negative cycles
    cycle_negatif = [False] * n
    for u, v in fleche_list:
        if dist[u] != float('inf') and dist[u] + M[u][v] < dist[v]:
            cycle_negatif[v] = True

    # Propagate nodes affected by negative cycles
    changed = True
    while changed:
        changed = False
        for u, v in fleche_list:
            if cycle_negatif[u] and not cycle_negatif[v]:
                cycle_negatif[v] = True
                changed = True

    # Display results
    for s in range(n):
        if s == s0:
            continue
        if dist[s] == float('inf'):
            print(f"Node {s} unreachable from {s0}")
        elif cycle_negatif[s]:
            print(f"Node {s} affected by negative cycle from {s0} (no shortest path)")
        else:
            # Reconstruct path (limited to n steps to avoid infinite loop)
            path = []
            current = s
            etapes = 0
            while current != s0 and etapes < n:
                path.append(current)
                current = pred[current]
                etapes += 1
            path.append(s0)
            path.reverse()
            # Commented out to avoid very long output
            #print(f"Path from {s0} to {s}: distance = {dist[s]}, route = {path}")

# Construct a random adjacency matrix
n = 50
max_weight = 10
M = []
for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row.append(0)
        else:
            if random.random() < 0.1:
                row.append(random.randint(1, max_weight))
            else:
                row.append(0)
    M.append(row)

print("\n=== Bellman-Ford with RANDOM ===")
Bellman_Ford(M, 0, parcours_aleatoire_fleche(M), label="Random")

print("\n=== Bellman-Ford with DEPTH ===")
Bellman_Ford(M, 0, transforme_parcours_en_fleche(M, pp(M, 0)), label="Depth")

print("\n=== Bellman-Ford with BREADTH ===")
Bellman_Ford(M, 0, transforme_parcours_en_fleche(M, pl(M, 0)), label="Breadth")

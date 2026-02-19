import numpy as np
from random import randint

def graphe2(n, p, a, b):
    M = np.random.binomial(1, p, size=(n, n))
    M = M.astype('float64')
    for i in range(n):
        for j in range(n):
            if M[i][j] == 0:
                M[i][j] = float('inf')
            else:
                M[i][j] = randint(a, b)
    return M

def dijkstra(M, depart):
    n = len(M)
    sommets = list(range(n))
    
    dist = {s: float('inf') for s in sommets}
    pred = {s: None for s in sommets}
    dist[depart] = 0

    restants = set(sommets)
    rencontre = []  # List of vertices visited

    while restants:
        u = min(restants, key=lambda s: dist[s])
        if dist[u] == float('inf'):
            break  # If all remaining vertices are unreachable

        restants.remove(u)
        rencontre.append(u)  # Record visited vertex

        for v in sommets:
            if M[u][v] > 0 and v in restants:  # If edge exists and v is in remaining
                new_dist = dist[u] + M[u][v]
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    pred[v] = u
                   
    chemins = {}
    for s in sommets:
        if dist[s] < float('inf'):
            chemin = []
            courant = s
            while courant is not None:
                chemin.insert(0, courant)
                courant = pred[courant]
            chemins[s] = chemin
        else:
            chemins[s] = None

    return dist, chemins, rencontre


# Removed prints to simplify readability for Question 6
def Bellman_Ford(M, s0, fleche_list, label=""):
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
    #print(f"[{label}] Number of iterations: {tours}")

    # Detect negative cycles
    cycle_negatif = [False] * n
    for u, v in fleche_list:
        if dist[u] != float('inf') and dist[u] + M[u][v] < dist[v]:
            cycle_negatif[v] = True

    # Propagate negative cycle marks (for vertices reachable from negative cycles)
    changed = True
    while changed:
        changed = False
        for u, v in fleche_list:
            if cycle_negatif[u] and not cycle_negatif[v]:
                cycle_negatif[v] = True
                changed = True

    for s in range(n):
        if s == s0:
            continue

        if dist[s] == float('inf'):
            pass
            #print(f"Vertex {s} unreachable from {s0}")
        elif cycle_negatif[s]:
            pass
            #print(f"Vertex {s} reachable from {s0} but no shortest path (negative cycle)")
        else:
            # Rebuild path with safety limit to avoid infinite loops
            path = []
            current = s
            etapes = 0
            while current != s0 and etapes < n:
                path.append(current)
                current = pred[current]
                etapes += 1
            path.append(s0)
            path.reverse()
            #print(f"Path from {s0} to {s}: distance = {dist[s]}, route = {path}")
            
# Depth-first traversal
def pp(M,s):
    n = len(M)                       # size of the array = number of vertices
    couleur = {}                     # color all vertices white and s green
    for i in range(n):
        couleur[i] = 'blanc'
    couleur[s] = 'vert'
    pile = [s]                       # initialize stack with s
    Resultat = [s]                   # initialize result list with s
    while pile != [] :
        i = pile[-1] # last vertex in stack
        Succ_blanc=[] # list of unvisited successors (white)
        for j in range(n):
            if (M[pile[-1]][j] != 0 and couleur[j] == 'blanc') :
                Succ_blanc.append(j)
        if Succ_blanc != [] :
            pile.append(Succ_blanc[0]) # push it
            couleur[Succ_blanc[0]] = 'vert'  # mark green
            Resultat.append(Succ_blanc[0])   # add to result list
        else :
            pile.pop(-1)   # otherwise remove i from stack
    return Resultat

def transforme_parcours_en_fleche(M,parcours):
    fleche = []
    L = parcours
    for i in L:
        for k in range (len(M)):
            if M[i][k] != 0:
                fleche.append((i,k))
    return fleche

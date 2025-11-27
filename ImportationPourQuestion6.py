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
    rencontre = []  # Liste des sommets rencontrés

    while restants:
        u = min(restants, key=lambda s: dist[s])
        if dist[u] == float('inf'):
            break  # Si tous les sommets restants sont inaccessibles

        restants.remove(u)
        rencontre.append(u)  # On enregistre le sommet rencontré

        
        for v in sommets:
            if M[u][v] > 0 and v in restants:  # Si une arête existe et v est dans restants
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


#on a enlever les prints pour faciliter la lisibilite pour la question 6, 
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
    #print(f"[{label}] Nombre de tours effectués : {tours}")

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
            #print(f"Sommet {s} non joignable à {s0} par un chemin dans le graphe G")
        elif cycle_negatif[s]:
            pass
            #print(f"Sommet {s} joignable depuis {s0} mais pas de plus court chemin (cycle négatif)")
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
            #print(f"Chemin de {s0} à {s} : longueur = {dist[s]}, itinéraire = {path}")
            
#Parcours en profondeur
def pp(M,s):
    n = len(M)                       #taille du tableau = nombre de sommets
    couleur = {}                     #On colorie tous les sommets en blanc et s en vert
    for i in range(n):
        couleur[i] = 'blanc'
    couleur[s] = 'vert'
    pile = [s]                       #On initialise la pile à s
    Resultat = [s]                   #On initialise la liste des résultats à s
    while pile != [] :
        i = pile[-1] # Le dernier sommet i dea la pile
        Succ_blanc=[] #On crée la liste des succeseurs non déjà visitées(blancs)
        for j in range(n):
            if (M[pile[-1]][j] != 0 and couleur[j] == 'blanc') :
                Succ_blanc.append(j)
        if Succ_blanc != [] :
            pile.append(Succ_blanc[0]) #On l'empile
            couleur[Succ_blanc[0]] = 'vert'  #On le colorie en vert
            Resultat.append(Succ_blanc[0])   # On le met en liste resultat
        else :
            pile.pop(-1)   #Sinon on sort i de la pile
    return Resultat

def transforme_parcours_en_fleche(M,parcours):
    fleche = []
    L = parcours
    for i in L:
        for k in range (len(M)):
            if M[i][k] != 0:
                fleche.append((i,k))
    return fleche
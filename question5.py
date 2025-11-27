import random

def parcours_aleatoire_fleche(M):
    """Renvoie la liste de toutes les arêtes (u,v) du graphe dans un ordre aléatoire."""
    edges = []
    n = len(M)
    for u in range(n):
        for v in range(n):
            if M[u][v] != 0:
                edges.append((u,v))
    random.shuffle(edges)
    return edges

# Parcours en largeur (BFS)
def pl(M,s):
    n = len(M)
    couleur = {i:'blanc' for i in range(n)}  # Tous les sommets sont blancs (non visités)
    couleur[s] = 'vert'                       # Le sommet de départ est vert (visité)
    file = [s]
    Parcours = [s]
    while file:
        i = file[0]  # on regarde le premier sommet dans la file
        for j in range(n):
            if M[i][j] != 0 and couleur[j] == 'blanc':
                file.append(j)
                couleur[j] = 'vert'  # on marque comme visité
                Parcours.append(j)
        file.pop(0)  # on enlève le sommet traité
    return Parcours

# Parcours en profondeur (DFS)
def pp(M,s):
    n = len(M)
    couleur = {i:'blanc' for i in range(n)}  # Tous les sommets sont non visités (blanc)
    couleur[s] = 'vert'                       # Sommet de départ marqué comme visité (vert)
    pile = [s]                               # Initialisation de la pile avec s
    Resultat = [s]                           # Liste des sommets visités

    while pile:                             # Tant que la pile n’est pas vide
        i = pile[-1]                       # Sommet au sommet de la pile
        # Liste des successeurs non visités de i
        Succ_blanc = [j for j in range(n) if M[i][j] != 0 and couleur[j] == 'blanc']

        if Succ_blanc:
            pile.append(Succ_blanc[0])      # Empile le premier successeur blanc
            couleur[Succ_blanc[0]] = 'vert' # Marque-le comme visité
            Resultat.append(Succ_blanc[0])  # Ajoute à la liste des visités
        else:
            pile.pop()                      # Pas de successeur blanc, dépile i

    return Resultat


def transforme_parcours_en_fleche(M, parcours):
    """Transforme une liste de sommets en liste d’arêtes (arcs) du graphe."""
    fleche = []
    for i in parcours:
        for k in range(len(M)):
            if M[i][k] != 0:
                fleche.append((i,k))
    return fleche

def Bellman_Ford(M, s0, fleche_list, label=""):
    """Algorithme de Bellman-Ford pour calculer les plus courts chemins depuis s0.

    M : matrice d'adjacence avec poids
    s0 : sommet source
    fleche_list : liste des arêtes à parcourir (ordre donné)
    label : chaîne pour identifier l’exécution
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
    print(f"[{label}] Nombre de tours effectués : {tours}")

    # Détection des cycles négatifs
    cycle_negatif = [False] * n
    for u, v in fleche_list:
        if dist[u] != float('inf') and dist[u] + M[u][v] < dist[v]:
            cycle_negatif[v] = True

    # Propagation des sommets atteints par un cycle négatif
    changed = True
    while changed:
        changed = False
        for u, v in fleche_list:
            if cycle_negatif[u] and not cycle_negatif[v]:
                cycle_negatif[v] = True
                changed = True

    # Affichage des résultats
    for s in range(n):
        if s == s0:
            continue
        if dist[s] == float('inf'):
            print(f"Sommet {s} non joignable depuis {s0}")
        elif cycle_negatif[s]:
            print(f"Sommet {s} atteint par un cycle négatif depuis {s0} (pas de plus court chemin)")
        else:
            # Reconstruction du chemin (limité à n étapes pour éviter boucle infinie)
            path = []
            current = s
            etapes = 0
            while current != s0 and etapes < n:
                path.append(current)
                current = pred[current]
                etapes += 1
            path.append(s0)
            path.reverse()
            # On a mit le print en commentaire pour eviter de tres longs affichage
            #print(f"Chemin de {s0} à {s} : distance = {dist[s]}, itinéraire = {path}")

# Construction d’une matrice d’adjacence aléatoire
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

print("\n=== Bellman-Ford avec ALEATOIRE ===")
Bellman_Ford(M, 0, parcours_aleatoire_fleche(M), label="Aléatoire")

print("\n=== Bellman-Ford avec PROFONDEUR ===")
Bellman_Ford(M, 0, transforme_parcours_en_fleche(M, pp(M, 0)), label="Profondeur")

print("\n=== Bellman-Ford avec LARGEUR ===")
Bellman_Ford(M, 0, transforme_parcours_en_fleche(M, pl(M, 0)), label="Largeur")

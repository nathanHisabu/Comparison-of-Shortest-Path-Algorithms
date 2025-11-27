import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

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


def afficher_graphe(M, chemin, rencontre):
    G = nx.DiGraph()

    noms = ['A', 'B', 'C', 'D', "E", "F"]  # Noms des sommets
    for i in range(len(M)):
        G.add_node(i)

    # Ajouter les arêtes du graphe
    for i in range(len(M)):
        for j in range(len(M)):
            if M[i][j] > 0:
                G.add_edge(i, j, weight=M[i][j])

    # Définir la disposition des noeuds pour le dessin
    pos = nx.spring_layout(G)
    node_labels = {i: noms[i] for i in range(len(M))}

    # Colorier les noeuds selon leur accessibilité
    node_colors = []
    for i in range(len(M)):
        if i in rencontre:  # Si le sommet a été visité
            node_colors.append("lightblue")
        else:
            node_colors.append("gray")  # Non accessible

    # Dessiner les noeuds et leurs labels
    nx.draw(G, pos, labels=node_labels, with_labels=True, node_color=node_colors, node_size=1000)

    # Créer la liste des arêtes du chemin
    if chemin:
        edges_chemin = [(chemin[i], chemin[i+1]) for i in range(len(chemin)-1)]
        # Dessiner les arêtes, rouge pour celles du chemin, noir pour les autres
        edge_colors = []
        for edge in G.edges():
            if edge in edges_chemin or (edge[1], edge[0]) in edges_chemin:  # Assurer que l'arête est bien dans le chemin
                edge_colors.append('red')
            else:
                edge_colors.append('black')

        nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=2)

    # Dessiner les poids des arêtes
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("Graphe avec le plus court chemin (en rouge) et sommets visités (en bleu)")
    plt.show()

# --------------------
# Exemple d'utilisation

M = np.array([
    [0, 2, 0, 0, 0, 1],  # A
    [0, 0, 3, 0, 0, 0],  # B
    [0, 0, 0, 4, 0, 0],  # C
    [0, 0, 0, 0, 2, 3],  # D
    [0, 0, 0, 0, 0, 5],  # E
    [0, 0, 0, 0, 0, 0]   # F
])

depart = 0  # A

# Exécution de Dijkstra
distances, chemins, rencontre = dijkstra(M, depart)

# Affichage des sommets visités
print("Sommets visités dans l'ordre : ", rencontre)

# Affichage des chemins pour chaque sommet
for sommet in range(len(M)):
    if sommet == depart:
        continue
    if chemins[sommet]:
        print(f"Chemin de {depart} à {sommet} : {chemins[sommet]} (longueur = {distances[sommet]})")
    else:
        print(f"Sommet {sommet} non joignable à partir de {depart}")

# Affichage du graphe
afficher_graphe(M, chemins[3], rencontre)
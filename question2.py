import matplotlib.pyplot as plt
import networkx as nx

# Matrice d'adjacence représentant le graphe pondéré
adj_matrix = [
    [0, 4, 0, 7, 0],
    [4, 0, 2, 0, 0],
    [0, 2, 0, 1, 3],
    [7, 0, 1, 0, 4],
    [0, 0, 3, 4, 0]
]



# Création du graphe dirigé (DiGraph)
G = nx.DiGraph()
n = len(adj_matrix)
G.add_nodes_from(range(n))

# Ajout des arêtes avec leurs poids respectifs
for i in range(n):
    for j in range(n):
        if adj_matrix[i][j] != 0:
            G.add_edge(i, j, weight=adj_matrix[i][j])

# Définir le chemin comme une liste de sommets visités (par exemple : 0 -> 1 -> 2 -> 3)
path = [0, 1, 2, 3]

# Calcul des positions des nœuds pour l'affichage graphique
pos = nx.spring_layout(G)

# Dessiner le graphe avec les nœuds, les arêtes et les labels
nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=800, arrows=True)

# Mettre en évidence le chemin en rouge
# On dessine les arêtes correspondant au chemin en rouge
for i in range(len(path) - 1):
    nx.draw_networkx_edges(G, pos, edgelist=[(path[i], path[i+1])], edge_color='red', width=2)

# Affichage des poids sur les arêtes
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))

# Titre du graphique
plt.title("Graphe avec chemin en rouge")

# Affichage du graphe
plt.show()

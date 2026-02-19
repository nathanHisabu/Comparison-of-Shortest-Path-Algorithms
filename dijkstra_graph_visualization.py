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
    rencontre = []  # List of visited nodes

    while restants:
        u = min(restants, key=lambda s: dist[s])
        if dist[u] == float('inf'):
            break  # If all remaining nodes are unreachable

        restants.remove(u)
        rencontre.append(u)  # Record the visited node

        
        for v in sommets:
            if M[u][v] > 0 and v in restants:  # If an edge exists and v is in remaining nodes
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

    noms = ['A', 'B', 'C', 'D', "E", "F"]  # Names of the nodes
    for i in range(len(M)):
        G.add_node(i)

    # Add the edges of the graph
    for i in range(len(M)):
        for j in range(len(M)):
            if M[i][j] > 0:
                G.add_edge(i, j, weight=M[i][j])

    # Compute positions of nodes for drawing
    pos = nx.spring_layout(G)
    node_labels = {i: noms[i] for i in range(len(M))}

    # Color nodes according to accessibility
    node_colors = []
    for i in range(len(M)):
        if i in rencontre:  # If the node has been visited
            node_colors.append("lightblue")
        else:
            node_colors.append("gray")  # Not accessible

    # Draw nodes and their labels
    nx.draw(G, pos, labels=node_labels, with_labels=True, node_color=node_colors, node_size=1000)

    # Create the list of edges for the path
    if chemin:
        edges_chemin = [(chemin[i], chemin[i+1]) for i in range(len(chemin)-1)]
        # Draw edges: red for path, black for others
        edge_colors = []
        for edge in G.edges():
            if edge in edges_chemin or (edge[1], edge[0]) in edges_chemin:  # Ensure edge is in the path
                edge_colors.append('red')
            else:
                edge_colors.append('black')

        nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=2)

    # Draw edge weights
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("Graph with shortest path (in red) and visited nodes (in blue)")
    plt.show()

# --------------------
# Example usage

M = np.array([
    [0, 2, 0, 0, 0, 1],  # A
    [0, 0, 3, 0, 0, 0],  # B
    [0, 0, 0, 4, 0, 0],  # C
    [0, 0, 0, 0, 2, 3],  # D
    [0, 0, 0, 0, 0, 5],  # E
    [0, 0, 0, 0, 0, 0]   # F
])

depart = 0  # A

# Run Dijkstra
distances, chemins, rencontre = dijkstra(M, depart)

# Display visited nodes
print("Visited nodes in order: ", rencontre)

# Display paths to each node
for sommet in range(len(M)):
    if sommet == depart:
        continue
    if chemins[sommet]:
        print(f"Path from {depart} to {sommet}: {chemins[sommet]} (length = {distances[sommet]})")
    else:
        print(f"Node {sommet} unreachable from {depart}")

# Display the graph
afficher_graphe(M, chemins[3], rencontre)

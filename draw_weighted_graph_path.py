import matplotlib.pyplot as plt
import networkx as nx

# Adjacency matrix representing the weighted graph
adj_matrix = [
    [0, 4, 0, 7, 0],
    [4, 0, 2, 0, 0],
    [0, 2, 0, 1, 3],
    [7, 0, 1, 0, 4],
    [0, 0, 3, 4, 0]
]

# Create the directed graph (DiGraph)
G = nx.DiGraph()
n = len(adj_matrix)
G.add_nodes_from(range(n))

# Add edges with their respective weights
for i in range(n):
    for j in range(n):
        if adj_matrix[i][j] != 0:
            G.add_edge(i, j, weight=adj_matrix[i][j])

# Define the path as a list of visited nodes (example: 0 -> 1 -> 2 -> 3)
path = [0, 1, 2, 3]

# Compute node positions for graphical display
pos = nx.spring_layout(G)

# Draw the graph with nodes, edges, and labels
nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=800, arrows=True)

# Highlight the path in red
# Draw the edges corresponding to the path in red
for i in range(len(path) - 1):
    nx.draw_networkx_edges(G, pos, edgelist=[(path[i], path[i+1])], edge_color='red', width=2)

# Display the weights on the edges
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))

# Graph title
plt.title("Graph with path in red")

# Show the graph
plt.show()

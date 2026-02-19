import numpy as np
from random import randint

# Generates a weighted adjacency matrix for a random graph:
# each edge has a 50% chance to exist, with a weight between a and b
# missing edges are represented by infinity
def graphe(n, a, b):
    M = np.random.randint(0, 2, size=(n, n))
    M = M.astype('float64')
    for i in range(n):
        for j in range(n):
            if M[i][j] == 0:
                M[i][j] = float('inf')
            else:
                M[i][j] = randint(a, b)
    return M

# Variant of graphe with probability p of creating an edge between each pair of nodes
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

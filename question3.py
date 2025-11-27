import numpy as np
from random import randint

# Génère une matrice d'adjacence pondérée pour un graphe aléatoire :
# chaque arête a une probabilité 0.5 d'exister, et un poids entre a et b
# les absences d'arêtes sont représentées par l'infini
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

# Variante de graphe avec probabilité p de créer une arête entre chaque paire de sommets
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

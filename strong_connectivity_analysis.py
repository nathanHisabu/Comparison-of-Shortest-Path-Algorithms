import numpy as np
from random import randint
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Function trans1: transforms a weight matrix into a binary connectivity matrix,
# then computes the transitive closure using successive matrix multiplications.
def trans1(M):
    n = len(M)
    # Replace all weights > 0 (and not inf) with 1, others with 0
    for a in range(n):
        for b in range(n):
            if M[a,b] > 0 and M[a,b] != float("inf"):
                M[a,b] = 1
            else:
                M[a,b] = 0                
    N = M            
    P = M
    # Transitive closure: N += N^2 + N^3 + ... + N^(n)
    for i in range(n-1):
        P = np.dot(N,P)
        N += P
    # Limit all elements to 1 (so 0 or 1 actually)
    for i in range(n):
        for j in range(n):
            N[i,j] = min(N[i,j],1)
    return(N)

# Question 7: test if a graph is strongly connected (transitive matrix equals all-ones matrix)
def fc(M1):  # takes a matrix M1
    t = trans1(M1)  # apply transitive closure
    taille = len(M1)
    # Create an all-ones matrix of the same size
    matrice_1 = []
    for i in range(taille):
        ligne = []
        for j in range(taille):
            ligne.append(1)
        matrice_1.append(ligne)
    # Compare t and matrice_1 element by element
    for i in range(taille):
        for j in range(taille):
            if t[i][j] != matrice_1[i][j]:
                return False
    return True

# Function graphe: creates a random matrix with weights or infinity
def graphe(n, a, b):
    M = np.random.randint(0, 2, size=(n, n))  # 0/1 matrix
    M = M.astype('float64')                    # convert to float
    # replace 0 with inf and 1 with a random weight between a and b-1
    for i in range(n):
        for j in range(n):
            if M[i][j] == 0:
                M[i][j] = float('inf')
            else:
                M[i][j] = randint(a, b)
    return M

# graphe2: similar creation but with probability p of 1 (binomial law)
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

# Question 8: statistical test, frequency of strong connectivity for graph with weights = 1
def test_stat_fc(n):
    count_fc = 0
    for _ in range(500):
        M = graphe(n,1,1)
        if fc(M):  # test if strongly connected
            count_fc += 1
    pourcentage = (count_fc / 500) * 100
    return pourcentage

# Question 9: same statistical test with probability p of edge presence
def test_stat_fc2(n,p):
    count_fc = 0
    for _ in range(500):
        M = graphe2(n,p,1,1)
        if fc(M):
            count_fc += 1
    pourcentage = (count_fc / 500) * 100
    return pourcentage

# Function threshold: searches for the minimal probability p to have more than 99% strong connectivity
def seuil(n):
    p = 1
    while test_stat_fc2(n,p) > 99 :
        p -= 0.01
    return p

# Plot threshold curve as a function of n
def courbe_seuil(min,max):
    ns = list(range(min,max+1))
    seuils = []
    for n in ns:
        s = seuil(n)
        seuils.append(s)
    plt.plot(ns,seuils,marker='o')
    plt.xlabel("Graph size (n)")
    plt.ylabel("Strong connectivity threshold p")
    plt.title("Evolution of strong connectivity threshold as a function of n")
    plt.grid(True)
    plt.show()

# Plot log-log graph of threshold with linear regression
def courbe_seuillog(min,max):
    ns = list(range(min,max+1))
    seuils = []
    for n in ns:
        s = seuil(n)
        seuils.append(s)
    log_n = np.log(ns)
    log_seuil = np.log(seuils)
    slope, intercept, r_value, _, _ = linregress(log_n, log_seuil)
    plt.scatter(log_n, log_seuil, color='blue', label='Log-Log Data')
    plt.plot(log_n,intercept + slope * log_n, marker='o')
    plt.xlabel("Log(n)")
    plt.ylabel("Log(Threshold)")
    plt.title("Log-Log Plot of Threshold(n)")
    plt.grid(True)
    plt.show()

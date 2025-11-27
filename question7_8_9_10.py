import numpy as np
from random import randint
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Fonction trans1 : transforme une matrice de poids en matrice binaire indiquant la connexité,
# puis calcule la fermeture transitive par multiplications matricielles successives.
def trans1(M):
    n = len(M)
    # On remplace tous les poids > 0 (et différents de inf) par 1, les autres par 0
    for a in range(n):
        for b in range(n):
            if M[a,b] > 0 and M[a,b] != float("inf"):
                M[a,b] = 1
            else:
                M[a,b] = 0                
    N = M            
    P = M
    # Fermeture transitive : N += N^2 + N^3 + ... + N^(n)
    for i in range(n-1):
        P = np.dot(N,P)
        N += P
    # On borne tous les éléments à 1 (0 ou 1 en fait)
    for i in range(n):
        for j in range(n):
            N[i,j] = min(N[i,j],1)
    return(N)

# Question 7 : test si un graphe est fortement connexe (matrice transitive égale à matrice de 1)
def fc(M1):  # prend une matrice M1
    t = trans1(M1)  # applique fermeture transitive
    taille = len(M1)
    # Crée une matrice pleine de 1 de même taille
    matrice_1 = []
    for i in range(taille):
        ligne = []
        for j in range(taille):
            ligne.append(1)
        matrice_1.append(ligne)
    # Compare t et matrice_1 élément par élément
    for i in range(taille):
        for j in range(taille):
            if t[i][j] != matrice_1[i][j]:
                return False
    return True

# Fonction graphe : crée une matrice aléatoire avec poids ou infini
def graphe(n, a, b):
    M = np.random.randint(0, 2, size=(n, n))  # matrice 0/1
    M = M.astype('float64')                    # convertit en float
    # remplace 0 par inf et 1 par un poids aléatoire entre a et b-1
    for i in range(n):
        for j in range(n):
            if M[i][j] == 0:
                M[i][j] = float('inf')
            else:
                M[i][j] = randint(a, b)
    return M

# graphe2 : création similaire mais avec probabilité p de 1 (loi binomiale)
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

# Question 8 : test statistique, fréquence de forte connexité pour graphe avec poids=1
def test_stat_fc(n):
    count_fc = 0
    for _ in range(500):
        M = graphe(n,1,1)
        if fc(M):  # teste si fortement connexe
            count_fc += 1
    pourcentage = (count_fc / 500) * 100
    return pourcentage

# Question 9 : même test statistique avec probabilité p de présence d’arêtes
def test_stat_fc2(n,p):
    count_fc = 0
    for _ in range(500):
        M = graphe2(n,p,1,1)
        if fc(M):
            count_fc += 1
    pourcentage = (count_fc / 500) * 100
    return pourcentage

# Fonction seuil : cherche la probabilité p minimale pour avoir plus de 99% de forte connexité
def seuil(n):
    p = 1
    while test_stat_fc2(n,p) > 99 :
        p -= 0.01
    return p

# Trace la courbe du seuil en fonction de n
def courbe_seuil(min,max):
    ns = list(range(min,max+1))
    seuils = []
    for n in ns:
        s = seuil(n)
        seuils.append(s)
    plt.plot(ns,seuils,marker='o')
    plt.xlabel("Taille du graphe (n)")
    plt.ylabel("Seuile de forte connexite p")
    plt.title("Evolution du seuil de forte connexite en fonction de n")
    plt.grid(True)
    plt.show()

# Trace le graphe log-log du seuil avec régression linéaire
def courbe_seuillog(min,max):
    ns = list(range(min,max+1))
    seuils = []
    for n in ns:
        s = seuil(n)
        seuils.append(s)
    log_n = np.log(ns)
    log_seuil = np.log(seuils)
    slope, intercept, r_value, _, _ = linregress(log_n, log_seuil)
    plt.scatter(log_n, log_seuil, color='blue', label='Donnees Log-Log')
    plt.plot(log_n,intercept + slope * log_n, marker='o')
    plt.xlabel("Log(n)")
    plt.ylabel("Log(Seuil)")
    plt.title("Graphique Log-Log de Seuil(n)")
    plt.grid(True)
    plt.show()


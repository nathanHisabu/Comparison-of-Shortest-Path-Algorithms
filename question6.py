import time
import ImportationPourQuestion6 as Im
# ImportationPourQuestion6 est un module contenant toutes les fonctions nécessaires pour simplifier notre travail dans cette question.

import matplotlib.pyplot as plt
import numpy as np

# Liste des tailles de graphes à tester (de 2 à 199 sommets)
n_values = list(range(2, 200))

# Listes pour stocker les temps d'exécution des deux algorithmes
temps_dijkstra = []
temps_bf = []

# Valeur fixe de la proportion d'arêtes (non utilisée ici, mais prévue pour d'autres tests)
p_fixe = 0.5

# Fonction pour mesurer le temps d'exécution de Dijkstra pour un graphe de taille n
def TempsDij(n):
    # Ici, on génère un graphe avec une proportion d'arêtes égale à 1/n.
    # Cela permet de tester le cas où le graphe devient de plus en plus creux quand n augmente.
    graphe = Im.graphe2(n, 1/n, 1, 10)
    debut = time.perf_counter()
    Im.dijkstra(graphe, 0)
    fin = time.perf_counter()
    temps = fin - debut
    return temps

# Fonction pour mesurer le temps d'exécution de Bellman-Ford pour un graphe de taille n
def TempsBF(n):
    # Même principe que pour Dijkstra : on utilise p = 1/n ici.
    graphe = Im.graphe2(n, 1/n, 1, 10)
    debut = time.perf_counter()
    # On transforme le parcours pour l'adapter à Bellman-Ford si nécessaire
    Im.Bellman_Ford(graphe, 0, Im.transforme_parcours_en_fleche(graphe, Im.pp(graphe, 0)), label="Profondeur")
    fin = time.perf_counter()
    temps = fin - debut
    return temps

# Remplir les listes avec les temps d'exécution pour chaque valeur de n
for n in n_values:
    temps_dijkstra.append(TempsDij(n))
    temps_bf.append(TempsBF(n))

# Tracer les courbes des temps d'exécution
plt.figure(figsize=(10, 6))
plt.plot(n_values, temps_dijkstra, label="Dijkstra", color="blue")
plt.plot(n_values, temps_bf, label="Bellman-Ford", color="red")
plt.xlabel("Nombre de sommets (n)")
plt.ylabel("Temps d'exécution (secondes)")
plt.title("Comparaison des temps d'exécution : Dijkstra vs Bellman-Ford")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# On passe maintenant à la partie log-log pour vérifier si les temps suivent une loi polynomiale
log_n = np.log(n_values)                # log(n)
log_temps_dij = np.log(temps_dijkstra) # log(temps_dijkstra)
log_temps_bf = np.log(temps_bf)        # log(temps_bellman-ford)

# Régression linéaire sur les valeurs en log-log
# Cela permet d'estimer l'exposant a dans la relation t(n) ≈ c * n^a
a_dij, b_dij = np.polyfit(log_n, log_temps_dij, 1)
a_bf, b_bf = np.polyfit(log_n, log_temps_bf, 1)

# Affichage des exposants estimés (pentes des droites en log-log)
print("Pente a pour Dijkstra :", a_dij)
print("Pente a pour Bellman-Ford :", a_bf)

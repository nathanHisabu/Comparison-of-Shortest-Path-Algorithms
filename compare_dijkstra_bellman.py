import time
import ImportationPourQuestion6 as Im
# ImportationPourQuestion6 is a module containing all necessary functions to simplify our work in this question.

import matplotlib.pyplot as plt
import numpy as np

# List of graph sizes to test (from 2 to 199 nodes)
n_values = list(range(2, 200))

# Lists to store execution times of the two algorithms
temps_dijkstra = []
temps_bf = []

# Fixed edge proportion value (not used here, but planned for other tests)
p_fixe = 0.5

# Function to measure execution time of Dijkstra for a graph of size n
def TempsDij(n):
    # Here, we generate a graph with an edge proportion equal to 1/n.
    # This tests the case where the graph becomes sparser as n increases.
    graphe = Im.graphe2(n, 1/n, 1, 10)
    debut = time.perf_counter()
    Im.dijkstra(graphe, 0)
    fin = time.perf_counter()
    temps = fin - debut
    return temps

# Function to measure execution time of Bellman-Ford for a graph of size n
def TempsBF(n):
    # Same principle as Dijkstra: we use p = 1/n here.
    graphe = Im.graphe2(n, 1/n, 1, 10)
    debut = time.perf_counter()
    # Transform the traversal to adapt it to Bellman-Ford if necessary
    Im.Bellman_Ford(graphe, 0, Im.transforme_parcours_en_fleche(graphe, Im.pp(graphe, 0)), label="Depth")
    fin = time.perf_counter()
    temps = fin - debut
    return temps

# Fill the lists with execution times for each n
for n in n_values:
    temps_dijkstra.append(TempsDij(n))
    temps_bf.append(TempsBF(n))

# Plot execution time curves
plt.figure(figsize=(10, 6))
plt.plot(n_values, temps_dijkstra, label="Dijkstra", color="blue")
plt.plot(n_values, temps_bf, label="Bellman-Ford", color="red")
plt.xlabel("Number of nodes (n)")
plt.ylabel("Execution time (seconds)")
plt.title("Execution time comparison: Dijkstra vs Bellman-Ford")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Now move to the log-log part to check if times follow a polynomial law
log_n = np.log(n_values)                # log(n)
log_temps_dij = np.log(temps_dijkstra) # log(temps_dijkstra)
log_temps_bf = np.log(temps_bf)        # log(temps_bellman-ford)

# Linear regression on log-log values
# This estimates the exponent a in the relation t(n) ≈ c * n^a
a_dij, b_dij = np.polyfit(log_n, log_temps_dij, 1)
a_bf, b_bf = np.polyfit(log_n, log_temps_bf, 1)

# Display estimated exponents (slopes of log-log lines)
print("Slope a for Dijkstra:", a_dij)
print("Slope a for Bellman-Ford:", a_bf)

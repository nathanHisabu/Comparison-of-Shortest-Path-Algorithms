# **Exploration Algorithmique d’un Problème – S.A.E 2.02**

**Authors:** Basset Adrien, Hisabu Nathan Tekeste, Magadiyev Imam
**Group:** B7
**Institution:** IUT de Toulouse
**Academic Year:** 2025-2026

---

## **Table of Contents**

**Project Overview**
**File Structure**
**Algorithms Implemented**
 - Dijkstra
 - Bellman-Ford
**Graph Representation and Visualization**
**Random Graph Generation**
**Bellman-Ford: Influence of Edge Ordering**
**Experimental Complexity Comparison**
**Strong Connectivity Threshold**
**Installation**
**Usage**
**Conclusions**

---

## **Project Overview**

This project explores **algorithmic graph problems**, focusing on:

* **Shortest-path algorithms** – Dijkstra and Bellman-Ford.
* **Strong connectivity of directed graphs** – statistical thresholds and asymptotic behavior.

Weighted graphs are generated randomly to analyze **performance, connectivity, and algorithmic behavior** under varying conditions.

---

## **File Structure**

**bellman_ford_edge_traversals.py** – Helper functions for Bellman-Ford with different edge orderings (DFS, BFS, random)
**bellman_ford_shortest_paths.py** – Bellman-Ford implementation for shortest path computation
**compare_dijkstra_bellman.py** – Compares execution times of Dijkstra and Bellman-Ford, performs log-log analysis
**dijkstra_graph_visualization.py** – Dijkstra implementation with graph and path visualization
**draw_weighted_graph_path.py** – Functions to visualize graphs and highlight shortest paths
**generate_random_graphs.py** – Functions to generate weighted adjacency matrices for graphs
**graph_utils_dijkstra_bellman.py** – Shared utilities for graph algorithms (matrix transformations, edge lists, DFS)
**strong_connectivity_analysis.py** – Functions to compute strong connectivity, thresholds, and statistical analysis
**Compte rendu (B7).pdf** – Detailed report of the project and experimental results
**README.md** – Project overview and instructions

---

## **Algorithms Implemented**

### **Dijkstra Algorithm**

* Computes shortest paths from a source vertex to all vertices with **non-negative weights**
* Iteratively selects the vertex with the smallest tentative distance and updates neighbors
* Implemented in `dijkstra_graph_visualization.py`

### **Bellman-Ford Algorithm**

* Computes shortest paths from a source even with **negative edge weights**
* Iteratively relaxes edges and detects negative cycles
* Supports **custom edge orderings** via traversal lists (DFS, BFS, random) in `bellman_ford_edge_traversals.py`
* Core shortest-path logic in `bellman_ford_shortest_paths.py`

---

## **Graph Representation and Visualization**

* Graphs are **adjacency matrices**, entries are edge weights or ∞ for no edge
* Graphs and paths can be visualized using `draw_weighted_graph_path.py`

---

## **Random Graph Generation**

* `generate_random_graphs.py` contains:

1. `graphe(n, a, b)` – full adjacency matrices with weights between a and b
2. `graphe2(n, p, a, b)` – matrices with **edge probability p**, weights between a and b

---

## **Bellman-Ford: Influence of Edge Ordering**

* Edge order affects convergence speed
* Traversals: DFS (`pp`), BFS (`pl`), or random
* Convert traversal list to edge list using:

```python
from graph_utils_dijkstra_bellman import transforme_parcours_en_fleche
fleche_list = transforme_parcours_en_fleche(M, parcours)
```

* `fleche_list` is passed to Bellman-Ford for computation

---

## **Experimental Complexity Comparison**

* `compare_dijkstra_bellman.py` compares execution times for graph sizes n = 2…199
* Observations:

  * **Dijkstra** faster for positive weights
  * **Bellman-Ford** handles negative weights but slower
* Log-log analysis confirms polynomial time growth:

t(n) ∼ c ⋅ n^a ⇒ log(t(n)) = a ⋅ log(n) + log(c)

---

## **Strong Connectivity Threshold**

* A graph is **strongly connected** if a path exists between every pair of vertices
* Implemented using **transitive closure** in `strong_connectivity_analysis.py`
* Functions:

  * `fc(M)` – checks strong connectivity of matrix M
  * `test_stat_fc2(n, p)` – computes connectivity probability
  * `seuil(n)` – computes minimal edge probability for >99% connectivity
* Statistical and log-log analyses identify asymptotic **power-law behavior**

---

## **Installation**

1. **Clone the repository:**

```bash
git clone <repo_url>
cd <repo_folder>
```

2. **Create a Python virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate    # Linux / macOS
venv\Scripts\activate       # Windows
```

3. **Install dependencies:**

```bash
pip install numpy matplotlib scipy networkx
```

> All code is compatible with **Python 3.9+**

---

## **Usage**

**Dijkstra (with visualization):**

```python
from dijkstra_graph_visualization import dijkstra
from draw_weighted_graph_path import draw_graph_with_path
from generate_random_graphs import graphe2

M = graphe2(6, 0.5, 1, 10)
distances, paths, _ = dijkstra(M, 0)
draw_graph_with_path(M, paths[5])
```

**Bellman-Ford (with custom edge ordering):**

```python
from bellman_ford_edge_traversals import pp
from bellman_ford_shortest_paths import Bellman_Ford
from graph_utils_dijkstra_bellman import transforme_parcours_en_fleche
from generate_random_graphs import graphe2

M = graphe2(6, 0.5, 1, 10)
parcours = pp(M, 0)
fleche_list = transforme_parcours_en_fleche(M, parcours)
Bellman_Ford(M, 0, fleche_list, label="DFS Traversal")
```

**Compare Dijkstra and Bellman-Ford:**

```python
import compare_dijkstra_bellman as cmp
cmp.run_experiments()
```

**Strong Connectivity Analysis:**

```python
import strong_connectivity_analysis as sc

n = 12
p = 0.5
fc_percentage = sc.test_stat_fc2(n, p)
threshold = sc.seuil(n)

sc.courbe_seuil(1, 20)
sc.courbe_seuillog(1, 20)
```

---

## **Conclusions**

* **Edge ordering** improves Bellman-Ford performance; structured traversals (DFS/BFS) outperform random
* **Dijkstra** is faster for large graphs with positive weights
* **Bellman-Ford** handles negative weights and detects negative cycles
* **Strong connectivity threshold** decreases with graph size, following a **power-law relationship**

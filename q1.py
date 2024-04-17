# 17 April 2024
#CSC461 – Assignment3 – IDS – Graph Analysis
# Saif ur Rehman
# FA20-BSE-109
# This task combines graph creation, visualization, loop detection, edge weight assignment, and shortest path calculation using Dijkstra's algorithm. It provides a comprehensive exercise in working with graphs and graph algorithms in Python.
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

adjacency_matrix = np.array([
    [0, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0]
])

G = nx.Graph()

for i in range(len(adjacency_matrix)):
    for j in range(i+1, len(adjacency_matrix[i])):
        if adjacency_matrix[i][j] == 1:
            G.add_edge(i, j)

nx.draw(G, with_labels=True, node_color='skyblue', node_size=1000, font_size=12)
plt.show()

loops = list(nx.selfloop_edges(G))
if loops:
    print("There is a loop in the graph at point(s):", loops)
else:
    print("There are no loops in the graph.")

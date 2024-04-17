# 17 April 2024
#CSC461 – Assignment3 – IDS – Graph Analysis
# Saif ur Rehman
# FA20-BSE-109
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
            
            weight = np.random.randint(1, 10)  
            G.add_edge(i, j, weight=weight)

nx.draw(G, with_labels=True, node_color='skyblue', node_size=1000, font_size=12)
plt.show()

shortest_path = nx.dijkstra_path(G, source=0, target=1, weight='weight')
shortest_path_length = nx.dijkstra_path_length(G, source=0, target=1, weight='weight')

print("Shortest path between nodes A and B:", shortest_path)
print("Length of the shortest path:", shortest_path_length)

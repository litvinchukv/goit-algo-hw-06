import matplotlib.pyplot as plt
import networkx as nx

# Creating a graph to represent a simple city transport network
G = nx.Graph()

# Adding nodes representing different locations in the city
nodes = [
    'Station A', 'Station B', 'Station C', 'Station D', 'Station E',
    'Station F', 'Station G', 'Station H', 'Station I'
]

G.add_nodes_from(nodes)

# Adding edges representing routes between the stations
edges = [
    ('Station A', 'Station B'), ('Station B', 'Station C'),
    ('Station C', 'Station D'), ('Station D', 'Station E'),
    ('Station E', 'Station F'), ('Station F', 'Station G'),
    ('Station G', 'Station H'), ('Station H', 'Station I'),
    ('Station I', 'Station A'), ('Station B', 'Station E'),
    ('Station D', 'Station G'), ('Station F', 'Station I')
]

G.add_edges_from(edges)

# Visualizing the graph
plt.figure(figsize=(8, 8))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=12, font_weight='bold')
plt.title('City Transport Network Graph')
plt.show()

# Analyzing main characteristics
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())

num_nodes, num_edges, degrees


# Implementing DFS and BFS to find paths in the graph

# Function to perform DFS
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for neighbor in set(graph.neighbors(vertex)) - set(path):
            if neighbor == goal:
                yield path + [neighbor]
            else:
                stack.append((neighbor, path + [neighbor]))


# Function to perform BFS
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for neighbor in set(graph.neighbors(vertex)) - set(path):
            if neighbor == goal:
                yield path + [neighbor]
            else:
                queue.append((neighbor, path + [neighbor]))


# Finding paths from 'Station A' to 'Station G' using DFS and BFS
dfs_path_list = list(dfs_paths(G, 'Station A', 'Station G'))
bfs_path_list = list(bfs_paths(G, 'Station A', 'Station G'))

# Comparing the paths found by DFS and BFS
print(dfs_path_list)
print(bfs_path_list)

import random

# Assigning random weights to edges to simulate a weighted city transport network
for (u, v) in G.edges():
    G[u][v]['weight'] = random.randint(1, 10)

# Function to find the shortest path between all pairs using Dijkstra's algorithm
def dijkstra_all_pairs(graph):
    shortest_paths = {}
    for node in graph.nodes:
        lengths = nx.single_source_dijkstra_path_length(graph, node, weight='weight')
        shortest_paths[node] = lengths
    return shortest_paths

# Finding the shortest paths between all nodes in the graph
shortest_paths = dijkstra_all_pairs(G)

import pandas as pd
shortest_paths_df = pd.DataFrame(shortest_paths)


import ace_tools_open as tools
tools.display_dataframe_to_user(name="Shortest Paths Using Dijkstra", dataframe=shortest_paths_df)

shortest_paths_df
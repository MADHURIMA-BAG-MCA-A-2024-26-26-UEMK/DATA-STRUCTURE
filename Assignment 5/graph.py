# Program to store and display a graph using Adjacency Matrix

def display_adj_matrix(graph):
    print("Adjacency Matrix:")
    for row in graph:
        print(row)

# Example Graph (Adjacency Matrix)
# Graph with 4 vertices (A, B, C, D)
graph = [
    [0, 1, 1, 0],  # A is connected to B and C
    [1, 0, 1, 1],  # B is connected to A, C, and D
    [1, 1, 0, 1],  # C is connected to A, B, and D
    [0, 1, 1, 0]   # D is connected to B and C
]

display_adj_matrix(graph)

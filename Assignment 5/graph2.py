# Program to store and display a graph using Adjacency List

def display_adj_list(graph):
    print("Adjacency List:")
    for vertex, neighbors in graph.items():
        print(f"{vertex}: {', '.join(neighbors)}")

# Example Graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

display_adj_list(graph)

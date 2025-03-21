# Program to check if a graph is complete

def is_complete(graph):
    num_vertices = len(graph)
    total_edges = sum(len(neighbors) for neighbors in graph.values()) // 2
    expected_edges = num_vertices * (num_vertices - 1) // 2

    if total_edges == expected_edges:
        return True
    return False

# Example Graph (Adjacency List)
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['A', 'B', 'C']
}

if is_complete(graph):
    print("The graph is complete")
else:
    print("The graph is not complete")

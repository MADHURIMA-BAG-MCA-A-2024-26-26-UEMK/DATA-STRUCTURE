# Program to count odd and even degree vertices in a graph

def count_odd_even_degree(graph):
    odd_count = 0
    even_count = 0

    for vertex, neighbors in graph.items():
        degree = len(neighbors)
        if degree % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print(f"Number of vertices with odd degree: {odd_count}")
    print(f"Number of vertices with even degree: {even_count}")

# Example Graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

count_odd_even_degree(graph)

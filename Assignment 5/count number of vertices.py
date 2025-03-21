# Program to count the number of vertices and edges in a graph

def count_vertices_edges(graph):
    num_vertices = len(graph)  # Number of vertices
    num_edges = sum(len(neighbors) for neighbors in graph.values()) // 2  # Count edges, divide by 2 for undirected graph
    
    print(f"Number of Vertices: {num_vertices}")
    print(f"Number of Edges: {num_edges}")

# Example Graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

count_vertices_edges(graph)

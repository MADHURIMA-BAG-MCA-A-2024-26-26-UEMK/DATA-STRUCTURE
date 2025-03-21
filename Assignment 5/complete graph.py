def is_complete_graph(graph, num_vertices):
    # Check if every vertex is connected to all other vertices
    for vertex, neighbors in graph.items():
        # Each vertex must have exactly num_vertices - 1 neighbors (connected to every other vertex)
        if len(neighbors) != num_vertices - 1:
            return False
    return True

def main():
    # Step 1: Take user input for number of vertices
    num_vertices = int(input("Enter the number of vertices: "))

    # Initialize an empty graph (Adjacency List)
    graph = {str(i): [] for i in range(num_vertices)}

    # Step 2: Take user input for edges
    num_edges = int(input("Enter the number of edges: "))
    
    print("Enter the edges as pairs of vertices (e.g., 0 1 for an edge between vertex 0 and 1):")
    
    for _ in range(num_edges):
        u, v = input().split()
        if u != v:
            graph[u].append(v)
            graph[v].append(u)  # Since it's an undirected graph

    # Step 3: Check if the graph is complete
    if is_complete_graph(graph, num_vertices):
        print("The graph is complete.")
    else:
        print("The graph is not complete.")

if __name__ == "__main__":
    main()

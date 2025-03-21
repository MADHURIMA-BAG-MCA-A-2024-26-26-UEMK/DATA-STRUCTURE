# Function to count the number of vertices and edges in the graph
def count_vertices_edges(graph):
    # Number of vertices is simply the number of keys in the graph dictionary
    num_vertices = len(graph)
    
    # Count the number of edges: sum of the lengths of all adjacency lists
    num_edges = sum(len(neighbors) for neighbors in graph.values())   
    
    print(f"Number of Vertices: {num_vertices}")
    print(f"Number of Edges: {num_edges}")

def main():
    # Input number of vertices and edges
    num_vertices = int(input("Enter the number of vertices: "))
    
    # Initialize an empty adjacency list graph
    graph = {str(i): [] for i in range(num_vertices)}

    # Input number of edges
    num_edges = int(input("Enter the number of edges: "))
    
    print("Enter the edges as pairs of vertices (e.g., 0 1 for an edge between vertex 0 and 1):")
    
    # Collect edges and update the adjacency list
    for _ in range(num_edges):
        u, v = input().split()
        if u != v:  # Prevent self-loops
            graph[u].append(v)
            graph[v].append(u)  # Since it's an undirected graph

    # Count and display the number of vertices and edges
    count_vertices_edges(graph)

if __name__ == "__main__":
    main()

# Function to count odd and even degree vertices
def count_odd_even_degree(graph):
    odd_count = 0
    even_count = 0

    # Loop through each vertex and check its degree
    for vertex, neighbors in graph.items():
        degree = len(neighbors)  # The degree is the length of the neighbor list
        if degree % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    # Display the counts
    print(f"Number of vertices with odd degree: {odd_count}")
    print(f"Number of vertices with even degree: {even_count}")

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

    # Count and display odd and even degree vertices
    count_odd_even_degree(graph)

if __name__ == "__main__":
    main()

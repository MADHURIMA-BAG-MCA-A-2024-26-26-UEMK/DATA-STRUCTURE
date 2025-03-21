# Function to detect cycle in an undirected graph using DFS
def detect_cycle(graph):
    visited = set()

    def dfs(v, parent):
        visited.add(v)  # Mark the current vertex as visited

        # Explore all neighbors of the vertex
        for neighbor in graph.get(v, []):
            # If the neighbor is not visited, continue DFS on that neighbor
            if neighbor not in visited:
                if dfs(neighbor, v):
                    return True
            # If the neighbor is visited and not the parent, a cycle is found
            elif neighbor != parent:
                return True
        return False

    # Check all vertices to ensure we cover all disconnected components
    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex, None):
                return True
    return False

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

    # Detect if the graph has a cycle
    if detect_cycle(graph):
        print("The graph contains a cycle.")
    else:
        print("The graph does not contain a cycle.")

if __name__ == "__main__":
    main()

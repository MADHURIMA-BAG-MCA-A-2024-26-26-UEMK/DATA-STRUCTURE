# Program to detect a cycle in a graph using DFS

def has_cycle(graph):
    visited = set()
    rec_stack = set()  # Recursion stack to track nodes in the current DFS path

    def dfs(v, parent):
        visited.add(v)
        rec_stack.add(v)
        
        for neighbor in graph.get(v, []):
            if neighbor not in visited:
                if dfs(neighbor, v):
                    return True
            elif neighbor != parent and neighbor in rec_stack:
                return True
        
        rec_stack.remove(v)
        return False

    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex, None):
                return True
    return False

# Example Graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

if has_cycle(graph):
    print("Graph contains a cycle")
else:
    print("Graph does not contain a cycle")

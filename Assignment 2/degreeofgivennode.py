class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to calculate the degree of a given node
def degree_of_node(node):
    degree = 0
    if node.left:
        degree += 1  # Increase degree if left child exists
    if node.right:
        degree += 1  # Increase degree if right child exists
    return degree

# Helper function to create a binary tree (optional)
def create_tree(data):
    if not data:
        return None
    root = Node(data[0])
    queue = [root]
    index = 1
    while index < len(data):
        node = queue.pop(0)
        if index < len(data):
            node.left = Node(data[index])
            queue.append(node.left)
            index += 1
        if index < len(data):
            node.right = Node(data[index])
            queue.append(node.right)
            index += 1
    return root

# Example usage:
data = [1, 2, 3, 4, 5, 6, 7]  # Example binary tree data
root = create_tree(data)

# Select a node for which you want to find the degree
# For example, let's find the degree of the node with value 2
node_to_check = root.left  # Node with value 2 (which has both left and right children)

# Calculate and display the degree of the selected node
print(f"Degree of node with value {node_to_check.data}:", degree_of_node(node_to_check))

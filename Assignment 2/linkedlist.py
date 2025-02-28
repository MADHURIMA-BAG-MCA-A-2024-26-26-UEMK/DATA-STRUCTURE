class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to count the number of nodes in a binary tree
def count_nodes_linked(root):
    if not root:  # If the tree is empty, return 0
        return 0
    # Count the current node (1) and recursively count the left and right subtrees
    return 1 + count_nodes_linked(root.left) + count_nodes_linked(root.right)

# Helper function to create a binary tree from a list (optional)
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

# Calculate and display the number of nodes in the tree
print("Number of nodes (using linked list):", count_nodes_linked(root))

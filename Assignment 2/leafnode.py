class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to count the number of leaf nodes in a binary tree
def count_leaf_nodes(root):
    if not root:  # If the tree is empty, return 0
        return 0
    if not root.left and not root.right:  # If the node is a leaf node
        return 1
    # Recursively count leaf nodes in both left and right subtrees
    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)

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

# Calculate and display the number of leaf nodes
print("Number of leaf nodes:", count_leaf_nodes(root))

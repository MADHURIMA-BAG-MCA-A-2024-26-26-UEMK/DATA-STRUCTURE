class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to count the number of internal nodes in a binary tree
def count_internal_nodes(root):
    if not root:  # If the tree is empty, return 0
        return 0
    # If the node has at least one child (either left or right), it's an internal node
    internal_node_count = 0
    if root.left or root.right:
        internal_node_count = 1
    # Recursively count internal nodes in both left and right subtrees
    return internal_node_count + count_internal_nodes(root.left) + count_internal_nodes(root.right)

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

# Calculate and display the number of internal nodes
print("Number of internal nodes:", count_internal_nodes(root))

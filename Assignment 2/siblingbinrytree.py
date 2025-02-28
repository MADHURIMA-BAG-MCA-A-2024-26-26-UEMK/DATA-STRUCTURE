class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to count the number of siblings for a given node
def count_siblings(root, key):
    if not root:
        return 0
    # If the node is the root, it has no siblings
    if root.data == key:
        return 0
    # Queue to hold nodes for level-order traversal
    queue = [root]
    while queue:
        node = queue.pop(0)
        # Check for siblings
        if node.left and node.right:
            if node.left.data == key:
                return 1 if node.right else 0
            elif node.right.data == key:
                return 1 if node.left else 0
        # Add the left and right children to the queue for further processing
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return 0

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

# Find the node whose siblings are to be counted
key = 4  # Example: Find the number of siblings of node with value 4

# Calculate and display the number of siblings
print(f"Number of siblings of node {key}:", count_siblings(root, key))

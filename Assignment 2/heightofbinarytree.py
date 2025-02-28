class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to calculate the height of a binary tree
def height_of_tree(root):
    if not root:  # If the tree is empty or the node is None, return 0
        return 0
    else:
        # Compute the height of each subtree and return the larger one plus 1
        left_height = height_of_tree(root.left)
        right_height = height_of_tree(root.right)
        return max(left_height, right_height) + 1

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

# Calculate and display the height of the tree
print("Height of the tree:", height_of_tree(root))

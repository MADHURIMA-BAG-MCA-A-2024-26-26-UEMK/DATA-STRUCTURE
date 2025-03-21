class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def min_value_node(node):
    """Find the node with the minimum value (leftmost node)."""
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete_node(root, key):
    if root is None:
        return root

    # Traverse the tree to find the node to delete
    if key < root.value:
        root.left = delete_node(root.left, key)
    elif key > root.value:
        root.right = delete_node(root.right, key)
    else:
        # Node to be deleted found
        if root.left is None and root.right is None:
            # Case 1: Node has no children (leaf node)
            root = None
        
        elif root.left is None:
            # Case 2: Node has one child (right child)
            return root.right
        
        elif root.right is None:
            # Case 2: Node has one child (left child)
            return root.left
        
        else:
            # Case 3: Node has two children
            # Get the inorder successor (smallest in the right subtree)
            temp = min_value_node(root.right)
            # Replace the value of the node to be deleted with the inorder successor
            root.value = temp.value
            # Delete the inorder successor
            root.right = delete_node(root.right, temp.value)
    
    return root

# Driver code to test the function
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

# Example usage
root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

print("Before deletion (in-order traversal):")
inorder_traversal(root)  # Output: 20 30 40 50 60 70 80
print()

# Let's delete a node (e.g., node 60)
key_to_delete = 60
root = delete_node(root, key_to_delete)

print("After deletion (in-order traversal):")
inorder_traversal(root)  # Output: 20 30 40 50 70 80

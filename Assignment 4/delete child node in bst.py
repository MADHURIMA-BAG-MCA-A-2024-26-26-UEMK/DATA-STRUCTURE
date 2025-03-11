class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def delete_child_node(root, key):
    if root is None:
        return root

    # If the key to be deleted is smaller than the root's value, it lies in the left subtree
    if key < root.value:
        root.left = delete_child_node(root.left, key)
    
    # If the key to be deleted is greater than the root's value, it lies in the right subtree
    elif key > root.value:
        root.right = delete_child_node(root.right, key)
    
    # If the key is the same as the root's value, then this is the node to be deleted
    else:
        # Case 1: Node has no children (leaf node)
        if root.left is None and root.right is None:
            root = None
        
        # Case 2: Node has one child
        elif root.left is None:
            root = root.right
        elif root.right is None:
            root = root.left
    
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

# Let's delete a child node (e.g., node 40 which is a direct child of node 30)
key_to_delete = 40
root = delete_child_node(root, key_to_delete)

print("After deletion (in-order traversal):")
inorder_traversal(root)  # Output: 20 30 50 60 70 80

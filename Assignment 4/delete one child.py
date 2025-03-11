class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def delete_node_one_child(root, key):
    if root is None:
        return root

    # Traverse the tree to find the node to delete
    if key < root.value:
        root.left = delete_node_one_child(root.left, key)
    elif key > root.value:
        root.right = delete_node_one_child(root.right, key)
    else:
        # Node to be deleted found
        # Case 1: Node has one child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
    
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

print("Before deletion (in-order traversal):")
inorder_traversal(root)  # Output: 20 30 50 70
print()

# Let's delete a node having one child (node 30, which has one child: 20)
key_to_delete = 30
root = delete_node_one_child(root, key_to_delete)

print("After deletion (in-order traversal):")
inorder_traversal(root)  # Output: 20 50 70

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def insert(root, key):
    """
    Function to insert a key into a BST. 
    It ensures that the property of BST is maintained.
    """
    if root is None:
        return Node(key)
    else:
        if key < root.value:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def inorder(root):
    """
    Function for in-order traversal of the BST. 
    It prints the values of the nodes in ascending order.
    """
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

# Driver Code

# Create an initial BST
root = Node(50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

# Insert a specific element into the BST
root = insert(root, 55)

# Display the BST after insertion (in-order traversal)
print("In-order Traversal of BST after inserting 55:")
inorder(root)

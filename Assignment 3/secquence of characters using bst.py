class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def insert(root, key):
    """
    Function to insert a key into the BST. 
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

# Take user input for name
name = input("Enter your name: ")

# Create an empty BST
root = None

# Insert each character of the name into the BST
for char in name:
    root = insert(root, char)

# Display the sorted sequence of characters using BST (in-order traversal)
print("Sorted sequence of characters using BST:")
inorder(root)

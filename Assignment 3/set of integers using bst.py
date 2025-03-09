class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.value:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

# Driver Code
numbers = [50, 30, 20, 40, 70, 60, 80]
root = None
for num in numbers:
    root = insert(root, num)

print("Sorted integers using BST:")
inorder(root)

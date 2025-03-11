class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def search_bst(root, key):
    # Base cases: root is null or key is present at the root
    if root is None or root.value == key:
        return root
    
    # Key is greater than root's value
    if key > root.value:
        return search_bst(root.right, key)
    
    # Key is smaller than root's value
    return search_bst(root.left, key)

# Driver code to test the above function
root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

key = 40
found_node = search_bst(root, key)
if found_node:
    print(f"Node {key} found in the BST.")
else:
    print(f"Node {key} not found in the BST.")

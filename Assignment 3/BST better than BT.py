# Binary Tree Example
class BinaryTreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def inorder_btree(root):
    if root:
        inorder_btree(root.left)
        print(root.value, end=" ")
        inorder_btree(root.right)

# BST Example
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def insert_bst(root, key):
    if root is None:
        return Node(key)
    if key < root.value:
        root.left = insert_bst(root.left, key)
    else:
        root.right = insert_bst(root.right, key)
    return root

# Driver Code for Binary Tree
root_btree = BinaryTreeNode(50)
root_btree.left = BinaryTreeNode(30)
root_btree.right = BinaryTreeNode(70)
root_btree.left.left = BinaryTreeNode(20)
root_btree.left.right = BinaryTreeNode(40)
root_btree.right.left = BinaryTreeNode(60)
root_btree.right.right = BinaryTreeNode(80)

# Driver Code for BST
root_bst = Node(50)
root_bst = insert_bst(root_bst, 30)
root_bst = insert_bst(root_bst, 20)
root_bst = insert_bst(root_bst, 40)
root_bst = insert_bst(root_bst, 70)
root_bst = insert_bst(root_bst, 60)
root_bst = insert_bst(root_bst, 80)

# In-order Traversal of Binary Tree (No specific order)
print("Binary Tree In-order Traversal:")
inorder_btree(root_btree)

# In-order Traversal of BST (Sorted order)
print("\nBST In-order Traversal:")
inorder_btree(root_bst)

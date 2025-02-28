class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def create_tree_from_array(arr):
    if not arr:
        return None
    root = Node(arr[0])
    queue = [root]
    index = 1
    while index < len(arr):
        node = queue.pop(0)
        if index < len(arr):
            node.left = Node(arr[index])
            queue.append(node.left)
            index += 1
        if index < len(arr):
            node.right = Node(arr[index])
            queue.append(node.right)
            index += 1
    return root

def level_order_traversal(root):
    if not root:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.data, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

arr = [1, 2, 3, 4, 5, 6, 7]
root = create_tree_from_array(arr)
print("Level-wise traversal (Array-based):")
level_order_traversal(root)

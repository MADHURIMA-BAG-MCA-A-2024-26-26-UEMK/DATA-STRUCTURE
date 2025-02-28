class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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

data = [1, 2, 3, 4, 5, 6, 7]
root = create_tree(data)
print("Level-wise traversal (Recursive):")
level_order_traversal(root)

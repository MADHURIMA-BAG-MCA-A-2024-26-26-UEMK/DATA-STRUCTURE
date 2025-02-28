def height_of_tree(root):
    if not root:
        return 0
    left_height = height_of_tree(root.left)
    right_height = height_of_tree(root.right)
    return max(left_height, right_height) + 1

root = create_tree([1, 2, 3, 4, 5, 6, 7])
print("Height of tree:", height_of_tree(root))

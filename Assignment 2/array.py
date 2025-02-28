# Function to count the number of nodes in a binary tree (using array)
def count_nodes_array(arr):
    return len(arr)  # The number of nodes is the length of the array

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7]  # Example binary tree data (level order representation)

# Calculate and display the number of nodes
print("Number of nodes (using array):", count_nodes_array(arr))

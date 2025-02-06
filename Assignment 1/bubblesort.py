def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all elements in the list
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

# Dataset
data = [27, 15, 39, 21, 28, 70]

# Sorting the dataset using bubble sort
sorted_data = bubble_sort(data)

print("Sorted dataset:", sorted_data)

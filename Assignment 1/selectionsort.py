def selection_sort(arr):
    n = len(arr)
    
    # Traverse through all elements in the list...
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

# Dataset
data = [27, 15, 39, 21, 28, 70]

# Sorting the dataset using selection sort
sorted_data = selection_sort(data)

print("Sorted dataset:", sorted_data)

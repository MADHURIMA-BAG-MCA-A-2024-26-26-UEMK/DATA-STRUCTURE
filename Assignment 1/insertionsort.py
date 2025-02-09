def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place the key after finding the correct position
        arr[j + 1] = key
    
    return arr

# Dataset
data = [27, 15, 39, 21, 28, 70]

# Sorting the dataset using insertion sort
sorted_data = insertion_sort(data)
print("Sorted dataset:", sorted_data)

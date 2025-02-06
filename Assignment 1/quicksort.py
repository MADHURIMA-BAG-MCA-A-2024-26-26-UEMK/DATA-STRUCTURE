def quick_sort(arr):
    # Base case: If the array has one or no elements, it's already sorted
    if len(arr) <= 1:
        return arr
    else:
        # Choose a pivot (in this case, the last element)
        pivot = arr[-1]
        
        # Partition the array into two subarrays: one with elements less than the pivot,
        # and one with elements greater than or equal to the pivot
        left = [x for x in arr[:-1] if x < pivot]
        right = [x for x in arr[:-1] if x >= pivot]
        
        # Recursively apply quick_sort to the left and right subarrays, then concatenate the results
        return quick_sort(left) + [pivot] + quick_sort(right)

# Dataset
data = [27, 15, 39, 21, 28, 70]

# Sorting the dataset using quick sort
sorted_data = quick_sort(data)

print("Sorted dataset:", sorted_data)

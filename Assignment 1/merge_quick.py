import random
import time

# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        merge_sort(left_half)
        merge_sort(right_half)
        
        i = j = k = 0
        
        # Merging the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        # Copy remaining elements
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            
    return arr

# Quick Sort Implementation
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x < pivot]
    right = [x for x in arr[:-1] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

# Generate a random dataset for testing
data_size = 1000
dataset = random.sample(range(1, 10001), data_size)  # Generate a random list of 1000 unique numbers

# Measure time for Merge Sort
merge_sort_data = dataset.copy()
start_time = time.time()
merge_sort(merge_sort_data)
merge_sort_time = time.time() - start_time

# Measure time for Quick Sort
quick_sort_data = dataset.copy()
start_time = time.time()
quick_sort(quick_sort_data)
quick_sort_time = time.time() - start_time

# Display the results
print(f"Time taken by Merge Sort: {merge_sort_time:.6f} seconds")
print(f"Time taken by Quick Sort: {quick_sort_time:.6f} seconds")

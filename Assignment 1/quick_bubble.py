import random
import time

# Bubble Sort Implementation
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Quick Sort Implementation
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]
        left = [x for x in arr[:-1] if x < pivot]
        right = [x for x in arr[:-1] if x >= pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

# Generate a random dataset for testing
data_size = 1000
dataset = random.sample(range(1, 10001), data_size)  # Generate a random list of 1000 unique numbers

# Measure time for Bubble Sort
bubble_sort_data = dataset.copy()
start_time = time.time()
bubble_sort(bubble_sort_data)
bubble_sort_time = time.time() - start_time

# Measure time for Quick Sort
quick_sort_data = dataset.copy()
start_time = time.time()
quick_sort(quick_sort_data)
quick_sort_time = time.time() - start_time

# Display the results
print(f"Time taken by Bubble Sort: {bubble_sort_time:.6f} seconds")
print(f"Time taken by Quick Sort: {quick_sort_time:.6f} seconds")

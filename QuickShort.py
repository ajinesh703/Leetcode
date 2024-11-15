def quick_sort(arr):
    # Base case: if the array has 1 or zero elements, it is already sorted
    if len(arr) <= 1:
        return arr
    else:
        # Choosing the pivot (commonly the last element)
        pivot = arr[-1]
        
        # Partitioning the array into two sub-arrays
        left = [x for x in arr[:-1] if x <= pivot]  # Elements less than or equal to pivot
        right = [x for x in arr[:-1] if x > pivot]   # Elements greater than pivot
        
        # Recursively sorting the sub-arrays and combining them with the pivot
        return quick_sort(left) + [pivot] + quick_sort(right)

# Example usage
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)

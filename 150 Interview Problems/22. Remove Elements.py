def removeElement(nums, val):
    # Pointer to track the position of the next valid element
    k = 0
    
    # Iterate through each number in the array
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]  # Move the valid number forward
            k += 1  # Increment the length of the result

    return k  # New length after removal

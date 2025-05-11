def removeDuplicates(nums):
    # If the array has 2 or fewer elements, it's already valid
    if len(nums) <= 2:
        return len(nums)

    # Pointer to place the next valid element
    k = 2

    # Iterate from the 3rd element onwards
    for i in range(2, len(nums)):
        # Compare current element with the element at k-2
        if nums[i] != nums[k - 2]:
            nums[k] = nums[i]  # Place it at the correct spot
            k += 1  # Increment the valid length

    return k  # Final length with at most two duplicates

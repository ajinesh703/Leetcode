def sortColors(nums):
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:  # Move 0 to the beginning
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:  # Keep 1 in place
            mid += 1
        else:  # Move 2 to the end
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

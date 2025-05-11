def merge(nums1, m, nums2, n):
    # Set pointers for nums1 and nums2 respectively
    p1 = m - 1  # Last element in the meaningful portion of nums1
    p2 = n - 1  # Last element in nums2

    # Start from the end of nums1 where the merged elements should go
    for i in range(m + n - 1, -1, -1):
        if p2 < 0:  # All elements from nums2 have been merged
            break
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[i] = nums1[p1]  # Move the larger one
            p1 -= 1
        else:
            nums1[i] = nums2[p2]
            p2 -= 1

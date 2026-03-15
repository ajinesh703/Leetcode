from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)          # hi = n, not n-1

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] < target:
                lo = mid + 1           # mid is too small, go right
            else:
                hi = mid               # mid >= target, could be answer

        return lo                      # no -1 check needed, always valid

from typing import *


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums: List[int] = [nums[0]]
        for i in range(1, len(nums)):
            sums.append(nums[i] + (sums[i - 1] if sums[i - 1] > 0 else 0))
        return max(sums)

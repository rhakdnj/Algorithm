from typing import *


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return nums

        r = []
        for i in range(len(nums) - k + 1):
            r.append(max(nums[i:i + k]))
        return r


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    solution.maxSlidingWindow(nums, k)
    
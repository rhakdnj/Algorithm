from typing import *


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        total = 0
        pair = []
        nums.sort()

        for i, n in enumerate(nums):
            if i % 2 == 0:
                total += n
        return total


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 4, 3, 2]
    res = solution.arrayPairSum(nums)
    print(res)

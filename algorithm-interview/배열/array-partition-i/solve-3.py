from typing import *


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 4, 3, 2]
    res = solution.arrayPairSum(nums)
    print(res)
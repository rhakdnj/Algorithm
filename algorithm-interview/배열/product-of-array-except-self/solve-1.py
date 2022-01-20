from typing import *


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        # 왼쪽 곱셈
        for i in range(len(nums)):
            out.append(p)
            p *= nums[i]
        p = 1
        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i] = out[i] * p
            p *= nums[i]
        return out


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4]
    res = solution.productExceptSelf(nums)
    print(res)
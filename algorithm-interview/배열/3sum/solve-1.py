from typing import *


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()     # 4 - 1 -1 0 1 2

        for i in range(len(nums) - 2):
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                for k in range(j + 1, len(nums)):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        results.append([nums[i], nums[j], nums[k]])

        return results
                

if __name__ == "__main__":
    solution = Solution()
    nums = [-1, 0, 1, 2, -1, 4]
    res = solution.threeSum(nums)
    print(res)


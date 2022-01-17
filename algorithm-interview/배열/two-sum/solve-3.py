from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {num: i for i, num in enumerate(nums)}

        # target 에서 첫 번째 수를 뺸 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [nums.index(num), nums_map[target - num]]


if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9

    print(solution.twoSum(nums, target))

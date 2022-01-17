from typing import *


# two-pointer 잘못된 풀이, nums 가 정렬 돼있지 않기에
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while not left == right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return [left, right]


if __name__ == "__main__":
    solution = Solution()
    nums = [3, 2, 4]
    target = 6

    print(solution.twoSum(nums, target))


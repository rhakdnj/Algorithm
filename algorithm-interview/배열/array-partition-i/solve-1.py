from typing import *


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        total = 0
        pair = []
        nums.sort()

        for n in nums:
            # 앞에서부터 오름차순으로 페어를 만들어서 계산
            pair.append(n)
            if len(pair) == 2:
                total += min(pair)
                pair = []
        return total


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 4, 3, 2]
    res = solution.arrayPairSum(nums)
    print(res)

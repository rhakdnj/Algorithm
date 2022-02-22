import sys
from typing import *


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = -sys.maxsize
        cur_sum = 0
        for num in nums:
            cur_sum = max(num, cur_sum + nums)
            best_sum = max(best_sum, cur_sum)
        return best_sum

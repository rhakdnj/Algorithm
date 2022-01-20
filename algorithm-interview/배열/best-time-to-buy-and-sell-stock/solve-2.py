import sys
from typing import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        # 최솟값과 최대값을 계속 갱신
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit


if __name__ == "__main__":
    solution = Solution()
    sample = [7, 1, 5, 3, 6, 4]
    res = solution.maxProfit(sample)
    print(res)

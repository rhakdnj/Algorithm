from typing import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0

        for i, price in enumerate(prices):
            for j in range(i, len(prices)):
                max_price = max(prices[j] - price, max_price)

        return max_price


if __name__ == "__main__":
    solution = Solution()
    sample = [7, 1, 5, 3, 6, 4]
    res = solution.maxProfit(sample)
    print(res)

"""
a = [1]
b = [2, 3]
a += b
a -> [1, 2, 3]

a += b,
a -> [1, [2, 3]]

a += [b]
a -> [1, [2, 3]]
"""

from typing import *


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        for i in sorted(intervals, key=lambda x: x[0]):
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged += i,

        return merged


if __name__ == '__main__':
    solution = Solution()
    interval = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(solution.merge(interval))
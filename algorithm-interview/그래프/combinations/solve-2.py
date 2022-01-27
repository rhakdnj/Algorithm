from typing import *
from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(map(list, combinations(range(1, n+1), k)))


if __name__ == "__main__":
    solution = Solution()
    n, k = map(int, input().split())
    print(solution.combine(n, k))

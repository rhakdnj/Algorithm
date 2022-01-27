from typing import *


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(elements: List, start: int, k: int):
            if k == 0:
                results.append(elements[:])

            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return results


if __name__ == "__main__":
    solution = Solution()
    n, k = map(int, input().split())
    print(solution.combine(n, k))

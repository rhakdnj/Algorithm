from typing import *


class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(csum, index, path):
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return

            for i in range(index, len(candidates)):
                dfs(csum-candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return result


if __name__ == "__main__":
    solution = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    solution.combinationSum(candidates, target)

from typing import *


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(index, path):
            # Add result each time
            result.append(path)

            # DFS by creating a path
            for i in range(index, len(nums)):
                dfs(i + 1, path + nums[i])

        dfs(0, [])
        return result


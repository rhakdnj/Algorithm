from typing import *


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(i, j):
            # Exit when no longer on land
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) \
                    or grid[i][j] != '1':
                return

            grid[i][j] = 0
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count


if __name__ == '__main__':
    solution = Solution()
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    islands = solution.numIslands(grid)
    print(islands)



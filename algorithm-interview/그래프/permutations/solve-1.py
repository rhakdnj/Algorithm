from typing import *


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            # Add result when leaf node
            if len(elements) == 0:
                results.append(prev_elements[:])

            # Permutation creation recursive call
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return results


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3]
    print(solution.permute(nums))

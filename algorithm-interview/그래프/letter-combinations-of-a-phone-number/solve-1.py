from typing import *


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        def dfs(index, path):

            # Backtracking if navigating to the end
            if len(path) == len(digits):
                res.append(path)
                return

            # Repeat input digit by digit
            for i in range(index, len(digits)):
                # Repeat all strings that match a number
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)

        # exception handling
        if not digits:
            return []

        dic = {'2': "abc",
               '3': "def",
               '4': 'ghi',
               '5': 'jkl',
               '6': 'mno',
               '7': 'pqrs',
               '8': 'tuv',
               '9': 'wxyz',
               }
        res = []
        dfs(0, "")

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations("23"))








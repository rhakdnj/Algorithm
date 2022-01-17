import collections
from typing import *


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # value 값은 list
        anagrams = collections.defaultdict(list)

        for word in strs:
            # dictionary 추가 하는 기능은 dict()로 구현 x
            # dict[key] = value
            anagrams[''.join(sorted(word))].append(word)
        return anagrams.values()


if __name__ == "__main__":
    solution = Solution()
    strs = ["eat", "ate", "tan", "tea", "nat", "bat"]

    print(list(solution.groupAnagrams(strs)))

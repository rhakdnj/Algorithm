import collections
import re
from typing import *


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'^\w', '', paragraph).lower().split() if word not in banned]

        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]


if __name__ == "__main__":
    solution = Solution()
    paragraph = "Bob hit a ball, the hit Ball flew far after it was hit"
    banned = ["hit"]

    print(solution.mostCommonWord(paragraph, banned))
import collections
import heapq
from typing import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        freqs_heap = []

        # insert negative number into heap
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))

        topk = list()

        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])

        return topk


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 3
    print(solution.topKFrequent(nums, k))

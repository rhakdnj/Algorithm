import heapq
from typing import *


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        # 키 역순, 인덱스 삽입
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))

        result = []
        # 키 역순, 인덱스 추출
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])

        return result


solution = Solution()
people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
queue = solution.reconstructQueue(people)
print(queue)
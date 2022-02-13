import collections
import heapq
from typing import *


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        # 큐 변수: [(가격, 정점, 남은 가능 경유지 수)]
        Q = [(0, src, K)]

        # 우선순위 큐 최솟갑 기준으로 도착점까지 최소 비용 판별
        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if k >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, k - 1))
        return -1


if __name__ == "__main__":
    solution = Solution()
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    n = 3
    K = 0
    src = 0
    dst = 2
    ans = solution.findCheapestPrice(n, flights, src, dst, K)
    print(ans)

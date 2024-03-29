import collections
import heapq
from typing import *


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 그래프 인접 리스트 구성
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        # graph = {i: [] for i in range(1, n+1)}
        # for u, v, w in times:
        #     graph[u].append((v, w))

        # 큐 변수: [(소요 시간, 정점)]
        Q = [(0, k)]
        dist = collections.defaultdict(int)

        # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))

        # 모든 노드의 최단 경로 존재 여부 판별
        if len(dist) == n:
            return max(dist.values())
        return -1


if __name__ == "__main__":
    solution = Solution()
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2
    ans = solution.networkDelayTime(times, n, k)
    print(ans)
        

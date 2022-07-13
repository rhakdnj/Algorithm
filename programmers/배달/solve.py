from typing import List, Tuple
from heapq import heappop, heappush

INF = int(1e9)


def solution(N: int, road: List[List], K: int) -> int:
    answer = 0
    graph: List[List[Tuple]] = [[] for _ in range(N + 1)]
    distance = [INF] * (N + 1)

    for r in road:
        a, b, c = r[0], r[1], r[2]
        graph[a].append((b, c))
        graph[b].append((a, c))

    def dijkstra(start):
        q = []
        heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, now = heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heappush(q, (cost, i[0]))

    dijkstra(1)

    for i in range(1, N + 1):
        if distance[i] == INF:
            continue
        if distance[i] <= K:
            answer += 1

    return answer

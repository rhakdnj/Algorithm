# https://www.acmicpc.net/problem/18352
# 특정 거리의 도시 찾기
import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n, m, k, x = map(int, input().split())
graph = [[] for i in range(n + 1)]
for _ in range(m):
    A, B = map(int, input().split())
    graph[A].append(B)

distance = [0] * (n + 1)
visited = [False] * (n + 1)


def bfs(start: int) -> None:
    answer = []
    q = deque([start])
    visited[start] = True
    distance[start] = 0
    while q:
        curr = q.popleft()
        for i in graph[curr]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                distance[i] = distance[curr] + 1
                if distance[i] == k:
                    answer.append(i)
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i)


bfs(x)

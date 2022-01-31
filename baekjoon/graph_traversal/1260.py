import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


# Depth First Search
def dfs(x):
    print(x, end=' ')
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            dfs(i)


# Breadth First Search
def bfs(x):
    visited[x] = True
    queue = deque([x])
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m, v = map(int, input().split())
graph = {i: [] for i in range(1, n+1)}

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
else:
    for i in range(1, len(graph) + 1):
        graph[i].sort()

    visited = [False] * (n + 1)
    dfs(v)
    print()
    visited = [False] * (n + 1)
    bfs(v)




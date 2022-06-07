import sys
from collections import defaultdict

sys.setrecursionlimit(5000)
def input():
    return sys.stdin.readline().rstrip()


def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)


n, m = map(int, input().split())  # 정점의 개수 N과 간선의 개수 M
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)
answer = 0

for i in range(1, n + 1):
    if not visited[i]:
        if not graph[i]:
            visited[i] = True
            answer += 1
        else:
            dfs(i)
            answer += 1

print(answer)

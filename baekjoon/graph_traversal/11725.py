import sys
sys.setrecursionlimit(10 ** 9)


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
graph = {i: [] for i in range(1, n+1)}
parents = [0] * (n + 1)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(start, graph, parents):
    for i in graph[start]:
        if parents[i] == 0:
            parents[i] = start
            dfs(i, graph, parents)


dfs(1, graph, parents)
for i in range(2, n+1):
    print(parents[i])

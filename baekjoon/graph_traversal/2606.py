# https://www.acmicpc.net/problem/2606
# dfs

import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


def dfs(v, graph, visited=[]):
    visited.append(v)
    for i in graph[v]:
        if i not in visited:
            visited = dfs(i, graph, visited)
    return visited


n = int(input())
edges = int(input())
graph = defaultdict(list)

for _ in range(edges):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

res = len(dfs(1, graph)) - 1
print(res)

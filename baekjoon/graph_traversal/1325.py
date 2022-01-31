import sys


def input():
    return sys.stdin.readline().rstrip()


n, m = map(int, input().split())
graph = {i: [] for i in range(1, n+1)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)


def dfs(start) -> int:
    discovered = []
    stack = [start]
    cnt = 1
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
                cnt += 1
    return cnt


result = []
max_cnt = 0
for i in range(1, n + 1):
    cnt = dfs(i)
    if cnt > max_cnt:
        max_cnt = cnt
    result.append((i, cnt))
else:
    for i, cnt in result:
        if cnt == max_cnt:
            print(i, end=' ')


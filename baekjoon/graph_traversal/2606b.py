n = int(input())
edge_cnt = int(input())
visited = [False] * (n + 1)
graph = {i: [] for i in range(1, n + 1)}
cnt = 0

for _ in range(edge_cnt):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)


def dfs(v):
    global cnt
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            cnt += 1
            dfs(i)


dfs(1)
print(cnt)

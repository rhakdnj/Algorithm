T = int(input())


def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    if graph[x][y] == 0:
        return False
    if graph[x][y]:
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True


for _ in range(T):
    N, M, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    visited = []
    cnt = 0
    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1
        visited.append((x, y))

    for x, y in visited:
        if dfs(x, y):
            cnt += 1

    print(cnt)
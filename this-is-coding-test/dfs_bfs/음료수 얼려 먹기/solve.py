n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]


def dfs(x, y):
    if x < 0 or x >= len(graph) or y < 0 or y >= len(graph):
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 상, 하, 좌, 우
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


answer = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            answer += 1
print(answer)

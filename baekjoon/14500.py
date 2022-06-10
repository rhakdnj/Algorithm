import sys

sys.setrecursionlimit(5000)


def input():
    return sys.stdin.readline().rstrip()


def dfs(x, y, idx, total):
    global answer
    if answer >= total + max_val * (3 - idx):
        return
    if idx == 3:
        answer = max(answer, total)
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if idx == 1:
                    visited[nx][ny] = 1
                    dfs(x, y, idx + 1, total + graph[nx][ny])
                    visited[nx][ny] = 0
                visited[nx][ny] = 1
                dfs(nx, ny, idx + 1, total + graph[nx][ny])
                visited[nx][ny] = 0


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
answer = 0
max_val = max(map(max, graph))
# 가로 4개, 가로 2 + 세로 2, 세로3 + 가로1,

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 0, graph[i][j])
        visited[i][j] = 0

print(answer)

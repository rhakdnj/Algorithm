import sys

sys.setrecursionlimit(5000)


def input():
    return sys.stdin.readline().rstrip()


def dfs(x, y):
    global answer, graph
    graph[x][y] = 0
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if graph[nx][ny]:
                dfs(nx, ny)


# 상,하, 좌, 우, 대각선 4방향(왼쪽 위, 왼쪽 아래, 오른쪽 아래, 오른쪽 위)
dx, dy = (-1, 1, 0, 0, -1, 1, 1, -1), (0, 0, -1, 1, -1, -1, 1, 1)

while True:
    answer = 0
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    graph = [[] for _ in range(m)]
    for i in range(m):
        graph[i] = list(map(int, input().split()))

    for i in range(m):
        for j in range(n):
            if graph[i][j]:
                dfs(i, j)
                answer += 1

    print(answer)

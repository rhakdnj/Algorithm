import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def bfs(x, y):
    queue = deque[(x, y)]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n - 1][m - 1]


n, m = map(int, input().split())
# 4 * 6
graph = [list(map(int, input())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
print(bfs(0, 0))

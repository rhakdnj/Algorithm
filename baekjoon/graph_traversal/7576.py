"""
여러 곳에서 동시에 bfs 할 때
"""


from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()
answer = 0

# 여러 곳에서 동시에 bfs 할 때 먼저 q에 넣어준다.
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j))


def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == -1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))


bfs()
for row in graph:
    if 0 in row:
        print(-1)
        exit(0)
    answer = max(max(row), answer)

print(answer - 1)

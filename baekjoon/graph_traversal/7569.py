from collections import deque


def checkMap():
    for z in range(h):
        for i in range(n):
            for j in range(m):
                if graph[z][i][j] == 0:
                    return False
    return True


def bfs():
    while q:
        item = q.popleft()
        z, x, y = item[0]
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or ny < 0 or nz < 0 or nx >= n or ny >= m or nz >= h:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                q.append((nz, nx, ny), item[1] + 1)
    if checkMap():
        return q[1]
    return -1


m, n, h = map(int, input().split())
graph = []
dx = [-1, 0, 1, 0, 0, 0]
dy = [0, -1, 0, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

q = deque()
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

for z in range(h):
    for i in range(n):
        for j in range(m):
            if graph[z][i][j] == 1:
                q.append(((z, i, j), 0))

answer = bfs()
print(answer)

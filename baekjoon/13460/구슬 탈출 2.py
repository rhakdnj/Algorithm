from collections import deque

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
dy, dx = (-1, 0, 1, 0), (0, 1, 0, -1)
visited = [[[[0 for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
ry, rx, by, bx = 0, 0, 0, 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            ry, rx = i, j
        if arr[i][j] == 'B':
            by, bx = i, j


def move(y, x, dy, dx):
    cnt = 0
    while arr[y + dy][x + dx] != '#' and arr[y][x] != 'O':
        y += dy
        x += dx
        cnt += 1
    return y, x, cnt


def bfs():
    dq = deque()
    dq.append((ry, rx, by, bx, 1))
    visited[ry][rx][by][bx] = 1
    while len(dq):
        r_y, r_x, b_y, b_x, depth = dq.popleft()
        if depth > 10:
            break
        for i in range(4):
            r_ny, r_nx, r_cnt = move(r_y, r_x, dy[i], dx[i])
            b_ny, b_nx, b_cnt = move(b_y, b_x, dy[i], dx[i])
            if arr[b_ny][b_nx] != 'O':
                if arr[r_ny][r_nx] == 'O':
                    return depth
                if r_ny == b_ny and r_nx == b_nx:
                    if r_cnt > b_cnt:
                        r_ny -= dy[i]
                        r_nx -= dx[i]
                    else:
                        b_ny -= dy[i]
                        b_nx -= dx[i]
                if not visited[r_ny][r_nx][b_ny][b_nx]:
                    visited[r_ny][r_nx][b_ny][b_nx] = 1
                    dq.append((r_ny, r_nx, b_ny, b_nx, depth + 1))
    return -1


print(bfs())

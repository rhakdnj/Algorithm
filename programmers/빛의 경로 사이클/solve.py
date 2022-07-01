# D, L, U, R
dx = (1, 0, -1, 0)
dy = (0, -1, 0, 1)
visited = []
n, m = 0, 0


def solution(grid):
    global visited, n, m
    n, m = len(grid), len(grid[0])
    visited = [[[False] * 4 for _ in range(m)] for _ in range(n)]
    answer = []
    for sx in range(n):
        for sy in range(m):
            for d in range(4):
                if not visited[sx][sy][d]:
                    res = simul(sx, sy, d, grid)
                    if res != 0:
                        answer.append(res)
    return sorted(answer)

def simul(sx, sy, sd, grid):
    global visited, n, m
    x, y, d = sx, sy, sd
    cnt = 0
    visited[sx][sy][sd] = True
    while True:
        x = (x + dx[d]) % n
        y = (y + dy[d]) % m
        cnt += 1
        if grid[x][y] == 'R':
            d = (d + 1) % 4
        elif grid[x][y] == 'L':
            d = (d - 1) % 4
        if visited[x][y][d]:
            if (x, y, d) == (sx, sy, sd):
                return cnt
            else:
                return 0
        visited[x][y][d] = True

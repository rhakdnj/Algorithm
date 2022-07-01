def solution(grid: list):
    n, m = len(grid), len(grid[0])
    dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
    visited = [[[0] * 4 for _ in range(m)] for _ in range(n)]

    def solve(x, y, d):
        res = 0
        while not visited[x][y][d]:
            visited[x][y][d] = 1
            x, y = (x + dx[d]) % n, (y + dy[d]) % m  # mod 계산
            if grid[x][y] == 'L':
                d = (d + 1) % 4
            elif grid[x][y] == 'R':
                d = (d - 1) % 4
            res += 1
        return res

    answer = []
    for i in range(n):
        for j in range(m):
            for k in range(4):
                if not visited[i][j][k]:
                    answer.append(solve(i, j, k))

    return sorted(answer)

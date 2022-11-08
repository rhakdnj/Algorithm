def solution(m, n, puddles):
    grid = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    if puddles:
        for a, b, in puddles:
            grid[b][a] = -1

    grid[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == j == 1:
                continue
            if grid[i][j] == -1:
                grid[i][j] = 0
                continue
            grid[i][j] = (grid[i][j - 1] + grid[i - 1][j]) % 1000000007

    return grid[n][m]

def in_range(y, x):
    return 1 <= y <= n and 1 <= x <= n


def set_flower(y, x):
    visited[y][x] = True

    cost = grid[y][x]

    for dy, dx in zip(dys, dxs):
        ny, nx = y + dy, x + dx
        visited[ny][nx] = True
        cost += grid[ny][nx]

    return cost


def can_go(y, x):
    if visited[y][x]:
        return False

    for dy, dx in zip(dys, dxs):
        ny, nx = y + dy, x + dx
        if not in_range(ny, nx) or visited[ny][nx]:
            return False

    return True


def remove_flower(y, x):
    visited[y][x] = False

    for dy, dx in zip(dys, dxs):
        ny, nx = y + dy, x + dx
        visited[ny][nx] = False


def go(cnt, total_cost):
    global ans

    if cnt == 3:
        ans = min(ans, total_cost)
        return

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if can_go(i, j):
                go(cnt + 1, total_cost + set_flower(i, j))
                remove_flower(i, j)


if __name__ == '__main__':
    n = int(input())
    grid = [[0 for _ in range(n + 1)]]
    for _ in range(n):
        grid.append([0] + list(map(int, input().split())))

    visited = [[False for _ in range(n + 1)] for _ in range(n + 1)]

    dys, dxs = (-1, 0, 1, 0), (0, 1, 0, -1)

    ans = int(1e9)

    go(0, 0)

    print(ans)

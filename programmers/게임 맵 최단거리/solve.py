from collections import deque


def solution(maps):
    dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
    n, m = len(maps), len(maps[0])

    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))

    if maps[-1][-1] != 1:
        return maps[-1][-1]
    return -1

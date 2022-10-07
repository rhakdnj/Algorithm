from collections import deque

r, c = map(int, input().split())
a = [list(input()) for _ in range(r)]
visited = [[0 for _ in range(c)] for _ in range(r)]
visited_swan = [[0 for _ in range(c)] for _ in range(r)]
swan_y, swan_x, y, x = 0, 0, 0, 0
dy, dx = (-1, 0, 1, 0), (0, 1, 0, -1)
water_dq, water_temp_dq, swan_dq, swan_temp_dq = deque(), deque(), deque(), deque()


def water_melting():
    while len(water_dq):
        y, x = water_dq.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= r or nx < 0 or nx >= c or visited[ny][nx]:
                continue
            if a[ny][nx] == 'X':
                visited[ny][nx] = 1
                water_temp_dq.append((ny, nx))
                a[ny][nx] = '.'


def move_swan() -> bool:
    global swan_dq
    while len(swan_dq):
        y, x = swan_dq.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= r or nx < 0 or nx >= c or visited_swan[ny][nx]:
                continue
            visited_swan[ny][nx] = 1
            if a[ny][nx] == '.':
                swan_dq.append((ny, nx))
            elif a[ny][nx] == 'X':
                swan_temp_dq.append((ny, nx))
            elif a[ny][nx] == 'L':
                return True
    return False


def solution():
    global water_dq, water_temp_dq, swan_y, swan_x, swan_dq, swan_temp_dq
    for i in range(r):
        for j in range(c):
            if a[i][j] == 'L':
                swan_y, swan_x = i, j
            if a[i][j] == '.' or a[i][j] == 'L':
                visited[i][j] = 1
                water_dq.append((i, j))

    swan_dq.append((swan_y, swan_x))
    visited_swan[swan_y][swan_x] = 1
    day = 0
    while True:
        if move_swan():
            break
        water_melting()
        water_dq = water_temp_dq
        swan_dq = swan_temp_dq
        water_temp_dq = deque()
        swan_temp_dq = deque()
        day += 1
    print(day)

    return


solution()

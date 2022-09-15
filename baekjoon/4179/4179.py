"""
https://www.acmicpc.net/problem/4179
불!
"""
from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()
R, C = 0, 0
dy, dx = (-1, 0, 1, 0), (0, 1, 0, -1)
INF = 1e9


# #: 벽 , .: 지나갈 수 있는 공간, J: 지훈 초기 위치, F: 불이 난 공간
def solution(r: int, c: int):
    global R, C
    R, C = r, c
    arr = [list(input()) for _ in range(R)]
    fire_check = [[INF] * C for _ in range(R)]
    man_check = [[INF] * C for _ in range(R)]

    dq = deque()
    sy, sx = 0, 0
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'F':
                fire_check[i][j] = 1
                dq.append((i, j))
            elif arr[i][j] == 'J':
                sy, sx = i, j

    while dq:
        y, x = dq.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or nx < 0 or ny >= R or nx >= C:
                continue
            if fire_check[ny][nx] != INF or arr[ny][nx] == '#':
                continue
            fire_check[ny][nx] = fire_check[y][x] + 1
            dq.append((ny, nx))

    ret = 0
    man_check[sy][sx] = 1
    dq.append((sy, sx))
    while dq:
        y, x = dq.popleft()

        # 종료 조건
        if y == 0 or x == 0 or y == R - 1 or x == C - 1:
            ret = man_check[y][x]
            break

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or nx < 0 or ny >= R or nx >= C:
                continue
            if man_check[ny][nx] != INF or arr[ny][nx] == '#':
                continue
            if man_check[y][x] + 1 >= fire_check[ny][nx]:
                continue
            man_check[ny][nx] = man_check[y][x] + 1
            dq.append((ny, nx))

    if ret == 0:
        print("IMPOSSIBLE")
    else:
        print(ret)


solution(*map(int, input().split()))

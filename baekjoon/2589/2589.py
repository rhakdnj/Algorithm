"""
https://www.acmicpc.net/problem/2589
보물섬
"""
from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()
dy, dx = (-1, 0, 1, 0), (0, 1, 0, -1)
N, M = 0, 0
arr, visited = [], []
ret = 0


def bfs(y: int, x: int) -> None:
    global N, M, arr, visited, dy, dx, ret

    visited[y][x] = 1
    dq = deque([(y, x)])
    while dq:
        y, x = dq.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= M:
                continue
            if visited[ny][nx] or arr[ny][nx] == 'W':
                continue
            visited[ny][nx] = visited[y][x] + 1
            dq.append((ny, nx))
            ret = max(ret, visited[ny][nx])


# 육지 L, 바다 W
def solution(n, m):
    global N, M, arr, visited, ret

    N, M = n, m
    arr = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'L':
                visited = [[0] * M for _ in range(N)]
                bfs(i, j)
    print(ret - 1)


solution(*map(int, input().split()))

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


def bfs(y: int, x: int) -> int:
    global N, M, arr, visited, dy, dx

    visited[y][x] = 1
    dq = deque([(y, x)])
    cnt = 0
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
            cnt = max(cnt, visited[ny][nx])
    return cnt - 1


# 육지 L, 바다 W
def solution(n, m):
    global N, M, arr, visited

    N, M = n, m
    arr = [list(input()) for _ in range(N)]

    ret = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'L':
                visited = [[0] * M for _ in range(N)]
                ret = max(ret, bfs(i, j))
    print(ret)


solution(*map(int, input().split()))

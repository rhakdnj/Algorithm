"""
https://www.acmicpc.net/problem/2178
미로 탐색
"""
from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]
dy, dx = (-1, 0, 1, 0), (0, 1, 0, -1)


def bfs(y, x):
    global n, m, arr, dy, dx
    dq = deque([(y, x)])
    while dq:
        y, x = dq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= m or arr[ny][nx] == 0: continue
            if arr[ny][nx] != 1: continue
            arr[ny][nx] = arr[y][x] + 1
            dq.append((ny, nx))


def solution():
    global arr
    bfs(0, 0)
    print(arr[n - 1][m - 1])


solution()

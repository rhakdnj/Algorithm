"""
https://www.acmicpc.net/problem/2468
안전 영역
"""
import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = []


def dfs(y, x, h) -> None:
    global n, arr, visited
    dy, dx = (-1, 0, 1, 0), (0, 1, 0, -1)
    visited[y][x] = 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or ny >= n or nx >= n: continue
        if not visited[ny][nx] and arr[ny][nx] > h: dfs(ny, nx, h)
    return


def solution():
    global n, arr, visited

    ret = 0
    for h in range(1, 101):
        visited = [[0] * n for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if arr[i][j] > h and not visited[i][j]:
                    dfs(i, j, h)
                    cnt += 1
        ret = max(ret, cnt)
    print(ret)


solution()

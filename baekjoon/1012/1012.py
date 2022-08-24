"""
https://www.acmicpc.net/problem/1012
유기농 배추
"""
import sys

sys.setrecursionlimit(10000)
input = lambda: sys.stdin.readline().rstrip()

arr = []
visited = []
dy, dx = (-1, 0, 1, 0), (0, 1, 0, -1)
n, m = 0, 0


def dfs(y, x) -> None:
    global visited, dy, dx, n, m
    visited[y][x] = 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or ny >= n or nx >= m: continue
        if arr[ny][nx] == 0 or visited[ny][nx]: continue
        dfs(ny, nx)
    return


def solution() -> None:
    global arr, visited, n, m
    t = int(input())
    for _ in range(t):
        ret = 0
        m, n, k = map(int, input().split())
        arr = [[0] * m for _ in range(n)]
        visited = [[0] * m for _ in range(n)]

        for _ in range(k):
            x, y = map(int, input().split())
            arr[y][x] = 1

        for i in range(n):
            for j in range(m):
                if arr[i][j] == 1 and not visited[i][j]:
                    dfs(i, j)
                    ret += 1
        print(ret)
    return


solution()

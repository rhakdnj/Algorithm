"""
https://www.acmicpc.net/problem/2583
영역 구하기
"""
import sys

sys.setrecursionlimit(10 ** 6)
input = lambda: sys.stdin.readline().rstrip()

m, n, k = map(int, input().split())
arr = [[0] * n for _ in range(m)]
visited = [[0] * n for _ in range(m)]
dy, dx = (-1, 0, 1, 0), (0, 1, 0, -1)


def dfs(y, x) -> int:
    global m, n, k, arr, visited, dy, dx
    visited[y][x] = 1
    ret = 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or ny >= m or nx >= n: continue
        if visited[ny][nx] or arr[ny][nx] == 1: continue
        print(ny, nx)
        ret += dfs(ny, nx)

    return ret


def solution():
    global m, n, k, arr, visited
    ret = []
    for _ in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        for i in range(y1, y2):
            for j in range(x1, x2):
                arr[i][j] = 1

    for i in range(m):
        for j in range(n):
            if not visited[i][j] and arr[i][j] == 0:
                ret.append(dfs(i, j))

    print(len(ret))
    for i in sorted(ret):
        print(i, end=' ')


solution()

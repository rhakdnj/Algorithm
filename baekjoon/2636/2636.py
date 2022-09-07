"""
https://www.acmicpc.net/problem/2636
치즈
"""
import sys

sys.setrecursionlimit(10 ** 6)

input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
arr = []
melt = []
dy, dx = (-1, 0, 1, 0), (0, 1, 0, -1)
visited = []


def dfs(y, x) -> None:
    global n, m, arr, visited, melt
    visited[y][x] = 1
    if arr[y][x] == 1:
        melt.append((y, x))
        return

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
            dfs(ny, nx)
    return


def exist_cheese():
    global n, m, arr
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                return True
    return False


def solution():
    global n, m, arr, visited, melt
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    time, cnt = 0, 0
    while True:
        cnt = 0
        visited = [[0] * m for _ in range(n)]
        melt = []

        dfs(0, 0)
        for i, j in melt:
            cnt += 1
            arr[i][j] = 0

        time += 1

        if not exist_cheese():
            break

    print(time, cnt, sep='\n')


solution()

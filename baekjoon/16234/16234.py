"""
https://www.acmicpc.net/problem/16234
인구 이동
"""
import sys
sys.setrecursionlimit(100000)

input = lambda: sys.stdin.readline().rstrip()
N, L, R = 0, 0, 0
arr, visited, temp = [], [], []
dy, dx = (-1, 0, 1, 0), (0, 1, 0, -1)
sum_ = 0


def dfs(y: int, x: int):
    global N, L, R, arr, visited, temp, sum_
    visited[y][x] = 1
    temp.append((y, x))
    sum_ += arr[y][x]

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if ny < 0 or nx < 0 or ny >= N or nx >= N or visited[ny][nx]:
            continue
        if L <= abs(arr[ny][nx] - arr[y][x]) <= R:
            dfs(ny, nx)


# L 명이상 R 명 이하 라면
def solution(n, l, r):
    global N, L, R, arr, visited, temp, sum_
    N, L, R = n, l, r
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    while True:
        flag = 0
        visited = [[0] * N for _ in range(N)]

        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    sum_, temp = 0, []  # 초기화
                    dfs(i, j)
                    if len(temp) == 1:
                        continue
                    for y, x in temp:
                        arr[y][x] = sum_ // len(temp)
                        flag = 1
        if not flag:
            break
        ans += 1
    print(ans)


solution(*map(int, input().split()))

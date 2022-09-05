"""
https://www.acmicpc.net/problem/14502
연구소
"""
from itertools import combinations
from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
arr = []
dy, dx = (-1, 0, 1, 0), (0, 1, 0, -1)


def get_area_size(a: list, v: list):
    global dy, dx, n, m
    dq = deque(v)
    visited = [[False] * m for _ in range(n)]
    while dq:
        y, x = dq.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                if a[ny][nx] == 0:
                    a[ny][nx] = 2
                    dq.append((ny, nx))

    ret = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                ret += 1
    return ret


def solution():
    global n, m, arr
    zero, virus = [], []
    ret = 0

    for _ in range(n):
        arr.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                zero.append((i, j))
            if arr[i][j] == 2:
                virus.append((i, j))

    for combi in combinations(zero, 3):
        temp = [item[:] for item in arr]
        for i, j in combi:
            temp[i][j] = 1
        ret = max(ret, get_area_size(temp, virus))

    print(ret)


solution()

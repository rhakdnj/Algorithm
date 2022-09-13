"""
https://www.acmicpc.net/problem/15686
치킨 배달
도시의 각 칸은 빈칸0, 집1, 치킨집2
도시에 있는 치킨집 중에서 최대 M 개를 고르고, 나머지 치킨집은 모두 폐업 시켜야 한다.
"""
from itertools import combinations
import sys

input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
arr, chicken, house = [], [], []
visited = []
dy, dx = (-1, 0, 1, 0), (0, 1, 0, -1)


def solution():
    global n, m, arr, visited
    arr = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                chicken.append((i, j))
            elif arr[i][j] == 1:
                house.append((i, j))

    ret = int(1e9)
    for combi in combinations(chicken, m):
        temp = 0
        for i in house:
            y, x = i[0], i[1]
            temp2 = 100
            for j in combi:
                temp2 = min(temp2, abs(y - j[0]) + abs(x - j[1]))

            temp += temp2
        ret = min(ret, temp)

    print(ret)


solution()

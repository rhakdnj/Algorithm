"""
https://www.acmicpc.net/problem/2910
빈도 정렬
"""
import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()
n, c = map(int, input().split())


def solution():
    global n, c
    cnt = defaultdict(list)

    idx = 1
    for i in map(int, input().split()):
        if not cnt[i]:
            cnt[i] = [1, idx]
            idx += 1
        else:
            cnt[i][0] += 1

    arr = [[i, j] for i, j in cnt.items()]
    arr.sort(key=lambda x: (-x[1][0], x[1][1]))

    ret = []
    for i, j in arr:
        ret += [i] * j[0]
    print(*ret)


solution()

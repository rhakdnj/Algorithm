# https://www.acmicpc.net/problem/20207
# 달력

import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
calendar = [0] * 366

for _ in range(n):
    s, e = map(int, input().split())
    for i in range(s, e + 1):
        calendar[i] += 1


def solution():
    global calendar
    row, col = 0, 0
    answer = 0

    for i in range(366):
        if calendar[i] != 0:
            row = max(row, calendar[i])
            col += 1
        else:
            answer += row * col
            row, col = 0, 0
    answer += row * col
    print(answer)


solution()

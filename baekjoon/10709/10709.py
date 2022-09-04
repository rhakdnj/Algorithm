"""
https://www.acmicpc.net/problem/10709
기상캐스터
"""
import sys

input = lambda: sys.stdin.readline().rstrip()
h, w = map(int, input().split())
arr = []


def solution():
    global arr
    for _ in range(h):
        arr.append(list(input()))

    for i in range(h):
        for j in range(w):
            if arr[i][j] == 'c':
                arr[i][j] = 0
                cnt = 1
                while j <= w - 2 and arr[i][j + 1] == '.':
                    arr[i][j + 1] = cnt
                    cnt += 1
                    j += 1

    for i in range(h):
        for j in range(w):
            if arr[i][j] == '.':
                print(-1, end=' ')
            else:
                print(arr[i][j], end=' ')
        print()


solution()

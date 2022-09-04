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
        v = 1
        flag = False
        for j in range(w):
            if arr[i][j] == 'c':
                arr[i][j] = 0
                if v == 1:
                    flag = True
                else:
                    flag = True
                    v = 1
            else:
                if flag:
                    arr[i][j] = v
                    v += 1
                if v == 1:
                    flag = False

    for i in range(h):
        for j in range(w):
            if arr[i][j] == '.':
                print(-1, end=' ')
            else:
                print(arr[i][j], end=' ')
        print()


solution()

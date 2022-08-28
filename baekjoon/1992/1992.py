"""
https://www.acmicpc.net/problem/1992
쿼드트리
"""
import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
arr = [list(input()) for _ in range(n)]


def go(y, x, size):
    global n, arr
    if size == 1:
        return arr[y][x]
    ret = ''
    a = arr[y][x]
    for i in range(y, y + size):
        for j in range(x, x + size):
            if a != arr[i][j]:
                ret += '('
                ret += go(y, x, size // 2)
                ret += go(y, x + size // 2, size // 2)
                ret += go(y + size // 2, x, size // 2)
                ret += go(y + size // 2, x + size // 2, size // 2)
                ret += ')'
                return ret
    return arr[y][x]


def solution():
    global n
    print(go(0, 0, n))


solution()

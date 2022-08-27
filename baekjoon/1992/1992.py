"""
https://www.acmicpc.net/problem/1992
쿼드트리
"""
import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
arr = [list(input()) for _ in range(n)]


def quard(y, x, size):
    global n, arr
    if size == 1: return arr[y][x]
    a = arr[y][x]
    ret = ''
    for i in range(y, y + size):
        for j in range(x, x + size):
            if a != arr[i][j]:
                ret = '('
                ret += quard(y, x, size // 2)
                ret += quard(y, x + size // 2, size // 2)
                ret += quard(y + size // 2, x, size // 2)
                ret += quard(y + size // 2, x + size // 2, size // 2)
                ret += ')'
                return ret
    return arr[y][x]


def solution():
    global n, arr
    print(quard(0, 0, n))


solution()

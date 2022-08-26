"""
https://www.acmicpc.net/problem/1629
곱셈
"""
import sys

input = lambda: sys.stdin.readline().rstrip()

a, b, c = map(int, input().split())


def sol(m: int, n: int) -> int:
    global c
    if n == 1: return m % c
    ret = sol(m, n // 2)
    ret = (ret * ret) % c

    if b % 2:
        ret = (ret * a) % c
    return ret


def solution():
    global a, b, c
    print(sol(a, b))


solution()

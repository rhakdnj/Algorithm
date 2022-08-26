"""
https://www.acmicpc.net/problem/1629
곱셈
"""
import sys

input = lambda: sys.stdin.readline().rstrip()

a, b, c = map(int, input().split())


def sol(x: int, y: int) -> int:
    global c
    if y == 1:
        return x % c
    ret = sol(x, y // 2)
    ret = (ret * ret) % c

    if y % 2:
        ret = (ret * x) % c
    return ret


def solution():
    global a, b, c
    print(sol(a, b))


solution()

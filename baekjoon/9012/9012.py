"""
https://www.acmicpc.net/problem/9012
괄호
"""
import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())


def check(s: str) -> bool:
    stk = []
    for c in s:
        if c == '(':
            stk.append(c)
        else:
            if len(stk) != 0:
                stk.pop()
            else:
                return False
    return len(stk) == 0


def solution():
    global n
    for _ in range(n):
        s = input()
        if check(s):
            print('YES')
        else:
            print('NO')


solution()

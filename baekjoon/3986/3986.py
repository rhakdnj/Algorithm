"""
https://www.acmicpc.net/problem/3986
좋은 단어
"""
import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
arr = [input() for _ in range(n)]


def solution(n, arr):
    ret = 0
    for s in arr:
        stk = []
        for ch in s:
            if len(stk) and stk[-1] == ch:
                stk.pop()
            else:
                stk.append(ch)
        if len(stk) == 0:
            ret += 1
    print(ret)


solution(n, arr)

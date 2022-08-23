"""
https://www.acmicpc.net/problem/3986
좋은 단어
"""
import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
arr = [input() for _ in range(n)]


def solution(n, arr):
    ret = n
    for s in arr:
        if ('AA' not in s) and ('BB' not in s):
            ret -= 1
            continue
        while ('AA' in s) or ('BB' in s):
            s = s.replace('AA', '')
            s = s.replace('BB', '')
        if s != '':
            ret -= 1
    print(ret)


solution(n, arr)

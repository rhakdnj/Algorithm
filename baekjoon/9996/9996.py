"""
https://www.acmicpc.net/problem/9996
"""
import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
pattern = input()


def solution():
    global n, pattern
    pre, suf = pattern.split('*')
    for _ in range(n):
        s = input()
        if len(s) < len(pre) + len(suf):
            print("NE")
            continue
        if s.startswith(pre) and s.endswith(suf):
            print("DA")
        else:
            print("NE")


solution()

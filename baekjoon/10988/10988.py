"""
https://www.acmicpc.net/problem/10988
팰린드롬인지 확인하기
"""
import sys

input = lambda: sys.stdin.readline().rstrip()


def solution():
    s = input()
    temp = s[::-1]
    if temp == s:
        print(1)
    else:
        print(0)


solution()

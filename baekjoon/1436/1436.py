"""
https://www.acmicpc.net/problem/1436
영화감독 숌
"""
import sys

input = lambda: sys.stdin.readline().rstrip()


def solution():
    n = int(input())

    cnt = 666
    while n:
        if '666' in str(cnt):
            n -= 1
        cnt += 1
    print(cnt - 1)


solution()

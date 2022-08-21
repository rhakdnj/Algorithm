"""
https://www.acmicpc.net/problem/9375
"""
import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()

testcase = int(input())


def solution():
    global testcase

    for _ in range(testcase):
        dic = defaultdict(int)
        for _ in range(int(input())):
            item, kind = input().split()
            dic[kind] += 1

        ret = 1
        for k in dic.keys():
            ret *= dic[k] + 1
        ret -= 1
        print(ret)


solution()

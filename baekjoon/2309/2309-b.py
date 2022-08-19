# https://www.acmicpc.net/problem/2309
# 일곱 난쟁이
from itertools import combinations
import sys

input = lambda: sys.stdin.readline().rstrip()


def solution():
    arr = [int(input()) for _ in range(9)]

    for combi in combinations(arr, 7):
        if sum(combi) == 100:
            for i in sorted(list(combi)):
                print(i)
            break


solution()

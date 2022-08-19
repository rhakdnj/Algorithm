# https://www.acmicpc.net/problem/2309
# 일곱 난쟁이

from itertools import combinations
import sys
import timeit

start_time = timeit.default_timer()

input = lambda: sys.stdin.readline().rstrip()

arr = []
total = 0


def solve() -> tuple:
    global arr, total
    for i in range(9):
        for j in range(i):
            if (total - arr[i] - arr[j]) == 100:
                return i, j


def solution():
    global arr, total
    arr = sorted([int(input()) for _ in range(9)])
    total = sum(arr)

    tupl = solve()

    for i in range(9):
        if i in tupl:
            continue
        print(arr[i])


solution()
terminate_time = timeit.default_timer()
print("수행 시간: %f초" % (terminate_time - start_time))

"""
https://www.acmicpc.net/problem/2559

"""
import sys

input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
psum = [0] * 100001


def solution():
    global n, k, psum
    ret = -100004
    i = 1
    for temp in map(int, input().split()):
        psum[i] = psum[i - 1] + temp
        i += 1

    for i in range(k, n + 1):
        ret = max(ret, psum[i] - psum[i - k])

    print(ret)


solution()

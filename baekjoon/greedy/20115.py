# https://www.acmicpc.net/problem/20115
import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
arr = list(map(int, input().split())).sort()

for i in range(N - 1):
    arr[-1] += arr[i] / 2

print(arr[-1])




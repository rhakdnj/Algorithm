import sys


def input():
    return sys.stdin.readline().rstrip()


n, k = map(int, input().split())
arr = list(map(int, input().split()))

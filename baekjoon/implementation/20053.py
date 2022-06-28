import sys


def input():
    return sys.stdin.readline().rstrip()


T = int(input())
for _ in range(T):
    n = int(input())
    arr = sorted(map(int, input().split()))
    print(arr[0], arr[-1])

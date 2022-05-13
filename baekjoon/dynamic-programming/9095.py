import sys


def input():
    return sys.stdin.readline().rstrip()


def solve(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return solve(n - 1) + solve(n - 2) + solve(n - 3)


# 1, 2, 3 더하기
T = int(input())
for _ in range(T):
    n = int(input())
    print(solve(n))

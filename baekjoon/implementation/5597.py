import sys


def input():
    return sys.stdin.readline().rstrip()


dp = [0] * 31

for _ in range(28):
    idx = int(input())
    dp[idx] = 1

for i in range(1, 31):
    if dp[i] == 0:
        print(i)

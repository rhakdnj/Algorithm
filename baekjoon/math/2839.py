# https://www.acmicpc.net/problem/2839
import sys

def input():
    return sys.stdin.readline().rstrip()

INF = 9999
dp = [INF for _ in range(5001)]
dp[3], dp[5] = 1, 1

for i in range(5, 5001):
    dp[i] = min((dp[i], dp[i-3] + 1, dp[i-5] + 1))

N = int(input())

if dp[N] == INF:
    dp[N] = -1
print(dp[N])

"""
input : x

정수 x가 주어졌을 때, 연산 4개를 적절히 사용해서 1을 만드려고 한다.

연산 4개:
1. x가 5로 나누어떨어지면 5로 나눈다.
2. x가 3으로 나누어떨어지면 3으로 나눈다.
3. x가 2으로 나누어떨어지면 2으로 나눈다.
4. x에서 1을 뺀다.

점화식: dp[i] = min(dp[i//2] + 1, dp[i//3] + 1, dp[i//5] + 1, dp[i])
"""

import sys


def input():
    return sys.stdin.readline().rstrip()


x = int(input())
dp = [0] * 30001

for i in range(2, x + 1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)

print(dp[x])

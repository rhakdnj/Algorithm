"""
가로의 길이 N  세로의 길이 2인 정사각형 형태의 얇은 바닥
덮개:
1 x 2
2 x 1
2 x 2

input : n
output: 2 x n 크기의 바닥을 채우는 방법의 수를 796,796으로 나눈 나머지를 출력

dp[i] = dp[i-1] + dp[i-2] * 2
"""

n = int(input())
dp = [0] * (n + 1)
dp[1], dp[2] = 1, 3

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] * 2) % 796796

print(dp[n])
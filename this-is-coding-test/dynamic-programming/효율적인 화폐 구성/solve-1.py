"""
n가지 종류의 화폐 존재
화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 함
불가능 할 때는 -1을 출력

input: n, m, 화폐 종류
output: 화폐 개수, 불가능할 때는 -1을 출력
"""

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

dp = [10001] * (m + 1)
# dp[0] = 0 을 통해 보텀업 방식으로
dp[0] = 0

for i in range(n):
    for j in range(arr[i], m + 1):
        # dp[j - arr[i]], arr[i]의 배수일 때
        if dp[j - arr[i]] != 10001:
            dp[j] = min(dp[j], dp[j - arr[i]] + 1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])

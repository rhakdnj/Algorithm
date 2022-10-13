n = int(input())
dp = [0] * (n + 1)

for day in range(1, n + 1):
    t, p = map(int, input().split())
    if day + t - 1 <= n:
        dp[t + day - 1] = max(p + dp[day - 1], dp[t + day - 1])
    dp[day] = max(dp[day], dp[day - 1])

print(dp[-1])

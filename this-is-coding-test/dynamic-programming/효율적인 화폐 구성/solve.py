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

for i in arr:
    cnt = 1
    while True:
        idx = i * cnt
        if idx > m:
            break
        dp[idx] = min(dp[idx], cnt)
        cnt += 1

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])

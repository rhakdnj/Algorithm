"""
개미 전사가 정찰병에게 들키지 않고 식량창고를 약탈하기 위해서는
최소한 한 칸 이상 떨어진 식량창고를 약탈해야 한다.

dp[i] = max(dp[i-2] + arr[i], dp[i-1])
"""

n = int(input())
arr = list(map(int, input().split()))
# dp 앞서 계산된 결과를 저장 하기 위한 DP 테이블 초기화
dp = [0] * n
dp[0], dp[1] = arr[0], max(arr[0], arr[1])

for i in range(2, n):
    try:
        dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
    except IndexError:
        exit()

print(dp[n-1])

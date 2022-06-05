def solution(price: int):
    dp = [0] * (price + 1)
    dp[0] = 1

    for coin in coin_list:
        for i in range(price + 1):
            if i >= coin:
                dp[i] += dp[i - coin]
    print(dp[price])


T = int(input())

for _ in range(T):
    N = int(input())
    coin_list = list(map(int, input().split()))
    solution(int(input()))

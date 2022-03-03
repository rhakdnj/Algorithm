# https://www.acmicpc.net/problem/11047
n, k = map(int, input().split())
coins = [int(input()) for i in range(n)]
answer = 0

# for coin in coins[ : :-1]
for i in range(n - 1, -1, -1):
    if k == 0:
        break
    if k // coins[i]:
        answer += k // coins[i]
        k %= coins[i]

print(answer)
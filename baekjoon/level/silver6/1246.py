import sys
input = sys.stdin.readline

n, m = map(int, input().split())
prices = sorted([int(input()) for i in range(m)])

'''for i in range(m):
    price = int(input())
    prices.append(price)
'''

price, res = 0, 0

for i in range(m):
    # 총 계란의 갯수보다 작은 양만 팔 수 있다 . min(m-i, n)
    max_egg = min(m-i, n)
    if res < prices[i] * max_egg:
        res = prices[i] * max_egg
        price = prices[i]

print(price, res)

# https://www.acmicpc.net/problem/13305
# min_price 변수를 통해 greedy 가장 작은 가격으로
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
roads = list(map(int, input().split()))
prices = list(map(int, input().split()))
min_price = prices[0]
res = 0

for i in range(N-1):
    if min_price > prices[i]:
        min_price = prices[i]
    res += min_price * roads[i]
else:
    print(res)

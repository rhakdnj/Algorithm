# https://www.acmicpc.net/problem/5618
# import math를 해서 구현도 가능 최대 공약수의 공약수를 구하는 문제
import sys

def input():
    return sys.stdin.readline().rstrip()

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

n = int(input())
arr = list(map(int, input().split()))
res = []
gcdValue = arr[0]
# 최대 공약수 찾기
for i in range(n):
    gcdValue = gcd(gcdValue, arr[i])

x = 1
while x * x <= gcdValue:
    if gcdValue % x == 0:
        res.append(x)
        if x * x != gcdValue:
            res.append(gcdValue // x)
    x += 1

res.sort()
print(*res, sep='\n')


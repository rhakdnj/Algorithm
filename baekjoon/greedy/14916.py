# https://www.acmicpc.net/problem/14916
# print(-1 if n==1 or n==3 else n//5+n%5//2+(n%5%2)*2)
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

if n < 5:
    if n % 2:
        ans = -1
    else:
        ans = n // 2
else:
    quote, remainder = divmod(n, 5)
    if remainder == 0:
        ans = quote
    else:
        if remainder % 2 == 0:
            quote += remainder // 2
            ans = quote
        else:
            quote += (remainder + 5) // 2 - 1
            ans = quote
print(ans)

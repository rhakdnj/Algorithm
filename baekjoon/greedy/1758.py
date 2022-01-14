# https://www.acmicpc.net/problem/1758
# tips.sort(key = lambda x : -x) == (reverse=True)
import sys

def input():
    return sys.stdin.readline().rstrip()

# 값 - index 만큼 빠지기에 결국에는 -index가 최소한으로 발생하는 내림차순 정렬을 한다.
N = int(input())
tips = sorted([int(input()) for _ in range(N)], reverse=True)
res = 0

for i in range(N):
    tip = tips[i] - i
    if tip > 0:
        res += tip
else:
    print(res)
# https://www.acmicpc.net/problem/11286
# 절댓값 힙
from heapq import heappush, heappop
import sys

input = lambda: sys.stdin.readline().rstrip()

hq = []
for _ in range(int(input())):
    x = int(input())
    if x == 0:
        print(heappop(hq)[1] if len(hq) else 0)
    else:
        heappush(hq, (abs(x), x))

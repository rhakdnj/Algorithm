# https://www.acmicpc.net/problem/2075
# N 번째 큰 수
from heapq import heappush, heappop
import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
hq = []

for _ in range(n):
    nums = list(map(int, input().split()))

    if not hq:
        for num in nums:
            heappush(hq, num)
    else:
        for num in nums:
            if hq[0] < num:
                heappush(hq, num)
                heappop(hq)
print(hq[0])

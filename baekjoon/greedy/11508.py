# https://www.acmicpc.net/problem/11508
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = sorted([int(input()) for _ in range(N)],reverse=True)
ans = []
res = 0

cnt = 1
for i in range(N):
    if cnt % 3 == 0:
        ct = 1
        continue
    res += arr[i]
    ct += 1
else:
    print(res)
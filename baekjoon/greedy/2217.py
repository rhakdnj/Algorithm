# https://www.acmicpc.net/problem/2217
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
rope = sorted([int(input()) for _ in range(N)], reverse=True)
# 모든 루프를 사용하지 않은 경우도 있기에, 루프 갯수에 따른 최대 무게중에서 최대 무게
res = []

for i in range(N):
    res.append(rope[i] * (i + 1))
else:
    print(max(res))

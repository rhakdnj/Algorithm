# https://www.acmicpc.net/problem/22864
# if문을 추가해줘서 A > M일때는 for문으로 안가게 만든다.
import sys

def input():
    return sys.stdin.readline().rstrip()

A, B, C, M = map(int, input().split())
hard = 0
res = 0

if A > M:
    print(0)
else:
    for _ in range(24):
        if hard + A > M:
            hard -= C
        else:
            res += B
            hard += A

print(res)

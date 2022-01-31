import sys


def input():
    return sys.stdin.readline().rstrip()


a, b, c, m = map(int, input().split())
work, hard = 0, 0

for _ in range(24):
    if hard < 0:
        hard = 0
    if hard + a > m:
        hard - c
    else:
        work += b
        hard += a
else:
    print(work)


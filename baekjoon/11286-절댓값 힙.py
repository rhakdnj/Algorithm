import sys
from heapq import heappush, heappop

input = lambda: sys.stdin.readline().rstrip()


def solution():
    hq = []
    for _ in range(N):
        num = int(input())
        if num == 0:
            print(heappop(hq)[1] if hq else 0)
        else:
            heappush(hq, (abs(num), num))


if __name__ == '__main__':
    N = int(input())
    solution()

from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()
n, l = map(int, input().split())


def solution():
    dq = deque()
    for i, curr in enumerate(list(map(int, input().split()))):
        while dq and dq[-1][1] > curr:
            dq.pop()

        dq.append((i, curr))
        if dq[0][0] <= i - l:
            dq.popleft()

        print(dq[0][1], end=" ")


solution()

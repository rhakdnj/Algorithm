# https://www.acmicpc.net/problem/2346
from collections import deque
import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
queue = deque(map(int, input().split()))
queue2 = deque(i for i in range(1, n + 1))

while queue:
    q = queue[0]
    if q > 0:
        queue.popleft()
        queue.rotate(-q + 1)
        print(queue2.popleft())
        queue2.rotate(-q + 1)
    else:
        queue.popleft()
        queue.rotate(-q)
        print(queue2.popleft())
        queue2.rotate(-q)

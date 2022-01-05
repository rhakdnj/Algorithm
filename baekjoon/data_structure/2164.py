# https://www.acmicpc.net/problem/2164
# queue.rotate(-1) = a = queue.popleft(); queue.append(a)
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
queue = deque(i+1 for i in range(N))

while True:
    queue.popleft()
    if len(queue) == 1:
        print(queue.popleft())
        break
    queue.rotate(-1)


# https://www.acmicpc.net/problem/18258
# queue는 deque 또는 list로도 충분히 구현 가능하다
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
queue = deque()

for _ in range(N):
    cmd = input().split()
    X = 0
    if len(cmd) == 2:
        X = cmd[1]
    cmd = cmd[0]

    if cmd == "push":
        queue.append(X)
    elif cmd == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif cmd == "size":
        print(len(queue))
    elif cmd == "empty":
        print(0 if len(queue) else 1)
    elif cmd == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif cmd == "rear":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
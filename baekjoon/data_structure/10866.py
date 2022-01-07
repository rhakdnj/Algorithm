# if not queue: === if len(queue) == 0:
# deque 는 front rear 양뱡향 자료구조
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
    if cmd == "push_front":
        queue.appendleft(X)
    elif cmd == "push_back":
        queue.append(X)
    elif cmd == "pop_front":
        if len(queue):
            print(queue.popleft())
        else:
            print(-1)
    elif cmd == "pop_back":
        if len(queue):
            print(queue.pop())
        else:
            print(-1)
    elif cmd == "size":
        print(len(queue))
    elif cmd == "empty":
        print(0 if len(queue) else 1)
    elif cmd == "front":
        if len(queue):
            print(queue[0])
        else:
            print(-1)
    elif cmd == "back":
        if len(queue):
            print(queue[-1])
        else:
            print(-1)

    

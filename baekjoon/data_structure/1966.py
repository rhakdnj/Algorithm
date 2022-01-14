# https://www.acmicpc.net/problem/1966
# list(map(int, "1234")), [1, 2, 3, 4] list로 형변환
# [map(int, "1234")], 형변한이 일어나는 것이 아니라 [map object ]
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    cnt = 1
    queue = deque(list(map(int, input().split())))
    queue_i = deque(list(range(N)))
    while True:
        if queue[0] == max(queue):
            if queue_i[0] == M:
                print(cnt)
                break
            else:
                queue.popleft()
                queue_i.popleft()
                cnt += 1
        else:
            queue.rotate(-1)
            queue_i.rotate(-1)
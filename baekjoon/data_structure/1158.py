# https://www.acmicpc.net/problem/1158
# deque rotate
# join(self, __iterable: Iterable[str]) -> str: ...
import sys
from collections import deque

def input() :
    return sys.stdin.readline().rstrip()

N , K = map(int, input().split())
lst = []    # list
q = deque([i+1 for i in range(N)])

while len(q) != 0:
    q.rotate(-K)
    lst.append(q.pop())

print('<' + ', '.join(map(str, lst)) + '>')
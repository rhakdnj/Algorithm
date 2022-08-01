# https://www.acmicpc.net/problem/7785
# 회사에 있는 사람
import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
s = set()
for _ in range(n):
    name, el = input().split()
    if el == 'enter':
        s.add(name)
    else:
        if name in s:
            s.remove(name)

for name in sorted(s, reverse=True):
    print(name)

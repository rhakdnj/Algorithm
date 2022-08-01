# https://www.acmicpc.net/problem/11866
# 요세푸스 문제 0
import sys

input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
arr = [i + 1 for i in range(n)]
pos = 0
ans = []

for i in range(n):
    pos += k - 1
    pos %= len(arr)
    ans.append(arr.pop(pos))

print(f"<{', '.join(map(str, ans))}>")

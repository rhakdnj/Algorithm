# https://www.acmicpc.net/problem/5397
# 키로거
import sys

input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    s = input()
    left, right = [], []

    for i in s:
        if i == '<' and left:
            right.append(left.pop())
        elif i == '>' and right:
            left.append(right.pop())
        elif i == '-' and left:
            left.pop()
        elif i not in ('<', '>', '-'):
            left.append(i)
    print(f"{''.join(left)}{''.join(right[::-1])}")

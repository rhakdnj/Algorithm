import sys


def input():
    return sys.stdin.readline().rstrip()


x, y, w, h = map(int, input().split())

answer = 1000

if w - x < answer:
    answer = w - x
if x < answer:
    answer = x
if h - y < answer:
    answer = h - y
if y < answer:
    answer = y
print(answer)
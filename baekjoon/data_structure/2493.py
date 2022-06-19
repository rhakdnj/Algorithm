# boj 2493 탑
# stack
import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
arr = map(int, input().split())
stack, answer = [], []

for i in range(n):
    while stack:
        if arr[stack[-1]] >= arr[i]:
            break
        else:
            stack.pop()
    if stack:
        answer.append(stack[-1] + 1)
    else:
        answer.append(0)
    stack.append(i)
print(' '.join(list(map(str, answer))))

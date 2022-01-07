# https://www.acmicpc.net/problem/1874
# 스택에 push하는 순서는 반드시 오름차순을 지키도록 하는 것을 count 변수로 해결
# flag로 수열의 만들 수 있음과 없음을 구분
import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
count = 0
stack = []
result = []
flag = True

for _ in range(n):
    num = int(input())
    while count < num:
        count += 1
        stack.append(count)
        result.append('+')
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        flag = False
else:
    if not flag:
        print("NO")


if flag:
    print('\n'.join(result))

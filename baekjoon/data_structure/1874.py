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

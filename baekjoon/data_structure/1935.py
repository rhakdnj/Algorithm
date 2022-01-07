# https://www.acmicpc.net/problem/1935
# https://www.acmicpc.net/source/37222963(queue & dictionary 로 해석)
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
str = input()
oper = "+-*/"
num_list = [int(input()) for _ in range(N)]
stack = []

for i in str:
    if i not in oper:
        stack.append(num_list[ord(i)-ord('A')])
    else:
        num1 = stack.pop()
        num2 = stack.pop()
        if i == '+':
            stack.append(num2 + num1)
        elif i == '-':
            stack.append(num2 - num1)
        elif i == '*':
            stack.append(num2 * num1)
        elif i == '/':
            stack.append(num2 / num1)
else:
    print("{:.2f}".format(stack[0]))
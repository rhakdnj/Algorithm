# https://www.acmicpc.net/problem/10799
# stack을 이요한 문제풀이
# stack을 대신하는 pipe_stack 변수
from os import pipe
import sys

def input():
    return sys.stdin.readline().rstrip()

# 괄호 표현
parentheses = input()
pipe_stack = 0
i, res = 0 , 0  # index 와 출력값

while i < len(parentheses):
    x = parentheses[i]
    # '('가 막대의 시작인지, 레이저의 시작인지 구분 
    if x == '(':
        if parentheses[i+1] == ')':    # 레이저
            res += pipe_stack
            i += 1
        else: # 막대
            res += 1
            pipe_stack += 1
    else: 
        pipe_stack -= 1
    i += 1

print(res)


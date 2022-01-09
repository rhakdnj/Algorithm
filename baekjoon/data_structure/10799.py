# https://www.acmicpc.net/problem/10799
# 1. stack을 이요한 문제풀이
# 2. stack을 대신하는 pipe_stack 변수

# 1
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
        # 레이저
        if parentheses[i+1] == ')':    
            res += pipe_stack
            i += 1
        else:
            # 새로운 막대 추가
            res += 1
            pipe_stack += 1
    else:
        pipe_stack -= 1
    i += 1

print(res)


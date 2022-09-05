"""
https://www.acmicpc.net/problem/4949
균형잡힌 세상
"""
import sys

input = lambda: sys.stdin.readline().rstrip()


def solution():
    while True:
        s = input()
        if s == '.':
            break
        stk = []
        check = True

        for c in s:
            if c == '(' or c == '[':
                stk.append(c)
            elif c == ')':
                if len(stk) == 0:
                    check = False
                if stk[-1] == '(':
                    stk.pop()
                else:
                    check = False
                    break
            elif c == ']':
                if len(stk) == 0:
                    check = False
                    break
                if stk[-1] == '[':
                    stk.pop()
                else:
                    check = False
                    break
        if check and len(stk) == 0:
            print('yes')
        else:
            print('no')


solution()

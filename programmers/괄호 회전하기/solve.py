from collections import deque


def is_correct(s: str) -> bool:
    stack = []
    for ch in s:
        if not stack:
            stack.append(ch)
        elif stack[-1] == '(':
            if ch == ')':
                stack.pop()
            else:
                stack.append(ch)
        elif stack[-1] == '{':
            if ch == '}':
                stack.pop()
            else:
                stack.append(ch)
        elif stack[-1] == '[':
            if ch == ']':
                stack.pop()
            else:
                stack.append(ch)
    return False if stack else True


def solution(s: str) -> int:
    answer = 0
    for i in range(len(s)):
        answer += is_correct(s[i:] + s[:i])

    return answer

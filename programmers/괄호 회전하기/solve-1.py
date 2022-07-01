from collections import deque


def solution(s):
    answer, cnt = 0, 0
    length = len(s)
    dic = {
        '[': ']',
        '{': '}',
        '(': ')'
    }

    while cnt != length:
        stack = []
        queue = deque(s)
        queue.rotate(-cnt)

        for i in range(length):
            stack.append(queue[i])
            if len(stack) == 1:
                continue
            if stack[-1] == dic[stack[-2]]:
                stack.pop()
                stack.pop()
        if not stack:
            answer += 1
        cnt += 1
    return answer


solution("[](){}")

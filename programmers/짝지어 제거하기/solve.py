def solution(s):
    answer = []

    for i in range(len(s)):
        answer.append(s[i])
        if len(answer) >= 2:
            if answer[-1] == answer[-2]:
                answer.pop()
                answer.pop()
    if len(answer) >= 2:
        if answer[-1] == answer[-2]:
            answer.pop()
            answer.pop()

    return 1 if not answer else 0



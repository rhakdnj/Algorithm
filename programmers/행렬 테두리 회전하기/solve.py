"""
for 변수는 for scope가 끝나도 유효하다.
"""


def solution(rows, columns, queries):
    answer = []

    arr = [[i + j * columns for i in range(1, columns + 1)] for j in range(rows)]

    for a, b, c, d in queries:
        stack = []
        r1, c1, r2, c2 = a - 1, b - 1, c - 1, d - 1

        for i in range(c1, c2 + 1):
            stack.append(arr[r1][i])
            if len(stack) == 1:
                continue
            else:
                arr[r1][i] = stack[-2]

        for j in range(r1 + 1, r2 + 1):
            stack.append(arr[j][i])
            arr[j][i] = stack[-2]

        for k in range(c2 - 1, c1 - 1, -1):
            stack.append(arr[j][k])
            arr[j][k] = stack[-2]

        for l in range(r2 - 1, r1 - 1, -1):
            stack.append(arr[l][k])
            arr[l][k] = stack[-2]

        answer.append(min(stack))

    return answer

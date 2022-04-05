def solution(triangle):
    memo = {}
    answer = func(triangle, 0, 0, memo)
    return answer


def func(triangle, i, j, memo):
    if i == len(triangle) - 1:
        return triangle[i][j]

    if (i, j) in memo:
        return memo[(i, j)]

    a = func(triangle, i + 1, j, memo)
    b = func(triangle, i + 1, j + 1, memo)
    x = triangle[i][j] + max(a, b)

    memo[(i, j)] = x

    return x

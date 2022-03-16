def dfs(numbers, target, depth):
    answer = 0
    if depth == len(numbers):
        if sum(numbers) == target:
            return 1
        else:
            return 0
    else:
        answer += dfs(numbers, target, depth + 1)
        numbers[depth] *= (-1)
        answer += dfs(numbers, target, depth + 1)
        return answer


# def solution(numbers, target):
#     answer = dfs(numbers, target, 0)
#     return answer

# def solution(numbers, target):
#     if not numbers and target == 0:
#         return 1
#     elif not numbers:
#         return 0
#     else:
#         return solution(numbers[1:], target - numbers[0]) + solution(numbers[1:], target + numbers[0])

from itertools import product


def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)


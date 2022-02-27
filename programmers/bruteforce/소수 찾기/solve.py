from math import sqrt
from itertools import permutations


def is_prime(number):
    if number in (0, 1):
        return False
    for i in range(2, int((number ** 0.5) + 1)):
        if number % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    numbers = list(map(str, numbers))
    nums = []

    for i in range(1, len(numbers) + 1):
        nums += permutations(numbers, i)
    numbers = set([int("".join(p)) for p in nums])

    for num in numbers:
        if is_prime(num):
            answer += 1
    return answer

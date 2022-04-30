import math


def convert(num, base):
    q, r = divmod(num, base)
    if q:
        return convert(q, base) + str(r)
    else:
        return str(r)


def check(num):
    if num == 2:
        return True
    if num == 1 or num % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(num) + 1, 2)):
        if num % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    num_str = str(n) if k == 10 else convert(n, k)
    nums = num_str.split('0')

    for value in nums:
        if len(value) and check(int(value)):
            answer += 1
    return answer

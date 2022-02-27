prime_set = set()


def is_prime(number):
    if number in (0, 1):
        return False
    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def make_combinations(str1, str2):
    if str1 != "":
        if is_prime(int(str1)):
            prime_set.add(int(str1))

    for i in range(len(str2)):
        make_combinations(str1 + str2[i], str2[:i] + str2[i + 1:])


def solution(numbers):
    make_combinations("", numbers)

    answer = len(prime_set)

    return answer

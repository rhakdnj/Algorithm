def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** (1 / 2)) + 1):
        if num % i == 0:
            return False
    return True


def solution(n, k):
    k_str = ""
    while True:
        if n < k:
            k_str += str(n)
            k_str = k_str[::-1]
            break
        n, mod = n // k, n % k
        k_str += str(mod)

    temp = list(map(int, k_str.split("0")))
    answer = 0
    for num in temp:
        if is_prime(num):
            answer += 1

    if answer:
        return answer
    else:
        return -1


print(solution(437674, 3))

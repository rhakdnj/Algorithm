def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** (1 / 2)) + 1):
        if num % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0

    k_str = ""
    while True:
        if n < k:
            k_str = str(n) + k_str
            break
        n, mod = n // k, n % k
        k_str = str(mod) + k_str

    temp = ""
    for i in k_str:
        if i == '0':
            if is_prime(int(temp)):
                answer += 1
            temp = ""
        else:
            temp += i

    return max(answer, -1)


print(solution(437674, 3))

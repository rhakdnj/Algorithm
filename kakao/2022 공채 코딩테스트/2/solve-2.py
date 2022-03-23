def convert_k_number(n, k):
    s = ''
    while n:
        n, mod = divmod(n, k)
        s += str(mod)
    return s[::-1]  # 문자열 reverse 하는 방법


def is_prime(n):
    if n <= 1: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True


def solution(n, k):
    s = convert_k_number(n, k)
    answer = 0
    for num in s.split('0'):
        if not num: continue # 빈 문자열에 대한 예외 처(내가 이것 때문에 틀린듯)
        if is_prime(int(num)): answer += 1
    return answer
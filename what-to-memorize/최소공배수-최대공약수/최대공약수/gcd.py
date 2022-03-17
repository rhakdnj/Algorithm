def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


n, m = 1234, 5678
# 최대 공약수 구하기
for i in range(min(n, m), 0, -1):
    if n % i == 0 and m % i == 0:
        print(i)
        break


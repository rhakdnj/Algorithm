n, k = map(int, input().split())
answer = 0

while n >= k:
    while n % k != 0:
        n -= 1
        answer += 1
    n //= k
    answer += 1

while n > 1:
    n -= 1
    answer += 1

print(answer)
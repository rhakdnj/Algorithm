n, k = map(int, input().split())
answer = 0

while n // k >= 1:
    answer += n % k
    n = n // k
    answer += 1

while n != 1:
    answer += 1
    n -= 1

print(answer)

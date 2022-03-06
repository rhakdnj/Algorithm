n, m = map(int, input().split())

answer = 0
for _ in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    answer = max(answer, min_value)

print(answer)

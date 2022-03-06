n, m, k = map(int, input().split())

data = list(map(int, input().split()))
data.sort()
first = data[n - 1]
second = data[n - 2]

count = int(m / k + 1) * k
count += m % (k + 1)

answer = 0
answer += count * first
answer += (m - count) * second

print(answer)
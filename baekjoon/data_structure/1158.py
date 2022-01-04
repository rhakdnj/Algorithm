import sys
input = sys.stdin.readline

N , K = map(int, input().split())

arr = [i + 1 for i in range(N)]
answer = [ ]
index = 0

# index
for i in range(N):
    index += K - 1;
    if index >= len(arr):
        index %= len(arr)
    answer.append(str(arr.pop(index)))

print('<', ', '.join(answer), '>', sep = '')


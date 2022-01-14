import sys
input = sys.stdin.readline

n , k = map(int, input().split())
arr = list(i + 1 for i in range(n))
answer = []
index = 0

for i in range(n):
    index += k-1
    if index >= len(arr):
        index %= len(arr)
    
    answer.append(str(arr.pop(index)))

print("<",", ".join(answer),">", sep="")

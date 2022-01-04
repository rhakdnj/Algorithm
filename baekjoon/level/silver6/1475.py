import sys
input = sys.stdin.readline

n = input().rstrip()

countSet = {i : 0 for i in range(9)}

for i in range(len(n)):
    if n[i] in ('6', '9'):
        countSet[6] += 1
    else:
        countSet[int(n[i])] += 1

if countSet[6] % 2:
    countSet[6] = countSet[6] // 2 + 1
else:
    countSet[6] = countSet[6] // 2

print(max(countSet.values()))

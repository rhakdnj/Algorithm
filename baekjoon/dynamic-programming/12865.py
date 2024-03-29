import sys


def input():
    return sys.stdin.readline().rstrip()


N, K = map(int, input().split())
stuff = [(0, 0)]
# 무게에 따른 가치를 memoization
knapsack = [[0] * (K + 1) for _ in range(N + 1)]
for _ in range(N):
    stuff.append(tuple(map(int, input().split())))

for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight, value, = stuff[i][0], stuff[i][1]

        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j]
        else:
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])
print(knapsack[N][K])

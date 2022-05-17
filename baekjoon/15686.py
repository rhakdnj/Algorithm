import sys
from itertools import combinations


def input():
    return sys.stdin.readline().rstrip()


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
house, chicken = [], []
answer = int(1e9)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

for comb in combinations(chicken, m):
    temp = 0
    for h in house:
        chi_len = 100
        for j in range(m):
            chi_len = min(chi_len, abs(h[0] - comb[j][0]) + abs(h[1] - comb[j][1]))
        temp += chi_len
    answer = min(answer, temp)

print(answer)

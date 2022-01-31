import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


# dfs
def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if graph[x][y] == 0:
        return False
    if graph[x][y] == 1:
        global cnt
        cnt += 1
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
cnt = 0
result = 0
num = []

for i in range(n):
    for j in range(n):
        if dfs(i, j):
            num.append(cnt)
            result += 1
            cnt = 0
else:
    print(result)
    for i in sorted(num):
        print(i)

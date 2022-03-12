import sys


def input():
    return sys.stdin.readline().rstrip()


def dfs(x, y):
    if x < 0 or x > len(graph[0]) or y > len(graph) or y < 0:
        return False
    else:
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)


n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            answer += 1

print(answer)

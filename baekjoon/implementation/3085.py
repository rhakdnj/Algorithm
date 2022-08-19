# https://www.acmicpc.net/problem/3085
# 사탕 게임
import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
graph = [list(input()) for _ in range(n)]
ans = 0


def search(row: int, col: int, isRow: bool) -> None:
    global ans, graph, n
    cnt = 1
    if isRow:
        for j in range(n - 1):
            if graph[row][j + 1] == graph[row][j]:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1

        cnt = 1
        for i in range(n - 1):
            if graph[i + 1][col] == graph[i][col]:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1

        cnt = 1
        for i in range(n - 1):
            if graph[i + 1][col + 1] == graph[i][col + 1]:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1
    else:
        for j in range(n - 1):
            if graph[row][j + 1] == graph[row][j]:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1

        cnt = 1
        for j in range(n - 1):
            if graph[row + 1][j + 1] == graph[row + 1][j]:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1

        cnt = 1
        for i in range(n - 1):
            if graph[i + 1][col] == graph[i][col]:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1


for i in range(n):
    for j in range(n):
        if j + 1 < n:
            graph[i][j], graph[i][j + 1] = graph[i][j + 1], graph[i][j]
            search(i, j, True)
            graph[i][j], graph[i][j + 1] = graph[i][j + 1], graph[i][j]

        if i + 1 < n:
            graph[i][j], graph[i + 1][j] = graph[i + 1][j], graph[i][j]
            search(i, j, False)
            graph[i][j], graph[i + 1][j] = graph[i + 1][j], graph[i][j]
else:
    print(ans)

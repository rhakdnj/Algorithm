# https://www.acmicpc.net/problem/14500
# 테트로미노

import sys

sys.setrecursionlimit(5000)

input = lambda: sys.stdin.readline().rstrip()


# dy : 4 | (dx, dy) = (0, 4), (1, 3), (2, 2)
def dfs(x, y, depth, total):
    global answer, max_val
    # pruning
    if answer >= total + max_val * (3 - depth):
        return
    if depth == 3:
        answer = max(answer, total)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            # 블록 : (1, 3) ㅜ, ㅗ (3, 1) ㅓ ㅏ 처리
            if depth == 1:
                visited[nx][ny] = 1
                dfs(x, y, depth + 1, total + graph[nx][ny])
                visited[nx][ny] = 0
            visited[nx][ny] = 1
            dfs(nx, ny, depth + 1, total + graph[nx][ny])
            visited[nx][ny] = 0


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
answer = 0
# 2차원 배열의 최대 값 찾기
max_val = max(map(max, graph))

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 0, graph[i][j])
        visited[i][j] = 0

print(answer)

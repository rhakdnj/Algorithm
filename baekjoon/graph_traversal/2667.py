n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
res = []


def dfs(x, y):
    stack = [(x, y)]
    cnt = 1
    graph[x][y] = 0
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny]:
                cnt += 1
                graph[nx][ny] = 0
                stack.append((nx, ny))
    return cnt


for i in range(n):
    for j in range(n):
        if graph[i][j]:
            res.append(dfs(i, j))

print(len(res))
for i in sorted(res):
    print(i)

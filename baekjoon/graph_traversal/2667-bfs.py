import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def bfs(x, y):
    queue = deque()  # iterable(리스트 등)을 인자로 건내면 이를 deque화 시켜준다.
    queue.append((x, y))
    graph[x][y] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count


n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(bfs(i, j))
else:
    print(len(result))
    for i in sorted(result):
        print(i)

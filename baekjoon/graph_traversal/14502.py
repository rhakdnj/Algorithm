"""
일부 칸 바이러스 존재, 바이러스 상하좌우 인접한 빈 칸으로 퍼져나감
새로 세울 수 있는 벽의 개수 3개, 꼭 3개는 세워야함

0은 빈 칸, 1은 벽, 2는 바이러스

2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

"""
from collections import deque
from itertools import combinations


def get_pos():
    empty, virus = [], []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                empty.append((i, j))
            elif graph[i][j] == 2:
                virus.append((i, j))
    return empty, virus


def set_wall(comb):
    for x, y in comb:
        graph[x][y] = 1


def collapse_wall(comb):
    for x, y in comb:
        graph[x][y] = 0


def bfs(virus):
    queue = deque(virus)
    visited = [[False] * m for _ in range(n)]
    cnt = len(virus)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    cnt += 1
    return cnt


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
empty, virus = get_pos()
combs = combinations(empty, 3)
count = int(1e9)

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for comb in combs:
    set_wall(comb)

    temp = bfs(virus)
    if temp < count:
        count = temp

    collapse_wall(comb)

# 벽의 개수 계산
wall = n * m - (len(empty) + len(virus))

# 출력
print(n * m - (count + wall + 3))


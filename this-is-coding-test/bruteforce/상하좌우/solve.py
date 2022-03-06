# 시작 좌표 (1, 1)
n = int(input())
route = list(input().split())
x, y = 1, 1

# L, R, U, D
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)
move_types = ['L', 'R', 'U', 'D']

for i in range(len(route)):
    j = move_types.index(route[i])
    nx = x + dx[j]
    ny = y + dy[j]

    if nx < 1 or nx > n or ny > n or ny < 1:
        continue
    x, y = nx, ny

print(x, y)

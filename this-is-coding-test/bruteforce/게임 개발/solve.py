n, m = map(int, input().split())
d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

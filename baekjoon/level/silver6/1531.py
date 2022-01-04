import sys
input = sys.stdin.readline

N , M = map(int, input().split())


picture = [[0] * 100 for _ in range(100)]
cnt = 0

for _ in range(N):
    x_1, y_1, x_2, y_2 = map(int, input().split())
    for x in range(x_1 - 1, x_2):
        for y in range(y_1 - 1, y_2):
            picture[x][y] += 1

for i in range(100):
    for j in range(100):
        if picture[i][j] > M:
            cnt += 1

print(cnt)





import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
m = int(input())

# 초기화
snail = [[0] * n for _ in range(n)]
x = y = (n - 1) // 2
snail[x][y] = 1

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

i = 2
start = 3

# if elif 로 순서를 정해줄 수 있음
while x != 0 or y != 0:
    while i <= start * start:
        if x == y == (n - 1) // 2:
            up, down, left, right = start, start - 1, \
                                    start - 1, start - 2
            x += dx[0]
            y += dy[0]
            up -= 1
        elif right > 0:
            x += dx[1]
            y += dy[1]
            right -= 1
        elif down > 0:
            x += dx[2]
            y += dy[2]
            down -= 1
        elif left > 0:
            x += dx[3]
            y += dy[3]
            left -= 1
        elif up > 0:
            x += dx[0]
            y += dy[0]
            up -= 1

        snail[x][y] = i
        i += 1
    n -= 2
    start += 2

for i in range(n):
    print(*snail[i])
    if m in start[i]:
        print(i + 1, snail[i].index(m) + 1)

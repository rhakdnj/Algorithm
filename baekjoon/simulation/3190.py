"""
사과를 억으면 뱀의 길이가 늘어남

N * N
뱀의 시작위치는 0, 0 뱀의 길이는 1 처음에 오른쪽을 향한다.
뱀은 매초마다 이동을 하는데
- 뱀은 몸길이를 늘려 머리를 다음칸에 위치


"""
from collections import deque

n = int(input())
k = int(input())
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
graph = [[0] * n for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 2  # apple -> 2

L = int(input())
dir_dict = dict()
queue = deque([(0, 0)])

for _ in range(L):
    x, c = input().split()
    dir_dict[int(x)] = c

x, y = 0, 0
graph[x][y] = 1
cnt = 0
direction = 0


def turn(alpha):
    global direction
    if alpha == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4


while True:
    cnt += 1
    x += dx[direction]
    y += dy[direction]

    if x < 0 or x >= n or y < 0 or y >= n:
        break
    if graph[x][y] == 2:
        graph[x][y] = 1
        queue.append((x, y))
        if cnt in dir_dict:
            turn(dir_dict[cnt])
    elif graph[x][y] == 0:
        graph[x][y] = 1
        queue.append((x, y))
        pop_x, pop_y = queue.popleft()
        graph[pop_x][pop_y] = 0
        if cnt in dir_dict:
            turn(dir_dict[cnt])
    else:
        break

print(cnt)
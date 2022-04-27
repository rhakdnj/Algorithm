from collections import deque

w, h = map(int, input().split())
graph = [[0] * (w + 2) for _ in range(h + 2)]

for i in range(1, h + 1):
    graph[i][1: w + 1] = list(map(int, input().split()))

# graph y,x 가 아닌 x,y 로 보기
dx = [0, 1, 1, 0, -1, -1]
dy = [[1, 0, -1, -1, -1, 0], [1, 1, 0, -1, 0, 1]]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited = [[False for _ in range(w + 2)] for _ in range(h + 2)]
    visited[x][y] = True
    cnt = 0
    while queue:
        x, y = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[x % 2][i]

            if 0 <= nx < h + 2 and 0 <= ny < w + 2:
                # 0이면 주변에 1을 체크를 위해 큐에 append
                if graph[nx][ny] == 0 and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                # 6각형 면마다 count
                elif graph[nx][ny] == 1:
                    cnt += 1
    return cnt


print(bfs(0, 0))

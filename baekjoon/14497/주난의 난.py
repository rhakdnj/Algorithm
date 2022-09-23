from collections import deque

# x, y 바꿈, 그리고 0 시작이 아닌 1이 시작!
n, m = map(int, input().split())
visited = [[0 for _ in range(301)] for _ in range(301)]

y1, x1, y2, x2 = map(int, input().split())
y1, x1, y2, x2 = y1 - 1, x1 - 1, y2 - 1, x2 - 1

arr = [list(input()) for _ in range(n)]
dy, dx = (-1, 0, 1, 0), (0, 1, 0, -1)


def solution():
    global arr
    cnt = 0

    dq = deque()
    dq.append((y1, x1))
    while arr[y2][x2] != '0':
        cnt += 1
        temp = deque()
        while len(dq):
            y, x = dq.popleft()
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if ny < 0 or ny >= n or nx < 0 or nx >= m or visited[ny][nx]:
                    continue
                visited[ny][nx] = cnt
                if arr[ny][nx] != '0':
                    arr[ny][nx] = '0'
                    temp.append((ny, nx))
                else:
                    dq.append((ny, nx))
        dq = temp

    print(visited[y2][x2])


solution()

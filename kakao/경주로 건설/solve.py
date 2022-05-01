from collections import deque


def solution(board: list):
    n = len(board)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((0, 0, 0, 0))  # 좌표, 방향
    dist = [[0] * n for _ in range(n)]

    while q:
        x, y, car_d, value = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] != 1:
                    if nx == 0 and ny == 0:
                        continue
                    if x == 0 and y == 0:
                        new_value = value + 100
                    else:
                        if car_d == i:
                            new_value = value + 100
                        else:
                            new_value = value + 600
                    if dist[nx][ny] == 0:
                        dist[nx][ny] = new_value
                        q.append((nx, ny, i, new_value))
                    else:
                        if dist[nx][ny] >= new_value:
                            dist[nx][ny] = new_value
                            q.append((nx, ny, i, new_value))
        return dist[-1][-1]

from collections import deque


def bfs(place, x, y):
    visited = [[0] * 5 for _ in range(5)]
    visited[x][y] = True
    q = deque()
    q.append((x, y, 0))
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        x, y, cnt = q.popleft()
        if cnt > 2:
            continue
        if cnt != 0 and place[x][y] == 'P':
            return False
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            if new_x < 0 or new_x >= 5 or new_y < 0 or new_y >= 5:
                continue
            if place[new_x][new_y] == 'X':
                continue
            if visited[new_x][new_y]:
                continue
            visited[new_x][new_y] = True
            q.append((new_x, new_y, cnt + 1))
    return True


def check(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                if not bfs(place, i, j):
                    return False
    return True


def solution(places):
    answer = []
    for place in places:
        if distance(place):
            answer.append(1)
        else:
            answer.append(0)
    return answer

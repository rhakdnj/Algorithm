### 경주로 건설

1. 글로벌 변수로 global 키워드
2. distance 변수로 메모이제이션
3. 

```python
from collections import deque


def calc_cost(cur_dir, nex_dir, cost):
    if (cur_dir == 'R' or cur_dir == 'L') and (nex_dir == 'L' or nex_dir == 'R'):
        return cost + 100
    if (cur_dir == 'D' or cur_dir == 'U') and (nex_dir == 'D' or nex_dir == 'U'):
        return cost + 100
    if (cur_dir == 'R' or cur_dir == 'L') and (nex_dir == 'D' or nex_dir == 'U'):
        return cost + 600
    if (cur_dir == 'D' or cur_dir == 'U') and (nex_dir == 'R' or nex_dir == 'L'):
        return cost + 600


def bfs(x, y, cost, direct):
    queue = deque([(x, y, cost, direct)])
    distance = [[0 for _ in range(N)] for _ in range(N)]
    distance[x][y] = 1
    while queue:
        x, y, cost, cur_dir = queue.popleft()
        if x == N - 1 and y == N - 1:
            answer.append(cost)
            continue
        for i, j, d in (0, 1, 'R'), (1, 0, 'D'), (0, -1, 'L'), (-1, 0, 'U'):
            new_x, new_y, new_cost = x + i, y + j, calc_cost(cur_dir, d, cost)
            if new_x < 0 or new_y < 0 or new_x >= N or new_y >= N:
                continue
            if not new_board[new_x][new_y]:
                if not distance[new_x][new_y] or distance[new_x][new_y] > new_cost:
                    distance[new_x][new_y] = new_cost
                    queue.append((new_x, new_y, new_cost, d))


def solution(board):
    global N, distance, new_board, answer
    answer = []
    N = len(board)
    new_board = [board[i][:] for i in range(N)]
    bfs(0, 0, 0, 'R')
    bfs(0, 0, 0, 'D')
    return min(answer)
```

### 거리두기 확인한기

1. P일 때만 bfs로 주변 거리 2에 P가 존재하는지 check

```python
from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(place, x, y):
    q = deque([(x, y, 0)])
    visited = [[0] * 5 for _ in range(5)]
    visited[x][y] = True
    while q:
        x, y, cnt = q.popleft()
        if cnt > 2:
            continue
        if place[x][y] == 'P' and cnt != 0:
            return False
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue
            if place[nx][ny] == 'X':
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, cnt + 1))
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
        if check(place):
            answer.append(1)
        else:
            answer.append(0)
    return answer
```


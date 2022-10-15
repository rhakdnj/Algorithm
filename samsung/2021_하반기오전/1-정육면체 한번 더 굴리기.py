from collections import deque

OUT_OF_GRID = (-1, -1)


def is_in_range(y, x):
    return 0 <= y < n and 0 <= x < n


def can_go(y, x, target_num):
    return is_in_range(y, x) and not visited[y][x] and grid[y][x] == target_num


# 현재 위치를 기준으로 점수를 계산
def get_score(target_num):
    # visited 초기화
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    # start 표시
    visited[curr_y][curr_x] = True
    dq.append((curr_y, curr_x))

    score = 0

    while len(dq):
        y, x = dq.popleft()
        score += target_num

        for dy, dx in zip(dys, dxs):
            ny, nx = y + dy, x + dx
            if can_go(ny, nx, target_num):
                dq.append((ny, nx))
                visited[ny][nx] = True

    return score


# 해당 방향으로 이동했을 때의 다음 위치를 구합니다.
# 이동이 불가능할 경우 OUT_OF_GRID를 반환합니다.
def next_pos():
    ny, nx = curr_y + dys[move_dir], curr_x + dxs[move_dir]
    return (ny, nx) if is_in_range(ny, nx) else OUT_OF_GRID


def solution():
    global ans
    global curr_y, curr_x, move_dir
    global up, front, right

    # 주사위 굴리다.
    ny, nx = next_pos()

    # 격자를 벗어난 위치:
    if (ny, nx) == OUT_OF_GRID:
        move_dir = (move_dir + 2) if move_dir < 2 else (move_dir - 2)
        ny, nx = next_pos()

    curr_y, curr_x = ny, nx

    ans += get_score(grid[curr_y][curr_x])

    # 주사위가 놓여있는 상태를 조정합니다.
    if move_dir == 0:  # 오른쪽
        up, front, right = 7 - right, front, up
    elif move_dir == 1:  # 아래쪽
        up, front, right = 7 - front, up, right
    elif move_dir == 2:  # 왼쪽 
        up, front, right = right, front, 7 - up
    else:  # 위쪽
        up, front, right = front, 7 - up, right

    # 주사위의 바닥면에 적혀있는 숫자와, 격자 숫자를 비교합니다.
    bottom = 7 - up
    # 주사위에 적힌 숫자가 더 크면 시계방향으로 90' 회전합니다.
    if bottom > grid[curr_y][curr_x]:
        move_dir = (move_dir + 1) % 4
    # 주사위에 적힌 숫자가 더 작으면 반시계방향으로 90' 회전합니다.
    elif bottom < grid[curr_y][curr_x]:
        move_dir = (move_dir - 1 + 4) % 4


if __name__ == "__main__":
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]

    # 오른쪽: 0, 아래: 1, 왼쪽: 2, 위: 3
    dys, dxs = (0, 1, 0, -1), (1, 0, -1, 0)
    curr_y, curr_x = 0, 0
    move_dir = 0
    up, front, right = 1, 2, 3

    dq = deque()
    ans = 0

    for _ in range(m):
        solution()

    print(ans)

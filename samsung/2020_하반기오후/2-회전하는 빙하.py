"""
n개의 정수가 순서대로 주어질 때, n−1개의 연산자를 정수 사이에 하나씩 배치하고자 합니다.
이 때 주어진 정수의 순서를 바꿀 수 없으며, 연산자는 덧셈, 뺄셈, 곰셈 이렇게 세 가지 종류가 있습니다.
연산자 간의 우선 순위를 무시하고 앞에서부터 차례대로 연산한다고 하였을 때,
가능한 식의 최솟값과 최댓값을 출력하는 코드를 작성해보세요.
"""
from collections import deque


def in_range(y, x):
    return 0 <= y < grid_size and 0 <= x < grid_size


def can_go(y, x):
    return in_range(y, x) and not visited[y][x] and grid[y][x]


def bfs():
    group_size = 0

    while len(dq):
        y, x = dq.popleft()
        group_size += 1

        for dy, dx in zip(dys, dxs):
            ny, nx = y + dy, x + dx

            if can_go(ny, nx):
                dq.append((ny, nx))
                visited[ny][nx] = True

    return group_size


# 남아 있는 빙하의 총 양
def get_number_of_ices():
    return sum([grid[i][j] for i in range(grid_size) for j in range(grid_size)])


# 얼음 군집 중 최대 크기를 계산
def get_biggest_size():
    max_size = 0

    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] and not visited[i][j]:
                # 시작 위치를 deque에 넣고 bfs
                # bfs 진행 이후 그룹의 크기 중 최대값을 찾습니다.
                visited[i][j] = True
                dq.append((i, j))
                max_size = max(max_size, bfs())

    return max_size


# start_row, start_col에서 half_size 크기의 격자를
# move_dir 방향으로 이동합니다.
def move(start_row, start_col, half_size, move_dir):
    for row in range(start_row, start_row + half_size):
        for col in range(start_col, start_col + half_size):
            n_row = row + dys[move_dir] * half_size
            n_col = col + dxs[move_dir] * half_size

            next_grid[n_row][n_col] = grid[row][col]


def rotate(level):
    # Step1.
    # rotate 이후의 상태를 저장할 배열을 0 으로 초기화한다.
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = 0

    box_size, half_size = 1 << level, 1 << (level - 1)

    # Step2. 조건에 맞게 회전을 진행합니다.

    # Step2-1 회전할 2**L 크기 격자의 왼쪽 위 모서리 위치를 잡습니다.
    for i in range(0, grid_size, box_size):
        for j in range(0, grid_size, box_size):
            # Step2-2. 움직여야하는 2** (L - 1) 크기 격자의
            # 왼쪽 위 모서리를 각각 잡아
            # 알맞은 방향으로 이동시킵니다.
            move(i, j, half_size, 0)
            move(i, j + half_size, half_size, 1)
            move(i + half_size, j, half_size, 2)
            move(i + half_size, j + half_size, half_size, 3)

    # Setp3.
    # rotate 이후의 결과를 다시 grid 배열로 가져옵니다.
    for i in range(grid_size):
        for j in range(grid_size):
            grid[i][j] = next_grid[i][j]


def get_neightbor_nums(curr_y, curr_x):
    cnt = 0
    for dy, dx in zip(dys, dxs):
        ny, nx = curr_y + dy, curr_x + dx

        if in_range(ny, nx) and grid[ny][nx]:
            cnt += 1

    return cnt


def melt():
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = 0

    for i in range(grid_size):
        for j in range(grid_size):
            cnt = get_neightbor_nums(i, j)
            if grid[i][j] and cnt < 3:
                next_grid[i][j] = grid[i][j] - 1
            else:
                next_grid[i][j] = grid[i][j]

    for i in range(grid_size):
        for j in range(grid_size):
            grid[i][j] = next_grid[i][j]


if __name__ == '__main__':
    n, q = map(int, input().split())

    grid_size = 1 << n
    grid = [list(map(int, input().split())) for _ in range(grid_size)]
    next_grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

    levels = list(map(int, input().split()))

    visited = [[False for _ in range(grid_size)] for _ in range(grid_size)]
    dys, dxs = (0, 1, 0, -1), (1, 0, -1, 0)
    dq = deque()

    for level in levels:
        if level:
            rotate(level)
        melt()

    print(get_number_of_ices())
    print(get_biggest_size())

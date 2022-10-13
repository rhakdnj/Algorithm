n = int(input())
square_n = n // 2
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
next_ = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 그룹의 개수를 관리합니다.
group_n = 0

# 각 칸에 그룹 번호를 적어줍니다.
group = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 각 그룹마다 칸의 수를 세줍니다.
group_cnt = [0 for _ in range(n * n + 1)]
visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

dy, dx = (-1, 0, 1, 0), (0, 1, 0, -1)


def is_out_range(y, x):
    return not (0 <= y < n and 0 <= x < n)


def dfs(y, x):
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if is_out_range(ny, nx) or visited[ny][nx]:
            continue
        if arr[ny][nx] == arr[y][x]:
            visited[ny][nx] = 1
            group[ny][nx] = group_n
            group_cnt[group_n] += 1
            dfs(ny, nx)


# 그룹을 만들어줍니다.
def make_group():
    global group_n

    group_n = 0
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0

    # DFS를 이용하여 그룹 묶는 작업을 진행합니다.
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                group_n += 1
                visited[i][j] = 1
                group[i][j] = group_n
                group_cnt[group_n] = 1
                dfs(i, j)


def get_art_score():
    art_score = 0

    # 특정 변을 사이에 두고 두 칸의 그룹이 다른
    for i in range(n):
        for j in range(n):
            for i in range(4):
                ny, nx = i + dy[i], j + dx[i]
                if is_out_range(ny, nx) or arr[i][j] == arr[ny][nx]:
                    continue
                g1, g2 = group[i][j], group[ny][nx]
                num1, num2 = arr[i][j], arr[ny][nx]
                cnt1, cnt2 = group_cnt[g1], group_cnt[g2],

                art_score += (cnt1 + cnt2) * num1 * num2

    # 중복 계산을 제거합니다.
    return art_score // 2


def get_score():
    # 그룹을 형성한다.
    make_group()

    # 예술 점수를 계산
    return get_art_score()


def rotate_square(sy, sx, square_n):
    # 정사각형을 시계방향으로 90' 회전합니다.
    for y in range(sy, sy + square_n):
        for x in range(sx, sx + square_n):
            oy, ox = y - sy, x - sx
            ry, rx = ox, square_n - oy - 1
            next_[ry + sy][rx + sx] = arr[y][x]


def rotate():
    for i in range(n):
        for j in range(n):
            next_[i][j] = 0

    for i in range(n):
        for j in range(n):
            # Case 2-1) 세로줄 (i, j) -> (j, i)
            if j == n // 2:
                next_[j][i] = arr[i][j]
            # Case 2-2) 가로줄 (i, j) -> (n - j - 1 , i)
            elif i == n // 2:
                next_[n - j - 1][i] = arr[i][j]

    rotate_square(0, 0, square_n)
    rotate_square(0, square_n + 1, square_n)
    rotate_square(square_n + 1, 0, square_n)
    rotate_square(square_n + 1, square_n + 1, square_n)

    # Step 3.
    for i in range(n):
        for j in range(n):
            arr[i][j] = next_[i][j]


answer = 0
for _ in range(4):
    answer += get_score()
    rotate()

print(answer)

# def cross_rotate():
#     temp = []
#     for i in range(size):
#         temp.append(board[size][i])
#
#     for i in range(size):
#         board[i][size] = board[size][-1 + i]
#
#     for i in range(size):
#         board[size][-1 + i] = board[-1 + i][size]
#
#     for i in range(size):
#         board[-1 + i][size] = board[size][i]
#
#     for i in range(size):
#         board[size][i] = temp[i]


# def rotate(y, x):
#     temp = []
#     for i in range(4):
#         temp = [k[::-1] for k in zip(*board[y: y + size][x: x + size])]
#     for i in range(y, y + size):
#         for j in range(x, x + size):
#             board[i][j] = temp[i - y][j - x]

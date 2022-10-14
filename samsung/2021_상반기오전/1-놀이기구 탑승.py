def is_in_range(y, x):
    return 0 <= y < n and 0 <= x < n


def is_friend(stu_num, friend_num):
    return friends[stu_num][friend_num]


def get_curr_cell(stu_num, y, x):
    friend_cnt, blank_cnt = 0, 0
    for dy, dx in zip(dys, dxs):
        ny, nx = y + dy, x + dx
        if not is_in_range(ny, nx):
            continue

        if grid[ny][nx] == -1:
            blank_cnt += 1
        elif is_friend(stu_num, grid[ny][nx]):
            friend_cnt += 1

    return friend_cnt, blank_cnt, -y, -x


def place_stu(stu_num):
    best_cell = (0, 0, -n, -n)
    # 우선순위가 가장 높은 칸을 선택
    for i in range(n):
        for j in range(n):
            if grid[i][j] == -1:
                curr_cell = get_curr_cell(stu_num, i, j)

                if best_cell < curr_cell:
                    best_cell = curr_cell

    _, _, y, x = best_cell
    grid[-y][-x] = stu_num


def get_score(y, x):
    cnt = 0
    for dy, dx in zip(dys, dxs):
        ny, nx = y + dy, x + dx
        if is_in_range(ny, nx) and is_friend(grid[y][x], grid[ny][nx]):
            cnt += 1

    return int(10 ** (cnt - 1))


def get_total_score():
    return sum([get_score(i, j) for i in range(n) for j in range(n)])


if __name__ == '__main__':
    n = int(input())

    student_order = [0 for _ in range(n ** 2)]
    friends = [[False for _ in range(n ** 2)] for _ in range(n ** 2)]

    for i in range(n ** 2):
        student_data = list(map(int, input().split()))

        student_order[i] = student_data[0] - 1

        for friend_num in student_data[1:]:
            friends[student_order[i]][friend_num - 1] = True

    # 0 도 배치하므로 grid -1로 초기화 해야 한다.
    grid = [[-1 for _ in range(n)] for _ in range(n)]

    dys, dxs = (-1, 0, 1, 0), (0, 1, 0, -1)

    ans = 0

    for i in range(n ** 2):
        place_stu(student_order[i])

    ans = get_total_score()

    print(ans)

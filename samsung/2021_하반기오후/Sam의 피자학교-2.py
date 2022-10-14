# 입력받기
n, k = map(int, input().split())  # n은 4의 배수
arr = list(map(int, input().split()))
n_arr = [0] * n  # 도우를 누를때 사용
arr_xy = [(-1, -1)] * n  # 좌표 담는 배열
arr_xy[0] = (0, 0)
row, col = 1, 1


# 1. 밀가루min에 +1
def step_one():
    m = min(arr)
    for i in range(n):
        if arr[i] == m:
            arr[i] += 1


def can_roll():
    return row <= n - (row * col)


# 2. 도우를 말아줍니다.
def step_two():
    global row, col
    row, col = 1, 1

    while True:
        # 말기 전에 검사 (말수 없으면 중단하기)
        if not can_roll():
            break

        # 한번 말기 (x, y) -> (y, row - x - 1)
        for i in range(row * col):
            x, y = arr_xy[i]
            next_x, next_y = y, row - x - 1
            arr_xy[i] = (next_x, next_y)

        # row 한번 늘어나고
        next_row = row + 1
        # 나머지 아래 행 채워주기
        enu = 0
        for i in range(row * col, next_row * col):
            arr_xy[i] = (next_row - 1, enu)
            enu += 1
        # 새로운 row 저장
        row = next_row

        # 말기 전에 검사 (말수 없으면 중단하기)
        if not can_roll():
            break

        # 두번째 말기
        for i in range(row * col):
            x, y = arr_xy[i]
            next_x, next_y = y, row - x - 1
            arr_xy[i] = (next_x, next_y)

        # col 한번 늘어나고
        next_col = col + 1
        # 나머지 아래 행 채워주기
        enu = 0
        for i in range(row * col, row * next_col):
            arr_xy[i] = (row - 1, enu)
            enu += 1
        # 새로운 col 저장
        col = next_col

    enu = col
    for i in range(row * col, n):
        arr_xy[i] = (row - 1, enu)
        enu += 1


# 3. 도우 상하좌우 값에 맞게 더해줍니다.
def step_three():
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    for i in range(n):
        n_arr[i] = 0  # 초기화

    for idx in range(n):
        x, y = arr_xy[idx]
        mil1 = arr[idx]  # 밀가루1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 좌표가 없으면 패스
            if (nx, ny) not in arr_xy:
                continue
            # 있으면 계산하여 +-
            mil2 = arr[arr_xy.index((nx, ny))]  # 밀가루2
            di = abs(mil1 - mil2) // 5  # 빼줄값
            # 현재 idx 칸에 해당하는 것만 수행
            if mil1 < mil2:
                n_arr[idx] += di
            if mil1 > mil2:
                n_arr[idx] -= di
    for i in range(n):
        arr[i] += n_arr[i]


# 4. 열이 작은 것> 행이 작은 것 나열
def step_four():
    # 각 좌표가 arr의 몇번째 값을 가지는지 저장
    arr_xy_dic = dict()
    for i in range(n):
        arr_xy_dic[arr_xy[i]] = i

    # 좌표를 정렬한다.
    arr_xy.sort(key=lambda x: (x[1], -x[0]))

    # 순서대로 넣어서 도우를 다시 펴준다. n_arr
    for i in range(n):
        mov_idx = arr_xy_dic[arr_xy[i]]
        n_arr[i] = arr[mov_idx]

    # 편 도우를 arr에 넣어준다.
    for i in range(n):
        arr[i] = n_arr[i]
        arr_xy[i] = (0, i)


# 5. 도우를 반으로 두번 접는다.
def step_five():
    # 한번 접는다. 0 1 2 3 n//2 = 4
    for i in range(n // 2):
        arr_xy[n // 2 - 1 - i] = (0, i)
        arr_xy[n // 2 + i] = (1, i)

    # 두번 접는다.
    for i in range(n):
        x, y = arr_xy[i]
        if y >= n // 4:
            arr_xy[i] = (x + 2, y - n // 4)
        else:
            arr_xy[i] = (abs(x - 1), n // 4 - y - 1)


ans = 0
# main
while max(arr) - min(arr) > k:
    ans += 1
    step_one()  # 밀가루를 1만큼 넣기
    step_two()  # 도우를 말아주기
    # print(arr, arr_xy)
    step_three()  # 도우를 눌러주기 1
    # print(arr, arr_xy)
    step_four()  # 도우를 눌러주기 2
    # print(arr, arr_xy)
    step_five()  # 도우를 두번 접기
    # print(arr, arr_xy)

    step_three()  # 도우를 눌러주기 1
    # print(arr, arr_xy)
    step_four()  # 도우를 눌러주기 2
    # print(arr, arr_xy)
    # print(' ')

print(ans)

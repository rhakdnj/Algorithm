from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
new_arr = [[0 for _ in range(n)] for _ in range(n)]
dy, dx = (-1, 0, 1, 0), (0, 1, 0, -1)


def is_in_range(y, x):
    return 0 <= y < n and 0 <= x < n


def get_art_score():
    group_arr = [[0 for _ in range(n)] for _ in range(n)]
    group = 1
    group_cnt = [1e9]
    group_val = [1e9]

    for i in range(n):
        for j in range(n):
            if group_arr[i][j] == 0:
                dq = deque()
                dq.append((i, j))
                group_arr[i][j] = group
                cnt = 1

                while len(dq):
                    y, x = dq.popleft()

                    for d in range(4):
                        ny, nx = y + dy[d], x + dy[d]

                        if is_in_range(ny, nx) and group_arr[ny][nx] == 0 and arr[ny][nx] == arr[i][j]:
                            dq.append((ny, nx))
                            group_arr[ny][nx] = group
                            cnt += 1

                group_cnt.append(cnt)
                group_val.append(arr[i][j])
                group += 1

    shared_lines = [[0 for _ in range(group)] for _ in range(group)]
    visited = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                dq = deque()
                dq.append((i, j))
                visited[i][j] = 1

                while len(dq):
                    y, x = dq.popleft()

                    for d in range(4):
                        ny, nx = y + dy[d], x + dx[d]

                        if is_in_range(ny, nx) and not visited[ny][nx]:
                            if group_arr[ny][nx] == group_arr[i][j]:  # Same Group
                                dq.append((ny, nx))
                                visited[ny][nx] = 1
                            else:  # Different Group
                                shared_lines[group_arr[i][j]][group_arr[ny][nx]] += 1
                                shared_lines[group_arr[ny][nx]][group_arr[i][j]] += 1

    art_score = 0

    for i in range(1, group):
        for j in range(i + 1, group):
            art_score += (group_cnt[i] + group_cnt[j]) * group_val[i] * group_val[j] * shared_lines[i][j]

    return art_score


def rotate(y, x):
    row = y

    for j in range(x, x + n // 2):
        stack = []
        for i in range(y + n // 2 - 1, y - 1, -1):
            stack.append([arr[i][j]])
        new_arr[row][x:x + n // 2] = stack
        row += 1


ans = 0

for _ in range(4):
    ans += get_art_score()

    for i in range(n):
        for j in range(n):
            new_arr[i][j] = 0

    rotate(0, 0)
    rotate(0, n // 2 + 1)
    rotate(n // 2 + 1, 0)
    rotate(n // 2 + 1, n // 2 + 1)

    new_arr[n // 2][n // 2] = arr[n // 2][n // 2]

    for i in range(n // 2):  # 상에서 좌로
        new_arr[n // 2][i] = arr[i][n // 2]

    for i in range(n // 2 + 1, n, 1):  # 하에서 우로
        new_arr[n // 2][i] = arr[i][n // 2]

    for i in range(n // 2):  # 좌에서 하로
        new_arr[n - 1 - i][n // 2] = arr[n // 2][i]

    for i in range(n // 2):  # 우에서 상으로
        new_arr[i][n // 2] = arr[n // 2][n - 1 - i]

    for i in range(n):
        for j in range(n):
            arr[i][j] = new_arr[i][j]

print(ans)

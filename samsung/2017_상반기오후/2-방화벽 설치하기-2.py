from collections import deque

# 변수 선언 및 입력
n, m = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

empty_places = list()
selected_indices = list()
dq = deque()
max_empty_cnt = 0


# 주어진 위치로 이동할 수 있는지 여부를 확인합니다.
def can_go(y, x):
    return 0 <= y < n and 0 <= x < m and \
           not visited[y][x] and arr[y][x] != 1


# visited 배열을 초기화해줍니다.
def initialize_visited():
    for i in range(n):
        for j in range(m):
            visited[i][j] = False


# BFS 탐색을 위해 존재하는 불을 queue에 넣어줍니다.
def enqueue_fires():
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                dq.append((i, j))
                visited[i][j] = True


# 선택된 위치에 방화벽을 설치합니다.
def place_firewalls():
    for i in range(len(selected_indices)):
        idx = selected_indices[i]
        y, x = empty_places[idx]

        arr[y][x] = 1


# 다음 탐색을 위해 설치했던 방화벽을 제거합니다.
def remove_firewalls():
    for i in range(len(selected_indices)):
        idx = selected_indices[i]
        y, x = empty_places[idx]

        arr[y][x] = 0


# 선택된 빈 칸에 방화벽을 설치했을 때 영역의 크기를 구합니다.
def get_area():
    global max_empty_cnt

    dys, dxs = (-1, 0, 1, 0), (0, 1, 0, -1)

    # BFS 탐색을 위한 초기화 작업을 수행합니다.
    initialize_visited()
    place_firewalls()
    enqueue_fires()

    # BFS 탐색을 통해 해당 불이 방문하게 되는 영역을 구합니다.
    while len(dq):
        y, x = dq.popleft()

        for dy, dx in zip(dys, dxs):
            ny, nx = y + dy, x + dx

            if can_go(ny, nx):
                dq.append((ny, nx))
                visited[ny][nx] = True

    # BFS 탐색 과정에서 방문한 적이 없는 빈 칸의 개수를 세줍니다.
    empty_cnt = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and arr[i][j] == 0:
                empty_cnt += 1

    max_empty_cnt = max(empty_cnt, max_empty_cnt)

    # 탐색이 끝난 뒤 설치한 방화벽을 제거해줍니다.
    remove_firewalls()


def search_combinations(curr_idx, cnt):
    if cnt == 3:
        get_area()
        return

    if curr_idx == len(empty_places):
        return

    selected_indices.append(curr_idx)
    search_combinations(curr_idx + 1, cnt + 1)
    selected_indices.pop()

    search_combinations(curr_idx + 1, cnt)


# 빈 칸인 경우 가능한 조합을 탐색하기 위해
# 배열에 따로 저장해줍니다.
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            empty_places.append((i, j))

search_combinations(0, 0)
print(max_empty_cnt)

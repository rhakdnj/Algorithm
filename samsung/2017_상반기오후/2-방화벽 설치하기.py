from collections import deque

n, m = map(int, input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = []
empty = []
ans = 0
dys, dxs = (-1, 0, 1, 0), (0, 1, 0, -1)
dq = deque()


def enqueue_fires():
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                visited[i][j] = True
                dq.append((i, j))


def combination(li, n):
    if n == 0:
        return []
    if n == 1:
        return [tuple([i]) for i in li]

    ret = []
    for i in range(len(li)):
        combi = combination(li[i + 1:], n - 1)
        for rest in combi:
            ret.append(tuple([li[i]]) + rest)

    return ret


def get_safe_area_size():
    global dq
    while len(dq):
        y, x = dq.popleft()

        for dy, dx in zip(dys, dxs):
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and arr[ny][nx] != 1:
                dq.append((ny, nx))
                visited[ny][nx] = True

    empty_cnt = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and arr[i][j] == 0:
                empty_cnt += 1
    return empty_cnt


def solution():
    global ans, visited
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                empty.append((i, j))

    for combi in combination(range(len(empty)), 3):
        tmp = []
        for c in combi:
            tmp.append(empty[c])

        # visited 초기화
        visited = [[0 for _ in range(m)] for _ in range(n)]

        # dq 초기화
        enqueue_fires()

        # set firewall
        for i, j in tmp:
            arr[i][j] = 1

        ans = max(ans, get_safe_area_size())

        # remove firewall
        for i, j in tmp:
            arr[i][j] = 0

    print(ans)


solution()

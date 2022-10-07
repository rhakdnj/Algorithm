R, C = map(int, input().split())
a = [list(input()) for _ in range(R)]

dy, dx = (-1, 0, 1, 0), (0, 1, 0, -1)
ret = 0


def solution():
    global ret
    set_ = {(0, 0, a[0][0])}

    while len(set_):
        y, x, route = set_.pop()
        ret = max(ret, len(route))

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or nx < 0 or ny >= R or nx >= C or a[ny][nx] in route:
                continue
            set_.add((ny, nx, route + a[ny][nx]))


solution()
print(ret)

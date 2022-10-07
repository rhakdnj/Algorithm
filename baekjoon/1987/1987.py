R, C = map(int, input().split())
a = [list(input()) for _ in range(R)]
visited = [0 for _ in range(26)]

dy, dx = (-1, 0, 1, 0), (0, 1, 0, -1)
ret = 0


def solution(y: int, x: int, cnt: int):
    global ret
    ret = max(ret, cnt)

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if ny < 0 or nx < 0 or ny >= R or nx >= C:
            continue
        next_ = ord(a[ny][nx]) - ord('A')
        if not visited[next_]:
            visited[next_] = 1
            solution(ny, nx, cnt + 1)
            visited[next_] = 0


visited[ord(a[0][0]) - ord('A')] = 1
solution(0, 0, 1)
print(ret)

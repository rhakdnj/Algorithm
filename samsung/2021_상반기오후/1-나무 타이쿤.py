"""
특수 영양제는 1 x 1 땅에 있는 리브로수의 높이를 1 증가시키며,
만약 해당 땅에 씨앗만 있는 경우에는 높이 1의 리브로수를 만들어냅니다.

격자의 모든 행,열은 각각 끝과 끝이 연결되어 있습니다. 즉 격자 바깥으로 나가면 마치 지구가 둥근것처럼 반대편으로 돌아옵니다.
만약 n번 열에서 오른쪽에서 이동하는 경우에는 1번 열으로 이동하게 됩니다.
n이면 ->0 n + 1 -> 1

1. 특수 영양제를 이동 규칙에 따라 이동시킵니다.

2. 특수 영양제를 이동 시킨 후 해당 땅에 특수 영양제를 투입합니다.

3. 특수 영양제를 투입한 리브로수의 대각선으로 인접한 방향에 높이가 1 이상인 리브로수가 있는 만큼 높이가 더 성장합니다.
    대각선으로 인접한 방향이 격자를 벗어나는 경우에는 세지 않습니다.

4. 특수 영양제를 투입한 리브로수를 제외하고 높이가 2 이상인 리브로수는 높이 2를 베어서 잘라낸 리브로수로 특수 영양제를 사고,
    해당 위치에 특수 영양제를 올려둡니다.
"""


def cut():
    global specials
    tmp = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] >= 2 and (i, j) not in specials:
                grid[i][j] -= 2
                tmp.append((i, j))
    specials = tmp


def move(idx):
    global specials
    dy, dx, p = directions[idx]
    temp = []
    # 특수 영양제가 있는 땅의 리브로수는 높이가 1만큼 증가
    for y, x in specials:
        ny, nx = (y + p * dy + n) % n, (x + p * dx + n) % n
        grid[ny][nx] += 1

    # 대각선으로 인접한 높이 1 이상의 리브로수의 개수 만큼 높이가 증가
    for y, x in specials:
        ny, nx = (y + p * dy + n) % n, (x + p * dx + n) % n
        cnt = 0
        for i in (2, 4, 6, 8):
            nny, nnx = ny + dys[i], nx + dxs[i]
            if nny < 0 or nnx < 0 or nny >= n or nnx >= n:
                continue
            if grid[nny][nnx] != 0:
                cnt += 1

        grid[ny][nx] += cnt
        temp.append((ny, nx))

    specials = temp

    cut()


def get_height():
    return sum([grid[i][j] for i in range(n) for j in range(n)])


if __name__ == '__main__':
    n, m = tuple(map(int, input().split()))

    grid = [list(map(int, input().split())) for _ in range(n)]

    # 특수 영양제
    specials = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]

    # 2, 4, 6, 8: 대각선
    dys, dxs = (0, 0, -1, -1, -1, 0, 1, 1, 1), (0, 1, 1, 0, -1, -1, -1, 0, 1)
    directions = []
    for _ in range(m):
        d, p = tuple(map(int, input().split()))
        directions.append((dys[d], dxs[d], p))

    for i in range(m):
        move(i)

    ans = get_height()

    print(ans)

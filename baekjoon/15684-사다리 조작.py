def check():
    for i in range(1, n + 1):
        start = i
        for j in range(1, h + 1):
            if visited[j][start]:
                start += 1
            elif visited[j][start - 1]:
                start -= 1
        if start != i:
            return False
    return True


def go(here, cnt):
    global answer

    if cnt > 3 or cnt >= answer:
        return
    if check():
        answer = min(answer, cnt)
        return

    for i in range(here, h + 1):
        for j in range(1, n + 1):
            if visited[i][j] or visited[i][j - 1] or visited[i][j + 1]:
                continue
            visited[i][j] = True
            go(i, cnt + 1)
            visited[i][j] = False


def solution():
    for _ in range(m):
        a, b = map(int, input().split())
        # b번 세로선과 b+1번 세로선을 a번 기로선 위치에서 연결
        visited[a][b] = True

    go(1, 0)


if __name__ == '__main__':
    n, m, h = map(int, input().split())
    visited = [[False for _ in range(31)] for _ in range(31)]
    MAX = int(1e9)
    answer = MAX

    solution()

    print(f"{-1 if answer == MAX else answer}")

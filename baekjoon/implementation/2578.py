import sys


def input():
    return sys.stdin.readline().rstrip()


graph = [list(map(int, input().split())) for _ in range(5)]
targets = list()
for _ in range(5):
    targets.extend(list(map(int, input().split())))
visited = [[False] * 5 for _ in range(5)]


def check_bingo() -> int:
    global visited
    cnt = 0
    for i in range(5):
        if all(visited[i]):
            cnt += 1
        col = [visited[j][i] for j in range(5)]
        if all(col):
            cnt += 1

    diagonal_up = [visited[4 - i][i] for i in range(5)]
    diagonal_down = [visited[i][i] for i in range(5)]
    if all(diagonal_up):
        cnt += 1
    if all(diagonal_down):
        cnt += 1
    return cnt


for k in range(25):
    target = targets[k]
    for i in range(5):
        for j in range(5):
            if graph[i][j] == target:
                visited[i][j] = True
                if check_bingo() >= 3:
                    print(k + 1)
                    exit()
                break

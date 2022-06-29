import sys

answer = []
graph = []
# 상 -> 하 시계 방향
dx, dy = [-1, -1, 0, 1, 1, 1, 0, - 1], [0, 1, 1, 1, 0, -1, -1, -1]


def input():
    return sys.stdin.readline().rstrip()


def solution():
    global answer, graph
    n = int(input())
    graph = [list(input()) for _ in range(n)]
    answer = [list(input()) for _ in range(n)]

    flag = False
    for i in range(n):
        for j in range(n):
            if graph[i][j] == '.' and answer[i][j] == 'x':
                cnt = 0
                for k in range(8):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[nx][ny] == '*':
                            cnt += 1
                answer[i][j] = chr(cnt + ord('0'))

            if graph[i][j] == '*' and answer[i][j] == 'x':
                flag = True

    if flag:
        for i in range(n):
            for j in range(n):
                if graph[i][j] == '*':
                    answer[i][j] = '*'

    for i in range(n):
        print(''.join(answer[i]))

    # answer = list(map(''.join, [answer[i] for i in range(n)]))
    # print(answer)


solution()

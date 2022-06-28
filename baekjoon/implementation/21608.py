import sys


def input():
    return sys.stdin.readline().rstrip()


dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def solution(n, students):
    graph = [[0] * n for _ in range(n)]

    for order in range(n ** 2):
        student = students[order]
        # 가능한 자리를 앉힘
        temp = []
        for i in range(n):
            for j in range(n):
                if graph[i][j] != 0:
                    continue
                like = 0
                blank = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[nx][ny] in student[1:]:
                            like += 1
                        if graph[nx][ny] == 0:
                            blank += 1
                temp.append((like, blank, i, j))
        # like, blank 클수록, 행 열은 작은 것으로 정렬
        temp.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
        graph[temp[0][2]][temp[0][3]] = student[0]

    students.sort(key=lambda x: x[0])
    answer = 0

    for i in range(n):
        for j in range(n):
            res = 0
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] in students[graph[i][j] - 1]:
                        res += 1
            if res != 0:
                answer += 10 ** (res - 1)
    print(graph)
    print(answer)


n = int(input())
students = [list(map(int, input().split())) for _ in range(n * n)]
solution(n, students)

def solution(rows, columns, queries):
    answer = []
    arr = [[0] * columns for _ in range(rows)]

    t = 1
    for i in range(rows):  # 행렬 초기화
        for j in range(columns):
            arr[i][j] = t
            t += 1

    for x1, y1, x2, y2 in queries:
        temp = arr[x1 - 1][y1 - 1]
        mini = temp

        for i in range(x1 - 1, x2 - 1):  # 왼쪽 세로 방향
            v = arr[i + 1][y1 - 1]
            arr[i][y1 - 1] = v
            mini = min(mini, v)

        for i in range(y1 - 1, y2 - 1):  # 아래 가로 방향
            v = arr[x2 - 1][i + 1]
            arr[x2 - 1][i] = v
            mini = min(mini, v)

        for i in range(x2 - 1, x1 - 1, -1):  # 오른쪽 세로 방향
            v = arr[i - 1][y2 - 1]
            arr[i][y2 - 1] = v
            mini = min(mini, v)

        for i in range(y2 - 1, y1 - 1, -1):
            v = arr[x1 - 1][i - 1]
            arr[x1 - 1][i] = v
            mini = min(mini, v)

        arr[x1 - 1][y1] = temp
        answer.append(mini)
    return answer

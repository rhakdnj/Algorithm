from collections import deque


def solution(rows, columns, queries):
    arr = [[i + columns * j for i in range(1, columns + 1)] for j in range(rows)]
    queue, answer = deque(), []
    for i in queries:
        x1, y1, x2, y2 = i[0] - 1, i[1] - 1, i[2] - 1, i[3] - 1

        for x in range(y2 - y1):
            queue.append(arr[x1][y1 + x])
        for y in range(x2 - x1):
            queue.append(arr[x1 + y][y2])
        for z in range(y2 - y1):
            queue.append(arr[x2][y2 - z])
        for k in range(x2 - x1):
            queue.append(arr[x2 - k][y1])

        queue.rotate(1)
        answer.append(min(queue))

        for x in range(y2 - y1):
            arr[x1][y1 + x] = queue.popleft()
        for y in range(x2 - x1):
            arr[x1 + y][y2] = queue.popleft()
        for z in range(y2 - y1):
            arr[x2][y2 - z] = queue.popleft()
        for k in range(x2 - x1):
            arr[x2 - k][y1] = queue.popleft()
    return answer

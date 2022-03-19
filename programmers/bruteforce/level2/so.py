def solution(n, left, right):
    graph = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i >= j:
                graph[i][j] = i + 1
            else:
                graph[i][j] = graph[i][j - 1] + 1
    answer = []
    for row in graph:
        answer += row

    return answer[left: right + 1]


print(solution(4, 7, 14))

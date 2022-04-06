def solution(m, n, puddles):
    # IndexError 처리 안 해줘도 되며, 시작 좌표 1, 1 을 맞춤
    graph = [[0] * (m + 1) for _ in range(n + 1)]
    graph[1][1] = 1
    # 행, 렬 위치를 바꿔줌
    puddles = [[q, p] for p, q in puddles]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            if [i, j] in puddles:
                graph[i][j] = 0
            else:
                graph[i][j] = (graph[i - 1][j] + graph[i][j - 1]) % 1000000007

    return graph[n][m]

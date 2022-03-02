def solution(n, computers):
    visited = [False] * n

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j] and not visited[j]:
                visited[j] = True
                dfs()

    answer = 0
    return answer

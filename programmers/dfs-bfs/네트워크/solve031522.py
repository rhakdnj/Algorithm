def dfs(computers, v, visited):
    visited[v] = True
    for i in range(len(computers)):
        if not visited[i] and i != v and computers[v][i]:
            dfs(computers, i, visited)


def solution(n, computers):
    visited = [0] * n
    answer = 0
    for i in range(n):
        if False in visited and not visited[i]:
            dfs(computers, i, visited)
            answer += 1
    return answer

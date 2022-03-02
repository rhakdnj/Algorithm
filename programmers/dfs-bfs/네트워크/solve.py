def dfs(computers, v, visited, n):
    visited[v] = True
    for i in range(n):
        if not visited[i] and i != v and computers[v][i]:
            dfs(computers, i, visited, n)


def solution(n, computers):
    visited = [0] * n
    answer = 0
    for i in range(n):
        if False in visited and not visited[i]:
            dfs(computers, i, visited, n)
            answer += 1
    return answer

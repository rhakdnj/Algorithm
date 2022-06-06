def solution(row, col, direct):
    global answer, graph, visited

    if not visited[row][col]:
        answer += 1
        visited[row][col] = True

    for i in range(4):
        left = (direct - i - 1) % 4
        new_row, new_col, = row + dx[left], col + dy[left]

        if 0 <= new_row < n and 0 <= new_col < m:
            if graph[new_row][new_col] == 0 and not visited[new_row][new_col]:
                solution(new_row, new_col, left)
                return

    back = (direct + 2) % 4
    new_row, new_col, = row + dx[back], col + dy[back]

    if graph[new_row][new_col]:
        return
    solution(new_row, new_col, direct)


n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
answer = 0
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

solution(r, c, d)
print(answer)

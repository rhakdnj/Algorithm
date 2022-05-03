INF = int(1e9)
# n 회사의 개수, m은 경로의 개수
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0
for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

k, x = map(int, input().split())
# 1번회사 --> K 회사 까지 최단거리, K번회사에서 X회사까지 최단거리

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

distance = graph[1][k] + graph[k][x]

if distance == INF:
    print("-1")
else:
    print(distance)

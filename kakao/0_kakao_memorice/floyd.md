### 합승 택시 요금
```python

INF = 20000001


def floyd(dist, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]


def solution(n, s, a, b, fares):
    dist = [[INF for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    for edge in fares:
        dist[edge[0] - 1][edge[1] - 1] = edge[2]
        dist[edge[1] - 1][edge[0] - 1] = edge[2]

    floyd(dist, n)

    s -= 1
    a -= 1
    b -= 1
    answer = INF
    for k in range(n):
        answer = min(answer, dist[s][k] + dist[k][a] + dist[k][b])

    return answer
```
### 플로이드 워셜 알고리즘 개요

- 모든 노드에서 다른 모든 노드까지의 최단 경로를 모두 계산합니다.

- 플로이드 워셜 알고리즘은 다익스트라 알고리즘과 마찬가지로 단계별로 거쳐 가는 노드를 기준으로 알고리즘을 수행합니다.

    - 다만 매 단계마다 방문하지 않은 노드 중에 최단 거리를 갖는 노드를 찾는 과정이 필요하지 않습니다.

- 플로이드 워셜은 2차원 테이블에 최단 거리 정보를 저장합니다.

- 플로이드 워셜 알고리즘은 다이나믹 프로그래밍 유형에 속합니다.

```python
INF = int(1e9)  # 무한을 의미하는 10억을 설정

# 노드의 개수 및 간선의 개수 입력받기
n = int(input())
m = int(input())
dist = [[INF] * (n + 1) for _ in range(m + 1)]

# 자기 자신으로 가는 비용은 0으로 초기화
for i in range(n):
    dist[i][i] = 0

# 각 간선에 대한 정보를 입력 받아 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split())
    dist[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# 수행된 결과를 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dist[i][j] == INF:
            print("INFINITY", end=" ")
        else:
            print(dist[a][b], end=" ")
    print()


```
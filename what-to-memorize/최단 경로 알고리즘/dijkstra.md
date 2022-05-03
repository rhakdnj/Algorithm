## 최단 경로 문제

최단 경로 알고리즘은 가장 짧은 경로를 찾는 알고리즘을 의미합니다.

- 다양한 문제 상황

    - 한 지점에서 다른 한 지점까지의 최단 경로

    - 한 지점에서 다른 모든 지점까지의 최단 경로 `다익스트라 알고리즘`

    - 모든 지점에서 다른 모든 지점까지의 최단 경로 `플로이드 워셜 알고리즘`

### 다익스트라 최단 경로 알고리즘

특정한 노드에서 출발하여 다른 모든 노드로 가는 최단 경로를 계산합니다.

- 다익스트라 최단 경로 알고리즘은 그리디 알고리즘으로 분류
    - 매 상황에서 가장 비용이 적은 노드를 선택해 임의의 과정을 반복

**동작과정**

1. 출발 노드를 설정
2. 최단 거리 테이블을 초기화(`출발 노드: 0, 나머지: INF`)
3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
5. 3번과 4번을 반복

```python
import sys


def input():
    return sys.stdin.readline().rstrip()


# 무한을 의미하는 값
INF = int(1e9)
# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드를 입력 받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for _ in range(n + 1)]
# 방문 여부 리스트
visited = [False] * (n + 1)
# 최단 거리 테이블을 모두 무한으로 초기화
dist = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a 번 노드에서 b번 노드로 가는 비용 -> c
    graph[a].append((b, c))


# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0  # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n + 1):
        if dist[i] < min_value and not visited[i]:
            min_value = dist[i]
            index = i
    return index


def dijkstra(start):
    # 시작 노드 초기화
    dist[start] = 0
    visited[start] = True
    for j in graph[start]:
        dist[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
    for i in range(n - 1):
        cur = get_smallest_node()
        visited[cur] = True
        for j in graph[cur]:
            cost = dist[cur] + j[1]
            if cost < dist[j[0]]:
                dist[j[0]] = cost


# 다익스트라 알고리즘을 수행  
dijkstra(start)

# 모든 노드를 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한이라고 출력
    if dist[i] == INF:
        print("INFINITY")
    else:
        print(dist[i])
```

**간단한 구현 방법 성는 분석**

- 총 O(V)번에 걸쳐서 최단 거리가 가장 짧은 노드 매번 선형 탐색

- 따라서 전체 시간 복잡도 O(V^2)입니다.

- 일반적으로 코딩 테스트의 최단 경로 문제에서 전체 노드의 개수가 5000개 이하라면 이 코드로 문제를 해결할 수 있습니다.
    - 하지만 노드의 개수가 10,000개를 넘어가는 문제이면, 시간이 오래 걸리게 됩니다.

### 다익스트라 알고리즘: 개선된 구현 방법

단계마다 방문하지 않은 노드 중에서 최단거리가 가장 짧은 노드를 선택하기 위해 힙을 이용합니다.

- 현재의 최단 거리가 가장 짧은 노드를 선택해야 하므로 최소 힙을 사용합니다.

```python
import sys
from heapq import heappush, heappop

input = sys.stdin.readline().rstrip()
# 무한을 의미하는 값
INF = int(1e9)
# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드를 입력 받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for _ in range(n + 1)]
# 방문 여부 리스트
visited = [False] * (n + 1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a 번 노드에서 b번 노드로 가는 비용 -> c
    graph[a].append((b, c))

def dijkstra(start):
    heap = []
    heappush(heap, (0, start))
    distance[start] = 0
    while heap:
        dist, cur = heappop(heap)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시 
        if distance[cur] < dist:
            continue
        # 현재 노드와 연결된 다른 노드들을 확인
        for i in graph[cur]:
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            cost = distance[cur] + i[1]
            if cost < dist[i[0]]:
                distance[i[0]] = cost
                heappush(heap, (cost, i[0]))


# 다익스트라 알고리즘을 수행  
dijkstra(start)

# 모든 노드를 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])


```

**개선된 구형 방법 성능 분석**

- 힙 자료구조를 이용하는 다익스트라 알고리즘의 시간 복잡도는 O(ELogV)입니다.

- 노드를 하나씩 꺼내 검사하는 반복문은 노드의 개수 V 이상의 횟수로는 처리되지 않습니다. 

  - 결과적으로 현재 우선순위 큐에서 꺼낸 노드와 연결된 다른 노드들을 확인하는 총 횟수는 최대 간선의 개수만큼 연산이 수행될 수 있습니다.

- 전체 과정은 E개의 원소를 우선순위 큐에 넣었다가 모두 빼내는 연산과 매우 유사합니다.

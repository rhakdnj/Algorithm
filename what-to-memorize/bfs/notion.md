## DFS

1. 탐색 시작노드를 큐에 삽입하고 방문 처리를 합니다.
2. 큐에서 최상단 노드를 꺼낸뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리합니다.
3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복합니다.

```python
from collections import deque


def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑기
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현
visited = [False] * 9

# 정의된 DFS 함수 호출
bfs(graph, 1, visited)
```
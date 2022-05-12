from heapq import heappush, heappop

INF = int(1e9)

# 노드의 개수, 간선의 개수
v, e = map(int, input().split())
# 시작 노드
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for _ in range(v + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (v + 1)

# 간선 정보 입력 받기
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


def dijkstra(start):
    heap = []
    heappush(heap, (0, start))
    distance[start] = 0
    while heap:
        dist, curr = heappop(heap)

        if distance[curr] < dist:
            continue

        for i in graph[curr]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(heap, (cost, i[0]))


dijkstra(start)
for i in range(1, len(distance)):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])

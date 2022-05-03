from heapq import heappush, heappop

INF = int(1e9)
n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append(y, z)


def dijkstra(start):
    heap = []
    heappush(heap, (0, start))
    distance[start] = 0
    while heap:
        dist, cur = heappop(heap)
        if distance[cur] < dist:
            continue
        for i in graph[cur]:
            cost = distance[cur] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(heap, (cost, i[0]))


dijkstra(c)
count = 0
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count - 1, max_distance)

import heapq


heap = []
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
print(heap)

print(heapq.heappop(heap))
print(heap)

heap = [4, 1, 7, 3, 8, 5]
heapq.heapify(heap)
print(heap)

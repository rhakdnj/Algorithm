import heapq


def solution(operations):
    heap = []
    max_heap = []

    for op in operations:
        cur = op.split()
        if cur[0] == 'I':
            num = int(cur[1])
            heapq.heappush(heap, num)
            heapq.heappush(heap, (-num, num))
        else:
            if len(heap) == 0:
                continue
            elif cur[1] == '1':
                max_value = heapq.heappop(max_heap)[1]
                heap.remove(max_value)
            elif cur[1] == '-1':
                min_value = heapq.heappop(heap)
                max_heap.remove((-min_value, min_value))
    if heap:
        return [heapq.heappop(max_heap)[1], heapq.heappop(heap)]
    else:
        return [0, 0]


print(solution(["I 7","I 5","I -5","D -1"]))

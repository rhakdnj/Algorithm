import heapq


def solution(operations):
    heap = []

    for operation in operations:
        operator, operand = operation.split(' ')
        operand = int(operand)

        if operator == 'I':
            heapq.heappush(heap, operand)
        elif heap:
            if operand < 0:
                heapq.heappop(heap)
            else:
                heap.pop()
                heapq.heapify(heap)

    if not heap:
        return [0, 0]

    return [max(heap), heap[0]]


print(solution(["I 3", "I 2", "I 1", "D 1", "D 1", "I 3", "D -1"]))

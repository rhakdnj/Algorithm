import heapq


def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    heap = []

    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                # j[1], j[0]을 통해 j[1]을 기준으로 정렬
                heapq.heappush(heap, [j[1], j[0]])

        if len(heap) > 0:
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]
            answer += now - cur[1]
            i += 1
        else:
            now += 1
    return answer // len(jobs)


solution([[0, 3], [1, 9], [2, 6]])

import heapq


def solution(jobs):
    tasks = sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0]), reverse=True)
    queue = []
    heapq.heappush(queue, tasks.pop())
    cur_time, total_time = 0, 0

    while len(queue) > 0:
        dur, arr = heapq.heappop(queue)
        cur_time = max(cur_time + dur, arr + dur)
        total_time += cur_time - arr

        while len(tasks) > 0 and tasks[-1][1] <= cur_time:
            heapq.heappush(queue, tasks.pop())

        if len(tasks) > 0 and len(queue) == 0:
            heapq.heappush(queue, tasks.pop())

    return total_time // len(jobs)

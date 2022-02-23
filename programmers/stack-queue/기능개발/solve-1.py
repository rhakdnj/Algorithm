def solution(progresses, speeds):
    queue = []
    for p, s in zip(progresses, speeds):
        if len(queue) == 0 or queue[-1][0] < -((p-100)//s):
            queue.append([-((p-100)//s), 1])
        else:
            queue[-1][1] += 1
    return [q[1] for q in queue]

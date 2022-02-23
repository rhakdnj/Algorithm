def solution(progresses, speeds):
    answer = []
    time, count = 0, 0

    while len(progresses) > 0:
        if (progresses[0] + time * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1

        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1  # 1 #2
    answer.append(count)

    return answer

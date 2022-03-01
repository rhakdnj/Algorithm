def solution(bridge_length, weight, truck_weights):
    time = 0
    queue = [0] * bridge_length
    sum_queue = 0

    while queue:
        time += 1
        temp1 = queue.pop(0)
        if temp1:
            sum_queue -= temp1

        if truck_weights:
            if sum_queue + truck_weights[0] <= weight:
                temp2 = truck_weights.pop(0)
                queue.append(temp2)
                sum_queue += temp2
            else:
                queue.append(0)
    return time
def solution(bridge_length, weight, truck_weights):
    t = 0
    on = []  # (weight, stayed)
    while truck_weights or on:
        for i, e in enumerate(on):
            on[i] = (e[0], e[1] + 1)
        on = list(filter(lambda x: x[1] < bridge_length + 1, on))

        weight_sum = 0
        for e in on:
            weight_sum += e[0]

        if truck_weights:
            if weight_sum + truck_weights[0] <= weight:
                on.append((truck_weights.pop(0), 1))
        t += 1
        # print(str(t)+":"+str(on))
    return t

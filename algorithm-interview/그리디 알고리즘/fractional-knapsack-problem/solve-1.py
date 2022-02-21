def fractional_knapsack(cargo):
    capacity = 15
    # 단가 계산 역순 정렬
    pack = sorted(cargo, key=lambda c: -(c[0] / c[1]))

    # 단가 순 그리디 계산
    total_value: float = 0
    for p in pack:
        if capacity - p[1] >= 0:
            capacity -= p[1]
            total_value += p[0]
        else:
            fraction = capacity / p[1]
            total_value += p[0] * fraction
            break
    return round(total_value, 1)


cargo = [
    (4, 12),
    (2, 1),
    (10, 4),
    (1, 1),
    (2, 2),
]

print(fractional_knapsack(cargo))



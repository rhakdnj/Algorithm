from itertools import combinations


def solution(orders, course):
    answer = []
    food_map = [{} for _ in range(11)]
    max_cnt = [0 for _ in range(11)]

    for order in orders:
        for num in range(2, len(order) + 1):
            for i in combinations(sorted(order), num):
                key = ''.join(i)
                if key in food_map[num]:
                    food_map[num][key] += 1
                    max_cnt[num] = max(max_cnt[num], food_map[num][key])
                else:
                    food_map[num][key] = 1

    for num in course:
        for key, value in food_map[num].items():
            if value >= 2 and value == max_cnt[num]:
                answer.append(key)

    return sorted(answer)

from itertools import combinations_with_replacement


def solution(n, info):
    answer = []
    max_diff = 0
    for arrows in combinations_with_replacement(range(0, 10), n):
        lion_info = [0] * 11
        for arrow in arrows:
            lion_info[10 - arrow] += 1

        lion, apeach = 0, 0
        for i in range(11):
            if lion[i] == 0 and apeach[i] == 0:
                continue
            if lion[i] > apeach[i]:
                lion += 10 - i
            else:
                apeach += 10 - i
        if lion > apeach:
            if max_diff < (lion - apeach):
                max_diff = lion - apeach
                answer = lion_info

    if not answer:
        return [-1]
    return answer


solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0])

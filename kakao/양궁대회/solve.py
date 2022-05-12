from itertools import combinations_with_replacement


def solution(n: int, info: list) -> list:
    answer = [-1]
    win = False
    max_num = 0

    for res in list(combinations_with_replacement(range(0, 11), n)):
        lion_info = [0] * 11
        for r in res:
            lion_info[10 - r] += 1
        lion_score = 0
        apeach_score = 0
        for i, (li, ap) in enumerate(zip(lion_info, info)):
            if li == ap == 0:
                continue
            if ap >= li:
                apeach_score += 10 - i
            elif li > ap:
                lion_score += 10 - i

        if lion_score > apeach_score:
            win = True
            if lion_score - apeach_score > max_num:
                max_num = lion_score - apeach_score
                answer = lion_info
    if not win:
        return [-1]
    return answer


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))

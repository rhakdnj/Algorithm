from collections import Counter


def solution(N, stages):
    answer = {}
    counter = Counter(stages)
    cnt_users = len(stages)

    for i in range(1, N + 1):
        if cnt_users:
            cnt_fail_users = counter[i]
            answer[i] = cnt_fail_users / cnt_users
            cnt_users -= cnt_fail_users
        else:
            answer[i] = 0

    return sorted(answer, key=lambda x: -answer[x])

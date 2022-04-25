def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reported = {user: 0 for user in id_list}

    for r in set(report):
        reported[r.split()[1]] += 1

    for r in set(report):
        if reported[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

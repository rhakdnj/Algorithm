def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = list(set(report))
    reported = {x: [] for x in id_list}

    for r in report:
        reported[r.split()[1]].append(r.split()[0])

    for user in reported:
        if len(reported[user]) >= k:
            for u in reported[user]:
                idx = id_list.index(u)
                answer[idx] += 1
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
solution(id_list, report, 2)

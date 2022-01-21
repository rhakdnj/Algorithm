def solution(id_list, report, k):
    id_dict = {id: 0 for id in id_list}
    report_set = {id: set() for id in id_list}

    for re in report:
        reporter, reported = re.split()
        report_set[reported].add(reporter)

    for key, value in report_set.items():
        if len(value) >= k:
            for id in value:
                id_dict[id] += 1

    answer = []

    for id in id_list:
        answer.append(id_dict[id])

    return answer


if __name__ == "__main__":
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    res = solution(id_list, report, 2)
    print(res)

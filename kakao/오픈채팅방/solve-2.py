def solution(record):
    answer = []
    dic = {}
    printer = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}
    for r in record:
        r_split = r.split()
        if r_split[0] in ('Enter', 'Change'):
            dic[r_split[1]] = r_split[2]

    for r in record:
        r_split = r.split()
        if r_split[0] in printer:
            answer.append(dic[r_split[1]] + printer[r_split[0]])

    return answer


print(solution(
    ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))

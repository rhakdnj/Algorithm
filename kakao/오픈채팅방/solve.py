dic = dict()


def fix(uid, nickname, result):
    for i in result:
        if i[1] == dic[uid] and uid == i[0]:
            i[1] = nickname
    dic[uid] = nickname


def solution(record):
    come_str = "님이 들어왔습니다."
    out_str = "님이 나갔습니다."
    result = []

    for r in record:
        if len(r.split()) == 3:
            method, uid, nickname = r.split()

            if method == "Enter":
                if uid in dic:
                    # out -> enter (change)
                    fix(uid, nickname, result)
                    result.append([uid, nickname, come_str])
                else:
                    # enter
                    dic[uid] = nickname
                    result.append([uid, nickname, come_str])
            else:
                # change
                fix(uid, nickname, result)
        else:
            uid = r.split()[1]
            result.append([uid, dic[uid], out_str])

    result = [i[1] + i[2] for i in result]

    return result

def solution(msg):
    dic = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(1, 27)))
    answer = []

    while True:
        if msg in dic:
            answer.append(dic[msg])
            break
        for i in range(1, len(msg) + 1):
            if msg[0:i] not in dic:
                answer.append(dic[msg[0:i - 1]])
                dic[msg[0:i]] = len(dic) + 1
                msg = msg[i - 1:]
                break

    return answer
def solution(msg):
    answer = []
    dic = {chr(i + 64): i for i in range(1, 27)}
    num = 27

    while msg:
        size = 1
        while msg[:size] in dic and size <= len(msg):
            size += 1
        size -= 1

        answer.append(dic[msg[:size]])
        dic[msg[:size + 1]] = num
        num += 1
        msg = msg[size:]

    return answer

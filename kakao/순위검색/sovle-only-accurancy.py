"""
효율성은 떨어지는 이유는 lan, postion, level, food, cnt 를 따로 두는 것은 어떨까?
"""

def solution(info, query):
    answer = []
    info_dic = {}
    # info_dic = dict([i: [lan, position, level, food] for i in range(len(info))])
    for i in range(len(info)):
        lan, position, level, food, cnt = info[i].split()
        info_dic[i] = [lan, position, level, food, cnt]

    for str in query:
        cnt = 0
        want_list = [i for i in str.split() if i != 'and']
        for i in range(len(info)):
            check = True
            for j in range(4):
                if want_list[j] == '-':
                    continue
                if info_dic[i][j] != want_list[j]:
                    check = False
                    break
            if check and int(info_dic[i][-1]) >= int(want_list[-1]):
                cnt += 1
        answer.append(cnt)

    return answer

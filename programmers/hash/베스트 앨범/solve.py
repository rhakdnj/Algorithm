def solution(genres: list, plays: list):
    answer = []
    dict_cnt_g = {}
    items = [[genres[i], plays[i], i] for i in range(len(plays))]
    items.sort(key=lambda x: (x[0], -x[1], x[2]))

    for g, p, _ in items:
        if g not in dict_cnt_g:
            dict_cnt_g[g] = p
        else:
            dict_cnt_g[g] += p

    dict_cnt_g = sorted(dict_cnt_g.items(), key=lambda x: -x[1])

    for i in dict_cnt_g:
        count = 0
        for j in items:
            if i[0] == j[0]:
                count += 1
                if count > 2:
                    break
                else:
                    answer.append(j[2])

    return answer

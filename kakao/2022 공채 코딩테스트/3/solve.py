import math


def time_to_minutes(time: str) -> int:
    h, m = map(int, time.split(':'))
    return h * 60 + m


def solution(fees, records):
    answer = []
    dtime, dfee, utime, ufee = fees
    dic = dict()

    for r in records:
        time, c_id, history = r.split()
        c_id = int(c_id)

        if c_id in dic:
            dic[c_id].append([time_to_minutes(time), history])
        else:
            dic[c_id] = [[time_to_minutes(time), history]]

    rList = list(dic.items())
    rList.sort(key=lambda x: x[0])
    for r in rList:
        t = 0
        for rr in r[1]:
            if rr[1] == "IN":
                t -= rr[0]
            else:
                t += rr[0]
        if r[1][-1][1] == "IN":
            t += time_to_minutes('23:59')

        if t <= dtime:
            answer.append(dfee)
        else:
            answer.append(dfee + math.ceil((t - dtime) / utime) * ufee)

    return answer




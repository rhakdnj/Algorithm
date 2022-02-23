from math import ceil


def solution(progresses, speeds):
    days_left = list(map(lambda x: (ceil((100 - progresses[x]) / speeds[x])), range(len(progresses))))
    count = 1
    ret_list = []

    for i in range(len(days_left)):
        try:
            if days_left[i] < days_left[i + 1]:
                ret_list.append(count)
                count = 1
            else:
                days_left[i + 1] = days_left[i]
                count += 1
        except IndexError:
            ret_list.append(count)

    return ret_list

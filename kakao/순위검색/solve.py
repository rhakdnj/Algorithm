from itertools import combinations
from collections import defaultdict
from bisect import bisect_left


def solution(info, query):
    answer = []
    dic = defaultdict(list)
    for str in info:
        str = str.split()
        cond = info[:-1]
        score = int(str[-1])
        for i in range(5):
            case = list(combinations([0, 1, 2, 3], i))
            for c in case:
                tmp = cond.copy()
                for idx in c:
                    tmp[idx] = '-'
                key = ''.join(tmp)
                dic[key].append(score)

    for value in dic.values():
        value.sort()

    for q in query:
        q = q.replace("and ", "")
        q = q.split()
        target_key = ''.join(q[:-1])
        target_score = int(q[-1])
        count = 0
        if target_key in dic:
            target_list = dic[target_key]
            idx = bisect_left(target_list, target_score)
            count = len(target_list) - idx
        answer.append(count)
    return answer

# Counter
from collections import Counter


def solution(str1, str2):

    str1_list = [str1[i: i + 2].lower() for i in range(len(str1) - 1) if str1[i: i + 2].isalpha()]
    str2_list = [str2[i: i + 2].lower() for i in range(len(str2) - 1) if str2[i: i + 2].isalpha()]
    Counter1 = Counter(str1_list)
    Counter2 = Counter(str2_list)

    inter = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())

    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)

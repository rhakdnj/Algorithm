def solution(str1, str2):

    list1 = [str1[i: i+2].lower() for i in range(len(str1) - 1) if str1[i: i+2].isalpha()]
    list2 = [str2[i: i+2].lower() for i in range(len(str2) - 1) if str2[i: i+2].isalpha()]

    total_list = set(list1) | set(list2)
    inter = []
    union = []

    if total_list:
        for i in total_list:
            inter.extend([i] * min(list1.count(i), list2.count(i)))
            union.extend([i] * max(list1.count(i), list2.count(i)))

        answer = int(len(inter) / len(union) * 65536)
        return answer
    else:
        return 65536
    


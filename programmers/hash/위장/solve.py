from collections import Counter


def solution(clothes):
    answer = 1
    category = []
    for cloth in clothes:
        category.append(cloth[1])

    counter = Counter(category)

    #옷을 고르는 경우 + 옷을 입지 않는 경우 -> cnt + 1
    for cnt in counter.values():
        answer *= cnt + 1
    else:
        answer -= 1

    return answer

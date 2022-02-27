def solution(answers):
    answer = []
    scores = []
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt_1, cnt_2, cnt_3 = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == first[i % 5]:
            cnt_1 += 1
        if answers[i] == second[i % 8]:
            cnt_2 += 1
        if answers[i] == third[i % 10]:
            cnt_3 += 1
    scores += [cnt_1, cnt_2, cnt_3]

    max_v = max(scores)

    for i in range(3):
        if max_v == scores[i]:
            answer.append(i + 1)

    return answer


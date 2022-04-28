def solution(gems):
    answer = []
    dic = {gems[0]: 1}
    start, end = 0, 0
    size = len(set(gems))

    while end < len(gems):
        if gems[end] not in dic:
            dic[gems[end]] = 1
        else:
            dic[gems[end]] += 1

        end += 1

        if len(dic) == size:
            while start < end:
                if dic[gems[start]] > 1:
                    dic[gems[start]] -= 1
                    start += 1

                elif shortest > end - start:
                    shortest = end - start
                    answer = [start + 1, end]
                    break

                else:
                    break

    return answer

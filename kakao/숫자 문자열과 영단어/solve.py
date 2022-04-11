def solution(s):
    dic = {'zero': 0, 'one': 1, 'two': 2,
           'three': 3, 'four': 4, 'five': 5,
           'six': 6, 'seven': 7, 'eight': 8,
           'nine': 9
           }
    answer = ''
    number = ''

    for c in s:
        if ord('a') <= ord(c) <= ord('z'):
            number += c
            if number in dic:
                answer += str(dic[number])
                number = ''
        else:
            answer += c




    return int(answer)


print(solution("one4seveneight"))

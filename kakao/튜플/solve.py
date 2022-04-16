def solution(s):
    answer = []
    set_list = []
    stack = []
    temp = ''
    for i in range(1, len(s) - 1):
        if s[i] == ',' and len(stack) == 0:
            continue
        if s[i] == '{':
            stack.append('{')
        elif s[i] == '}':
            stack.pop()
            set_list.append(temp)
            temp = ''
        else:
            temp += s[i]
    set_list.sort(key=lambda x: len(x))
    answer.append(int(set_list[0]))
    for i in range(1, len(set_list)):
        temp = set_list[i].split(',')
        for j in temp:
            if int(j) in answer:
                continue
            else:
                answer.append(int(j))

    return answer

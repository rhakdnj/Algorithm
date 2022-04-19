def get_head_idx(file):
    for i in range(len(file)):
        if file[i].isalpha() or file[i] in (' ', '.', '-'):
            continue
        else:
            return i
    return len(file)


def get_num_idx(num):
    for i in range(len(num)):
        if num[i].isalpha() or num[i] in (' ', '.', '-'):
            return i
    return len(num)


def solution(files):
    answer = []
    temp = []
    for file in files:
        h_idx = get_head_idx(file)
        head, number = file[0:h_idx], file[h_idx:]
        n_idx = get_num_idx(number)
        number, tail = number[:n_idx], number[n_idx:]

        temp.append([head, number, tail])

    temp.sort(key=lambda x: (x[0].lower(), int(x[1])))

    answer = ["".join(file) for file in temp]
    return answer

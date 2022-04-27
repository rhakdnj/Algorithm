from collections import defaultdict


def string_game(string):
    alpha = defaultdict(list)

    for i in range(len(string)):
        if string.count(string[i]) >= k:
            alpha[string[i]].append(i)

    if not alpha:
        return -1,

    # k개 이상 있는 문자에 대해 문자열 게임 진행
    min_str = 10000
    max_str = 0

    for idx_list in alpha.values():
        for j in range(len(idx_list) - k + 1):
            temp = idx_list[j + k - 1] - idx_list[j] + 1
            if temp < min_str:
                min_str = temp
            if temp > max_str:
                max_str = temp
    return min_str, max_str


t = int(input())
for _ in range(t):
    string = input()
    k = int(input())

    print(*string_game(string))

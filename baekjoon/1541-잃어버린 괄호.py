import sys

input = lambda: sys.stdin.readline().rstrip()


def solution(string):
    split = string.split('-')

    answer = 0
    for i in range(len(split)):
        tmp = 0
        for num in split[i].split('+'):
            tmp += int(num)
        if i == 0:
            answer += tmp
        else:
            answer -= tmp

    print(answer)


if __name__ == '__main__':
    solution(input())

import re
from functools import cmp_to_key

t = int(input())
# 나뉘어진 데이터가 저장되는 위치
data = []

for _ in range(t):
    str = input()
    temp = re.findall("[a-zA-z]|\d+", str)
    data.append([str, temp])

alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"


def cmp(first, second):
    for i in range(min(len(first[1]), len(second[1]))):
        # 숫자열 > 알파벳
        if first[1][i].isdigit() and second[1][i].isalpha():
            return -1

        elif first[1][i].isalpha() and second[1][i].isdigit():
            return 1
        # 숫자 숫자 비교는 작은 숫자가 왼쪽이나 같은 경우 0의 갯수가 작은 것이 왼쪽으로 간다.
        elif first[1][i].isdigit() and second[1][i].isdigit():

            if int(first[1][i]) == int(second[1][i]):
                if len(first[1][i]) == len(second[1][i]):
                    continue
                # 0의 개수를 통해 return
                return len(first[1][i]) - len(second[1][i])
            else:
                # 십진수 값을 통해 return
                return int(first[1][i]) - int(second[1][i])
        # 문자열 문자열 비교
        else:
            if first[1][i] == second[1][i]:
                continue
            else:
                return alphabet.index(first[1][i]) - alphabet.index(second[1][i])

    return len(first[1]) - len(second[1])


answer = sorted(data, key=cmp_to_key(cmp))
for i in answer:
    print(i[0])

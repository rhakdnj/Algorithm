"""
숫자는 기본적으로 이진수로 합, 교집합 가능
bit 단위 0, 1을 or and 계산 |, &
"""


def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        # binary
        a12 = str(bin(i | j)[2:])
        a12 = a12.rjust(n, '0')
        a12 = a12.replace('1', '#')
        a12 = a12.replace('0', ' ')
        answer.append(a12)
    return answer

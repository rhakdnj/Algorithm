"""
n 진법, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p
"""


def solution(n, t, m, p):
    data = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    numbers = "0"
    # 인원 x 미리 구할 숫자의 갯수 보다는 적다.
    for number in range(1, t * m):
        temp = ''
        while number > 0:
            number, num = divmod(number, n)
            temp += data[num] + temp

    return numbers[p - 1:t * m:m]


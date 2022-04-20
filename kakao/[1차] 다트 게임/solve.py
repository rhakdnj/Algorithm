"""1S2D*3T	37	11 * 2 + 22 * 2 + 33
    1D2S#10S	9	12 + 21 * (-1) + 101
3	1D2S0T	3	12 + 21 + 03
4	1S*2T*3S	23	11 * 2 * 2 + 23 * 2 + 31
5	1D#2S*3S	5	12 * (-1) * 2 + 21 * 2 + 31
6	1T2D3D#	-4	13 + 22 + 32 * (-1)
7	1D2S3T*	59	12 + 21 * 2 + 33 * 2


1S2D 3T

1S 2D   + 3T

1D 2S # 10S

1S 2T 3S

1D # 2S * 3S

"""


def solution(dartResult: str):
    answer = 0
    score = []
    temp = ""
    for i in dartResult:
        if i == '*':
            if len(score) >= 2:
                score[-1] *= 2
                score[-2] *= 2
            else:
                score[-1] *= 2
            continue
        if i == '#':
            score[-1] *= -1
            continue

        if i.isdigit():
            temp += i
        else:
            if i == 'S':
                score.append(int(temp))
            elif i == 'D':
                score.append(int(temp) ** 2)
            elif i == 'T':
                score.append(int(temp) ** 3)
            temp = ""

    return sum(score)

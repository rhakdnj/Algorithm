from math import sqrt


def solution(brown, yellow):
    # 근의 방정식
    w = ((brown+4)/2 + sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    h = ((brown+4)/2 - sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    return [w, h]

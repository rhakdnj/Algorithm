"""
작은 순서대로 먼저 합치는 것이 전체 비교 횟수를 줄일 수 있다.
따라서, 현재 데이터 중 가장 작은 카드의 개수를 가진 묵음 2개를 뽑고
이 2개를 기준으로 합친 새로운 카드 묶음을 다시 데이터에 넣고 정렬해야 한다!!
"""

import sys
from heapq import heappush, heappop

input = lambda: sys.stdin.readline().rstrip()


def solution(n):
    answer = 0
    hq = []
    for i in range(n):
        heappush(hq, int(input()))

    while len(hq) != 1:
        a, b = heappop(hq), heappop(hq)
        answer += (a + b)
        hq.append(a + b)

    print(answer)


if __name__ == '__main__':
    N = int(input())
    solution(N)

import sys
from heapq import heappop, heappush

input = lambda: sys.stdin.readline().rstrip()


def solution(n):
    plus_lst = list()
    minus_lst = list()
    one_cnt, zero_cnt = 0, 0
    for _ in range(n):
        num = int(input())
        if num > 1:
            heappush(plus_lst, (-num, num))
        elif num == 1:
            one_cnt += 1
        elif num == 0:
            zero_cnt += 1
        else:
            heappush(minus_lst, num)

    answer = 0

    # 양수 처리
    while len(plus_lst) > 1:
        a, b = heappop(plus_lst)[1], heappop(plus_lst)[1]
        answer += a * b

    if plus_lst:
        answer += plus_lst.pop()[1]

    # 음수 처리
    while len(minus_lst) > 1:
        a, b = heappop(minus_lst), heappop(minus_lst)
        answer += a * b

    if minus_lst and zero_cnt == 0:
        answer += minus_lst.pop()

    # 1 처리하기
    answer += one_cnt

    print(answer)


if __name__ == '__main__':
    solution(int(input()))

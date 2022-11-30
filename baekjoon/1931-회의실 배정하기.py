"""
종료 시간이 같을 때는 시작 시간이 빠른 순으로 정렬하는 기준이 포함돼야 한다.
문제에서 시작 시간과 종료 시간이 같을 수도 있다고 했기 때문이다.
예를 들어 (2, 2), (1, 2) 2개의 회의가 있다고 하면
(2, 2)가 먼저 나오면 나중에 나온 (1, 2)가 불가능할 수 있다.
"""
import sys

input = lambda: sys.stdin.readline().rstrip()


def solution(n, lst):
    lst.sort(key=lambda x: (x[1], x[0]))

    answer, curr_end = 0, 0

    for start, end in lst:
        if curr_end <= start:
            answer += 1
            curr_end = end

    print(answer)


if __name__ == '__main__':
    N = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    solution(N, arr)

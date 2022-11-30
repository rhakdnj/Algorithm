"""
크기는 모두 같고 녹화 순서가 바뀌지 않아야 함
모두 저장할 수 있다면 크기를 줄이고 저장할 수 없다면 크기를 늘리는 방식으로 크기의 최솟값을 알 수 있다.
"""
import sys

input = lambda: sys.stdin.readline().rstrip()


def solution(n, m, lst):
    start, end = max(lst), sum(lst)

    while start <= end:
        mid = (start + end) // 2

        cnt, sum_ = 0, 0
        for lesson in arr:
            if sum_ + lesson > mid:
                sum_ = 0
                cnt += 1
            sum_ += lesson

        if sum_ != 0:
            cnt += 1

        if cnt > m:
            start = mid + 1
        else:
            end = mid - 1

    print(start)


if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    solution(N, M, arr)

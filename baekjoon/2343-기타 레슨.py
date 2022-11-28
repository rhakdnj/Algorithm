import sys

input = lambda: sys.stdin.readline().rstrip()


def solution():
    start, end = max(arr), sum(arr)

    while start <= end:
        mid = (start + end) // 2
        cnt, sum_ = 0, 0
        for i in range(N):
            if sum_ + arr[i] > mid:
                cnt += 1
                sum_ = 0
            sum_ += arr[i]
        if sum_ != 0:
            cnt += 1
        if cnt > M:
            start = mid + 1
        else:
            end = mid - 1

    print(start)


if __name__ == '__main__':
    N, M = map(int, input().split())  # 강의의 수 N, M
    arr = list(map(int, input().split()))
    solution()

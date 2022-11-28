import sys

input = lambda: sys.stdin.readline().rstrip()


def solution():
    n = int(input())  # 데이터 갯수
    datas = list(map(int, input().split()))
    find_cnt = int(input())
    find_numbers = list(map(int, input().split()))

    datas.sort()

    def binary_search(target):
        start, end = 0, len(datas) - 1
        while start <= end:
            mid = (start + end) // 2
            if datas[mid] == target:
                return 1
            elif datas[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return 0

    for number in find_numbers:
        print(binary_search(number))


if __name__ == '__main__':
    solution()

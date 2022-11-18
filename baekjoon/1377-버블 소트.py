import sys

input = lambda: sys.stdin.readline().rstrip()


def solution():
    lst = [(i, int(input())) for i in range(N)]
    lst.sort(key=lambda x: x[1])
    print(max([lst[i][0] - i for i in range(N)]) + 1)


if __name__ == '__main__':
    N = int(input())
    solution()

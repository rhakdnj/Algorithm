import sys


def input():
    return sys.stdin.readline().rstrip()


def solution():
    n = int(input())
    like_info_list = dict()
    for _ in range(n * n):
        data = list(map(int, input().split()))
        student, like_list = data[0], data[1:]
        like_info_list[student] = like_list
    # print(like_info_list)


solution()

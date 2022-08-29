"""
https://www.acmicpc.net/problem/2828
사과 담기 게임
"""
import sys

input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
j = int(input())
arr = [int(input()) for _ in range(j)]


def solution(a: list):
    global n, m, j
    ret = 0

    left = 1
    for i in a:
        right = left + m - 1
        if left <= i <= right:
            continue
        else:
            if i < left:
                ret += left - i
                left = i
            else:
                ret += i - right
                left += i - right
    print(ret)


solution(arr)

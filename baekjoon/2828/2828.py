"""
https://www.acmicpc.net/problem/2828
사과 담기 게임
그림을 그려서 풀기
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
    for temp in a:
        right = left + m - 1
        if left <= temp <= right:
            continue
        else:
            if temp < left:
                ret += left - temp
                left = temp
            else:
                ret += temp - right
                left += temp - right
    print(ret)


solution(arr)

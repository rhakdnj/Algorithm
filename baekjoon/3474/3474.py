"""
https://www.acmicpc.net/problem/3474
교수가 된 현우

2, 5의 갯수로 확인 가능하다.
"""
import sys

input = lambda: sys.stdin.readline().rstrip()
t = int(input())


def solution():
    global t
    for _ in range(t):
        n = int(input())
        cnt_2, cnt_5 = 0, 0
        i = 2
        while i <= n:
            cnt_2 += n // i
            i *= 2
        j = 5
        while j <= n:
            cnt_5 += n // j
            j *= 5

        print(min(cnt_2, cnt_5))


solution()

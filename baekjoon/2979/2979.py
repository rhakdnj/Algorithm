"""
https://www.acmicpc.net/problem/2979
트럭 주차
counting 배열을 통해 구할 수 있으며 시간은 항상 이상으로 시작하고 미만으로 끝난다.
"""
import sys

input = lambda: sys.stdin.readline().rstrip()

cnt = [0] * 101


def solution():
    a, b, c = map(int, input().split())
    times = [tuple(map(int, input().split())) for _ in range(3)]
    ret = 0

    for time in times:
        for i in range(time[0], time[1]):
            cnt[i] += 1
    for j in range(1, 100):
        if cnt[j]:
            if cnt[j] == 1:
                ret += a
            elif cnt[j] == 2:
                ret += b * 2
            elif cnt[j] == 3:
                ret += c * 3
    print(ret)


solution()

"""
https://www.acmicpc.net/problem/1159
농구 경기
"""
import sys

input = lambda: sys.stdin.readline().rstrip()


def solution():
    answer = ''
    n = int(input())
    cnt = [0] * 26
    for _ in range(n):
        s = input()
        cnt[ord(s[0]) - ord('a')] += 1

    for i in range(26):
        if cnt[i] >= 5:
            answer += chr(ord('a') + i)

    if answer:
        print(answer)
    else:
        print('PREDAJA')


solution()

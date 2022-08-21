"""
https://www.acmicpc.net/problem/1213
"""
import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def solution():
    s = input()
    cnt = [0] * 91
    for ch in s:
        cnt[ord(ch)] += 1

    flag = 0
    mid, ret = '', deque()
    for i in range(ord('Z'), ord('A') - 1, - 1):
        if cnt[i]:
            if cnt[i] & 1:
                mid = chr(i)
                flag += 1
                cnt[i] -= 1
            if flag == 2:
                break
            for j in range(0, cnt[i], 2):
                ret.appendleft(chr(i))
                ret.append(chr(i))

    if mid:
        ret.insert(len(ret) // 2, mid)
    if flag == 2:
        print("I'm Sorry Hansoo")
    else:
        print(''.join(ret))


solution()

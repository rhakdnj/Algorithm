import sys

input = lambda: sys.stdin.readline().rstrip()


def solution():
    s = input()
    cnt = [0] * 26
    for ch in s:
        cnt[ord(ch) - ord('a')] += 1

    for i in cnt:
        print(i, end=" ")


solution()

"""
https://www.acmicpc.net/problem/2870
수학숙제
"""
import sys

input = lambda: sys.stdin.readline().rstrip()
m = int(input())


def solution():
    global m
    arr = []
    for _ in range(m):
        s = input()
        temp = ''
        for i in range(len(s)):
            if s[i].isdigit():
                temp += s[i]
            else:
                if temp == '':
                    continue
                arr.append(int(temp))
                temp = ''
        if temp != '':
            arr.append(int(temp))

    for i in sorted(arr):
        print(i)


solution()

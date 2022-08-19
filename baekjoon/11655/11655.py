"""
https://www.acmicpc.net/problem/11655
ROT13
+13 ASCII
파이썬 문자열에서는 변경이 불가하기에 list로 변경하고 마지막 join으로 문자열 처리
"""
import sys

input = lambda: sys.stdin.readline().rstrip()


def solution():
    arr = list(input())
    for i in range(len(arr)):
        if ord('a') <= ord(arr[i]) <= ord('z'):
            if ord(arr[i]) + 13 > ord('z'):
                arr[i] = chr(ord(arr[i]) + 13 - 26)
            else:
                arr[i] = chr(ord(arr[i]) + 13)
        elif ord('A') <= ord(arr[i]) < ord('Z'):
            if ord(arr[i]) + 13 > ord('Z'):
                arr[i] = chr(ord(arr[i]) + 13 - 26)
            else:
                arr[i] = chr(ord(arr[i]) + 13)
    print(''.join(arr))


solution()

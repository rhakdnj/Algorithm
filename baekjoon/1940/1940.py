"""
https://www.acmicpc.net/problem/1940
주몽
"""
import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
m = int(input())
arr = list(map(int, input().split()))


def solution(n: int, m: int, arr: list):
    ret = 0
    arr.sort()
    if m > 200000:
        print(ret)
        return
    else:
        left, right = 0, len(arr) - 1
        while left < right:
            total = arr[left] + arr[right]
            if total < m:
                left += 1
            elif total > m:
                right -= 1
            else:
                ret += 1
                left += 1
                right -= 1
    print(ret)


solution(n, m, arr)

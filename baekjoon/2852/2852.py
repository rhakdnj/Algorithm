"""
https://www.acmicpc.net/problem/2852
NBA 농구
"""
import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
a, b, a_sum, b_sum = 0, 0, 0, 0
prev = ''


def change_to_sec(s):
    return int(s[0: 2]) * 60 + int(s[3: 5])


def change_to_time(t):
    m = '00' + str(t // 60)
    s = '00' + str(t % 60)
    return m[len(m) - 2: len(m)] + ":" + s[len(s) - 2: len(s)]


def solution():
    global n, a, b, a_sum, b_sum, prev

    for i in range(n):
        num, s = input().split()
        if a > b:
            a_sum += change_to_sec(s) - change_to_sec(prev)
        elif b > a:
            b_sum += change_to_sec(s) - change_to_sec(prev)

        if num == '1':
            a += 1
        else:
            b += 1
        prev = s
    if a > b:
        a_sum += change_to_sec('48:00') - change_to_sec(prev)
    elif b > a:
        b_sum += change_to_sec('48:00') - change_to_sec(prev)
    print(change_to_time(a_sum))
    print(change_to_time(b_sum))


solution()

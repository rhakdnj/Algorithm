"""
https://www.acmicpc.net/problem/2852
NBA 농구
"""
import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
team_1, team_2 = 0, 0
sum_1, sum_2 = 0, 0
prev = ''


def change_to_sec(s: str):
    m, sec = s.split(':')
    return int(m) * 60 + int(sec)


def change_to_time_format(t: int):
    m = '00' + str(t // 60)
    sec = '00' + str(t % 60)
    return m[len(m) - 2: len(m)] + ':' + sec[len(sec) - 2: len(sec)]


def solution():
    global n, team_1, team_2, sum_1, sum_2, prev
    for _ in range(n):
        team, s = input().split()
        if team_1 > team_2:
            sum_1 += change_to_sec(s) - change_to_sec(prev)
        elif team_2 > team_1:
            sum_2 += change_to_sec(s) - change_to_sec(prev)

        if team == '1':
            team_1 += 1
        elif team == '2':
            team_2 += 1
        prev = s

    if team_1 > team_2:
        sum_1 += change_to_sec('48:00') - change_to_sec(prev)
    elif team_2 > team_1:
        sum_2 += change_to_sec('48:00') - change_to_sec(prev)

    print(change_to_time_format(sum_1))
    print(change_to_time_format(sum_2))


solution()

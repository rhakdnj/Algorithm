"""
https://www.acmicpc.net/problem/4659
비밀번호 발음하기
"""
import sys

input = lambda: sys.stdin.readline().rstrip()


def solution():
    while True:
        s = input()
        if s == 'end':
            break

        v_cnt, c_cnt = 0, 0
        has_vowel = False
        flag = True
        prev = ''
        for i in range(len(s)):
            char = s[i]
            if char in 'aeiou':
                has_vowel = True
                v_cnt += 1
                c_cnt = 0
            else:
                v_cnt = 0
                c_cnt += 1

            if v_cnt == 3 or c_cnt == 3:
                flag = False
                break

            if i >= 1 and prev == char and prev not in 'eo':
                flag = False
                break
            prev = char

        if not has_vowel:
            flag = False

        if flag:
            print(f'<{s}> is acceptable.')
        else:
            print(f'<{s}> is not acceptable.')


solution()

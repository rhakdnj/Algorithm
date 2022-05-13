import sys
from itertools import combinations


def input():
    return sys.stdin.readline().rstrip()


L, C = map(int, input().split())
char_list = sorted(list(input().split()))
vowel = 'aeiou'
candidates = combinations(char_list, L)

for candidate in candidates:
    vow_cnt = 0
    for i in candidate:
        if i in vowel:
            vow_cnt += 1
    if vow_cnt >= 1 and L - vow_cnt >= 2:
        print(''.join(candidate))

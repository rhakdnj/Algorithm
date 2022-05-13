import sys


def input():
    return sys.stdin.readline().rstrip()


def is_pwd(arr):
    cnt_vow = 0
    for i in arr:
        if i in vowel:
            cnt_vow += 1
    if cnt_vow >= 1 and L - cnt_vow >= 2:
        print(''.join(arr))


L, C = map(int, input().split())
char_list = sorted(list(input().split()))
vowel = 'aeiou'


def make_pwd(v, arr):
    if len(arr) == L:
        is_pwd(arr)
        return
    if v == C:
        return
    arr.append(char_list[v])
    make_pwd(v + 1, arr)
    arr.pop()
    make_pwd(v + 1, arr)


make_pwd(0, [])

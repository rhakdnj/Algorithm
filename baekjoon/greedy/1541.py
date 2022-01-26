# https://www.acmicpc.net/problem/1541
import sys


def input():
    return sys.stdin.readline().rstrip()


s = list(input().split('-'))
res = 0














for i in s[0].split('+'):
    res += int(i)
for i in s[1:]:
    for j in i.split('+'):
        res -= int(j)


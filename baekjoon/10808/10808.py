"""
https://www.acmicpc.net/problem/10808
알파벳 개수
counting star -> map 또는 배열
dict: key가 string
arr: key가 integer (sparse 뜨문뜨문하게 하면 x), 배열 1000만정도 크기는 또한 x
ord('a') = 97, chr(97) = 'a'
"""
import sys

input = lambda: sys.stdin.readline().rstrip()


def solution():
    s = input()
    dic = dict()
    for i in range(ord('a'), ord('z') + 1):
        dic[i] = 0
    for i in s:
        dic[ord(i)] += 1

    for i in dic.values():
        print(i, end=" ")


solution()

"""
https://www.acmicpc.net/problem/
"""
import sys

input = lambda: sys.stdin.readline().rstrip()
arr = [[]]
MAX = int(1e9)


def combination(arr: range, n: int) -> list[list]:
    ret = []
    if n == 0:
        return [[]]
    if n == 1:
        return [[i] for i in arr]

    for i in range(len(arr)):
        elem = arr[i]
        combi = combination(arr[i + 1:], n - 1)
        for rest in combi:
            ret.append([elem] + rest)
    return ret


def solution(n):
    global arr
    mp, mf, ms, mv = map(int, input().split())
    ret = MAX
    answer = []

    for _ in range(n):
        arr.append(list(map(int, input().split())))

    for i in range(1, n + 1):
        for combi in combination(range(1, n + 1), i):
            p = sum([arr[k][0] for k in combi])
            f = sum([arr[k][1] for k in combi])
            s = sum([arr[k][2] for k in combi])
            v = sum([arr[k][3] for k in combi])
            cost = sum([arr[k][4] for k in combi])
            if p >= mp and f >= mf and s >= ms and v >= mv:
                if ret > cost:
                    ret = cost
                    answer = combi
                elif ret == cost:
                    answer = sorted([answer, combi])[0]

        if ret == MAX:
            print(-1)
            return

        print(ret)
        for i in answer:
            print(i, end=" ")


solution(int(input()))

"""
https://www.acmicpc.net/problem/1068
트리
"""
import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
adj = []
root, r = 0, 0


def dfs(here: int) -> int:
    global adj, r
    ret, child = 0, 0
    for there in adj[here]:
        if there == r:
            continue
        ret += dfs(there)
        child += 1
    if child == 0:
        return 1
    return ret


def solution():
    global n, adj, root, r
    adj = [[] for _ in range(n)]
    for i, v in enumerate(list(map(int, input().split()))):
        if v == -1:
            root = i
        else:
            adj[v].append(i)

    r = int(input())
    if r == 0:
        print(0)
    else:
        print(dfs(root))


solution()

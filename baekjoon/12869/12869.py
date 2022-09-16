"""
https://www.acmicpc.net/problem/12869
뮤탈리스크
"""
from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()
N = 0
arr, visited = [0, 0, 0], [[[0] * 64 for _ in range(64)] for _ in range(64)]
permu = [
    (9, 3, 1),
    (9, 1, 3),
    (3, 9, 1),
    (3, 1, 9),
    (1, 9, 3),
    (1, 3, 9)
]


def solution(n, li):
    global N, arr, permu, visited
    for i in range(len(li)):
        arr[i] = li[i]

    visited[arr[0]][arr[1]][arr[2]] = 1
    dq = deque([arr])
    while dq:
        a, b, c = dq.popleft()
        if visited[0][0][0]:
            break
        for i in range(6):
            na, nb, nc = max(0, a - permu[i][0]), max(0, b - permu[i][1]), max(0, c - permu[i][2])
            if visited[na][nb][nc]:
                continue
            visited[na][nb][nc] = visited[a][b][c] + 1
            dq.append([na, nb, nc])

    print(visited[0][0][0] - 1)


solution(int(input()), list(map(int, input().split())))

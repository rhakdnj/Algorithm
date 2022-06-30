import sys


def input():
    return sys.stdin.readline().rstrip()


def solution():
    n = int(input())
    target = int(input())

    def is_target(num: int) -> bool:
        if num == target:
            return True
        return False

    answer = [[0] * n for _ in range(n)]
    point = []
    v = n * n
    idx = 0
    while v != 0:
        for i in range(n):
            if answer[i][idx] == 0:
                answer[i][idx] = v
                if is_target(v):
                    point = [i, idx]
                v -= 1
        for i in range(n):
            if answer[n - idx - 1][i] == 0:
                answer[n - idx - 1][i] = v
                if is_target(v):
                    point = [n - idx - 1, i]
                v -= 1
        for i in range(n):
            if answer[n - 1 - i][n - 1 - idx] == 0:
                answer[n - 1 - i][n - 1 - idx] = v
                if is_target(v):
                    point = [n - 1 - i, n - 1 - idx]
                v -= 1
        for i in range(n):
            if answer[idx][n - 1 - i] == 0:
                answer[idx][n - 1 - i] = v
                if is_target(v):
                    point = [idx, n - 1 - i]
                v -= 1
        idx += 1

    for i in range(n):
        for j in range(n):
            print(answer[i][j], end=' ')
        print()
    print(point[0] + 1, point[1] + 1)


solution()

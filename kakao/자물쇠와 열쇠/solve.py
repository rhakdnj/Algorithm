"""
자물쇠를 고정 시키고 열쇠를 자물쇠의 크기만큼 순회를 해서 맞는지 확인하는 것
따라서 offset을 생각하고 4가지 회전을 다 찾아보는 방법
"""

def match(arr, key, rot, r, c):
    n = len(key)
    for i in range(n):
        for j in range(n):
            if rot == 0:
                arr[r + i][c + j] += key[i][j]
            elif rot == 1:
                arr[r + i][c + j] += key[n - 1 - j][i]
            elif rot == 2:
                arr[r + i][c + j] += key[n - 1 - i][n - 1 - j]
            else:
                arr[r + i][c + j] += key[j][n - 1 - i]


def check(arr, offset, n):
    for i in range(n):
        for j in range(n):
            if arr[offset + i][offset + j] != 1:
                return False
    return True


def solution(key, lock):
    offset = len(key) - 1

    for r in range(offset + len(lock)):
        for c in range(offset + len(lock)):
            for rot in range(4):
                arr = [[0 for _ in range(58)] for _ in range(58)]
                for i in range(len(lock)):
                    for j in range(len(lock)):
                        arr[offset + i][offset + j] = lock[i][j]

                match(arr, key, rot, r, c)
                if check(arr, offset, len(lock)):
                    return True
    return False

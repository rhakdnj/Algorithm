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
    m = len(key)
    offset = m - 1
    n = len(lock)

    for r in range(offset + n):
        for c in range(offset + n):
            for rot in range(4):
                arr = [[0 for _ in range(58)] for _ in range(58)]
                for i in range(n):
                    for j in range(n):
                        arr[offset + i][offset + j] = lock[i][j]

                match(arr, key, rot, r, c)
                if check(arr, offset, n):
                    return True
    return False

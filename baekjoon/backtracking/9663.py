import sys


def input():
    return sys.stdin.readline().rstrip()


def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True


def n_queen(x):
    global answer
    if x == n:
        answer += 1
        return
    for i in range(n):
        if visited[i]:
            continue
        row[x] = i
        if is_promising(x):
            visited[i] = True
            n_queen(x + 1)
            visited[i] = False


n = int(input())
answer = 0
row = [0] * n
visited = [False] * n

n_queen(0)
print(answer)

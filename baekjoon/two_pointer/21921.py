import sys


def input():
    return sys.stdin.readline().rstrip()


N, X = map(int, input().split())
visit = list(map(int, input().split()))

if max(visit) == 0:
    print("SAD")
else:
    max_visit = sum(visit[0:X])
    value, count = max_visit, 1

    for i in range(X, N):
        value -= visit[i - X]
        value += visit[i]
        if value > max_visit:
            max_visit = value
            count = 1
        elif value == max_visit:
            count += 1
    print(max_visit, count, sep="\n")

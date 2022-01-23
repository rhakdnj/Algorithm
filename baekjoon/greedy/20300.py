import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
loss = list(map(int, input().split()))
loss.sort()
res = 0


if N % 2:
    for i in range(len(loss) // 2):
        res = max(res, loss[i] + loss[N - i - 2])
    res = max(res, loss[-1])
else:
    for i in range(len(loss) // 2):
        res = max(res, loss[i] + loss[N - i - 1])

print(res)


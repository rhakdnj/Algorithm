from collections import deque

n, l = map(int, input().split())
arr = list(map(int, input().split()))
answer = []


def solution():
    dq = deque()
    for i, curr in enumerate(arr):
        while dq and dq[-1][1] > curr:
            dq.pop()

        dq.append((i, curr))
        if dq[0][0] <= i - l:
            dq.popleft()

        answer.append(dq[0][1])

    print(f"{' '.join(map(str, answer))}")


solution()

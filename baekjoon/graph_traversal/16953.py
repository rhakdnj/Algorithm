from collections import deque

A, B = map(int, input().split())


def bfs(a, b):
    q = deque([(a, 1)])
    while q:
        a, cnt = q.popleft()
        if a > b:
            continue
        if a == b:
            return cnt
        q.append((2 * a, cnt + 1))
        q.append((int((str(a) + '1')), cnt + 1))
    return -1


print(bfs(A, B))

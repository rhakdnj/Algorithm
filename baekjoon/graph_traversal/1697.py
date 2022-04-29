from collections import deque

MAX = 100000
n, k = map(int, input().split())
queue = deque()
queue.append((n, 0))

while queue:
    x, cnt = queue.popleft()
    if x == k:
        print(cnt)
        break
    for i in (x - 1, x + 1, x * 2):
        if 0 <= i <= MAX:
            queue.append((i, cnt + 1))

from collections import deque

n, k = map(int, input().split())
MAX = int(5e5)
visited = [[0 for _ in range(MAX + 1)] for _ in range(2)]


def bfs():
    global n, MAX, visited
    dq = deque([(n, 0)])

    visited[0][n] = 1
    while len(dq):
        now, cnt = dq.popleft()
        flag = cnt % 2

        for next_ in (now - 1, now + 1, now * 2):
            if 0 <= next_ <= MAX and not visited[1 - flag][next_]:
                visited[1 - flag][next_] = cnt + 1
                dq.append((next_, cnt + 1))


def solution():
    global n, k, MAX, visited

    if n == k:
        print(0)

    bfs()

    t = 0
    flag = 0
    ret = -1
    while k <= MAX:
        if visited[flag][k]:
            if visited[flag][k] <= t:
                ret = t
                break
        flag = 1 - flag
        t += 1
        k += t

    print(ret)


solution()

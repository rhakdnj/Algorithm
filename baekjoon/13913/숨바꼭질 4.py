from collections import deque

n, k = map(int, input().split())
MAX = 100001
ret = 0
visited = [0] * MAX
prev = [0] * MAX


def solution():
    global n, k, MAX, visited, ret

    visited[n] = 1
    dq = deque([n])
    while dq:
        now = dq.popleft()
        if now == k:
            ret = visited[k]
            break

        for next_ in now + 1, now - 1, now * 2:
            if 0 <= next_ < MAX:
                if not visited[next_]:
                    visited[next_] = visited[now] + 1
                    dq.append(next_)
                    prev[next_] = now

    i = k
    move = [k]
    while i != n:
        move.append(prev[i])
        i = prev[i]

    print(ret - 1)
    for i in reversed(move):
        print(i, end=" ")


solution()

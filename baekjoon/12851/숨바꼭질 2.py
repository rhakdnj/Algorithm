from collections import deque

n, k = map(int, input().split())
MAX = 100000
visited = [0] * (MAX + 4)
cnt = [0] * (MAX + 4)


def solution():
    global visited, cnt

    if n == k:
        print(0, 1, sep="\n")
        return

    visited[n] = 1
    cnt[n] = 1
    dq = deque([n])
    while dq:
        now = dq.popleft()
        for next_ in (now + 1, now - 1, 2 * now):
            if 0 <= next_ <= MAX:
                if not visited[next_]:
                    dq.append(next_)
                    visited[next_] = visited[now] + 1
                    cnt[next_] += cnt[now]
                elif visited[next_] == visited[now] + 1:
                    cnt[next_] += cnt[now]

    print(visited[k] - 1, cnt[k], sep="\n")


solution()

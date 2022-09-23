from collections import deque

MAX_N = int(5e5)


def solution():
    n, k = map(int, input().split())
    visited = [[0 for _ in range(MAX_N + 1)] for _ in range(2)]
    turn, flag = 1, 0

    if n == k:
        print(0)
        return

    dq = deque()
    visited[0][n] = 1
    dq.append(n)
    while len(dq):
        k += turn

        if k > MAX_N:
            break
        if visited[turn % 2][k]:
            flag = 1
            break

        for i in range(len(dq)):
            now = dq.popleft()
            for nxt in (now + 1, now - 1, now * 2):
                if nxt < 0 or nxt > MAX_N or visited[turn % 2][nxt]:
                    continue
                visited[turn % 2][nxt] = visited[(turn + 1) % 2][now] + 1

                if nxt == k:
                    flag = 1
                    break

                dq.append(nxt)

            if flag:
                break
        if flag:
            break
        turn += 1

    if flag:
        print(turn)
    else:
        print(-1)
    return


solution()

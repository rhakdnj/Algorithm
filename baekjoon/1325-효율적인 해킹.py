import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def solution(n, m, lst):
    graph = [[] for _ in range(n + 1)]
    cnt = [0 for _ in range(n + 1)]

    for a, b in lst:
        graph[a].append(b)

    def bfs(start):
        visited = [False for _ in range(n + 1)]
        dq = deque()
        dq.append(start)
        visited[start] = True

        while dq:
            curr = dq.popleft()

            for next_ in graph[curr]:
                if not visited[next_]:
                    dq.append(next_)
                    visited[next_] = True
                    cnt[next_] += 1

    for i in range(1, n + 1):
        bfs(i)

    max_ = max(cnt)

    for i in range(1, n + 1):
        if cnt[i] == max_:
            print(i, end=" ")


if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    solution(N, M, arr)

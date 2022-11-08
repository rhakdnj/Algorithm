n = int(input())
INF = int(1e9)
dp = [[INF for _ in range(1 << n)] for _ in range(n)]
grid = [list(map(int, input().split())) for _ in range(n)]


def dfs(here, visited):
    # 모든 도시를 방문했다면
    if visited == (1 << n) - 1:
        # 출발점으로 가는 경로의 존재 여부
        return grid[here][0] if grid[here][0] else INF

    # 이미 최소비용이 계산되어 있다면
    if dp[here][visited] != INF:
        return dp[here][visited]

    # 모든 도시를 탐방
    for i in range(1, n):
        # 가는 경로가 없는 경우
        if not grid[here][i]:
            continue
        if visited & (1 << i):
            continue

        dp[here][visited] = min(dp[here][visited], dfs(i, visited | (1 << i)) + grid[here][i])

    return dp[here][visited]


print(dfs(0, 1))


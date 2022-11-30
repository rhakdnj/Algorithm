import sys

input = lambda: sys.stdin.readline().rstrip()


def solution(n, k, coins):
    cnt = 0
    # for coin in coins[ : :-1]
    for i in range(n - 1, -1, -1):
        if coins[i] <= k:
            cnt += k // coins[i]
            k = k % coins[i]
    print(cnt)


if __name__ == '__main__':
    N, K = map(int, input().split())
    arr = [int(input()) for _ in range(N)]
    solution(N, K, arr)

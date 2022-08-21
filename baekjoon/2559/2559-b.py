import sys

input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
arr = list(map(int, input().split()))


def solution():
    global n, k, arr
    total = sum(arr[:k])
    psum = [total]
    for i in range(1, len(arr) - k + 1):
        total = total - arr[i - 1] + arr[i + k - 1]
        psum.append(total)

    print(max(psum))


solution()

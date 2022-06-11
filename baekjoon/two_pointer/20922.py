import sys


def input():
    return sys.stdin.readline().rstrip()


n, k = map(int, input().split())
arr = list(map(int, input().split()))
counter = [0] * (max(arr) + 1)
left, right = 0, 0
answer = 0
while right < n:
    if counter[arr[right]] < k:
        counter[arr[right]] += 1
        right += 1
    else:
        counter[arr[left]] -= 1
        left += 1

    answer = max(answer, right - left)
print(answer)

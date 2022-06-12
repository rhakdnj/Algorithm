import sys


def input():
    return sys.stdin.readline().rstrip()


n, k = map(int, input().split())
arr = list(map(int, input().split()))
left, right = 0, k
answer = sum(arr[:k])
temp = answer

while right < n:
    temp += arr[right] - arr[left]
    if temp > answer:
        answer = temp
    left += 1
    right += 1

print(answer)

import sys


def input():
    return sys.stdin.readline().rstrip()


n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
answer = []

pointer_a, pointer_b = 0, 0
len_a, len_b = len(A), len(B)

while pointer_a != len_a or pointer_b != len_b:
    if pointer_a == len_a:
        answer.append(B[pointer_b])
        pointer_b += 1
    elif pointer_b == len_b:
        answer.append(A[pointer_a])
        pointer_a += 1
    else:
        if A[pointer_a] < B[pointer_b]:
            answer.append(A[pointer_a])
            pointer_a += 1
        else:
            answer.append(B[pointer_b])
            pointer_b += 1

print(*answer)

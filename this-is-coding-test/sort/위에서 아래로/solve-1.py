import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)

for i in array:
    print(i, end=" ")

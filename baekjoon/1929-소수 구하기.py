import sys

input = lambda: sys.stdin.readline().rstrip()


def solution(num1, num2):
    global n, m
    n, m = num1, num2

    for i in range(n, m + 1):
        # for 문에서 break 안되기에 1이 출력된다.
        if i == 1:
            continue

        for j in range(2, int(i ** (1 / 2) + 1)):
            if i % j == 0:
                break
        else:
            print(i)


if __name__ == '__main__':
    n, m = 0, 0
    solution(*map(int, input().split()))

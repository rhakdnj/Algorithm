import sys

input = lambda: sys.stdin.readline().rstrip()


def solution():
    answer = [0 for _ in range(n)]
    stk = [0]
    for i in range(1, n):
        num = lst[i]
        while stk and lst[stk[-1]] < num:
            answer[stk.pop()] = num
        stk.append(i)

    while stk:
        answer[stk.pop()] = -1

    for num in answer:
        print(num, end=" ")


if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))
    solution()

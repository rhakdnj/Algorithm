import sys

input = lambda: sys.stdin.readline().rstrip()
n, ret = 0, -int(1e9)
nums = []
ops = []  # 연산자


def oper(a: str, b: int, c: int) -> int:
    if a == '+':
        return b + c
    if a == '-':
        return b - c
    if a == '*':
        return b * c


def go(here, num):
    global nums, ops, ret
    if here == len(nums) - 1:
        ret = max(ret, num)
        return

    go(here + 1, oper(ops[here], num, nums[here + 1]))

    if here + 2 <= len(nums) - 1:
        temp = oper(ops[here + 1], nums[here + 1], nums[here + 2])
        go(here + 2, oper(ops[here], num, temp))


def solution(num, expression: str):
    global n, nums, ops, ret
    n = num
    for i in range(n):
        if i % 2 == 0:
            nums.append(int(expression[i]))
        else:
            ops.append(expression[i])

    go(0, nums[0])
    print(ret)


solution(int(input()), input())

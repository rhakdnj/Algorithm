n = int(input())
s = input()
nums, ops = [], []  # 숫자, 연산자
ret = -int(1e9)


def oper(op: str, a: int, b: int) -> int:
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b


def go(here: int, value: int):
    global ret
    if here == len(nums) - 1:
        ret = max(ret, value)
        return

    go(here + 1, oper(ops[here], value, nums[here + 1]))

    if here + 2 <= len(nums) - 1:
        temp = oper(ops[here + 1], nums[here + 1], nums[here + 2])
        go(here + 2, oper(ops[here], value, temp))


def solution():
    global n, ops, nums, ret
    for i in range(n):
        if i % 2:
            ops.append(s[i])
        else:
            nums.append(int(s[i]))

    go(0, nums[0])
    print(ret)


solution()

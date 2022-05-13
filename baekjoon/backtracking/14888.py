import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
num_list = list(map(int, input().split()))
operator = list(map(int, input().split()))  # +, -, *, //

maximum = -int(1e9)
minimum = int(1e9)


def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == n:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth + 1, total + num_list[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num_list[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num_list[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num_list[depth]), plus, minus, multiply, divide - 1)


dfs(1, num_list[0], operator[0], operator[1], operator[2], operator[3])
print(maximum)
print(minimum)

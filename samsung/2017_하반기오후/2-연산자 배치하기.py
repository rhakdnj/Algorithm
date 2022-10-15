"""
n개의 정수가 순서대로 주어질 때, n−1개의 연산자를 정수 사이에 하나씩 배치하고자 합니다.
이 때 주어진 정수의 순서를 바꿀 수 없으며, 연산자는 덧셈, 뺄셈, 곰셈 이렇게 세 가지 종류가 있습니다.
연산자 간의 우선 순위를 무시하고 앞에서부터 차례대로 연산한다고 하였을 때,
가능한 식의 최솟값과 최댓값을 출력하는 코드를 작성해보세요.
"""
n = int(input())
nums = list(map(int, input().split()))

# 덧셈, 뺄셈, 곱셈의 개수
ops = list(map(int, input().split()))

min_, max_ = int(1e9), -int(1e9)


# op: 0 -> + 1-> - 2 -> *
def calculate(num1, num2, op: int):
    if op == 0:
        return num1 + num2
    if op == 1:
        return num1 - num2
    if op == 2:
        return num1 * num2


def solution(curr_idx, curr_val):
    global min_, max_
    if curr_idx == n:
        if min_ > curr_val:
            min_ = curr_val
        if max_ < curr_val:
            max_ = curr_val
        return

    if curr_idx == 0:
        solution(curr_idx + 1, nums[curr_idx])
    else:
        for i in range(3):
            if ops[i] != 0:
                ops[i] -= 1
                solution(curr_idx + 1, calculate(curr_val, nums[curr_idx], i))
                ops[i] += 1


solution(0, 0)
print(f"{min_} {max_}")

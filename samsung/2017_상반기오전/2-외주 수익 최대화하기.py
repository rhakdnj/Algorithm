n = int(input())

time_profits = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

# 인덱스: 작업의 시작 시간, 종료 시간
times = [
    (i, i + time - 1)
    for i, (time, _) in enumerate(time_profits, start=1)
]

profits = [
    profit
    for _, profit in time_profits
]

selected_jobs = []
max_profit = 0


# 선택 외주 작업에 대한 수익을 반환
def get_profit():
    return sum([
        profits[job_idx]
        for job_idx in selected_jobs
    ])


# 수행하고자 하는 외주 작업들이 수행 가능한지 여부를 확인합니다.
def is_available():
    # 이전 외주의 종료일이 그 다음 외주의 시작 보다 늦은 경우 이는 불가능한 경우이다.
    for i in range(len(selected_jobs) - 1):
        _, end_time = times[selected_jobs[i]]
        start_time, _ = times[selected_jobs[i + 1]]
        if end_time >= start_time:
            return False

    # 각 외주의 종료일이 휴가 기간을 초과하는 경우 이는 불가능한 경우이다.
    for job_idx in selected_jobs:
        _, end_time = times[job_idx]
        if end_time > n:
            return False

    return True


def find_max_profit(curr_idx):
    global max_profit

    # 모든 외주 작업에 대해 다 탐색한 경우 스케줄링이 가능한지를 확인한 뒤
    # 가능한 최대 수익을 갱신합니다.
    if curr_idx == n:
        if is_available():
            max_profit = max(max_profit, get_profit())
        return

    # 해당 인덱스의 외주 작업을 수행하지 않았을 때의 경우를 탐색합니다.
    find_max_profit(curr_idx + 1)

    # 해당 인덱스의 외주 작업을 수행했을 때의 경우를 탐색합니다.
    selected_jobs.append(curr_idx)
    find_max_profit(curr_idx + 1)
    selected_jobs.pop()


find_max_profit(0)
print(max_profit)

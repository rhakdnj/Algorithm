def get_throughput(time, start_end_times):
    throughput = 0
    start_time = time
    end_time = start_time + 1000

    for start_end_time in start_end_times:
        if start_end_time[1] >= start_time and start_end_time[0] < end_time:
            throughput += 1

    return throughput


def solution(lines):
    answer = 0
    start_end_times = []
    for line in lines:
        _, time, duration = line.split()
        time_arr = time.split(':')
        # ms로 형변환
        duration = float(duration[:-1]) * 1000
        end_time = (int(time_arr[0]) * 3600 + int(time_arr[1]) * 60 + float(time_arr[2])) * 1000
        start_time = end_time - duration + 1
        start_end_times.append([start_time, end_time])

    for start_end_time in start_end_times:
        temp1 = get_throughput(start_end_time[0], start_end_times)
        temp2 = get_throughput(start_end_time[1], start_end_times)
        answer = max(answer, temp1, temp2)
    return answer

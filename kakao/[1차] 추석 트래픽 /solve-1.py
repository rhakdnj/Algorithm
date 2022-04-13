def solution(lines):
    # get input
    start_times, end_times = [], []
    total_lines = 0
    for line in lines:
        total_lines += 1
        type(line)
        (d, s, t) = line.split('')

        # time to float and sec
        t = float(t[0:-1])
        (hh, mm, ss) = s.split(':')
        seconds = float(hh) * 3600 + float(mm) * 60 + float(ss)

        end_times.append(seconds + 1)
        start_times.append(seconds - t + 0.001)

    # count the maxTraffic
    start_times.sort()

    cur_traffic = 0
    max_traffic = 0
    count_end = 0
    count_start = 0
    while (count_end < total_lines) & (count_start < total_lines):
        if start_times[count_start] < end_times[count_end]:
            cur_traffic += 1
            max_traffic = max(max_traffic, cur_traffic)
            count_start += 1
        else:  # it means that a line is over.
            cur_traffic -= 1
            count_end += 1

    return max_traffic

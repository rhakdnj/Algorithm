if __name__ == '__main__':
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort(key=lambda x: (x[1], x[0]))

    ans = 0

    start_time, end_time = 0, 0

    for start, end in arr:
        if end_time <= start:
            ans += 1
            start_time, end_time = start, end

    print(ans)

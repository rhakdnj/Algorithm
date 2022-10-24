if __name__ == '__main__':
    ans = 0
    n = int(input())
    li = list()

    for _ in range(n):
        arrival, during = map(int, input().split())
        li.append((arrival, during))

    li.sort(key=lambda x: (x[0], x[1]))

    ans = li[0][0] + li[0][1]
    for i in range(1, len(li)):
        start_time = li[i][0]
        during_time = li[i][1]
        ans = max(ans, start_time)
        ans += during_time

    print(ans)

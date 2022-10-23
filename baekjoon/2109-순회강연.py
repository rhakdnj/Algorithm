from heapq import heappush, heappop

if __name__ == '__main__':
    ans = 0
    d = [False for _ in range(10001)]
    n = int(input())

    li = list()
    for _ in range(n):
        price, day = map(int, input().split())
        li.append((day, price))

    li.sort()

    hq = list()
    for i in range(n):
        heappush(hq, li[i][1])
        if len(hq) > li[i][0]:
            heappop(hq)

    while hq:
        ans += heappop(hq)

    print(ans)

from heapq import heappush, heappop

if __name__ == '__main__':
    ans = 0
    n, k = map(int, input().split())

    jew = []
    for _ in range(n):
        heappush(jew, tuple(map(int, input().split())))

    bags = [int(input()) for _ in range(k)]

    bags.sort()

    tmp = []
    for bag in bags:
        while jew and bag >= jew[0][0]:
            heappush(tmp, -heappop(jew)[1])
        if tmp:
            ans -= heappop(tmp)

    print(ans)
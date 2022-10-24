from heapq import heappush, heappop

if __name__ == '__main__':
    ans = 0
    n = int(input())
    li = [(0, 0)]
    for _ in range(n):
        li.append(tuple(map(int, input().split())))

    li.sort()

    hq = list()
    for i in range(1, n + 1):
        heappush(hq, li[i][1])
        if len(hq) > li[i][0]:
            heappop(hq)

    print(sum(hq))
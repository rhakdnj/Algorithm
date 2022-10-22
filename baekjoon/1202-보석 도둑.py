from heapq import heappop, heappush

if __name__ == '__main__':
    n, k = map(int, input().split())
    jew_hq = []

    # (m, v) heappop을 진행하면 m이 작은 순서대로 나온다.
    for _ in range(n):
        heappush(jew_hq, list(map(int, input().split())))

    bags = [int(input()) for _ in range(k)]
    #
    bags.sort()

    ans = 0
    tmp = []
    for bag in bags:
        while jew_hq and bag >= jew_hq[0][0]:
            # tmp 에는 bag이 허용 가능한 무게중 가치를 넣는다.
            # 최대 힙을 위해 -heeappop(jew_hq)[1]
            heappush(tmp, -heappop(jew_hq)[1])
        if tmp:
            # -로 -의 값을 보상
            ans -= heappop(tmp)
        elif not jew_hq:
            break

    print(ans)

from heapq import heappush, heappop

if __name__ == '__main__':
    n = int(input())

    scores = []
    for _ in range(n):
        curr_score = float(input())
        if len(scores) == 7:
            heappush(scores, -curr_score)
            heappop(scores)
        else:
            heappush(scores, -curr_score)

    ans = []
    while scores:
        ans.append(heappop(scores))

    while ans:
        print('{0:.3f}'.format(-ans.pop()))


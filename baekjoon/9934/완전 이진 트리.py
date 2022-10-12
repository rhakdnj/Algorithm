k = int(input())
a = list(map(int, input().split(' ')))
ret = [[] for _ in range(11)]


def go(s: int, e: int, level: int):
    if s > e:
        return
    if s == e:
        ret[level].append(a[s])
        return
    mid = (s + e) // 2
    ret[level].append(a[mid])
    go(s, mid - 1, level + 1)
    go(mid + 1, e, level + 1)


def solution():
    end = 2 ** k - 1
    go(0, end - 1, 1)

    for j in ret:
        if not j:
            continue
        else:
            for i in j:
                print(i, end=" ")
        print()


solution()

def go(start, end, depth):
    if start > end:
        return
    if start == end:
        answer[depth].append(buildings[start])
        return

    mid = (start + end) // 2
    answer[depth].append(buildings[mid])
    go(start, mid - 1, depth + 1)
    go(mid + 1, end, depth + 1)


def solution():
    start = 0
    end = 2 ** k - 1 - 1
    depth = 1
    go(start, end, depth)

    for li in answer:
        if not li:
            continue
        for element in li:
            print(element, end=" ")
        print()


if __name__ == '__main__':
    k = int(input())
    buildings = list(map(int, input().split()))
    answer = [[] for _ in range(11)]

    solution()

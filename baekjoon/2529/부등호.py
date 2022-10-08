k = int(input())
a = list(input().split())
visited = [0 for _ in range(10)]
ret = []


def good(a: str, b: str, c: str):
    if a < b and c == '<':
        return True
    if a > b and c == '>':
        return True
    return False


def go(idx: int, num: str):
    if idx == k + 1:
        ret.append(num)
        return

    for i in range(10):
        if visited[i]:
            continue
        if idx == 0 or good(num[idx - 1], str(i), a[idx - 1]):
            visited[i] = 1
            go(idx + 1, num + str(i))
            visited[i] = 0
    return


def solution():
    go(0, "")
    ret.sort()
    print(ret[-1], ret[0], sep="\n")


solution()

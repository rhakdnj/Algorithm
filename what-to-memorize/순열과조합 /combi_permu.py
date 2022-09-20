def combination(arr: list, n: int) -> list[list]:
    ret = []
    if n == 0:
        return [[]]
    if n == 1:
        return [[i] for i in arr]

    for i in range(len(arr)):
        elem = arr[i]
        c = combination(arr[i + 1:], n - 1)
        for rest in c:
            ret.append([elem] + rest)
    return ret


def permutation(arr: list, n: int) -> list[list]:
    ret = []
    if n == 0:
        return [[]]
    if n == 1:
        return [[i] for i in arr]

    for i in range(len(arr)):
        elem = arr[i]
        p = permutation(arr[:i] + arr[i + 1:], n - 1)
        for rest in p:
            ret.append([elem] + rest)
    return ret


data = [1, 2, 3, 4]
print(permutation(data, 2))
print(combination(data, 2))

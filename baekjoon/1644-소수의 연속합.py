if __name__ == '__main__':
    ans = 0
    n = int(input())

    nums = [True for _ in range(n + 1)]
    primes = []
    for i in range(2, n + 1):
        if nums[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                nums[j] = False

    start, end = 0, 1
    while end <= len(primes):
        total = sum(primes[start: end])
        if total < n:
            end += 1
        elif total > n:
            start += 1
        else:
            ans += 1
            start += 1

    print(ans)

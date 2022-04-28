def check(a: str, left, right):
    while left < right:
        if a[left] != a[right]:
            return False
        left += 1
        right -= 1
    return True


s = input()
n = len(s)

if not check(s, 0, n - 1):
    print(n)
elif not check(s, 0, n - 2):
    print(n - 1)
else:
    print(-1)


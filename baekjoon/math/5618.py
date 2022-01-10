#
#
import sys

def input():
    return sys.stdin.readline().rstrip()

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

n = int(input())
arr = list(map(int, input().split()))
res = []
cd = arr[0]

for i in range(n):
    cd = gcd(cd, arr[i])

x = 1
while x * x <= gcd:
    if gcd % x == 0:
        res.append(x)
        if x * x != gcd:
            res.append(gcd // x)
    x += 1

res.sort()
print(*res)


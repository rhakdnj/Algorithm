import sys
input = sys.stdin.readline

case = 1

while 1:
    # 데이터 입력
    n = int(input().rstrip())
    if n == 0:
        break
    names = [input().rstrip() for _ in range(n)]
    values = [0] * n

    for _ in range(2 * n - 1):
        i = int(input().split()[0])
        values[i - 1] += 1

    result = names[[i for i in range(n) if values[i] != 2][0]]
    print(f"{case} {result}")
    case += 1




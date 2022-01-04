import sys
input = sys.stdin.readline

N = int(input())

numbers = [int(input()) for _ in range(N)]
dasom = numbers[0]
numbers = numbers[1:]

if N == 1:
    print(0)
else:
    num = 0
    numbers.sort(reverse=True)

    while numbers[0] >= dasom:
        dasom += 1
        numbers[0] -= 1
        num += 1
        numbers.sort(reverse=True)
        
    print(num)


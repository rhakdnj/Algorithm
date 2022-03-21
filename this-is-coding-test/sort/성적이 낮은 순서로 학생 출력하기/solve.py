n = int(input())
# array = [input() for _ in range(n)] -> '홍길동 95' '이순신 77' 따라서 input().split()
array = [input().split() for _ in range(n)]

array.sort(key=lambda x: int(x[1]))

for i in array:
    print(i[0], end=" ")

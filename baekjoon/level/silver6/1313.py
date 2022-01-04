# runtime error
# import sys
# input = sys.stdin.readline

# a, b, n = map(int, input().split())
# str = str(a/b).split('.')[1]

# print(str[n-1])
# print(str(a/b).split('.')[1:][n])

# real 수학적인 방법으로 접근함
# TOdo 
import sys
input = sys.stdin.readline
A, B, N = map(int, input().split())
A %= B
for i in range(N-1):
    A = (A * 10) % B
    
print((A * 10) // B)
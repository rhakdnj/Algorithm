# import sys
# input = sys.stdin.readlin을 할 때는 
# split()으로 나누지 않으면, \n 이 마지막에 붙음
# 만약 import sys를 하지 않으면 \n 개행문자가 붙지 않음
# a =  list (input())

# print(a)

import sys
input = sys.stdin.readline

# 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 
A, B = map(int, input().split())

res = [0]

for i in range(1, (B+1) // 2 + 1):
    for j in range(i):
        res.append(i)
        
for i in range(1, B+1):
    res[i] += res[i-1]
print(res[B] - res[A-1])

# 다른 사람의 코드
a,b = map(int,input().split())

arr = [0]
for i in range(46):
    for j in range(i):
        arr.append(i)

print(sum(arr[a:b+1]))
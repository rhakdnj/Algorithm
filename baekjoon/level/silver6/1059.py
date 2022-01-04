import sys
input = sys.stdin.readline


# input값 
L = int(input())
num_list = list(map(int, input().split()))
n = int(input())

if n in num_list:
    print(0)
    sys.exit()

result = 0

num_list += [0]
num_list.sort()

for idx in range(L):
    section_f = num_list[idx]
    section_l = num_list[idx+1]
    if n in range(section_f, section_l):
        break

section_f += 1
section_l -= 1

result = (section_l - section_f) + (n - section_f) * (section_l - n)
print(result)



'''
8
3 7 12 18 25 100 33 1000
59
'''

# while True:
#     if arr[idx-1] + 1 <= n:
#         ans += arr[idx] - arr[idx-1] - 2
#         arr[idx-1] += 1
#     else :
#         print(ans)
#         break

# def solution():
#     L = int(input())
#     arr = sorted(list(map(int, input().split())))
#     n = int(input())

#     prev = 0

#     for num in arr:
#         if num == n:
#             return 0

#         if num > n:
#             min_val = prev + 1
#             max_val = num - 1
#             break
#         prev = num  

#     return (n - min_val) * (max_val - n + 1) + (max_val - n)
# solution()    
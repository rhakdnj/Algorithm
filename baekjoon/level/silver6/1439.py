import sys
input = sys.stdin.readline

str = input().rstrip()

res_0, res_1 = 0, 0

if str[0] == '1':
    for i in range(len(str) - 1):
        if str[i] != str[i + 1]:
            if str[i+1] == '0':
                res_0 += 1
    print(res_0)
else:
    for i in range(len(str) - 1):
        if str[i] != str[i + 1]:
            if str[i+1] == '1':
                res_1 += 1
    print(res_1)    



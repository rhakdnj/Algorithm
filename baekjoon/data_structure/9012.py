# https://www.acmicpc.net/problem/9012
# for else :

import sys

def input():
    return sys.stdin.readline().rstrip()

T = int(input())
result = ""

for _ in range(T):
    testData = input()
    cnt = 0
    for ch in testData:
        cnt += 1 if ch == '(' else -1
        if cnt < 0:
            result += "NO\n"
            break
    else:
        result += "YES\n" if cnt == 0 else "NO\n"
    
    print(result)

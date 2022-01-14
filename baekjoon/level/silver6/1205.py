import sys
input = sys.stdin.readline

# input
n, new, p = map(int, input().split())

if n == 0:
    print(1)
    
else:
    scores = list(map(int, input().split()))
    if n == p and scores[-1] >= new:
        print(-1)
    else:
        result = n + 1
        for i in range(n):
            if scores[i] <= new:
                result = i + 1
                break
        print(result)


# 2 
n, new, p = map(int, input().split())

if n:
    scores = list(map(int, input().split()))
    scores.append(new)
    scores.sort(reverse=True)
    idx = scores.index(new) + 1
    if idx > p:
        print(-1)
    else:
        if n == p and scores[-1] == new:
            print(-1)
        else:
            print(idx)
else:
    print(1)

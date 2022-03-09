n = int(input())
answer = 0
# 0:00:00 ~ n:59:59 3이 하나라도 포함되는 모든 경우의 수를 출력

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                answer += 1

print(answer)

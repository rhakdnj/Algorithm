import sys

input = sys.stdin.readline

n = int(input())
crane_list = list(map(int, input().split()))
crane_list.sort(reverse=True)
m = int(input())
box_list = sorted(list(map(int, input().split())))
box_list.sort(reverse=True)

answer = [0] * n

if box_list[0] > crane_list[0]:
    print(-1)
    quit()
time = (m - 1) // n + 1
box = 0
while box < m:
    for i in range(n):
        if answer[i] < time and crane_list[i] >= box_list[box]:
            answer[i] += 1
            box += 1
            break
        if crane_list[i] < box_list[box]:
            time += 1
            break
print(max(answer))

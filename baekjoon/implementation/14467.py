n = int(input())
cow_list = [2] * (n + 1)
answer = 0

for _ in range(8):
    num, road = map(int, input().split())

    if cow_list[num] == 2:
        cow_list[num] = road
    else:
        if cow_list[num] != road:
            answer += 1
            cow_list[num] = road

print(answer)

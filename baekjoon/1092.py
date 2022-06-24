import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
crane_list = list(map(int, input().split()))
m = int(input())
box_list = list(map(int, input().split()))
crane_list.sort(reverse=True)
box_list.sort(reverse=True)

# 배로 옮길 수 없는 경우
if box_list[0] > crane_list[0]:
    print(-1)
    sys.exit()
else:
    time = 0
    while box_list:
        for crane in crane_list:
            for box in box_list:
                if crane >= box:
                    box_list.remove(box)
                    break
        time += 1
    print(time)

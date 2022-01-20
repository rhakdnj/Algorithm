import sys


def input():
    return sys.stdin.readline().rstrip()


def isBig():
    if now[0] < plan[0]:
        return 1
    elif now[0] == plan[0]:
        if now[1] < plan[1]:
            return 1
        elif now[1] == plan[1]:
            if now[2] < plan[2]:
                return 1
            elif now[2] == plan[2]:
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1


now = list(map(int, input().split(':')))
plan = list(map(int, input().split(':')))
total = now[0] * 3600 + now[1] * 60 + now[2]
total2 = plan[0] * 3600 + plan[1] * 60 + plan[2]
if isBig() == 1:
    ans = total2 - total
    hour, minute, second = str(ans // 3600), str(ans % 3600 // 60), str(ans % 60)
    hour = '0' * (2 - len(hour)) + hour
    minute = '0' * (2 - len(minute)) + minute
    second = '0' * (2 - len(second)) + second
    print(f'{hour}:{minute}:{second}')
elif isBig() == 0:
    print('24:00:00')
else:
    ans = total2 - total + 3600 * 24
    hour, minute, second = str(ans // 3600), str(ans % 3600 // 60), str(ans % 60)
    hour = '0' * (2 - len(hour)) + hour
    minute = '0' * (2 - len(minute)) + minute
    second = '0' * (2 - len(second)) + second
    print(f'{hour}:{minute}:{second}')

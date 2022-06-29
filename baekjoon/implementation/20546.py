import sys


def input():
    return sys.stdin.readline().rstrip()


prices = []


def bnp(money: int) -> int:
    cnt = 0
    for i in range(len(prices)):
        if prices[i] > money: continue
        cnt = money // prices[i]
        money %= prices[i]

    return money + cnt * prices[-1]


def timing(money: int) -> int:
    cnt, down_cnt, up_cnt = 0, 0, 0

    for i in range(1, 14):
        if prices[i - 1] > prices[i]:
            down_cnt += 1
            up_cnt = 0
        elif prices[i - 1] < prices[i]:
            down_cnt = 0
            up_cnt += 1
        else:
            down_cnt = up_cnt = 0

        if prices[i] <= money and down_cnt >= 3:
            cnt += money // prices[i]
            money %= prices[i]
        if up_cnt == 3:
            money += cnt * prices[i]
            up_cnt = cnt = 0

    return money + cnt * prices[-1]


def solution():
    global prices
    money = int(input())
    prices = list(map(int, input().split()))

    BNP = bnp(money)
    TIMING = timing(money)

    if BNP > TIMING:
        print("BNP")
    elif BNP < TIMING:
        print("TIMING")
    else:
        print("SAMESAME")


solution()

# https://www.acmicpc.net/problem/1343
import sys

def input():
    return sys.stdin.readline().rstrip()

board = input()

board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")

if 'X' in board:
    print(-1)
else:
    print(board)
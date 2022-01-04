import sys
input = sys.stdin.readline

board = input().rstrip()
# greedy, replace는 원본을 변경하지 않기에 원래 변수에 다시 저장해야한다.
board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")

if 'X' in board:
    print(-1)
else:
    print(board)


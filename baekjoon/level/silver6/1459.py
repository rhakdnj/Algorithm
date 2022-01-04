import sys
input = sys.stdin.readline

x, y, w, s = map(int, input().split())

move_1 = (x + y) * w

if (x + y) % 2:
    move_2 = (max(x, y) - 1) * s + w
else:
    move_2 = max(x, y) * s

move_3 = min(x, y) * s + ((max(x, y) - min (x, y)) * w)

print(min(move_1, move_2, move_3))








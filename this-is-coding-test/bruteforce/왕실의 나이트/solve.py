# 8 * 8 -> 1~8 a~h
input_data = input()
row = int(input_data[1])
col = ord(input_data[0]) - ord('a') + 1

steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

answer = 0

for step in steps:
    nrow = row + step[0]
    ncol = col + step[1]
    if 1 <= nrow <= 8 and 1 <= ncol <= 8:
        answer += 1

print(answer)
